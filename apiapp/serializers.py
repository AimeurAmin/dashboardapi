from rest_framework import serializers

from .models import Comment, Domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
      model = Domain
      fields = ('id', 'domain_name')


class CommentSerializer(serializers.ModelSerializer):
  # comment = serializers.CharField(max_length=500, required=True)
  domain = DomainSerializer()

  def create(self, validated_data):
    return Comment.objects.create(
      comment=validated_data.get('comment')
    )

  def update(self, instance, validated_data):
    instance.comment = validated_data.get('comment', instance.comment)
    instance.save()
    return instance

  class Meta:
    model = Comment
    fields = (
      'id',
      'comment',
      'domain'
    )