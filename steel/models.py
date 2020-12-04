from django.db import models

class Steel(models.Model):
    name = models.CharField(max_lenth = 40, db_index = True, unique = True)
    slug = models.SlugField(max_length = 40)

    class Meta:

        db_table = 'steel'

        ordering = ('name',)

    def __str__(self):
        return self.name