

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from address.models import AddressField

class Lead(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    facebook_page = models.URLField(blank=True, null=True)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    country = models.CharField(max_length=30, blank=True, null=True)
    lead_source = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.name


class Interaction(models.Model):

    INTERACTION_TYPE_CHOICES = (
        ('email', 'Email'),
        ('phone_call', 'Phone Call'),
        ('in_person_meeting', 'In-Person Meeting'),
        ('video_call', 'Video Call'),
        ('social_media', 'Social Media'),
        ('other', 'Other'),

    )
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    interaction_date = models.DateTimeField()
    interaction_type = models.CharField(max_length=30, choices=INTERACTION_TYPE_CHOICES)
    notes = models.TextField()

    def __str__(self):
        return f'{self.lead.name} - {self.interaction_date}'


class InteractionTemplate(models.Model):

    name = models.CharField(max_length=255)
    template_contents = models.TextField()

    def __str__(self):
        return self.name