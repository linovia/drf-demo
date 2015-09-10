from rest_framework import routers
from drf_demo.model_less.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, base_name='tasks')
urlpatterns = router.urls
