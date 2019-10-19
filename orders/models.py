from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=60 , verbose_name="نام")
    last_name = models.CharField(max_length=60 , verbose_name="نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    address = models.CharField(max_length=150 , verbose_name="آدرس")
    postal_code = models.CharField(max_length=30 , verbose_name="کد پستی")
    city = models.CharField(max_length=100 , verbose_name="شهر")
    created = models.DateTimeField(auto_now_add=True , verbose_name="تاریخ ساخت")
    updated = models.DateTimeField(auto_now=True , verbose_name="تاریخ به روز رسانی")
    paid = models.BooleanField(default=False , verbose_name="پرداخت شده")

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارشات"
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE , verbose_name="سفارش")
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE , verbose_name="محصول")
    price = models.DecimalField(max_digits=10, decimal_places=2 , verbose_name="قیمت")
    quantity = models.PositiveIntegerField(default=1 , verbose_name="تعداد")


    class Meta:
        verbose_name = "آیتم سفارش"
        verbose_name_plural = "آیتم های سفارش"

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

