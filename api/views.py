from django.shortcuts import render
from rest_framework import viewsets
from .models import Articles
from .serializers import ArticleSerializer

# Create your views here.
class ArticleView(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    