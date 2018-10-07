from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class AllBoard(APIView):

    def get(self, req, format=None):

        # 1. get all boards
        
        boards = models.Board.objects.all()

        serializer = serializers.BoardSerializer(boards, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, req, format=None):

        serializer = serializers.InputBoardSerializer(data=req.data)

        if serializer.is_valid():
            
            serializer.save(creator=req.user)
            
            return Response(status=status.HTTP_201_CREATED)

        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Board(APIView):
    
    def get(self, req, board_id, format=None):

        try:
            find_board = models.Board.objects.filter(id=board_id)
        except models.Board.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.BoardSerializer(find_board, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, req, board_id, format=None):
        
        try:
            find_board = models.Board.objects.filter(id=board_id)
        except models.Board.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        find_board.delete()

        return Response(status=status.HTTP_200_OK)


class Comment(APIView):
    
    def get(self, req, board_id, format=None):
        
        try:
            find_comment = models.Comment.objects.filter(board__id=board_id)
        except models.comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(find_comment, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, req, board_id, format=None):

        find_board = models.Board.objects.get(id=board_id)

        serializer = serializers.InputCommentSerializer(data=req.data)

        if serializer.is_valid():
            
            serializer.save(creator=req.user, board=find_board)
            
            return Response(status=status.HTTP_201_CREATED)

        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)