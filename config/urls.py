"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pybo.views import base_views # 빨간줄에서 전구를 클릭하면 자동으로 임포트 할 수 있다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), # views.py 파일의 index 함수를 의미한다.
    # 그런데 urlpatterns에 입력한 URL은 웹 브라우저에 입력한 localhost:8000/pybo에서 호스트명 localhost와 :8000이 생략된
    # pybo/인데 호스트명과 포트는 장고가 실행되는 환경에 따라 변하는 값이며 장고가 이미 알고 있는 값이다.
    # 그리고 pybo에 슬래시(/)를 붙여 입력한 점에서 슬래시를 붙이면 사용자가 슬래시 없이 주소를 입력해도 장고가 자동으로 슬래시를 붙여
    # 준다. 이는 URL을 정규화하는 장고의 기능 덕분. 특별한 경우가 아니면 호스트명과 포트를 생략하고 끝에는 슬래시를 붙이자.

    # include ~ 는 pybo/로 시작되는 페이지 요청은 모두 pybo/urls.py 파일에 있는 URL 매핑을 참고 처리하라는 의미이다.
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'), # / 페이지에 해당하는 urlpatterns
]
