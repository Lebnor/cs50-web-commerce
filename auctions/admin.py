from django.contrib import admin
from .models import User, Comment, Listing



class ListingAdmin(admin.ModelAdmin):
    filter_horizontal=('following',)


# Register your models here.
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Listing, ListingAdmin)