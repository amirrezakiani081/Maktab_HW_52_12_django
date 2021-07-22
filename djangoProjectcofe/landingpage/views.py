from django.shortcuts import render
from .models import *
# Create your views here.
from django.views import generic, View
from django.utils.translation import gettext as _

# def landingview(request):
#     return render(request,'landingpage/landing_home.html')
#
# def landingview_hom(request):
#     return render(request,'landingpage/landing_about.html')

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landingpage/landing_home.html')
    # template_name = 'landingpage/landing_home.html'


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landingpage/landing_about.html')
    # template_name = 'landingpage/landing_about.html'


class OrderList(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landingpage/landing_orderlist.html')
    # template_name = 'landingpage/landing_order_list.css'


class Contactus(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landingpage/landing_contactus.html')
    # template_name = 'landing_page/contact_us.css'


class Menu(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landingpage/landing_menu.html')

    template_name = 'landing_page/menu.css'

    # def get(self, *args, **kwargs):
    #     context = super().get(*args, **kwargs)
    #     context['category'] = Category.objects.all()
    #     context['menuitem'] = MenuItem.objects.all()
    #     return context


