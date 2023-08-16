from django.contrib import admin
from django.urls import path
from . import views
from .views import menuview,bookingview,bootstapPage,form
urlpatterns = [
    path('menu/',menuview.as_view()),
    path('booking/',bookingview.as_view()),
    path('bootstrap/',bootstapPage),
    path('form/',form),

]