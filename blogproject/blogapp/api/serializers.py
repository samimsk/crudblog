from rest_framework.serializers import ModelSerializer, CharField, EmailField
from django.contrib.auth import get_user_model
from blogapp.models import Post, Response


User = get_user_model()

class PostSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'detail',
			'time',
			'written_by'
		]

class PostCreateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'title',
			'detail',
		]

class ResponseListSerializer(ModelSerializer):
	class Meta:
		model = Response
		fields = [
			'id',
			'detail',
			'response_by',
		]

class CreateResponseSerializer(ModelSerializer):
	class Meta:
		model = Response
		fields = [
			'detail',
		]

class UserCreateSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'email',
		]
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		password = validated_data['password']
		user_instance = User(
			username = username,
			email = email
			)
		user_instance.set_password(password)
		user_instance.save()
		return validated_data

class LoginSerializer(ModelSerializer):
	token = CharField(read_only=True, allow_blank = True)
	username = CharField(required = False, allow_blank = True)

	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'token'
		]
		extra_kwargs = {'password': {'write_only': True}}

	def validate(self, data):
		username = data.get('username', None)
		password = data.get('password', None)

		if not username or not password:
			raise ValidationError('Invalid login credentials')

		user_instance = User.objects.get(username = username)

		if user_instance:
			if not user_instance.check_password(password):
				raise ValidationError('Incorrect credentials provided!')
		data['token'] = "Sample token"
		return data