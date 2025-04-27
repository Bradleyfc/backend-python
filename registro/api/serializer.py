from rest_framework import serializers
from registro.models import Registro


class RegistroSerializer(serializers.ModelSerializer):
    # Rename these fields to avoid conflicts with the model fields
    sexo_display = serializers.CharField(source='get_sexo_display', read_only=True)
    grado_display = serializers.CharField(source='get_grado_display', read_only=True)
    ocupacion_display = serializers.CharField(source='get_ocupacion_display', read_only=True)
    
    class Meta:
        model = Registro
        fields = '__all__'