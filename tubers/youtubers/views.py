from django.shortcuts import render
from .models import Youtuber
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers,
    }
    
    return render(request, 'youtubers/youtubers.html', data)

    

@login_required(login_url='login')
def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber
    }
    return render(request, 'youtubers/youtubers_detail.html', data)

@login_required(login_url='login')
def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains= keyword)
            # tubers = tubers.filter(fullname__icontains=keyword)

    if 'city'in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact= city)

    if 'camera_type'in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact= camera_type)


    if 'category'in request.GET:
        category = request.GET['category']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact= category_search)



    data = {
        'tubers' : tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search': category_search,
        
    }

    return render(request, 'youtubers/search.html', data)
