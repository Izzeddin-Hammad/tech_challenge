from django.shortcuts import render
from .models import countries

def home(request):
    query = request.GET.get('q')

    results = countries.objects.all()

    if query:
        results = results.filter(country_name__icontains=query)

    context = {
        'results': results,
        'query': query
    }
    
    return render(request, 'home.html', context)