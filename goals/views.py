# from django.db import transaction
# from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination

# from goals.filters import GoalDateFilter
from goals.models import GoalCategory#, Goal, GoalComment, Board
#from goals.permissions import BoardPermissions, GoalCategoryPermissions#, IsOwnerOrReadOnly, GoalPermissions, \
#     CommentPermissions
from goals.serializer import GoalCategoryCreateSerializer, GoalCategorySerializer, GoalCreateSerializer#, \
    # GoalSerializer, GoalCommentCreateSerializer, GoalCommentSerializer, BoardCreateSerializer, BoardSerializer, \
    # BoardListSerializer

class GoalCategoryCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCategoryCreateSerializer

class GoalCategoryListView(ListAPIView):
    model = GoalCategory
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GoalCategorySerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    #filterset_fields = ["board"]

    ordering_fields = ["title", "created"]
    ordering = ["title"]
    search_fields = ["title"]

    def get_queryset(self):
        return GoalCategory.objects.filter(
            user=self.request.user,
            is_deleted=False
        )

class GoalCategoryView(RetrieveUpdateDestroyAPIView):
    model = GoalCategory
    serializer_class = GoalCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return GoalCategory.objects.filter(
            user=self.request.user,
            is_deleted=False
        )

    def perform_destroy(self, instance: GoalCategory):
        instance.is_deleted = True
        instance.save(update_fields=("is_deleted",))
        return instance

class GoalCreateView(CreateAPIView):
    serializer_class = GoalCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

