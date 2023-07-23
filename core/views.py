from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
import json

from django.views import View
from .serializers import TodoSerializer
from .models import Usuario


class ViewSetUserChanges(View):
    
    @staticmethod
    @api_view(['GET'])
    def get(request):
        users = Usuario.objects.all()
        serializer = TodoSerializer(users, many=True)
        return Response(serializer.data)        
    
class NewUser(APIView):
    
    def post(self, request):
    
        data = json.loads(request.body)
        newName = data.get('name')
        new = Usuario.objects.create(name=newName)
        users = Usuario.objects.all()
        serializer = TodoSerializer(users, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        # import pdb
        # pdb.set_trace()    
        user = Usuario.objects.filter(id=pk).first()
        data = json.loads(request.body)
        user.name = data['name']
        user.save()
        users = Usuario.objects.all()
        serializer = TodoSerializer(users, many=True)
        return Response(serializer.data)