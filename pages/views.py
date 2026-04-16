from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()

class PagesView(LoginRequiredMixin,TemplateView):
    pass

#Utility 
pages_utility_starterpage_view = PagesView.as_view(template_name="pages/utility/starterpage.html")
pages_utility_maintenance_view = PagesView.as_view(template_name="pages/utility/maintenance.html")
pages_utility_comingsoon_view = PagesView.as_view(template_name="pages/utility/comingsoon.html")
pages_utility_timeline_view = PagesView.as_view(template_name="pages/utility/timeline.html")
pages_utility_faqs_view = PagesView.as_view(template_name="pages/utility/faqs.html")
pages_utility_pricing_view = PagesView.as_view(template_name="pages/utility/pricing.html")
pages_utility_404_error_view = PagesView.as_view(template_name="pages/utility/404error.html")
pages_utility_500_error_view = PagesView.as_view(template_name="pages/utility/500error.html")

#Vertical
pages_vertical_view = PagesView.as_view(template_name="pages/vertical/vertical.html")


#Authentication pages
pages_authentication_auth_login_view = PagesView.as_view(template_name="pages/authentication/auth-login.html")
pages_authentication_auth_register_view = PagesView.as_view(template_name="pages/authentication/auth-register.html")
pages_authentication_auth_recoverpassword_view= PagesView.as_view(template_name="pages/authentication/auth-recoverpassword.html")
pages_authentication_auth_lockscreen_view= PagesView.as_view(template_name="pages/authentication/auth-lockscreen.html")
pages_authentication_auth_logout_view= PagesView.as_view(template_name="pages/authentication/auth-logout.html")
pages_authentication_auth_confirm_mail_view = PagesView.as_view(template_name="pages/authentication/auth-confirm-mail.html")
pages_authentication_auth_email_verification_view = PagesView.as_view(template_name="pages/authentication/auth-email-verification.html")
pages_authentication_auth_two_step_verification_view = PagesView.as_view(template_name="pages/authentication/auth-two-step-verification.html")










