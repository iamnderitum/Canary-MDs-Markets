from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ProfileForm
# Create your views here.

@login_required
def profile_edit(request):
    # profile, created = Profile.objects.get_or_create(
    #         user = request.user
    #     )
    
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "apps/contacts/userprofile.html",
        {
            "form": form,
        },
    )