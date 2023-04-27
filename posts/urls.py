from . import views
from django.urls import path

urlpatterns = [
    path("home/", views.homepage, name="home"),
    path("", views.PostListCreateView.as_view(), name="list_posts"),
    path("<int:pk>", views.PostRetriveUpdateDeleteView.as_view(), name="post_detail"),
]
