from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView,DeletePostView, CategoryView,AddCategoryView,likePostView

urlpatterns = [
       # path('', views.home, name="home"),
       path('',HomeView.as_view(), name="home"),
       path('article/<int:pk>',ArticleDetailView.as_view(), name="article-detail"),
       path('add-post/',AddPostView.as_view(), name="add-post"),
       path('article/edit/<int:pk>',UpdatePostView.as_view(), name="update-post"),
       path('article/<int:pk>/delete',DeletePostView.as_view(), name="delete-post"),
       path('category/<int:pk>',CategoryView, name="category"),
       path('add-category/',AddCategoryView.as_view(), name="add-category"),
       path('like/<int:pk>',likePostView, name="like-post"),
       

]