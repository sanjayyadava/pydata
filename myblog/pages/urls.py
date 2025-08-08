from django.urls import path
from . import views

# urlpatterns = [
#     path('<slug:slug>/', views.page_detail, name='page_detail'),
#     path('', views.page_detail, name='page_detail'),  # home page
# ]


urlpatterns = [
    path('', views.page_list, name='page_list'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]

