from django.db import models
from django.urls import reverse





class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True , verbose_name="نام")
    slug = models.SlugField(max_length=150, unique=True ,db_index=True , verbose_name="اسلاگ")
    created_at = models.DateTimeField(auto_now_add=True , verbose_name="تاریخ ساخت")
    updated_at = models.DateTimeField(auto_now=True , verbose_name="تاریخ به روز رسانی")

    class Meta:
        ordering = ('name', )
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE , verbose_name="دسته بندی")
    name = models.CharField(max_length=100, db_index=True , verbose_name="نام")
    slug = models.SlugField(max_length=100, db_index=True , verbose_name="اسلاگ")
    description = models.TextField(blank=True , verbose_name="توضیحات")
    price = models.DecimalField(max_digits=10, decimal_places=2 , verbose_name="قیمت")
    available = models.BooleanField(default=True , verbose_name="در دسترس")
    stock = models.PositiveIntegerField(verbose_name="موجودی")
    created_at = models.DateTimeField(auto_now_add=True , verbose_name="تاریخ ساخت")
    updated_at = models.DateTimeField(auto_now=True , verbose_name="تاریخ به روز رسانی")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True , verbose_name="عکس")

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

        permissions = (("can_see_product_detail","can_see_product_detail"),
            ("can_add_new_product","can_add_new_product"),
            ("can_see_orders","can_see_orders")
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])



