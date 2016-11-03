from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/class/(?P<clazz>[a-zA-Z "-]+)/$', views.clazz_posts, name='clazz_posts'),
    #url(r'^post/when/(?P<when>[a-zA-Z ]+)/$', views.remember_posts, name='remember_posts'),
    url(r'^post/user/(?P<author>[a-zA-Z0-9_-]+)/$', views.user_posts, name='user_posts'),
    url(r'^post/to_field/(?P<to_field>[a-zA-Z0-9 "-]+)/$', views.to_posts, name='to_posts'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^post/(?P<post>\d+)/comment/$', views.CommentCreate.as_view(), name='comment_new'),
    url(r'^like/$', views.like_button, name='like_button'),
    url(r'^follow/$', views.follow_button, name='follow_button'),
    url(r'^post/mylist/$', views.my_list, name='my_list'),
    url(r'^home/$', views.home, name='home'),
]



# url(r'^post/genre/(?P<content_type>[a-zA-Z ]+)/$', views.genre_posts, name='genre_posts'),
# content_type above links to the parameter in the view function
# third is the name of the view
# second is method you are going to call when the url matches