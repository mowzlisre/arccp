from django import forms
from .models import Post, Announcement, PageDetail, Website
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title', 'content', 'tag', 'link', 'author']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['announcement', 'author']

class PageDetailForm(forms.ModelForm):
    class Meta:
        model = PageDetail
        fields = '__all__'

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = '__all__'