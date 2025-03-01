from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from accounts.views import (
    CustomLoginView, 
    signup, 
    dashboard, 
    opportunities_list, 
    apply_for_event, 
    create_event, 
    manage_events, 
    event_applications, 
    admin_dashboard, 
    user_management,
    home,
    custom_logout,
)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    
    # Volunteer URLs
    path('opportunities/', opportunities_list, name='opportunities'),
    path('apply/<int:event_id>/', apply_for_event, name='apply_for_event'),
    
    # Recruiter URLs
    path('events/create/', create_event, name='create_event'),
    path('events/manage/', manage_events, name='manage_events'),
    path('events/<int:event_id>/applications/', event_applications, name='event_applications'),
    
    # Admin URLs
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin/users/', user_management, name='user_management'),
    
    # Include default auth URLs for password reset
    path('accounts/', include('django.contrib.auth.urls')),
] 