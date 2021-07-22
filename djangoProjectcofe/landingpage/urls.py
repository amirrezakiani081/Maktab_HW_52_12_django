from django.urls import path
from .views import *
from django.conf.urls.static import static
from djangoProjectcofe import settings
app_name='landingpage'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('ab/', About.as_view(), name='about'),
    path('co/', Contactus.as_view(), name='contactus'),
    path('or/', OrderList.as_view(), name='orderlist'),
    path('me/', Menu.as_view(), name='menu'),
]
