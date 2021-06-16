from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

# Register
@api_view(['POST', ])
def register_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            users = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = users.email
            data['username'] = users.username
            data['address'] = users.address
            token = Token.objects.get(user=users).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
