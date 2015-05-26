#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BBS(models.Model):
	category = models.ForeignKey('Category')
	title = models.CharField(max_length=64)
	summary = models.CharField(max_length=256,blank=True)
	content = models.TextField()
	author = models.ForeignKey('BBS_user')
	view_count = models.IntegerField()
	ranking = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=32,unique = True)
	def __unicode__(self):
		return self.name

class BBS_user(models.Model):
	user = models.OneToOneField(User)
	signature = models.CharField(max_length=128,default = 'this guy is too lazy to leave anything here')
	photo = models.ImageField(upload_to='./up_load/',blank=True)
	
	def __unicode__(self):
		return  self.user.username

class love(models.Model):
	trust = 'tr'
	respective = 're'
	freedom = 'fr'
	
	love_in_choice = (
		(trust, 'trust'),
		(respective,'respective'),
		(freedom,'freedom'),
	)
	love_in = models.CharField(max_length=2,choices=love_in_choice,default=trust)
