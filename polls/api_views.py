from .serializers import PollsSerializer, PollsDetailSerializer
from rest_framework.response import Response
from rest_framework import generics

from .models import Question

# API views
# Making my own view ---Practice---

class PollsList(generics.ListAPIView):
        queryset = Question.objects.all()
        serializer_class = PollsSerializer


class PollsDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Question.objects.all()
        serializer_class = PollsDetailSerializer