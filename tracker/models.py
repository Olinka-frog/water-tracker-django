from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField(validators=[MinValueValidator(30)], help_text="Вес в кг")
    age = models.IntegerField(validators=[MinValueValidator(12)], help_text="Возраст")
    city = models.CharField(max_length=100, default="Moscow")
    
    ACTIVITY_CHOICES = [
        ('low', 'Низкая'),
        ('medium', 'Средняя'),
        ('high', 'Высокая'),
    ]
    activity_level = models.CharField(max_length=10, choices=ACTIVITY_CHOICES, default='medium')
    
    def __str__(self):
        return f"{self.user.username}"

class DailyNorm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    calculated_norm = models.FloatField(default=0)
    consumed_total = models.FloatField(default=0)
    weather_temp = models.FloatField(null=True, blank=True)
    
    class Meta:
        unique_together = ['user', 'date']

class WaterIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.amount}ml"