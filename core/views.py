from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Event, TeamMember
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'core/home.html')

from django.db.models import Case, When, IntegerField

def meet_team(request):
    role_order = Case(
        When(role='President', then=1),
        When(role='Vice President', then=2),
        When(role='Event Head', then=3),
        When(role='Management Head', then=4),
        When(role='Secretary', then=5),
        When(role='Core Committee Member', then=6),
        When(role='Coordinator', then=7),
        When(role='Design Team Member', then=8),
        When(role='Committee Member', then=9),
        default=10,
        output_field=IntegerField()
    )

    team_members = TeamMember.objects.annotate(
        role_priority=role_order
    ).order_by('role_priority', 'name')

    return render(request, 'core/meet_team.html', {'team_members': team_members})


def signup_view(request):
    """
    User signup view with email field.
    Uses Django's session-based authentication - login() creates a session.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-login after signup using session-based authentication
            # login() function creates a session and stores user ID in session
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)  # Creates session, stores user in request.session
                return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})


@require_http_methods(["GET"])
def events_api(request):
    """API endpoint to get all events as JSON."""
    events = Event.objects.all()
    events_data = [
        {
            'id': event.id,
            'title': event.title,
            'date': event.date.strftime('%B %d, %Y'),
            'description': event.description,
            'registration_link': event.registration_link,
        }
        for event in events
    ]
    return JsonResponse({'events': events_data})


@require_http_methods(["GET"])
def team_api(request):
    """API endpoint to get all team members as JSON."""
    team = TeamMember.objects.all().order_by('-role', 'name')
    team_data = [
        {
            'id': member.id,
            'name': member.name,
            'role': member.role,
            'bio': member.bio,
            'photo': member.photo.url if member.photo else None,
        }
        for member in team
    ]
    return JsonResponse({'team': team_data})

