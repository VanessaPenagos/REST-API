from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer

class HelloApiView(APIView):
    """API View de prueba""" 
    serializer_class = serializer.HelloSerielizer

    def get(self, request, format=None):
        """retorna lista de caracteristicas del APIView"""     

        an_apiview = [
            'Usamos metodos http como funciones (get, post, parch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra app',
            'Esta mapeado manualmente a los url'
        ]

        return Response({'message': 'Hello mundo', 'an_apiview': an_apiview})

    def post(self, request):
        """Crea un mensaje con nuestro nombre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message' : message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
            return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
            return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
            return Response({'method': 'DELETE'})