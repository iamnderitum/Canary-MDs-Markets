from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from django.db import models
from .fields import OrderField

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["title"]
        app_label = "Subect"

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(
        User,
        related_name="courses_created",
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject,
        related_name="courses",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(
        User,
        related_name="courses_joined",
        blank=True,
    )
    class Meta:
        ordering = ["-created"]
        app_label = "Course"

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(
        Course,
        related_name="modules",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=444)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    def __str__(self):
        return f'{self.order}. {self.title}'

    class Meta:
        ordering = ["order"]
        app_label = "Module"


class Content(models.Model):
    module = models.ForeignKey(
        Module,
        related_name="contents",
        on_delete=models.CASCADE,
        
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            "model_in":("text", "video", "image", "file")
        }
    )
    object_id = models.PositiveBigIntegerField()
    item = GenericForeignKey("content_type", "object_id")
    order = OrderField(blank=True, for_fields=["module"])

    class Meta:
        ordering = ["order"]
        app_label = "Content"

class ItemBase(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='%(class)s_related',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=444)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        app_label = "Itembase"

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string(
            f"apps/courses/content/{self._meta.model_name}.html",
            {"item": self}
        )


class Text(ItemBase):
    content = models.TextField()
    class Meta:
        app_label = "Text"

class File(ItemBase):
    file = models.FileField(upload_to="elearning/files")
    class Meta:
        app_label = "file"

class Image(ItemBase):
    file = models.FileField(upload_to="elerning/images")
    class Meta:
        app_label = "Image"

class Video(ItemBase):
    url = models.URLField()
    class Meta:
        app_label = "Video"