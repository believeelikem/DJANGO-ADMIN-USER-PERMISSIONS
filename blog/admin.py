from tkinter.tix import Tree
from django.contrib import admin
from .models import Book, Post
from django.contrib import messages


class TestAdminPermissions(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return True
    
    def has_change_permission(self, request, obj = None):
        # if obj is None:
        #     return True
        return True
    
    def has_delete_permission(self, request, obj =  None):
        # if obj is None:
        #     return False
        # return True
        # if obj is None:
        #     return False
        # return obj.pk != 5
        
        
        ''' note the below doesnt check if the users group has a permission. it is only 
         checking if the user is in a specific group
        
        if request.user.groups.filter(name = "Editors").exists():    
             return True  '''
    
        # if request.POST.get("action") == "delete_selected":
        #     messages.info(request, " Deleting action happening")
        
        return True
    
    # def has_view_permission(self, request, obj = ...):
    #     return False
    
    
class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    
blog_site = BlogAdminArea(name="Blog Admin")

blog_site.register(Post, TestAdminPermissions)
blog_site.register(Book)