from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Proyecto
from .serializers import ProyectoSerializer
# Create your views here.

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]