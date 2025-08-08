from rest_framework.routers import DefaultRouter
from .views import DistrictViewSet

router = DefaultRouter()
router.register(r'districts', DistrictViewSet)

urlpatterns = router.urls
