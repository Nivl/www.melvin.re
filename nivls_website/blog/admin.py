from django.contrib import admin
from django.contrib.comments.models import Comment
from blog.models import Post, Link, Menu, Category, Tag, PostImage
from django.conf import settings

# Post
class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        js = (settings.STATIC_URL + 'js/blog/admin_post_preview.js',)

admin.site.register(Post, AdminPost)

# Other

class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    def get_ordering(self, request):
        return ["left"]

class AdminTag(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class AdminMenu(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tag, AdminTag)
admin.site.register(PostImage)
admin.site.register(Menu, AdminMenu)
admin.site.register(Link)
admin.site.register(Category, AdminCategory)
