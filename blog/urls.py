from django.urls import path
from blog.views import my_blogs,MyView,home,details,add_news,register

urlpatterns = [
    path('', home,name="home"),
    path('register/', register,name="create-account"),
    path('news/', my_blogs,name="news"),
    path('add-news/', add_news,name="add_news"),
    path('detail/<int:id>/', details,name="details"),
    path('view/',MyView.as_view())
]
