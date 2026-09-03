from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ProfileForm, CourseEnrollForm
# Create your views here.

@login_required
def profile(request):
    return render(
        request,
        "apps/contacts/userprofile.html"
    )

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
            return redirect("profiles:profile_edit")

    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "apps/contacts/userprofile.html",
        {
            "form": form,
        },
    )

class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_invalid(self, form):
        self.course = form.cleaned_data["course"]
        self.course.students.add(self.request.user)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy(
            "student_course_detail", args=[self.course.id]
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["enroll_form"] = CourseEnrollForm(
            initial={"course":self.object}
        )
        return context