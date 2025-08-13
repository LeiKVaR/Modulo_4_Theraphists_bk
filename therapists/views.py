"""
Vistas para la aplicación de terapeutas.
Maneja las operaciones CRUD y renderizado de templates.
"""

from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Therapist
from .serializers import TherapistSerializer


class TherapistViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de terapeutas.
    Incluye soft delete, restauración y filtros.
    """
    serializer_class = TherapistSerializer
    queryset = Therapist.objects.all()  # pylint: disable=no-member
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'first_name', 'last_name_paternal', 'last_name_maternal',
        'document_number', 'document_type', 'email', 'phone', 'location'
    ]

def index(request):
    """
    Vista para renderizar la página principal de terapeutas.
    """
    return render(request, 'therapists_ui.html')