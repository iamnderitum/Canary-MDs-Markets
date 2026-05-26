
from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from allauth.account.views import PasswordChangeView,PasswordSetView

from blog.models import Post
from shop.models import Product

class DashboardView(LoginRequiredMixin,View):
    template_view = "dashboard.html"
    products = Product.objects.all()
    blog_posts = Post.published.all()

    def get(self, request):  
        # return self.render_to_response(
        #     {
        #         "products": self.products,
        #         "blogs":self.blog_posts
        #     }
        # )  
        context =  {
            "products": self.products,
            "blogs":self.blog_posts
            }
        return render(request, 'dashboard.html',{"products": self.products, "blogs":self.blog_posts})
        
def logout(request):
    auth.logout(request)
    return render(request,'account/logout.html')
        
class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('dashboard')        

class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy('dashboard')          