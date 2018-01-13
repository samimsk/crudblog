from django.conf.urls import url


from .views import (
	PostListAPIView,
	PostDetailAPIView,
	PostCreateAPIView,
	PostUpdateAPIView,
	PostDeleteAPIView,
	ResponseListAPIView,
	ResponseCreateAPIView,

	UserCreateAPIView,
	LoginAPIView
	)

urlpatterns = [
	url(r'^posts/$', PostListAPIView.as_view(), name = 'list'),
	url(r'^posts/(?P<pk>\w+)/$', PostDetailAPIView.as_view(), name = 'detail'),
	url(r'^posts/(?P<pk>\w+)/responselist$', ResponseListAPIView.as_view(), name = 'response_list'),
	url(r'^posts/(?P<pk>\w+)/create-response$', ResponseCreateAPIView.as_view(), name = 'create_response'),
	url(r'^create-post/$', PostCreateAPIView.as_view(), name = 'create'),
	url(r'^posts/(?P<pk>\w+)/edit/$', PostUpdateAPIView.as_view(), name = 'update'),
	url(r'^posts/(?P<pk>\w+)/delete/$', PostDeleteAPIView.as_view(), name = 'delete'),


	url(r'^register/$', UserCreateAPIView.as_view(), name = 'register'),
	url(r'^login/$', LoginAPIView.as_view(), name = 'login'),

    ]