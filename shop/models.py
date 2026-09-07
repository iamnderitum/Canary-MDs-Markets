from django.db import models
from django.urls import reverse
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class IsAvailableManager(models.Manager):
    def get_queryset(self):
        return(
            super().get_queryset().filter(available=Product.Status.IS_AVAILABLE)
        ) 
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"
        app_label = "category"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])
    
class Product(models.Model):
    class Status(models.TextChoices):
        IS_AVAILABLE = "YES","is_vailable"
        NOT_AVAILABLE = "NO","unavailable"

    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_available = models.CharField(
        max_length=10,
        choices=Status,
        default=Status.NOT_AVAILABLE
    )
    objects = models.Manager()
    in_stock = IsAvailableManager()


    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

        verbose_name = "Product"
        verbose_name_plural = "Products"
        app_label = "Products"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
    
    
    # def get_absolute_url(self):
    #     return reverse(
    #         "product:prduct_detail",
    #         args=[
    #             self.name,
    #             self.category.name
    #         ]
    #     )