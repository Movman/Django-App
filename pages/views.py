from django.shortcuts import render
from wagtail.search.models import Query
from wagtail.core.models import Page

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
    return render(request, 'pages/blog_page.html', {
        'search_query': search_query,
        'search_results': search_results,
    })