from django.shortcuts import render
from .serializers import UniversitySerializer, ProgramSerializer
from .models import University, ProgramHighlights
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()

    def list(self, request, *args, **kwargs):
        universities = self.get_queryset()
        if request.query_params.get('order', None):
            universities = universities.order_by(
                request.query_params.get('order'))

        serializer = UniversitySerializer(universities, many=True)

        return Response(serializer.data)


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = ProgramHighlights.objects.all()
    serializer_class = ProgramSerializer
