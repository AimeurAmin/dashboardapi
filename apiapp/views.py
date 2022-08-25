from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Comment
from .serializers import CommentSerializer


class CommentListView(
  APIView, 
  UpdateModelMixin, 
  DestroyModelMixin, 
):

  # GET COMMENT / COMMENTS
  def get(self, request, id=None):
    if id:
      try:
        queryset = Comment.objects.get(id=id)
      except Comment.DoesNotExist:
        return Response({'errors': 'This comment item does not exist.'}, status=400)
      read_serializer = CommentSerializer(queryset)
    else:
      queryset = Comment.objects.all()
      read_serializer = CommentSerializer(queryset, many=True)

    return Response(read_serializer.data)

  # POST / PUT COMMENT
  def post(self, request):
    create_serializer = CommentSerializer(data=request.data)

    if create_serializer.is_valid():      
      comment_item_object = create_serializer.save()
      read_serializer = CommentSerializer(comment_item_object)

      return Response(read_serializer.data, status=201)

    return Response(create_serializer.errors, status=400)


class AnswersListView(
  APIView, 
  UpdateModelMixin, 
  DestroyModelMixin, 
):

  def get(self, request, id=None):
    if id:
      try:
        queryset = Answer.objects.get(id=id)
      except Answer.DoesNotExist:
        return Response({'errors': 'This comment item does not exist.'}, status=400)
      read_serializer = CommentSerializer(queryset)
    else:
      queryset = Comment.objects.all()
      read_serializer = CommentSerializer(queryset, many=True)

    return Response(read_serializer.data)