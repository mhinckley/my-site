from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<content_type>[a-zA-Z ]+)/$', views.genre_posts, name='genre_posts'),
]

# content_type above links to the parameter in the view function
# name is the name of the view
# method you are going to call when the url matches