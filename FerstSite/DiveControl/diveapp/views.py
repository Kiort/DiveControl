from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from diveapp.models import *
from django.views.generic import ListView
from datetime import datetime


def index(request):
    return render(request, 'diveapp/index.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

class VlasnikClubList(ListView):
    model = VlasnikClub
class DiverList(ListView):
    model=Diver
class DiveclubList(ListView):
    model=DiveClub
class lokacijaList(ListView):
    model=Locacija
class DClist(ListView):
    model=DC

def sviobjekti(request):
     # Get date filters from the GET request (if provided)
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Check if both start_date and end_date are provided
    if start_date and end_date:
        try:
            # Parse the date strings to datetime objects
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            
            # Apply the filters using 'stvoreno' field (the creation date)
            vlasnik_club_list = VlasnikClub.objects.filter(stvoreno__range=[start_date, end_date])
            dive_club_list = DiveClub.objects.filter(stvoreno__range=[start_date, end_date])
            diver_list = Diver.objects.filter(stvoreno__range=[start_date, end_date])
            dc_list = DC.objects.filter(stvoreno__range=[start_date, end_date])
            location_list = Locacija.objects.filter(stvoreno__range=[start_date, end_date])
        except ValueError:
            # If there's an error parsing the dates, return all objects
            return render(request, 'diveapp/lista_svih_sort.html', {
                'error': 'Invalid date format. Please use YYYY-MM-DD.'
            })
    else:
        # If no date filters are applied, show all objects
        vlasnik_club_list = VlasnikClub.objects.all()
        dive_club_list = DiveClub.objects.all()
        diver_list = Diver.objects.all()
        dc_list = DC.objects.all()
        location_list = Locacija.objects.all()

    # Return the rendered page with filtered or all objects
    context = {
        'vlasnik_club_list': vlasnik_club_list,
        'dive_club_list': dive_club_list,
        'diver_list': diver_list,
        'dc_list': dc_list,
        'location_list': location_list,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'diveapp/lista_svih_sort.html', context)