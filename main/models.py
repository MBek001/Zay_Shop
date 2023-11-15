from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Products(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title


class Img(models.Model):
    image = models.ImageField(upload_to='pics', blank=True, null=True, verbose_name=_("image"))
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name=_("product"))

class ShoppingCart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name=_("product"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    upload_at = models.DateTimeField(auto_now_add=True, verbose_name=_("upload_at"))
    count = models.IntegerField(default=1, verbose_name=_("count"))

    def __str__(self):
        return f'{self.product.title} from {self.user.username}'