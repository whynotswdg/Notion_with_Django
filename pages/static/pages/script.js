// pages/static/pages/script.js

// DOMContentLoaded는 HTML 문서가 완전히 로드되고 파싱되었을 때 발생합니다.
// 스크립트가 실행될 때 HTML 요소들이 이미 존재하도록 보장합니다.
document.addEventListener('DOMContentLoaded', function() {
    // 사이드바 토글 버튼 요소와 전체 컨테이너 요소를 가져옵니다.
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const container = document.querySelector('.container'); // .container 클래스를 가진 요소를 선택

    if (sidebarToggle && container) { // 요소들이 존재하는지 확인
        // 버튼에 클릭 이벤트 리스너를 추가합니다.
        sidebarToggle.addEventListener('click', function() {
            // .container 요소에 'sidebar-collapsed' 클래스를 토글합니다.
            // 클래스가 없으면 추가하고, 있으면 제거합니다.
            container.classList.toggle('sidebar-collapsed');

            // 버튼 내부의 화살표 방향을 변경하여 상태를 시각적으로 표시합니다.
            const toggleIcon = sidebarToggle.querySelector('.toggle-icon');
            if (container.classList.contains('sidebar-collapsed')) {
                // 사이드바가 접혔을 때: 오른쪽 화살표 (또는 원하는 표시)
                toggleIcon.textContent = '>>';
            } else {
                // 사이드바가 펼쳐졌을 때: 왼쪽 화살표 (또는 원하는 표시)
                toggleIcon.textContent = '<<';
            }

            // (선택 사항) 사용자가 선택한 사이드바 상태를 브라우저의 Local Storage에 저장하여 페이지를 새로고침해도 유지되도록 할 수 있습니다.
            // if (container.classList.contains('sidebar-collapsed')) {
            //     localStorage.setItem('sidebarState', 'collapsed');
            // } else {
            //     localStorage.setItem('sidebarState', 'expanded');
            // }
        });

        // (선택 사항) 페이지 로드 시 Local Storage에 저장된 상태를 확인하여 사이드바를 설정합니다.
        // const savedState = localStorage.getItem('sidebarState');
        // if (savedState === 'collapsed') {
        //     container.classList.add('sidebar-collapsed');
        //     sidebarToggle.querySelector('.toggle-icon').textContent = '>>';
        // }
    } else {
        console.error("Sidebar toggle button or container element not found!");
    }
});