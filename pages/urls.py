# pages/urls.def
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]
