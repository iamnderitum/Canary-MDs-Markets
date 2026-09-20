from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
)
from .models import Category, Product
from cart.forms import CartAddProductForm
from .recommender import Recommender

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    #products = Product.objects.filter(available=True)
    #products = Product.in_stock.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Pagination with 6 products per page
    paginatior = Paginator(products, 6)
    page_number = request.GET.get("page", 1)
    try:
        products = paginatior.page(page_number)

    except PageNotAnInteger:
        products = paginatior.page(1)

    except EmptyPage:
        products = paginatior.page(paginatior.num_pages)

    # Search advanced using PostgreSQL
    query = request.GET.get("q", "").strip()
    if query:
        search_vector = (
            SearchVector(
                "name",
                weight="A",
                config="english"
            )
            +
            SearchVector(
                "description",
                weight="B",
                config="engilish"
            )
            +
            SearchVector(
                "category__name",
                weight="C",
                config="english"
            )
        )

        search_query = SearchQuery(
            query,
            config="english",
            search_type="websearch"
        )
        products = (
            products
            .annotate(
                rank=SearchRank(
                    search_vector,
                    search_query
                )
            )
            .filter(
                rank__gt=0
            )
            .order_by(
                "-rank"
            )
        )

    return render(
        request,
        "apps/ecommerce/ecommerce-products.html",
        {
            'category': category,
            "categories": categories,
            "products": products,
            "page": products,
            "query":query,
        }
    )

def product_detail(request, id, slug):
    product = get_object_or_404(
        Product, id=id, slug=slug, available=True
    )

    cart_product_form = CartAddProductForm()

    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    return render(
        request,
        "apps/ecommerce/ecommerce-product-detail.html",
        {
            "product": product,
            "cart_product_form":cart_product_form,
            "recommended_products":recommended_products
        }
    )