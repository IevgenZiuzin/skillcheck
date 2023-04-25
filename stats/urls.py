from rest_framework import routers
from .views import ModeratorCompletionViewSet, StudentCompletionViewSet

router = routers.DefaultRouter()
router.register(r'api/completions/moderator', ModeratorCompletionViewSet)
router.register(r'api/completions/student', StudentCompletionViewSet)

urlpatterns = []

urlpatterns += router.urls
