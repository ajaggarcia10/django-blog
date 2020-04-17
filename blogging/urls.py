from django.urls import path
from blogging.views import list_view, detail_view
from blogging.feeds import LatestPostFeed
from django.conf.urls import url

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name='blog_detail'),
    url('latest/feed', LatestPostFeed()),
]