from django.db import models
from django.urls.base import reverse

class Category(models.Model):

    name = models.CharField(max_length = 70, db_index = True, unique = True)
    slug = models.SlugField(max_length = 70)

    class Meta:

        db_table = 'category'
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    
    def getAbsoluteUrl(self):
        return reverse('cart:productListPerCategory', args=[self.slug])