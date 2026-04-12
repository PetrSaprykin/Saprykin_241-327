import random
import datetime
from .models import Tour
from django.db import transaction
from faker import Faker

fk = Faker('ru_RU')

COUNTRIES = [
    'Канада', 'Германия', 'Бельгия', 'Филиппины', 'Греция',
    'Испания', 'Италия', 'Мальдивы', 'Гавайи', 'США',
]
TRANSPORTS = ['plane', 'bus', 'cruise']


def gentestdata():
    with transaction.atomic():
        tours = []
        for _ in range(100):
            tours.append(Tour(
                title=f'Тур «{fk.city()}»',
                country=random.choice(COUNTRIES),
                transport=random.choice(TRANSPORTS),
                duration_days=random.choice([7, 10, 14, 21]),
                price_per_person=round(random.uniform(30000, 300000), 2),
                departure_date=fk.date_between(
                    start_date=datetime.date(2025, 1, 1),
                    end_date=datetime.date(2026, 12, 31)
                ),
                is_available=random.random() > 0.2,
            ))
        Tour.objects.bulk_create(tours)
    print('OK: создано 100 туров')