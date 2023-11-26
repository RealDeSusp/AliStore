from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # "on_delete=models.CASCADE" - action if an object is deleted. If a product category is deleted, all products from
    # this category will also be deleted
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    characteristic = models.ManyToManyField('Characteristic')

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parentcategory = models.ForeignKey('ParentCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ParentCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    TYPE_CHOICES = [
        (PRIMARY, 'Primary'),
        (SECONDARY, 'Secondary'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
