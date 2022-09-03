from rest_framework import serializers
from .models import Comment,Domain,User,City,Question,Answer,UserAnswer


class DomainSerializer(serializers.ModelSerializer):
  class Meta:
    model=Domain
    fields="__all__"



class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model=City
    fields="__all__"

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields="__all__"

class UserSerializerShow(serializers.ModelSerializer):
  city= CitySerializer(read_only=True)
  class Meta:
    model=User
    fields="__all__"

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Comment
    fields="__all__"

class CommentSerializerShow(serializers.ModelSerializer):
  user= UserSerializerShow(read_only=True)
  class Meta:
    model=Comment
    fields="__all__"

class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model=Answer
    fields="__all__"

class QuestionSerializer(serializers.ModelSerializer):
  answers=AnswerSerializer(read_only=True,many=True)
  class Meta:
    model=Question
    fields="__all__"

class UserAnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model=UserAnswer
    fields="__all__"