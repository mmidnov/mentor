from django.shortcuts import render
from django.http import HttpResponse
from .models import Ads,Category
from .forms import AdForm
# Create your views here.

def category_list(request):
    all_categories = Category.objects.all()
    context={
        "all_categories":all_categories
    }
    return render(request, 'category.html', context=context)
def ads_list(request):
    all_ads = Ads.objects.all()
    context={
        "all_ads":all_ads
    }
    return render(request, 'index.html', context=context)

def created_at(request):
    if request.method == 'POST':
        pass
    else:
        form_of_ad = AdForm()
    return render(request, 'create_ad.html',{'form_of_ad':form_of_ad})