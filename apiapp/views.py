from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Comment, Domain, User, UserAnswer, Question, Answer, City
from .serializers import CommentSerializer, DomainSerializer, UserSerializer, UserAnswerSerializer, QuestionSerializer, AnswerSerializer, CitySerializer

from rest_framework.decorators import action
from rest_framework.response import Response

import apiapp.helpers.classifier as classifier

class CountModelMixin(object):
    """
    Count a queryset.
    """
    @action(detail=False)
    def count(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        content = {'count': queryset.count()}
        return Response(content)

class Commentapi(viewsets.ModelViewSet, CountModelMixin):
  queryset=Comment.objects.all()
  serializer_class=CommentSerializer
  @action(detail=False, methods=['post'])
  def classify(self, request):
    
    comment = request.data.get('comment')
    prediction = classifier.classifyComment(comment)
    return Response({'result': prediction})

class Domainapi(viewsets.ModelViewSet, CountModelMixin):
  queryset=Domain.objects.all()
  serializer_class=DomainSerializer

class Userapi(viewsets.ModelViewSet, CountModelMixin):
  queryset=User.objects.all()
  serializer_class=UserSerializer


class UserAnswerapi(viewsets.ModelViewSet, CountModelMixin):
  queryset=UserAnswer.objects.all()
  serializer_class=UserAnswerSerializer


class Questionapi(viewsets.ModelViewSet, CountModelMixin):
  queryset=Question.objects.all()
  serializer_class=QuestionSerializer


class Answerapi(viewsets.ModelViewSet, CountModelMixin):
  queryset=Answer.objects.all()
  serializer_class=AnswerSerializer

class Cityapi(viewsets.ModelViewSet, CountModelMixin):
  queryset=City.objects.all()
  serializer_class=CitySerializer