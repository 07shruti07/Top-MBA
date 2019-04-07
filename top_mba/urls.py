
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import UniversityViewSet, ProgramViewSet

router = routers.DefaultRouter()
router.register(r'universities', UniversityViewSet, base_name="university")
# router.register(r'programs', ProgramViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
