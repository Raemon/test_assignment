from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class TimeStampMixin(TimeStampedModel):
    class Meta:
        abstract = True

    @property
    def updated(self):
        return self.modified


class NameSlugMixin(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(verbose_name=_('name'), max_length=255)
    slug = models.SlugField(verbose_name=_('slug'), max_length=40, unique=True)

    def __str__(self):
        return self.name


class IsEnabledMixin(models.Model):
    class Meta:
        abstract = True

    is_enabled = models.BooleanField(verbose_name=_('is enabled'), default=True)
