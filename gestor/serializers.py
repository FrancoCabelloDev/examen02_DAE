from rest_framework import serializers
from .models import Carpeta, Etiqueta, Nota, Documento

class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpeta
        fields = '__all__'

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'
