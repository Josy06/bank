from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, Branch
from django.shortcuts import render, redirect
from .models import Team

def home(request): # ORM form
    team = Team.objects.all()
    return render(request, "index.html", {'team': team})


def form_page(request):
    return render(request, 'Form page.html')
# def person_create_view(request):
#     form = PersonCreationForm()
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('person_add')
#     return render(request, 'persons/home.html', {'form': form})
#
#
# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request, 'persons/home.html', {'form': form})
#
#
#
# # AJAX
# def load_cities(request):
#     country_id = request.GET.get('country_id')
#     cities = Branch.objects.filter(country_id=country_id).all()
#     return render(request, 'Form page.html', {'cities': cities})

