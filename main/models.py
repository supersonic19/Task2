from django.db import models

# Create your models here.

COLOR_CHOICES = (
        ('green','GREEN'),
        ('blue', 'BLUE'),
        ('red','RED'),
        ('orange','ORANGE'),
        ('black','BLACK'),
)

class info(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    mobile = models.IntegerField()
    colour = models.CharField(max_length=6, choices=COLOR_CHOICES , default = 'green')