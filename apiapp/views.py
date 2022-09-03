from curses import meta
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Comment, Domain, User, UserAnswer, Question, Answer, City
from .serializers import CommentSerializer, CommentSerializerShow, DomainSerializer, UserSerializer, UserAnswerSerializer, QuestionSerializer, AnswerSerializer, CitySerializer, UserSerializerShow
from django.core import serializers

from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse

import apiapp.helpers.classifier as classifier
import json

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
  @action(detail=False, methods=['post', 'get'])
  def classify(self, request):
    if(request.method == 'POST'):
      comment = request.data.get('comment')
      prediction = classifier.classifyComment(comment)
      return Response({'result': prediction})

    if(request.method == 'GET'):
      return Response({'ok': '1'})

  @action(detail=False, methods=['get'])
  def CountComments(self, request):
    querySet=Comment.objects.all()
    comments = CommentSerializer(querySet)
    return JsonResponse(comments.data)


class CommentapiShow(viewsets.ModelViewSet, CountModelMixin):
  queryset=Comment.objects.all()
  serializer_class=CommentSerializerShow

class Domainapi(viewsets.ModelViewSet, CountModelMixin):
  queryset=Domain.objects.all()
  serializer_class=DomainSerializer

class Userapi(viewsets.ModelViewSet, CountModelMixin):
  queryset=User.objects.all()
  serializer_class=UserSerializer

class UserapiShow(viewsets.ModelViewSet, CountModelMixin):
  queryset=User.objects.all()
  serializer_class=UserSerializerShow

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