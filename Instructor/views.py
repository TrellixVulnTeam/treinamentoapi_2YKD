from Instructor.pagination import CustomPageNumberPagination
from Instructor.serializers import InstructorSerializer
from django.shortcuts import render
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from Instructor.models import Instructor
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class InstructorAPIView(ListCreateAPIView):
    serializer_class = InstructorSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'name']

    def perform_create(self, serializer):
        return serializer.save(username=self.request.user)

    def get_queryset(self):
        return Instructor.objects.filter(username=self.request.user)


class InstructorDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer

    permission_classes = (IsAuthenticated,)

    lookup_field = "id"

    def get_queryset(self):
        return Instructor.objects.filter(username=self.request.user)