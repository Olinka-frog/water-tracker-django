from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum, Count, Avg
from django.conf import settings
from datetime import date
from django.shortcuts import get_object_or_404

from .models import UserProfile, DailyNorm, WaterIntake
from .forms import UserProfileForm, WaterIntakeForm
from .utils import get_weather, calculate_water_norm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('setup_profile')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})


@login_required
def setup_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(request.POST or None, instance=profile)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('dashboard')
    except UserProfile.DoesNotExist:
        form = UserProfileForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    
    return render(request, 'tracker/setup_profile.html', {'form': form})


@login_required
def dashboard(request):
    profile = UserProfile.objects.get(user=request.user)
    today = date.today()

    temperature = get_weather(profile.city)

    norm = calculate_water_norm(
        profile.weight, profile.age, 
        profile.activity_level, temperature
    )
    
    daily_norm, _ = DailyNorm.objects.get_or_create(
        user=request.user, date=today,
        defaults={'calculated_norm': norm, 'weather_temp': temperature}
    )
    
    if daily_norm.calculated_norm != norm:
        daily_norm.calculated_norm = norm
        daily_norm.weather_temp = temperature
        daily_norm.save()
    
    today_intakes = WaterIntake.objects.filter(
        user=request.user, timestamp__date=today
    )

    form = WaterIntakeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        intake = form.save(commit=False)
        intake.user = request.user
        intake.save()
        total = today_intakes.aggregate(total=Sum('amount'))['total'] or 0
        daily_norm.consumed_total = total
        daily_norm.save()
        return redirect('dashboard')
    
    stats = WaterIntake.objects.filter(user=request.user).aggregate(
        total_water=Sum('amount'),
        total_entries=Count('id'),
        avg_intake=Avg('amount')
    )
    
    consumed = today_intakes.aggregate(total=Sum('amount'))['total'] or 0
    
    context = {
        'profile': profile,
        'daily_norm': daily_norm,
        'consumed': consumed,
        'remaining': max(0, norm - consumed),
        'progress': int((consumed / norm) * 100) if norm > 0 else 0,
        'temperature': temperature,
        'today_intakes': today_intakes,
        'form': form,
        'stats': stats,
    }
    return render(request, 'tracker/dashboard.html', context)


@login_required
def add_water(request):
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST)
        if form.is_valid():
            intake = form.save(commit=False)
            intake.user = request.user
            intake.save()
    return redirect('dashboard')

@login_required
def delete_water(request, intake_id):
    intake = get_object_or_404(WaterIntake, id=intake_id, user=request.user)
    intake.delete()
    return redirect('dashboard')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'tracker/login.html', {'error': 'Неверное имя пользователя или пароль'})
    return render(request, 'tracker/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')