from django.conf import settings
from django.conf.urls.static import static

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

    path("shop/", include("shop.urls", namespace="shop")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )