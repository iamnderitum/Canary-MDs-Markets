from django.urls import path

from .views import (
    pages_utility_starterpage_view,
    pages_utility_maintenance_view,
    pages_utility_comingsoon_view,
    pages_utility_timeline_view,
    pages_utility_faqs_view,
    pages_utility_pricing_view,
    pages_utility_404_error_view,
    pages_utility_500_error_view,

    pages_vertical_view,

    pages_authentication_auth_login_view,
    pages_authentication_auth_register_view,
    pages_authentication_auth_recoverpassword_view,
    pages_authentication_auth_lockscreen_view,
    pages_authentication_auth_logout_view,
    pages_authentication_auth_confirm_mail_view,
    pages_authentication_auth_email_verification_view,
    pages_authentication_auth_two_step_verification_view,
)

app_name = "pages"

urlpatterns=[
    #Utility
    path("utility/starterpage", pages_utility_starterpage_view, name="utility.starterpage"),
    path("utility/maintenance", pages_utility_maintenance_view, name="utility.maintenance"),
    path("utility/comingsoon",pages_utility_comingsoon_view, name="utility.comingsoon"),
    path("utility/timeline",pages_utility_timeline_view, name="utility.timeline"),
    path("utility/faqs", pages_utility_faqs_view, name="utility.faqs"),
    path("utility/pricing", pages_utility_pricing_view, name="utility.pricing"),
    path("utility/404error", pages_utility_404_error_view, name="utility.404error"),
    path("utility/500error", pages_utility_500_error_view, name="utility.500error"),

    #Vertical
    path("vertical", pages_vertical_view, name="pages.vertical"),

    #authentication pages
    path("authentication/auth-login", view=pages_authentication_auth_login_view, name="authentication.auth-login"),
    path("authentication/auth-register", view=pages_authentication_auth_register_view, name="authentication.auth-register"),
    path("authentication/auth-recoverpassword", view=pages_authentication_auth_recoverpassword_view, name="authentication.auth-recoverpassword"),
    path("authentication/auth-lockscreen", view=pages_authentication_auth_lockscreen_view, name="authentication.auth-lockscreen"),
    path("authentication/auth-logout", view=pages_authentication_auth_logout_view, name="authentication.auth-logout"),
    path("authentication/auth-confirm-mail", view=pages_authentication_auth_confirm_mail_view, name="authentication.auth-confirm-mail"),
    path("authentication/auth-email-verification", view=pages_authentication_auth_email_verification_view, name="authentication.auth-email-verification"),
    path("authentication/auth-two-step-verification", view= pages_authentication_auth_two_step_verification_view, name="authentication.auth-two-step-verification"),

]