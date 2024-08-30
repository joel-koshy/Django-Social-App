from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status 

from rest_framework.views import APIView

# Create your views here.


@api_view(['GET'])
def test(request): 
    return Response({"Message": "App is working"}, status.HTTP_200_OK)




