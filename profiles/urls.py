from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path(
        "",
        views.profile,
        name="profile",
    ),
    path(
        "edit/",
        views.profile_edit,
        name="profile_edit",
    ),
    path(
        "enroll-course/",
        views.StudentEnrollCourseView.as_view(),
        name="student_enroll_course"
    ),
    path(
        "courses",
        views.StudentCourseListView.as_view(),
        name="student_course_list"
    ),
    path(
        "course/<pk>",
        views.StudentCourseDetailView.as_view(),
        name="student_course_detail"
    ),
    path(
        "course/<pk>/module_id",
        views.StudentCourseDetailView.as_view(),
        name="student_course_detail_module"
    )
]