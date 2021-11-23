from .serializers import PollsSerializer, PollsDetailSerializer, ChoiceSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Choice, Question

# API views
# Making my own view ---Practice---

class PollsList(generics.ListAPIView):
        queryset = Question.objects.all()
        serializer_class = PollsSerializer


class PollsDetail(generics.RetrieveAPIView):
        queryset = Question.objects.all()
        serializer_class = PollsDetailSerializer


@api_view(['POST'])
def voteView(request, pk):
    question = get_object_or_404(Question, pk=pk)
    serializer = PollsDetailSerializer(question, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)