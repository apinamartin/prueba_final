from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet

router = DefaultRouter()
router.register('', ToDoViewSet)

urlpatterns = router.urls