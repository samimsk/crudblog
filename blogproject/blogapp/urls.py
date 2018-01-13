from django.conf.urls import url
from django.contrib.auth import views as auth_views


from blogapp.views import (
	home,
	register,
	account,
	logout,
	create_post,
	delete_post,
	edit_post,
	post_detail,
	post_response,
	)

urlpatterns = [
    url(r'^$', home, name="home"),
	url(r'^login/$', auth_views.login, {'template_name': 'body/login.html'}, name="login"),
    url(r'^register/$', register, name="register"),
    url(r'^account/$', account, name="account"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^post/(?P<post_id>\w+)/$', post_detail, name="post_detail"),
    url(r'^account/create-post/$', create_post, name="create_post"),
    url(r'^post/response/(?P<post_id>\w+)/$', post_response, name="post_response"),
    url(r'^account/delete-post/(?P<post_id>\w+)/$', delete_post, name="delete_post"),
    url(r'^account/edit-post/(?P<post_id>\w+)/$', edit_post, name="edit_post"),

    ]