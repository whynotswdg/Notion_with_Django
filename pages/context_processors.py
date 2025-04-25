from .models import Workspace, Page

def sidebar_data(request):
    workspaces = Workspace.objects.all()

    for workspace in workspaces:
        workspace.top_level_pages = workspace.pages.filter(parent_page__isnull=True).order_by('title')

    return {
        'all_workspaces_with_pages': workspaces,
    }