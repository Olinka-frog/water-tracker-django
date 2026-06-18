from django.contrib import admin
from .models import UserProfile, DailyNorm, WaterIntake

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'weight', 'city', 'activity_level']
    search_fields = ['user__username', 'city']

@admin.register(DailyNorm)
class DailyNormAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'calculated_norm', 'consumed_total']
    list_filter = ['date']

@admin.register(WaterIntake)
class WaterIntakeAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'timestamp']
    list_filter = ['timestamp']