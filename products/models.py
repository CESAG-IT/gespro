from django.db import models

# Create your models here.

class Product(models.Model):

    STATUS = (
        ('A','Disponible'),
        ('U', 'Indisponible')
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=1000)
    qty = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='products/', default='default.jpg')
    status = models.CharField(max_length=1, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name


    class Meta:
        db_table = 'produts'
        ordering = ['-created_at']
        verbose_name = 'product'
        verbose_name_plural = "products"