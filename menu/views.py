from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from menu.models import Menu
from menu.serializers import MenuSerializer

# Create your views here.
class MenuView(APIView):
    """
        View to represent the menu endpoints
    """
    def get(self, request):
        try:
            menu = Menu.objects.all()
            serializer = MenuSerializer(menu, many=True)
            response = {'response': serializer.data}
            return Response(response)
        except Exception:
            return Response(
                {'message': 'Error getting menu'},
                status.HTTP_400_BAD_REQUEST
            )

    def post(self, request, format=None):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
