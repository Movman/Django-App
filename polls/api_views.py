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

    # zoberiem z request ID odpovede, najdem ju a "zahlasujem" -> votes + 1
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
    except (Choice.DoesNotExist): 
        return Response({"message": "Nenasiel som Odpoved"}, status=400)
    except (KeyError):
        return Response({"message": "Neposlal si choice ;)"}, status=400)
    else:
        # vratim "updatnuty" cely question
        return Response(PollsDetailSerializer(question).data)