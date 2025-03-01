from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, EventForm, CustomLoginForm
from .models import CustomUser, Event, Application
from django.utils import timezone
from django.contrib.auth.views import LoginView
from django.views.decorators.http import require_http_methods

def home(request):
    return render(request, 'home.html')

@require_http_methods(["POST"])
def custom_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect(user.get_dashboard_url())
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

# Volunteer Views
def is_volunteer(user):
    return user.is_authenticated and user.user_type == 'volunteer'

@user_passes_test(is_volunteer, login_url='login')
def opportunities_list(request):
    events = Event.objects.filter(date__gte=timezone.now().date()).order_by('date')
    applied_events = []
    if request.user.is_authenticated:
        applied_events = Application.objects.filter(
            volunteer=request.user
        ).values_list('event_id', flat=True)
    
    context = {
        'events': events,
        'applied_events': applied_events
    }
    return render(request, 'volunteer/opportunities.html', context)

@user_passes_test(is_volunteer)
def apply_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        if not Application.objects.filter(volunteer=request.user, event=event).exists():
            Application.objects.create(volunteer=request.user, event=event)
            messages.success(request, 'Application submitted successfully!')
        else:
            messages.warning(request, 'You have already applied for this event.')
    return redirect('opportunities')

# Recruiter Views
def is_recruiter(user):
    return user.is_authenticated and user.user_type == 'recruiter'

@user_passes_test(is_recruiter)
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.recruiter = request.user
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('manage_events')
    else:
        form = EventForm()
    return render(request, 'recruiter/create_event.html', {'form': form})

@user_passes_test(is_recruiter)
def manage_events(request):
    events = Event.objects.filter(recruiter=request.user).order_by('-created_at')
    return render(request, 'recruiter/manage_events.html', {'events': events})

@user_passes_test(is_recruiter)
def event_applications(request, event_id):
    event = get_object_or_404(Event, id=event_id, recruiter=request.user)
    applications = Application.objects.filter(event=event)
    
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        action = request.POST.get('action')
        
        if application_id and action in ['approve', 'reject']:
            application = get_object_or_404(Application, id=application_id, event=event)
            application.status = 'approved' if action == 'approve' else 'rejected'
            application.save()
            messages.success(request, f'Application {action}d successfully!')
            
    return render(request, 'recruiter/event_applications.html', {
        'event': event,
        'applications': applications
    })

# Admin Views
def is_admin(user):
    return user.is_authenticated and (user.user_type == 'admin' or user.is_superuser)

@user_passes_test(is_admin)
def admin_dashboard(request):
    total_volunteers = CustomUser.objects.filter(user_type='volunteer').count()
    total_recruiters = CustomUser.objects.filter(user_type='recruiter').count()
    total_events = Event.objects.count()
    total_applications = Application.objects.count()
    
    context = {
        'total_volunteers': total_volunteers,
        'total_recruiters': total_recruiters,
        'total_events': total_events,
        'total_applications': total_applications,
        'recent_users': CustomUser.objects.all().order_by('-date_joined')[:5],
        'recent_events': Event.objects.all().order_by('-created_at')[:5]
    }
    return render(request, 'admin/dashboard.html', context)

@user_passes_test(is_admin)
def user_management(request):
    users = CustomUser.objects.all().order_by('-date_joined')
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        
        if user_id and action:
            user = get_object_or_404(CustomUser, id=user_id)
            if action == 'activate':
                user.is_active = True
                messages.success(request, f'User {user.username} has been activated.')
            elif action == 'deactivate':
                user.is_active = False
                messages.success(request, f'User {user.username} has been deactivated.')
            elif action == 'delete':
                user.delete()
                messages.success(request, f'User {user.username} has been deleted.')
                return redirect('user_management')
            user.save()
    
    return render(request, 'admin/user_management.html', {'users': users})

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        return self.request.user.get_dashboard_url() 