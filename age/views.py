from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Person

from .serializer import PersonSerializer


class PersonIin(APIView):
    def get(self, request, format=None):
        person_iin = Person.objects.all()
        serializer = PersonSerializer(person_iin, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
