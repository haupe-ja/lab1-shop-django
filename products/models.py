from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name