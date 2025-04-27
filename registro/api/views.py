from rest_framework import viewsets
from registro.models import Registro
from registro.api.serializer import RegistroSerializer



class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

