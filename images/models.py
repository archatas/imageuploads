# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


def upload_to(instance, filename):
    return '/'.join(['images', unicode(instance.pk), filename])


class Image(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    image = models.ImageField(_("Image"), upload_to=upload_to)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        ordering = ("image",)

    def __unicode__(self):
        return self.image.path