from django import forms
from .models import Workspace, Page

class WorkspaceForm(forms.ModelForm):
    class Meta:
        model = Workspace
        fields = ['name']

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'parent_page']