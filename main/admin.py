from django.contrib import admin
from .models import post, likedpost,comments
# Register your models here

class postadmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class likedpostadmin(admin.ModelAdmin):
    pass

class commentpostadmin(admin.ModelAdmin):
    pass

    
admin.site.register(post, postadmin)
admin.site.register(likedpost, likedpostadmin)
admin.site.register(comments, commentpostadmin)
