from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from diveapp.models import *
from django.views.generic import ListView
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Locacija, DiveClub
from django.shortcuts import render, redirect
from .forms import DiverProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now




def diver_profile(request):
    diver, created = Diver.objects.get_or_create(user=request.user)  
    
    if request.method == 'POST':
        form = DiverProfileForm(request.POST, instance=diver)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = DiverProfileForm(instance=diver)
    
    return render(request, 'diveapp/diver_profile.html', {'form': form})


def pridruzi_se_klubu(request, club_id):
    klub = get_object_or_404(DiveClub, id=club_id)
    diver = request.user.diver
    diver.clanstvo.add(klub)  
    return redirect('prijava_klub')  

def izlaz_klub(request, club_id):
    klub = get_object_or_404(DiveClub, id=club_id)
    diver = request.user.diver
    diver.clanstvo.remove(klub)
    return redirect('prijava_klub')

def prijava_klub(request):
    klubovi = DiveClub.objects.all()
    diver = request.user.diver
    
    
    query = request.GET.get('q')
    if query:
        klubovi = klubovi.filter(naziv__icontains=query)

    
    filter_option = request.GET.get('filter')
    if filter_option == 'moji':
        klubovi = klubovi.filter(id__in=diver.clanstvo.all())
    elif filter_option == 'dostupni':
        klubovi = klubovi.exclude(id__in=diver.clanstvo.all())

    return render(request, 'prijava_klub.html', {'klubovi': klubovi})


def lokacije_all(request):
    lokacije = Locacija.objects.select_related('divclub').all()
    diver = request.user.diver   # uzmemo tekućeg korisnika

    
    moji_klubovi = diver.clanstvo.all() # polje sa svim klubovima upišemo 

    
    od = request.GET.get('od')
    do = request.GET.get('do')
    if od and do:
        lokacije = lokacije.filter(stvoreno__date__range=[od, do])

   
    filter_option = request.GET.get('filter')
    if filter_option == 'moje':
        
        lokacije = lokacije.filter(divclub__in=moji_klubovi)
    elif filter_option == 'dostupne':
       
        lokacije = lokacije.filter(divclub__in=moji_klubovi)

    return render(request, 'diveapp/lokacije.html', {
        'lokacije': lokacije,
        'moji_klubovi': moji_klubovi
    })


def lokacije(request):
    user = request.user
    if hasattr(user, 'diver'):  
        diver = user.diver
    else:
        diver = Diver.objects.create(user=user)  
    
    sve_lokacije = Locacija.objects.all()
    
    if 'filter' in request.GET:
        if request.GET['filter'] == 'moje':
            sve_lokacije = sve_lokacije.filter(clanstvo=diver)
        elif request.GET['filter'] == 'dostupne':
            sve_lokacije = sve_lokacije.exclude(clanstvo=diver)

    return render(request, 'lokacije.html', {'lokacije': sve_lokacije})


def lokacija_list(request):
    lokacije = Locacija.objects.all()
    return render(request, 'lokacija_list.html', {'lokacije_list': lokacije})

def pridruzi_se(request, lokacija_id):
    lokacija = get_object_or_404(Locacija, id=lokacija_id)
    lokacija.clanstvo.add(request.user.diver)
    return redirect('lokacije')


def odjavi_se(request, lokacija_id):
    lokacija = get_object_or_404(Locacija, id=lokacija_id)
    lokacija.clanstvo.remove(request.user.diver)
    return redirect('lokacije')

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
        location_list = Locacija.objects.all()

    # Return the rendered page with filtered or all objects
    context = {
        'vlasnik_club_list': vlasnik_club_list,
        'dive_club_list': dive_club_list,
        'diver_list': diver_list,
        'location_list': location_list,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'diveapp/lista_svih_sort.html', context)