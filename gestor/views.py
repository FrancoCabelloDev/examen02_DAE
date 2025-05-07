from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Carpeta, Etiqueta, Nota, Documento
from .serializers import CarpetaSerializer, EtiquetaSerializer, NotaSerializer, DocumentoSerializer

# CRUD para Carpeta
class CarpetaViewSet(viewsets.ModelViewSet):
    queryset = Carpeta.objects.all()
    serializer_class = CarpetaSerializer

# CRUD para Etiqueta
class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

# CRUD para Nota
class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    # Método para compartir una nota
    @action(detail=True, methods=['get'])
    def compartir(self, request, pk=None):
        nota = self.get_object()
        return Response({'mensaje': f'Nota "{nota.titulo}" compartida exitosamente.'})

# CRUD para Documento
class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    # Método para compartir un documento
    @action(detail=True, methods=['get'])
    def compartir(self, request, pk=None):
        documento = self.get_object()
        return Response({'mensaje': f'Documento "{documento.nombre}" compartido exitosamente.'})
