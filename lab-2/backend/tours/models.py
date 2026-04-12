from django.db import models


class Tour(models.Model):
    TRANSPORT_CHOICES = [
        ('plane',  'Самолёт'),
        ('bus',    'Автобус'),
        ('cruise', 'Круиз'),
    ]

    title            = models.CharField(max_length=200)
    country          = models.CharField(max_length=100)
    transport        = models.CharField(max_length=10, choices=TRANSPORT_CHOICES)
    duration_days    = models.PositiveSmallIntegerField()
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    departure_date   = models.DateField()
    is_available     = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} → {self.country}"