from .serializers import PollsSerializer, PollsDetailSerializer, ChoiceSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view

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
    votes = Choice.objects.get(id = pk)
    serializer = ChoiceSerializer(instance=votes, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)