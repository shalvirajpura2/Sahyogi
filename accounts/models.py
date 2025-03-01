from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('volunteer', 'Volunteer'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='volunteer')
    phone_number = models.CharField(max_length=15, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    
    def get_dashboard_url(self):
        if self.user_type == 'volunteer':
            return reverse('opportunities')
        elif self.user_type == 'recruiter':
            return reverse('manage_events')
        else:
            return reverse('admin_dashboard')

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    recruiter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_events')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_applications', args=[str(self.id)])

class Application(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    
    volunteer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('volunteer', 'event')
        ordering = ['-applied_at'] 