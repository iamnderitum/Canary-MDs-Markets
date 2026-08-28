from django.urls import reverse_lazy
from django.views.generic.edit import(
    CreateView,
    DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django import forms
from django.views.generic.list import ListView
from .models import Course

# class ManageCourseListView(ListView):
#     model = Course
#     template_name = "apps/courses/manage/course/list.html"

#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(owner = self.request.user)


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner = self.request.user)

class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OwnerCourseMixin(
    OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin
):
    model = Course
    fields = ["subject", "title", "slug", "overview"]
    widgets = {
        "title": forms.Textarea(
            attrs = {
                "class": "form-control",
                "placeholder":"Course Title Here"
            }
        ),
        "slug": forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Course Slug goes Here"
            }
        ),
        "overview": forms.Textarea(
            attrs = {
                "class": "form-control",
                "placeholder": "Course Overview Here"
            }
        ),
        "subject": forms.Select(
            attrs ={
                "class": "form-select"
            }
        ),

    }

    labels = {
        "title": "Title",
        "slug": "Slug 'title_under'",
        "overview": "Overview",
        "subject": "Subject"
    }
    success_url = reverse_lazy("manage_course_list")

class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = "apps/courses/manage/course/form.html"

class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = "apps/courses/manage/course/list.html"
    permission_required = "courses.view_course"
    # permission_required = "courses.delete_course"

class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = "courses.add_course"

class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = "courses.change_course"

class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = "apps/courses/manage/course/delete.html"
    permission_required = "courses.delete_course"