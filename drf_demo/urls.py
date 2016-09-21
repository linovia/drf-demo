from rest_framework import routers
from drf_demo.api.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, base_name='tasks')
urlpatterns = router.urls
