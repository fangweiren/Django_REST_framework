from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from snippets import views

# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API URL 现在由路由器自动确定。
urlpatterns = [
    url(r'^', include(router.urls))
]
