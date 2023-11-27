from django.db import models


class Product(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)


class Category(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('ParentCategory', on_delete=models.CASCADE, null=True, blank=True)


class ParentCategory(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Manufacturer(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Characteristic(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class ProductCharacteristics(models.Model):
    characteristic = models.ForeignKey('Characteristic', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
