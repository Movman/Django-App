from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from wagtail.core.models import Page
from wagtail.search.models import Query
from django.contrib import messages

from .forms import ContactForm

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
    form_class = ContactForm
    success_url = '/contact/'
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        messages.success(self.request, "Message successfully sent")

        Contact.objects.create(name=name, email=email, message=message)

        return super().form_valid(form)