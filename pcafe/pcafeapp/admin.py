from models import *
from django.contrib import admin

class UserDetailsAdmin(admin.ModelAdmin):
	list_display = ['userid','email']
	search_fields = ['userid']
	class Meta:
		model = UserDetails
class UserAddressAdmin(admin.ModelAdmin):
	list_display = ['address']
	class Meta:
		model = UserAddress

admin.site.register(UserDetails,UserDetailsAdmin)
admin.site.register(UserAddress,UserAddressAdmin)
