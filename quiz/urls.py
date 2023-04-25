from rest_framework import routers
from .views import (
    QuizCategoryViewSet,
    QuizViewSet,
    QuizStudentViewSet,
    QuestionViewSet,
    OptionViewSet,
    AnswerViewSet,
    AnswerStudentViewSet
)

router = routers.DefaultRouter()
router.register(r'api/category', QuizCategoryViewSet)
router.register(r'api/moderator/quiz', QuizViewSet),
router.register(r'api/student/quiz', QuizStudentViewSet)
router.register(r'api/question', QuestionViewSet)
router.register(r'api/option', OptionViewSet)
router.register(r'api/moderator/answer', AnswerViewSet)
router.register(r'api/student/answer', AnswerStudentViewSet)

urlpatterns = []

urlpatterns += router.urls




