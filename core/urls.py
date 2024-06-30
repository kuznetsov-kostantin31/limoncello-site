from django.urls import path

from core.views import main, banquets, customcake, contact, mainEng, banquetsEng, customcakeEng, contactEng, menu, banquets_menu

urlpatterns = [
    path('', main, name="main"),
    path('banquets/', banquets, name="banquets"),
    path('customcake/', customcake, name="customcake"),
    path('contact/', contact, name="contact"),
    path('mainEng/', mainEng, name="mainEng"),
    path('banquetsEng/', banquetsEng, name="banquetsEng"),
    path('customcakeEng/', customcakeEng, name="customcakeEng"),
    path('contactEng/', contactEng, name="contactEng"),
    path('menu/', menu, name="menu"),
    path('banquets_menu/', banquets_menu, name="banquets-menu")
]
