from rest_framework import serializers
from v2x_solution.users import serializers as user_serializers
from . import models

class BoardSerializer(serializers.ModelSerializer):

    creator = user_serializers.UserSerializer()

    class Meta:
        model = models.Board
        fields = (
            'id',
            'title',
            'message',
            'creator',
            'created_at'
        )

class CommentSerializer(serializers.ModelSerializer):

    board = BoardSerializer()
    creator = user_serializers.UserSerializer()

    class Meta:
        model = models.Comment
        fields = (
            'comment',
            'creator',
            'board',
            'created_at'
        )

class InputBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Board
        fields = (
            'title',
            'message',
        )

class InputCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = (
            'comment',
        )