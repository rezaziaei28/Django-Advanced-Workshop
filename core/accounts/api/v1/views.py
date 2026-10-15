from rest_framework import generics
from rest_framework import status
from .serializers import (RegisterSerializer, CustomTokenObtainPairSerializers, CustomAuthTokenSerializer,
                          ChangePasswordSerializer, ProfileSerializer, ActivationResandSerializers)

from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from accounts.models import Profile
from django.shortcuts import get_object_or_404
# from django.core.mail import send_mail
from mail_templated import send_mail
from ..utils import EmailThread
from mail_templated import EmailMessage

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from django.conf import settings

User = get_user_model()

class RegisterAPIView(generics.GenericAPIView):
      """
      API view for user registration.
      """
      serializer_class = RegisterSerializer

      def post(self, request, *args, **kwargs):
            serializer = RegisterSerializer(data= request.data)
            if serializer.is_valid():
                  serializer.save()
                  email = serializer.validated_data['email']
                  data = {
                        'email': email
                  }

                  user_object = get_object_or_404(User, email = email)
                  token = self.get_tokens_for_user(user_object)
      
                  email_object = EmailMessage('email/activation_email.tpl', {'token': token},
                                          'ziazia@gmail.com', to=[email])
                  EmailThread(email_object).start()
                  return Response(data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def get_tokens_for_user(self,user):
            if not user.is_active:
                  raise AuthenticationFailed("User is not active")

            refresh = RefreshToken.for_user(user)

            return str(refresh.access_token)

      
class CustomObtainAuthToken(ObtainAuthToken):
      serializer_class = CustomAuthTokenSerializer

      def post(self, request, *args, **kwargs):
            serializer = self.serializer_class(data=request.data,
                                                context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                  'token': token.key,
                  'user_id': user.pk,
                  'email': user.email
            })


class CustomDiscardAuthToken(APIView):
     '''This class for logout at the site'''
     permission_classes = [IsAuthenticated]

     def post(self, request):
            request.user.auth_token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class CustomTokenObtainPairView(TokenObtainPairView):
     serializer_class = CustomTokenObtainPairSerializers

class ChangePasswordApiView(generics.GenericAPIView):
      """
      An endpoint for changing password.
      """
      serializer_class = ChangePasswordSerializer
      model = User
      permission_classes = (IsAuthenticated,)

      def get_object(self, queryset=None):
            obj = self.request.user
            return obj

      def put(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                  # Check old password
                  if not self.object.check_password(serializer.data.get("old_password")):
                        return Response(
                              {"old_password": ["Wrong password."]},
                              status=status.HTTP_400_BAD_REQUEST)

                  # Set new password
                  self.object.set_password(serializer.data.get("new_password"))
                  self.object.save()

                  return Response(
                        {'detail': 'password changed successfully'},
                        status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           

class ProfileApiView(generics.RetrieveUpdateAPIView):
      '''Retrieve and update user information'''

      permission_classes = [IsAuthenticated]
      serializer_class = ProfileSerializer
      queryset = Profile.objects.all()

      def get_object(self):
            queryset = self.get_queryset()
            obj = get_object_or_404(queryset, user=self.request.user)
            return obj

      # def get_queryset(self):
      #       return super().get_queryset()

      # learn deffrents get_object and get_queryset

class TestEmailSend(generics.GenericAPIView):

      def get(self, request, *args, **kwargs):
            self.email = "rezaziaei28@gmail.com"

            # User.objects.get() it's equal with get_object_or_404()
            user_object = get_object_or_404(User, email= self.email)
            token = self.get_tokens_for_user(user_object)

            email_object = EmailMessage('email/hello.tpl', {'token': token},
                                    'ziazia@gmail.com', to=[self.email])
            EmailThread(email_object).start()
            return Response("email send")


      def get_tokens_for_user(self,user):
            if not user.is_active:
                  raise AuthenticationFailed("User is not active")

            refresh = RefreshToken.for_user(user)

            return str(refresh.access_token)

class ActivationApiViews(APIView):

      def get(self, request,token, *args, **kwargs):
            
            # first I just: decode -> id user
            try:
                  token = jwt.decode(token, settings.SECRET_KEY , algorithms=['HS256'])
                  user_id = token.get("user_id")
            except ExpiredSignatureError:
                  return Response({"details":"token has been expired"}, status=status.HTTP_400_BAD_REQUEST)
            except InvalidTokenError:
                  return Response({"details": "token is not valid"}, status=400)
            
            # object user 
            # user_object = User.objects.get(pk = user_id)
            user_object = get_object_or_404(User, pk=user_id)
            # is_verified -> True
            user_object.is_verified = True
            user_object.save()

            return Response({'detaile': 'your accounts have been verified and activated seccussfully'})

class ActivationResandApiViews(generics.GenericAPIView):
      serializer_class = ActivationResandSerializers

      def post(self, request, *args, **kwargs):
            serializers = self.serializer_class(data=request.data) 
            serializers.is_valid(raise_exception=True)
            user_object = serializers.validated_data['user'] 
            token = self.get_tokens_for_user(user_object)

            email_object = EmailMessage('email/activation_email.tpl', {'token': token},
                                    'ziazia@gmail.com', to=[user_object.email])
            EmailThread(email_object).start()

            return Response({'detaile': 'your activation resand successfuly'}, status=status.HTTP_200_OK)
            # else:
            #       return Response({'detaile': 'request failed'}, status=status.HTTP_400_BAD_REQUEST)


      def get_tokens_for_user(self,user):
            if not user.is_active:
                  raise AuthenticationFailed("User is not active")

            refresh = RefreshToken.for_user(user)

            return str(refresh.access_token)