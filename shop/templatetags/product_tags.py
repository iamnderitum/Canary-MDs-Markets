from django import template
from django.db.models import Count
import markdown
from django.utils.safestring import mark_safe
from ..models import Product

register = template.Library()

@register.simple_tag(name="product_count")
def total_products():
    products = Product.objects.all()
    count = products.count()
    print("No of Products", count)
    # Add query by category
    return Product.objects.filter(available=True).count()