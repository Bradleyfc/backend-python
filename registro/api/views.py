from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import logging
from registro.models import Registro
from registro.api.serializer import RegistroSerializer

# Configurar logger
logger = logging.getLogger(__name__)

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            
            if serializer.is_valid():
                # Guardar el registro
                registro = serializer.save()
                
                # Verificar si se debe enviar correo
                if request.data.get('send_email', True):
                    # Obtener la contraseña del request
                    password = request.data.get('password')
                    
                    if registro.correo and password:
                        subject = 'Tu registro en CFBC'
                        message = f'Hola {registro.nombre},\n\nGracias por registrarte en CFBC. Tu contraseña es: {password}\n\nSaludos,\nEquipo CFBC'
                        from_email = settings.DEFAULT_FROM_EMAIL
                        recipient_list = [registro.correo]
                        
                        try:
                            send_mail(subject, message, from_email, recipient_list)
                        except Exception as e:
                            logger.error(f"Error al enviar correo: {str(e)}")
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error en create: {str(e)}")
            return Response({"error": "Ha ocurrido un error interno"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

