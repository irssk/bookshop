from django.urls import path
from .views import home, book

urlpatterns = [
    path('', home),
    path('<slug:slug>', book, name="<slug>")
]
