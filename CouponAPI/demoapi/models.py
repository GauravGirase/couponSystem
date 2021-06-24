from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Code(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount = models.IntegerField(default=15, validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
