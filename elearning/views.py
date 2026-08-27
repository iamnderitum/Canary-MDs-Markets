from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.views.generic.list import ListView
from .models import Course

class ManageCourseListView(ListView):
    model = Course
    template_name = "apps/e-learning/manage/course/list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner = self.request.user)


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner = self.request.user)

class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OwnerCourseMixin(OwnerMixin):
    model = Course
    fields = ["subject", "title", "slug", "overview"]
    success_url = reverse_lazy("manage_course_list")

