from rest_framework import serializers

from polls.models import Choice, Question

class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'question', 'votes']


class PollsDetailSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many = True)
    
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'choices']