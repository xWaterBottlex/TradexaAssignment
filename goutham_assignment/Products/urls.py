from django.urls import path
from .views import ProductCreateView

urlpatterns = [
    path('', ProductCreateView),
]
