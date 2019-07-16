from rest_framework.authentication import TokenAuthentication


class MyTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        try:
            user, token = super().authenticate(request)
        except TypeError:
            return None

        return user, token
