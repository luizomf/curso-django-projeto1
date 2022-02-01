import string
from random import SystemRandom

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    # Aqui começam os campo para a relação genérica

    # Representa o model que queremos encaixar aqui
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Representa o id da linha do model descrito acima
    object_id = models.CharField(max_length=255)
    # Um campo que representa a relação genérica que conhece os
    # campos acima (content_type e object_id)
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, *args, **kwargs):
        if not self.slug:
            rand_letters = ''.join(
                SystemRandom().choices(
                    string.ascii_letters + string.digits,
                    k=5,
                )
            )
            self.slug = slugify(f'{self.name}-{rand_letters}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
