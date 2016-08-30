from rest_framework.response import  Response
from rest_framework.views import APIView

from .models import User,Request
from .serializers import UserSerializer, RequestSerializer


class UserList(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class Requestlist(APIView):
    def get(self,request):
        request = Request.objects.all()
        serializer = RequestSerializer(request,many=True)
        return Response(serializer.data)

from django.http import HttpResponse
from django.template import RequestContext

def handler404(request):
    response = HttpResponse("This is a custom 404 page")
    response.status_code = 404
    return response


def handler500(request):
    response = HttpResponse("This is a custom 500 page")
    response.status_code = 500
    return response
