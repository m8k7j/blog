from django.contrib import admin
from blog import models
# Register your models here.

class BBS_admin(admin.ModelAdmin):
	list_display = ('title','summary','author','created_at')
	list_filter = ('created_at',)
	list_searchfield = ('title','author__user__username')
	def signature(self,obj):
		return self.obj.author.signature
	signature.short_description = 'hah'
	

admin.site.register(models.BBS,BBS_admin)
admin.site.register(models.love)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
