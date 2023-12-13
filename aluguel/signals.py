from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Usuario



@receiver(post_save, sender=get_user_model())
def criar_usuario(sender, instance, created, **kwargs):
    if created:        
        usuario = Usuario.objects.create(nome= instance.get_full_name(), email = instance.email, user = instance)