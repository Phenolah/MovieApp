from sys import prefix
from django.conf import settings
import jwt
from coreapi import auth
from rest_framework import authentication, exceptions
from django.contrib.auth.models import User

# set up the authentication schema
class JWTAuthentication(authentication.BaseAuthentication):

# check whrether with should authenticate the user or not
    def authenticate(self, request):

        #header where user would be sending the token
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        # converts data from byte format to string format
        prefix, token = auth_data.decode('utf-8').split('')

        #get the JWT payload and signature
        try:
            payload = jwt.decode(
                token, settings.JWT_SECRET_KEY, algorithms="HS256")

            #adds the username to the token after its been decoded
            user = User.objects.get(username=payload["username"]
            )
            return (user, token)

        #throws an error if token is invalid/tampered with
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is invalid, login'
            )

        #throws an invalid if token is expired
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed(
                'Your token is expired, login'
            )
        return super().authenticate(request)
