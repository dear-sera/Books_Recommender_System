from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views.book import *
from api.views.best import *

app_name = "api"

router = DefaultRouter()  # viewset 은 router 를 사용하여 URL 을 관리할 수 있습니다.
router.register(r"book", BookModelViewSet)
router.register(r"best", BestsellerModelViewSet)

urlpatterns = [
    path("", include(router.urls)),  # 위에 선언한 router 를 사용
]
