from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    form = PostAdminForm

admin.site.register(Post, PostAdmin)
