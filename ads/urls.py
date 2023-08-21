from django.urls import path
from .views import ads_list, category_list,created_at


urlpatterns=[
    path("", ads_list),
    path("category", category_list),
    path('create',created_at)
]