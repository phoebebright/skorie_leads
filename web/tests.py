from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from .models import Lead, Interaction
from django.contrib.auth.models import User

class ModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_lead(self):
        lead = Lead.objects.create(
            name="Test Lead",
            website="https://testlead.com",
            facebook_page="https://facebook.com/testlead",
            contact_name="John Doe",
            contact_email="john@testlead.com",
            contact_phone="1234567890",
            lead_source="Online",
            created_by=self.user  # Add this line
        )

        self.assertEqual(lead.name, "Test Lead")

    def test_create_interaction(self):
        lead = Lead.objects.create(
            name="Test Lead",
            website="https://testlead.com",
            facebook_page="https://facebook.com/testlead",
            contact_name="John Doe",
            contact_email="john@testlead.com",
            contact_phone="1234567890",
            lead_source="Online",
            created_by=self.user  # Add this line
        )
        interaction = Interaction.objects.create(
            lead=lead,
            interaction_type="Email",
            notes="Sent an introductory email",
            interaction_date=timezone.now(),
            user=self.user,
        )
        self.assertEqual(interaction.lead, lead)

class ViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_lead_api(self):
        url = reverse('api_lead_list_create')
        data = {
            "name": "Test Lead",
            "website": "https://testlead.com",
            "facebook_page": "https://facebook.com/testlead",
            "contact_name": "John Doe",
            "contact_email": "john@testlead.com",
            "contact_phone": "1234567890",
            "lead_source": "Online",
            "created_by" : self.user.pk,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lead.objects.count(), 1)
        self.assertEqual(Lead.objects.get().name, 'Test Lead')

    def test_create_interaction_api(self):
        lead = Lead.objects.create(
            name="Test Lead",
            website="https://testlead.com",
            facebook_page="https://facebook.com/testlead",
            contact_name="John Doe",
            contact_email="john@testlead.com",
            contact_phone="1234567890",
            lead_source="Online",
            created_by=self.user
        )
        url = reverse('api_interaction_list_create')
        data = {
            "lead": lead.id,
            "interaction_type": "email",
            "interaction_date": timezone.now(),
            "user": self.user.id,
            "notes": "Sent an introductory email"
        }
        response = self.client.post(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Interaction.objects.count(), 1)
        self.assertEqual(Interaction.objects.get().notes, 'Sent an introductory email')
