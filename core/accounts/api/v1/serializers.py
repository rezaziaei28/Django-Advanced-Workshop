from rest_framework  import serializers
from accounts.models import User, Profile
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
      password = serializers.CharField(max_length=255, write_only=True)
      password1 = serializers.CharField(max_length = 255, write_only=True)
      class Meta:
            model = User
            fields = ['email', 'password', 'password1']

      def validate(self, attrs):
            if attrs.get('password') != attrs.get('password1'):
                  raise serializers.ValidationError({'detail':'password dose not match'})

            try:
                  validate_password(attrs.get('password'))
                  # validate_password(attrs.get('password1'))
            except exceptions.ValidationError as e:
                  raise serializers.ValidationError({'password':list(e.messages)})

            
            return super().validate(attrs)

      def create(self, validated_data):
            validated_data.pop('password1' ,None)
            return User.objects.create_user(**validated_data)


class CustomTokenObtainPairSerializers(TokenObtainPairSerializer):

      def validate(self, attrs):
            validate_data = super().validate(attrs)
            if not self.user.is_verified:
                  raise serializers.ValidationError({'detail':'user is not verified'})
            validate_data['email'] = self.user.email
            validate_data['user_id'] = self.user.id
            return validate_data

class CustomAuthTokenSerializer(serializers.Serializer):
      email = serializers.CharField(label=_("Email"),write_only=True)
      password = serializers.CharField(label=_("Password"),style={'input_type': 'password'},
            trim_whitespace=False,write_only=True)
      token = serializers.CharField(label=_("Token"),read_only=True)

      def validate(self, attrs):
            username = attrs.get('email')
            password = attrs.get('password')

            if username and password:
                  user = authenticate(request=self.context.get('request'),
                  username=username, password=password)
            
                  if not user:
                        msg = _('Unable to log in with provided credentials.')
                        raise serializers.ValidationError(msg, code='authorization')

                  if not user.is_verified:
                        raise serializers.ValidationError({'detail':'user is not verified'})

            else:
                  msg = _('Must include "username" and "password".')
                  raise serializers.ValidationError(msg, code='authorization')

            attrs['user'] = user
            return attrs

class ChangePasswordSerializer(serializers.Serializer):

      old_password = serializers.CharField(required=True)
      new_password = serializers.CharField(required=True)
      new_password1 = serializers.CharField(required=True)

      def validate(self, attrs):
            '''This function for chacking that this password is valid'''
            if attrs.get('new_password') != attrs.get('new_password1'):
                  raise serializers.ValidationError(
                        {'detail':'password dose not match'}
                        )
            try:
                  validate_password(attrs.get('new_password'))
            except exceptions.ValidationError as e:
                  raise serializers.ValidationError({'new_password1':list(e.messages)})
            

            return super().validate(attrs)


class ProfileSerializer(serializers.ModelSerializer):

      email = serializers.CharField(source='user.email', read_only=True)

      class Meta:
            model = Profile
            fields = ('id', 'first_name', 'last_name','image', 'description', 'email',)
            
            # read_only_fields = ['email'] I have problem at this line is 
            # read_only_fields does not execute, and it display this field on the page.
            # This problem is solved by adding read_only=True to email Nested fields is issue
