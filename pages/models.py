from django.db import models

class Workspace(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_page = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subpages')

    def __str__(self):
        return self.title