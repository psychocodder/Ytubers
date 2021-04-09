from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    sliders = Slider.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=False)
    teams = Team.objects.all()
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'youtubers': youtubers,
    }
    return render(request, 'webpages/home.html', data)

@login_required(login_url='login')
def about(request):
    return render(request, 'webpages/about.html')

@login_required(login_url='login')
def services(request):
    return render(request, 'webpages/services.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'webpages/contact.html')
