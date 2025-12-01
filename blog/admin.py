from tkinter.tix import Tree
from django.contrib import admin
from .models import Book, Post



class TestAdminPermissions(admin.ModelAdmin):
    
    # def has_add_permission(self, request):
    #     return False
    
    def has_change_permission(self, request, obj = None):
        # if obj is None:
        #     return True
        return False
    
    # def has_delete_permission(self, request, obj =  None):
    #     if obj is None:
    #         return False
    
    # def has_view_permission(self, request, obj = ...):
    #     return False
    
    
class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    
blog_site = BlogAdminArea(name="Blog Admin")

blog_site.register(Post, TestAdminPermissions)
blog_site.register(Book)