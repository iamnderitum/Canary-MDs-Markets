from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from pages.forms import UserLoginForm
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd["username"],
                password=cd["password"]
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated Successfully")
                else:
                    return HttpResponse("Disabled Account")

            else:
                return HttpResponse("Invalid Login")

        else:
            form = UserLoginForm()

        return render(request, "account/login.html", {"form": form})