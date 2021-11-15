from rest_framework.decorators import api_view
from .serializers import PollsSerializer, ChoiceSerializer, PollsDetailSerializer
from rest_framework.response import Response

from .models import Question, Choice

# API views
# Making my own view ---Practice---

@api_view(['GET'])
def pollsList(request):
    question = Question.objects.all()
    serializer = PollsSerializer(question, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def pollsDetail(request, pk):
    poll = Question.objects.get(id=pk)
    # serializer = ChoiceSerializer(choice, many=True)
    serializer = PollsDetailSerializer(poll)

    return Response(serializer.data)