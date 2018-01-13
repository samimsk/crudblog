from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.TextField()
	detail = models.TextField(blank=True, null=True)
	time = models.DateTimeField(auto_now = True)
	written_by = models.ForeignKey(User, default=1, related_name='written_by', blank=True, null=True)


	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-time"]

class Response(models.Model):
	post_name = models.ForeignKey(Post, related_name='post_name', blank=True, null=True)
	detail = models.TextField(blank=True, null=True)
	response_by = models.ForeignKey(User, default=1, related_name='response_by', blank=True, null=True)

	def __str__(self):
		return self.detail
	class Meta:
		ordering = ["-id"]



