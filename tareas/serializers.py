from rest_framework import serializers
from .models import Lista, Tarea, Etiqueta, TareaEtiqueta

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'

class TareaEtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaEtiqueta
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    etiquetas = EtiquetaSerializer(many=True, read_only=True)

    class Meta:
        model = Tarea
        fields = '__all__'
