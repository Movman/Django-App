import datetime
import json

from django.db.models.query_utils import Q
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import response, status

from .models import Choice, Question
from .serializers import PollsSerializer, PollsDetailSerializer, ChoiceSerializer


# Create your tests here.
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(pub_date = time)
    
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)

        self.assertIs(recent_question.was_published_recently(), True)



def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def create_question_with_choices(question_text, choice_text_1, choice_text_2):
    question = create_question(question_text, -1)
    Choice.objects.create(question=question, choice_text=choice_text_1)
    Choice.objects.create(question=question, choice_text=choice_text_2)
    return question



class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

    def test_question_with_choices(self):
        """
        Otestujem ci na detaile Question sa mi zobrazia Choices.
        """
        # SETUP
        question = create_question(question_text='Past Question.', days=-5)
        Choice.objects.create(question=question, choice_text='Dobre')
        Choice.objects.create(question=question, choice_text='Zle')
        self.assertEqual(question.choices.count(), 2)

        # ACTION
        # idem na detail question
        url = reverse('polls:detail', args=(question.id,))
        response = self.client.get(url)
        # pozriem ci je tam text otazky
        self.assertContains(response, question.question_text)
        # pozriem ci mam aj odpovede (choices)
        # import pdb;pdb.set_trace() # "zastavi beh pythonu" - pouzi `c` pre continue
        self.assertContains(response, 'Dobre')
        self.assertContains(response, 'Zle')


class QuestionVoteViewTests(TestCase):
    # dorobit ;)
    def test_can_vote(self):
        # setup
        question = create_question_with_choices('Aky je den?', 'Piatok', 'Pondelok')
        choice = question.choices.first()
        self.assertEqual(question.choices.count(), 2)
        self.assertEqual(choice.votes, 0)

        # akcia
        url = reverse('polls:vote', args=(question.id,))
        self.assertEqual(url, '/polls/1/vote/')
        response = self.client.post(url, {'choice': choice.id})
        self.assertEqual(response.status_code, 302)

        # TEST
        choice.refresh_from_db()
        self.assertEqual(choice.votes, 1)



class PollsTestCase(APITestCase):
    def test_non_exist_polls_list(self):
        # Setup - none
        # with empty DB its empty JSON response
        # Action:
        response = self.client.get("/api/polls/")
        # Test
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_can_create_poll(self):
    #     # Setup - create object in DB
    #     data = Question.objects.create({'question_text': 'test'})
    #     # Action
    #     response = self.client.post("/api/polls/", data)
    #     # Test
    #     self.assertEqual(response.data == data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_non_exist_polls_vote(self):
        # empty DB - error expected
        response = self.client.post("/api/polls/votes/1/", {})
        # mal by to byt JSON 
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_vote_poll(self):
        # setup
        question = create_question_with_choices('Aky je den?', 'Piatok', 'Pondelok')
        choice = question.choices.first()
        self.assertEqual(question.choices.count(), 2)
        self.assertEqual(choice.votes, 0)

        url = reverse("polls-votes", args=(question.id,))

        self.assertEqual(url, "/api/polls/1/vote/")
        # akciu
        response = self.client.post(url, {'choice': choice.id})

        # TEST :)
        choice.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(choice.votes, 1)

    def test_cannot_vote_poll_with_nonexisting_choice(self):
        # setup
        question = create_question_with_choices('Aky je den?', 'Piatok', 'Pondelok')

        url = reverse("polls-votes", args=(question.id,))

        self.assertEqual(url, "/api/polls/1/vote/")
        # akciu
        response = self.client.post(url, {'choice': 238746})

        # TEST :)
        self.assertEqual(response.status_code, 400)


    def test_cannot_vote_poll_with_no_data_sent(self):
        # setup
        question = create_question_with_choices('Aky je den?', 'Piatok', 'Pondelok')

        url = reverse("polls-votes", args=(question.id,))

        self.assertEqual(url, "/api/polls/1/vote/")
        # akciu
        response = self.client.post(url)

        # TEST :)
        self.assertEqual(response.status_code, 400)