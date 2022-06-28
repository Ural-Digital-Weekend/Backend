from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from avia.models import Comment, Airport
from avia.serializers import CommentListSerializer, CommentSerializer


class CommentsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    queryset = Comment.objects
    ordering = ('-created',)  # Сортировка по умолчанию

    def get_queryset(self):
        queryset = super(CommentsViewSet, self).get_queryset()

        airport_id = self.kwargs.get('airport_id')

        if not Airport.objects.filter(id=airport_id).count():
            raise Http404

        queryset = queryset.filter(airport_id=airport_id)
        return queryset

    def get_object(self):
        comment_id = self.kwargs.get('pk')
        user_id = self.request.user.id
        comment = Comment.objects.filter(id=comment_id, user=user_id).first()

        if comment:
            return comment

        raise Http404

    def list(self, request, *args, **kwargs):
        self.permission_classes = []
        self.serializer_class = CommentListSerializer
        return super(CommentsViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data={
            "airport": kwargs.get('airport_id'),
            "user": request.user.id,
            "comment": request.data.get("comment")
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = self.serializer_class(comment, data={
            "airport": comment.airport_id,
            "user": request.user.id,
            "comment": request.data.get("comment")
        })
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        data = self.get_serializer(comment).data
        return Response(data=data, status=status.HTTP_200_OK)

    def remove(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
