from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Ads,Category
from .forms import AdForm
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from users.models import User
from django.views import View
from django.views.generic import DetailView,ListView,UpdateView,DeleteView,CreateView
# Create your views here.

def category_list(request):
    all_categories = Category.objects.all()
   
    context={
        "all_categories":all_categories
    }
    return render(request, 'category.html', context=context)


class AdsListView(ListView):
    template_name = 'index.html'
    queryset = Ads.objects.all()
    context_object_name = 'all_ads'
    # def get(self,request, *args,**kwargs):
    #    all_ads = Ads.objects.all()
    #    return render(request,self.templete_name,{'all_ads':all_ads})

    # all_ads = Ads.objects.all()
    # 1
    # all_ads=Ads.objects.filter(created_at__lte=timezone.now())
    # 2
    # all_ads=Ads.objects.filter(title__icontains='test')
    # 3
    # all_ads = Ads.objects.filter(owner=None)
    # 4
    # all_ads = Ads.objects.filter(created_at__iso_year=2023, description__icontains='b')
    # 5
    # admin = User.objects.get(username="admin")
    # all_ads =Ads.objects.filter(owner=admin)
    # 6
    # all_ads = Ads.objects.filter(price__in=[200,3500,343,2345])
class AdsDetailView(DetailView):
    template_name = 'retrieve_ad.html'
    queryset = Ads.objects.all()
    context_object_name = 'ad'


class AdsDeleteView(DeleteView):
    queryset = Ads.objects.all()
    template_name = 'delete_ad.html'
    success_url = reverse_lazy('ads_list')



class AdsUpdateView(UpdateView):
    template_name = 'update_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self):
        return reverse('ads_list')


class AdsCreateView(CreateView):
    template_name = 'create_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self):
        return reverse('ads_list')