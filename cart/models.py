from django.db import models
from category.models import Category

class CartTable(models.Model):

    category = models.ForeignKey(Category, related_name="cart" ,on_delete = models.DO_NOTHING)
    name = models.CharField(max_length = 100, db_index = True, unique = True)
    description = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    steel = models.CharField(max_length = 100, blank = True, choices = (("1060", "1060"), ("1075", "1075"),("1095", "1095"),("9260", "9260"),("damasco", "damasco"),("dobrado", "dobrado")))
    color = models.CharField(max_length = 100, blank = True)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return self.name
