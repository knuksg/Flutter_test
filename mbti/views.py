from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MbtiQuestion
from .serializers import MbitQuestionSerializer
import random
from rest_framework import viewsets

# Create your views here.
@api_view(['GET'])
def randomQuestion(request, id):
    totalQuestions = MbtiQuestion.objects.all()
    randomQuestions = random.sample(list(totalQuestions), id)
    serializer = MbitQuestionSerializer(randomQuestions, many=True)
    return Response(serializer.data)

class MbtiView(viewsets.ModelViewSet):
    queryset = MbtiQuestion.objects.order_by('?')[:3]
    serializer_class = MbitQuestionSerializer
