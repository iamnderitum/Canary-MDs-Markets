from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from django.contrib import admin
from django.urls import path,include
#from django.conf.urls import url
from symox import views
#from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
#from . import MyPasswordChangeView
from .views import MyPasswordChangeView ,MyPasswordSetView

from blog.sitemaps import PostSitemap
from shop.sitemaps import ProductSitemap

sitemaps = {
    "posts": PostSitemap,
    "products":ProductSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    #Dashboard
    path('',views.DashboardView.as_view(),name='dashboard'),
    #Apps
    path('apps/',include('apps.urls')),
    #Bootstrap
    path('bootstrap/',include('bootstrap.urls')),
    #Components
    path('components/',include('components.urls')),
    #Pages
    path('pages/',include('pages.urls')),
    #Accounts    
    path("account/", include("allauth.urls")),

    path('logout',views.logout,name ='logout'),

    path('accounts/password/change/', login_required(MyPasswordChangeView.as_view()), name="account_change_password"),
    path('accounts/password/set/', login_required(MyPasswordSetView.as_view()), name="account_set_password"),

    path("profile/", include("profiles.urls")),
    path("shop/", include("shop.urls", namespace="shop")),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path("payment/", include("payment.urls", namespace="payment")),
    path("coupons/", include("coupons.urls", namespace="coupon")),
    
    path("blog/", include("blog.urls", namespace="blog")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap"
    ),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )