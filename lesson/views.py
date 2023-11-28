from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Category, Author, Course
from .serializers import CategorySerializer, CourseSerializer, AuthorSerializer

from rest_framework.response import Response

from rest_framework import viewsets, generics


@api_view(['GET'])
def homepage(request):
    category = Category.objects.all()
    author = Author.objects.all()
    course = Course.objects.all()

    serializerCategory = CategorySerializer(category, many=True)
    serializerAuthor = AuthorSerializer(author, many=True)
    serializerCourse = CourseSerializer(course, many=True)

    return Response({
        'category': serializerCategory.data,
        'author': serializerAuthor.data,
        'course': serializerCourse.data
    })


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


