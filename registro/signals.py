from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Registro

@receiver(post_save, sender=Registro)
def crear_usuario(sender, instance, created, **kwargs):
    if created and not instance.usuario:
        # Crear nombre de usuario basado en el carnet (que es único)
        username = f"user_{instance.carnet}"
        
        try:
            # Crear el usuario
            user = User.objects.create_user(
                username=username,
                email=instance.correo,
                first_name=instance.nombre,
                last_name=instance.apellidos,
                # Establecer una contraseña temporal que el usuario deberá cambiar
                password=f"{instance.carnet}"  # Usar el carnet como contraseña inicial
            )
            
            # Asociar el usuario al registro
            instance.usuario = user
            # Guardar sin activar la señal nuevamente
            post_save.disconnect(crear_usuario, sender=Registro)
            instance.save()
            post_save.connect(crear_usuario, sender=Registro)
        except Exception as e:
            print(f"Error al crear usuario: {e}")