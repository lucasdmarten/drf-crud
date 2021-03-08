from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from core import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('navers', views.NaverViewSet)
router.register('projetos', views.ProjetoViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


