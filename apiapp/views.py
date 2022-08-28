from rest_framework import viewsets
from .models import Comment, Domain, User, UserAnswer, Question, Answer, City
from .serializers import CommentSerializer, DomainSerializer, UserSerializer, UserAnswerSerializer, QuestionSerializer, AnswerSerializer, CitySerializer

class Commentapi(viewsets.ModelViewSet):
  queryset=Comment.objects.all()
  serializer_class=CommentSerializer

class Domainapi(viewsets.ModelViewSet):
  queryset=Domain.objects.all()
  serializer_class=DomainSerializer

class Userapi(viewsets.ModelViewSet):
  queryset=User.objects.all()
  serializer_class=UserSerializer


class UserAnswerapi(viewsets.ModelViewSet):
  queryset=UserAnswer.objects.all()
  serializer_class=UserAnswerSerializer


class Questionapi(viewsets.ModelViewSet):
  queryset=Question.objects.all()
  serializer_class=QuestionSerializer


class Answerapi(viewsets.ModelViewSet):
  queryset=Answer.objects.all()
  serializer_class=AnswerSerializer

class Cityapi(viewsets.ModelViewSet):
  queryset=City.objects.all()
  serializer_class=CitySerializer