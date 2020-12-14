from django.db import models
from category.models import Category

# Create your models here.
class ProductAjax(models.Model):
    category = models.ForeignKey(Category, related_name="ProductAjax" ,on_delete = models.DO_NOTHING)
    name = models.CharField(max_length = 100, db_index = True, unique = True)
    slug = models.SlugField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    quantity = models.IntegerField(default = 0)

    class Meta:
        db_table = 'ProductAjax'

    def __str__(self):
        return self.name
    def getName(self):
        return self.name
    def getQuantity(self):
        return self.quantity
    def getPrice(self):
        return self.price
    def getCategory(self):
        return self.category