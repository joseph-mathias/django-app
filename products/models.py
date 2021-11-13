from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=100)
    product_img = models.ImageField(default='default.jpg', upload_to='productImg')
    discription = models.CharField(max_length=100)
    old_price = models.FloatField()
    new_price = models.FloatField()
    stock = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})
