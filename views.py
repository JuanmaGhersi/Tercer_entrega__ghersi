from django.shortcuts import render
from .forms import InsertDataForm, SearchForm
from .models import Model1, Model2, Model3

def insert_data(request):
    if request.method == 'POST':
        form = InsertDataForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = InsertDataForm()
    return render(request, 'insert_data.html', {'form': form})

def search_data(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = []
            results.extend(Model1.objects.filter(field__icontains=query))
            results.extend(Model2.objects.filter(field__icontains=query))
            results.extend(Model3.objects.filter(field__icontains=query))
            return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

def home(request):
    return render(request, 'home.html')
