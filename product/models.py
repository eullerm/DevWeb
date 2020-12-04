from django.db import models
from category.models import Category
from django.urls.base import reverse

class Product(models.Model):

    category = models.ForeignKey(Category, related_name="products" ,on_delete = models.DO_NOTHING)
    name = models.CharField(max_length = 100, db_index = True, unique = True)
    description = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100)
#    image = models.CharField(max_length = 50, blank = True)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    registeredDate = models.DateField()
    available = models.BooleanField(default = False)
    bestSeller = models.BooleanField(default = False)
    steel = models.CharField(max_length = 100, blank = True, choices = (("1060", "1060"), ("1075", "1075"),("1095", "1095"),("9260", "9260"),("damasco", "damasco"),("dobrado", "dobrado")))
    color = models.CharField(max_length = 100, blank = True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name

    def getAvailable(self):
        return "Sim" if self.available else "Não"

    def getAbsoluteUrl(self):
        return reverse('cart:showProduct', args=[self.id, self.slug])