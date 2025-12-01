from django.contrib import admin
from .models import Post



class TestAdminPermissions(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return False

class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    
blog_site = BlogAdminArea(name="Blog Admin")

blog_site.register(Post, TestAdminPermissions)