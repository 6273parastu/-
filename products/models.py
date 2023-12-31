from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    name = models.CharField(_("Persian Name"), max_length=200)
    en_name = models.CharField(_("English Name"), max_length=200)
    description = models.TextField(_("Description"))
    category = models.ForeignKey("Category", verbose_name=("Category"), on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.id} {self.name}"
    

class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"))
    icon = models.ImageField(_("Icon"), upload_to='category_images')
    image = models.ImageField(_("Image"), upload_to='category_images')