# pages/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Workspace, Page
from .forms import WorkspaceForm, PageForm # Form은 아직 안 만들었지만 미리 임포트

# --- Workspace 관련 뷰 ---

def workspace_list(request):
    """
    모든 워크스페이스 목록을 보여주는 뷰
    """
    workspaces = Workspace.objects.all() # 데이터베이스에서 모든 Workspace 객체를 가져옵니다.
    # pages/templates/pages/workspace_list.html 템플릿을 렌더링하고, 'workspaces' 변수를 넘겨줍니다.
    return render(request, 'pages/workspace_list.html', {'workspaces': workspaces})

def workspace_create(request):
    """
    새 워크스페이스를 생성하는 뷰
    """
    if request.method == 'POST':
        # POST 요청이면 사용자가 폼을 제출한 것입니다.
        form = WorkspaceForm(request.POST) # 제출된 데이터로 폼 객체를 생성합니다.
        if form.is_valid():
            # 폼 데이터가 유효하면 (예: 필수 필드가 채워져 있는지 등)
            workspace = form.save() # 폼 데이터를 바탕으로 새로운 Workspace 객체를 생성하고 데이터베이스에 저장합니다.
            # 워크스페이스 생성 후 해당 워크스페이스의 페이지 목록 페이지로 이동합니다.
            return redirect('page_list', workspace_id=workspace.id)
    else:
        # GET 요청이면 빈 폼을 보여줍니다.
        form = WorkspaceForm() # 빈 폼 객체를 생성합니다.

    # pages/templates/pages/workspace_create.html 템플릿을 렌더링하고, 'form' 변수를 넘겨줍니다.
    return render(request, 'pages/workspace_create.html', {'form': form})

# --- Page 관련 뷰 ---

def page_list(request, workspace_id):
    """
    특정 워크스페이스에 속한 페이지 목록을 보여주는 뷰
    """
    # URL에서 캡처한 workspace_id를 사용하여 해당 Workspace 객체를 가져옵니다.
    # 만약 ID에 해당하는 워크스페이스가 없으면 404 오류 페이지를 보여줍니다.
    workspace = get_object_or_404(Workspace, id=workspace_id)
    # 해당 워크스페이스에 속한 모든 페이지를 가져옵니다.
    # models.py에서 related_name='pages'로 설정했기 때문에 workspace.pages로 접근 가능합니다.
    pages = workspace.pages.filter(parent_page__isnull=True) # 일단 최상위 페이지들만 가져옵니다.
    # pages/templates/pages/page_list.html 템플릿을 렌더링하고 필요한 변수들을 넘겨줍니다.
    return render(request, 'pages/page_list.html', {'workspace': workspace, 'pages': pages})


def page_create(request, workspace_id):
    """
    특정 워크스페이스 안에 새 페이지를 생성하는 뷰
    """
    # 페이지를 생성할 워크스페이스 객체를 가져옵니다.
    workspace = get_object_or_404(Workspace, id=workspace_id)

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            # 폼 데이터를 바탕으로 새로운 Page 객체를 생성하지만, 아직 데이터베이스에 저장하지는 않습니다 (commit=False).
            page = form.save(commit=False)
            page.workspace = workspace # 생성할 페이지의 워크스페이스를 현재 워크스페이스로 설정합니다.
            page.save() # 이제 데이터베이스에 저장합니다.
            # 페이지 생성 후 해당 페이지의 상세 보기 페이지로 이동합니다.
            return redirect('page_detail', page_id=page.id)
    else:
        form = PageForm()

    # pages/templates/pages/page_create.html 템플릿을 렌더링하고 필요한 변수들을 넘겨줍니다.
    return render(request, 'pages/page_create.html', {'workspace': workspace, 'form': form})


def page_detail(request, page_id):
    """
    특정 페이지의 상세 내용을 보여주는 뷰
    """
    # URL에서 캡처한 page_id를 사용하여 해당 Page 객체를 가져옵니다. 없으면 404.
    page = get_object_or_404(Page, id=page_id)
    # pages/templates/pages/page_detail.html 템플릿을 렌더링하고 'page' 변수를 넘겨줍니다.
    return render(request, 'pages/page_detail.html', {'page': page})