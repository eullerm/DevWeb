from django.db import models
from category.models import Category

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products" ,on_delete = models.DO_NOTHING)
    name = models.CharField(max_length = 100, db_index = True, unique = True)
    description = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100)
    image = models.CharField(max_length = 50, blank = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    registeredDate = models.DateField()
    available = models.BooleanField(default = False)
    bestSeller = models.BooleanField(default = False)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name

    def getAvailable(self):
        return "Sim" if self.available else "Não"

