from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class News(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateTimeField(auto_now_add=False ,null=True,blank=True)
    email=models.EmailField(unique=True)
    description=models.TextField()
    is_published=models.BooleanField(default=False)
    done_at=models.DateTimeField(auto_now_add=True)


    # def save(self, *args, **kwargs):
    #     # Capitalize name before saving
    #     if self.name:
    #         self.name = self.name.strip().upper()
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Reporting New")
        verbose_name_plural = _(" Reporting News")
        ordering = ("first_name",)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"


class Author(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(Author,related_name="author",on_delete=models.CASCADE)
    publish_date=models.DateTimeField()

class Genre(models.Model):
    name=models.CharField(max_length=255)
    books=models.ManyToManyField(Book)