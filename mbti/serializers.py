from rest_framework import serializers
from .models import MbtiQuestion, Mbti

class MbitQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MbtiQuestion
        fields = ('title', 'body', 'answer',)

class MbitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mbti
        fields = ('name', 'description',)