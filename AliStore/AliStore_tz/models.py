from django.db import models


class Product(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    def product_characteristics(self):
        # Get all characteristics for the given category
        category_characteristics = self.category.characteristics.all()

        # Get all characteristics for the product through the intermediate table
        product_characteristics = self.productcharacteristics_set.all()

        # Return the union of category and product characteristics
        return category_characteristics | product_characteristics


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
    values = models.JSONField()


class ProductCharacteristics(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    characteristic = models.ForeignKey('Characteristic', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
