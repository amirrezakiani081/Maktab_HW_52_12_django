from django.db import models
from .validators import price_menu_validator
from django.utils.translation import gettext


# Create your models here.

class Table(models.Model):
    number = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    status = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class MenuItem(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,
                            help_text='enter menu item name')
    price = models.IntegerField(help_text='enter the price',
                                verbose_name='price(ir)',
                                validators=[price_menu_validator])  # maxlenght nadin
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    discount = models.IntegerField(null=True, blank=True, verbose_name='takhfifat')
    serving_time_period = models.IntegerField()
    estimated_cooking_time = models.IntegerField()
    image = models.FileField(help_text='enter pic', verbose_name='menu image ', upload_to='menu_items/images/',
                             blank=True, null=True)
    creat_timestamp = models.DateTimeField(verbose_name='time creat', auto_now_add=True, null=True)  # زمان ساخت
    modify_timestamp = models.DateTimeField(auto_now=True, null=True, verbose_name='time edit')  # زمان ادیت

    def __str__(self):
        return f"{self.id}# {self.name}:{self.price}"


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    number = models.IntegerField()
    date_time_stamp = models.DateTimeField()

    # time_time_stamp = models.TimeField()

    def __str__(self):
        return f"{self.number}"


class OrderMenuItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order_id}-{self.menu_item_id}"


class Receipt(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    final_price = models.IntegerField()
    date_time_stamp = models.DateTimeField()

    # time_time_stamp = models.TimeField()

    def __str__(self):
        return f"{self.order_id}"
