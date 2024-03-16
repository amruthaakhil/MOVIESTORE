from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Movie

@receiver(pre_save, sender=Movie)
def create_movie_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)