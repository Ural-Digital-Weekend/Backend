from django.http import Http404
from drf_spectacular.utils import extend_schema, OpenApiResponse, inline_serializer
from rest_framework import status, serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from avia.api.schemas import order_parameter, pagination_parameters, response_400, response_201
from avia.api.schemas.responses import response_200, response_204, response_401, response_403
from avia.models import Comment, Airport
from avia.serializers import CommentListSerializer, CommentSerializer

comment_request = inline_serializer(
    name="CommentRequest",
    fields={
        "comment": serializers.CharField()
    }
)


class CommentsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    filter_backends = [OrderingFilter]

    queryset = Comment.objects
    ordering = ('created',)  # Сортировка по умолчанию

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
        comment = Comment.objects.filter(id=comment_id)

        if not comment:
            raise Http404

        comment = comment.filter(user=user_id).first()

        if not comment:
            raise PermissionDenied

        return comment



    @extend_schema(
        summary="Получение комментариев об аэропорте",
        tags=['Airports | Comments'],
        parameters=[
            order_parameter,
            *pagination_parameters
        ],
        responses={
            200: OpenApiResponse(
                description="Успешно получен список комментариев к аэропорту",
                response=CommentListSerializer,
            ),
            400: response_400,
        }
    )
    def list(self, request, *args, **kwargs):
        self.serializer_class = CommentListSerializer
        return super(CommentsViewSet, self).list(request, *args, **kwargs)

    @extend_schema(
        summary="Добавления комментария об аэропорте",
        tags=['Airports | Comments'],
        request=comment_request,
        responses={
            201: response_201,
            400: response_400,
            401: response_401,
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data={
            "airport": kwargs.get('airport_id'),
            "user": request.user.id,
            "comment": request.data.get("comment")
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        summary="Обновление комментария об аэропорте",
        tags=['Airports | Comments'],
        request=comment_request,
        responses={
            200: response_200,
            400: response_400,
            403: response_403,
        }
    )
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

    @extend_schema(
        summary="Удаление комментария об аэропорте",
        tags=['Airports | Comments'],
        responses={
            200: response_204,
            400: response_400,
            403: response_403,
        }
    )
    def remove(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
