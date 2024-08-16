from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()

    def clean(self):
        # Ensure price_total is 0
        if self.price_total != 0:
            raise ValidationError('Price total must be zero')
        # Ensure price_total is equal to the actual price
        if self.price_total != self.price:
            raise ValidationError('Price total must be equal to the actual price')
        # Ensure price_total is equal to price minus discount
        if self.price_total != self.price - self.discount:
            raise ValidationError('Price total must be equal to price minus discount')

        # Additional checks to mimic constraints
        if self.price < 0:
            raise ValidationError('Price cannot be negative')
        if self.discount < 0:
            raise ValidationError('Discount cannot be negative')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
