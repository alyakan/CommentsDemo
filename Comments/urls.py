from django.conf.urls import patterns, url
from .views import CommentListView, CommentCreateView

urlpatterns = patterns(
    '',
    url(r'^$', CommentListView.as_view(), name='comment-list'),
    url(r'^create/$', CommentCreateView.as_view(), name='comment-create')
    )
