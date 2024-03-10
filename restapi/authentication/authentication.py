from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class SimpleAuthentication(BaseAuthentication):
    def authenticate(self, request):
        
        token = request.headers.get("Authentication")
        if token == 'myscrettoken':

            return ('authenticated_user', None)
        raise  AuthenticationFailed("invalidtoken")