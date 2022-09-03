from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

simplerouter = SimpleRouter()

router=DefaultRouter()
router.register('CommentModel', views.Commentapi)
router.register('CommentModelShow', views.CommentapiShow)
simplerouter.register('Comments', views.Commentapi)
router.register('DomainModel', views.Domainapi)
router.register('CityModel', views.Cityapi)
router.register('UserModel', views.Userapi)
router.register('UserModelShow', views.UserapiShow)
router.register('QuestionModel', views.Questionapi)
router.register('AnswerModel', views.Answerapi)
router.register('UserAnswerModel', views.UserAnswerapi)

urlpatterns = [
  path('', include(router.urls))
]