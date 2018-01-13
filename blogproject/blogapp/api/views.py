from django.contrib.auth import get_user_model
from rest_framework.generics import (
	ListAPIView,
	CreateAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	RetrieveUpdateAPIView,
	)
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)
from rest_framework.response import Response as Responseresult
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .permissions import IsOwner
from blogapp.models import Post, Response
from .serializers import (
	PostSerializer, 
	ResponseListSerializer, 
	PostCreateSerializer, 
	CreateResponseSerializer,
	UserCreateSerializer,
	LoginSerializer
	)

User = get_user_model()

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [AllowAny]

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [AllowAny]

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(written_by = self.request.user)


class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [IsOwner]

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = [IsOwner]

class ResponseListAPIView(ListAPIView):
	serializer_class = ResponseListSerializer
	permission_classes = [AllowAny]

	def get_queryset(self, *args, **kwargs):
		return Response.objects.filter(post_name = self.kwargs['pk'])

class ResponseCreateAPIView(CreateAPIView):
	queryset = Response.objects.all()
	serializer_class = CreateResponseSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer, *args, **kwargs):
		print(self.kwargs['pk'])
		post_instance = Post.objects.get(id = self.kwargs['pk'])
		serializer.save(response_by = self.request.user, post_name = post_instance)


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	permission_classes = [AllowAny]

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Responseresult(new_data, status=HTTP_200_OK)
        return Responseresult(serializer.errors, status=HTTP_400_BAD_REQUEST)