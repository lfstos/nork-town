from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    is_opportunity = models.BooleanField(default=True)

    @property
    def car_count(self):
        return self.cars.count()

    def increment_car_count(self):
        self.cars.create()
        self.save()

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    COLOR_CHOICES = [
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('gray', 'Gray'),
    ]
    MODEL_CHOICES = [
        ('hatch', 'Hatch'),
        ('sedan', 'Sedan'),
        ('convertible', 'Convertible'),
    ]
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    model = models.CharField(max_length=20, choices=MODEL_CHOICES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True, related_name='cars')

    def __str__(self) -> str:
        return self.model