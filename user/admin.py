from django.contrib import admin
from .models import profile
# Register your models here

class profileadmin(admin.ModelAdmin):
    pass

# # class signupadmin(admin.ModelAdmin):
# #     pass

admin.site.register(profile, profileadmin)
# # admin.site.register(signup, signupadmin)
