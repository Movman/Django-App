from django.views.generic.list import ListView
from .models import AuthorProfile



class AuthorListView(ListView):
    model = AuthorProfile
    template_name = 'pages/authors.html'
    context_object_name = 'authors'
    