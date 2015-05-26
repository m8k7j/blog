from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from blog import models
from django.contrib import comments

# Create your views here.

def index(request):
	
	bbs_list = models.BBS.objects.all()
	bbs_categories = models.Category.objects.all()
	return render_to_response('index.htm',{
	'bbs_list':bbs_list,
	'user':request.user,
	'bbs_category':bbs_categories,
	})

def bbs_detail(request,bbs_id):
	bbs = models.BBS.objects.get(id=bbs_id)
	return render_to_response('bbs_detail.htm',{'bbs_obj': bbs,'user':request.user})

def sub_comment(request):
	
	bbs_id = request.POST.get('bbs_id')
	comment = request.POST.get('comment_content')
	comments.models.Comment.objects.create(
		content_type_id=7,
		object_pk = bbs_id, 
		site_id = 1,
		user = request.user,
		comment = comment,
		
	)

	return HttpResponseRedirect('/blog/detail/%s' %bbs_id)

def login(request):

	return render_to_response('login.html')
def logout_view(request):
	user = request.user
	auth.logout(request)
	return HttpResponse("<h3>User %s logout success</h3><br><a href='/login/'>Re-login</a>" %user)


def acc_login(request):
	print request.POST
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request,user)
		content = '''
		welcome %s !!!
		<a href = '/logout/'>logout</a>
		''' % user.username
		return HttpResponseRedirect("/")
	else:
		return render_to_response("login.html",{'login_err':"Wrong username and password",'user':user})


def bbs_pub(request):
	return render_to_response('bbs_pub.htm',{'user':request.user})


def bbs_sub(request):
	content = request.POST.get('content')	
	cata_id = request.POST.get('cata_id')
	summary = request.POST.get('summary')
	title = request.POST.get('title')
	
	print cata_id
	author = models.BBS_user.objects.get(user__username=request.user)
	models.BBS.objects.create(
		title = title,
		summary=summary,
		content = content,
		author = author,
		view_count = 1,
		ranking = 1,
		category_id =cata_id,
		
	)
	return HttpResponseRedirect('/blog/')

def category(request,cata_id):
	bbs_list = models.BBS.objects.filter(category__id=cata_id)
	bbs_categories = models.Category.objects.all()
	return render_to_response(
	'index.htm',
	{
		'bbs_list':bbs_list,
		'user':request.user,
		'bbs_category':bbs_categories,
		'cata_id':cata_id,
	}
	)
