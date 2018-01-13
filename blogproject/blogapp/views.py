from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth as permissionauth

from blogapp.forms import (
	RegistrationForm,
	PostForm,
	ResponseForm,
	)
from blogapp.models import Post, Response


def home(request):
	args = {}
	args['posts'] = Post.objects.all()
	return render(request, 'body/home.html', args)

def register(request):
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password2')
		user.set_password(password)
		user.save()
		return redirect("/login")
	return render(request, 'body/register.html', {'form': form })

def account(request):
	if request.user.is_authenticated():
		form = PostForm()
		args = {}
		args['posts'] = request.user.written_by.all()
		args['form'] = form
		return render(request, 'body/account.html', args)
	else:
		return redirect("/login")

def post_detail(request, post_id):
	args = {}
	args['post'] = Post.objects.get(pk = post_id)
	args['form'] = ResponseForm()
	return render(request, 'body/post_detail.html', args)


@login_required(login_url='/login')
def post_response(request, post_id):
	post_instance = Post.objects.get(pk = post_id)
	form = ResponseForm(request.POST)
	if form.is_valid():
		response = form.save(commit = False)
		response.post_name = post_instance
		response.response_by = request.user
		response.save()
		return redirect(request.META['HTTP_REFERER'])



@login_required(login_url='/login')
def create_post(request):
	form = PostForm(request.POST)
	if form.is_valid():
		post = form.save(commit = False)
		post.written_by = request.user
		post.save()
		return redirect('/account')

@login_required(login_url='/login')
def delete_post(request, post_id):
	Post.objects.get(pk = post_id).delete()
	return redirect('/account')

@login_required(login_url='/login')
def edit_post(request, post_id):
	post_instance = Post.objects.get(pk = post_id)
	form = PostForm(request.POST or None, instance = post_instance)
	if form.is_valid():
		post = form.save(commit = False)
		post.written_by = request.user
		post.save()
		return redirect('/account')

	return render(request, 'body/edit_post.html', {'form': form, 'post_id': post_id })

def logout(request):
	permissionauth.logout(request)
	return redirect('/')



