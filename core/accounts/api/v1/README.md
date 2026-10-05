## Challenges I Faced

### Change password API returned 401 Unauthorized in Swagger

When I tried to change a password with `PUT /accounts/api/v1/password-change/`, I got `401 Unauthorized`. In Swagger only `basicAuth` was showing and not `Bearer` and the JWT token was getting Base64 encoded twice like `Basic QmVhcmVy...:undefined` which looked strange.

After some searching I understood that the problem was the order of `DEFAULT_AUTHENTICATION_CLASSES` in my settings. I had `BasicAuthentication` first and `JWTAuthentication` last. DRF checks the list in order and when `BasicAuthentication` is first it tries that first and never reaches JWT. That is why Swagger was only showing `basicAuth` as an option.

I removed `BasicAuthentication` from the list and after that everything worked:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',   # removed this caused the bug
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}
```

To use it in Swagger I click the Authorize button and in the Bearer field I paste the token with the word `Bearer ` in front of it like this:

```
Bearer eyJhbGciOiJIUzI1NiIs...
```

The `Bearer ` with the space is part of the value. I also learned that after changing the password the old JWT token becomes invalid and I need to log in again and that the browser is not good for testing JWT because it does not send the token so Swagger or Postman is better and that I should use the `access` token and not the `refresh` token.

### UpdateAPIView adds PATCH method that I did not want

I found a Change Password example on Stack Overflow that used `UpdateAPIView` but `UpdateAPIView` adds both `PUT` and `PATCH` automatically and I only wanted `PUT` for changing the password and I did not want `PATCH` to work.

`UpdateAPIView` extends `UpdateModelMixin` and gives both `PUT` (update) and `PATCH` (partial_update) by default and there is no easy way to disable just `PATCH` while keeping `PUT`.

So I replaced `UpdateAPIView` with `generics.GenericAPIView` and wrote the `put` method myself:

```python
class ChangePasswordApiView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"detail": "password changed successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

With `GenericAPIView` I have full control and I can define only the methods I want. If someone sends `PATCH` now they get `405 Method Not Allowed` which is exactly what I want.

This also taught me that not every Stack Overflow answer fits my needs and sometimes I need to adapt the code instead of copying it directly.

### read_only_fields in Meta does not work for nested fields

In my ProfileSerializer I had an email field that comes from user.email and I wanted it to be read only so I added read_only_fields = ['email'] in the Meta class. But it did not work and the email field was still showing on the page as editable.

After some testing I understood that read_only_fields in Meta only works for fields that are automatically taken from the model. When I define a field manually in the serializer class, the Meta class does not control it and I have to set read_only=True directly on the field itself.

So I changed the email field to this:

```python
email = serializers.CharField(source='user.email', read_only=True)
```

And after that it worked. This taught me that Meta options only apply to auto generated fields and not to fields that I define myself in the serializer.