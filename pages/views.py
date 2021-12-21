from django.shortcuts import render, redirect
from wagtail.search.models import Query
from wagtail.core.models import Page
from pages.models import Contact
from django.http import HttpResponse
from django.views.generic.edit import FormView

from django.core.mail import send_mail
# Create your views here.

def search(request):
    # Search
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = Page.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Render template
    return render(request, 'search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
    })


class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = Contact

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)