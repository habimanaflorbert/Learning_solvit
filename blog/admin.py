from django.contrib import admin
from blog.models import News,Author,Book, Genre

# Register your models here.
admin.site.register(News)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
