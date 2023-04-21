"""skorie_leads URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import *
from web import api_views

urlpatterns = [

    path('api/lead/', api_views.LeadListCreate.as_view(), name='api_lead_list_create'),
    path('api/lead/<int:pk>/', api_views.LeadRetrieveUpdateDestroy.as_view(), name='api_lead_retrieve_update_destroy'),
    path('api/interaction/', api_views.InteractionListCreate.as_view(), name='api_interaction_list_create'),
    path('api/interaction/<int:pk>/', api_views.InteractionRetrieveUpdateDestroy.as_view(),
         name='api_interaction_retrieve_update_destroy'),
    path('api/interaction_template/<int:pk>/', api_views.InteractionTemplateRetrieveUpdateDestroy.as_view(),
         name='api_interaction_template_retrieve_update_destroy'),

    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('leads/', LeadListView.as_view(), name='lead_list'),
    path('interactions/', InteractionListView.as_view(), name='interaction_list'),
    path('interaction_templates/', InteractionTemplateListView.as_view(), name='interactiontemplate_list'),
    path('lead/create/', LeadCreateView.as_view(), name='lead_create'),
    path('lead/update/<int:pk>/', LeadUpdateView.as_view(), name='lead_update'),
    path('lead/delete/<int:pk>/', LeadDeleteView.as_view(), name='lead_delete'),
    path('interaction/create/<int:lead_id>/', InteractionCreateView.as_view(),
         name='interaction_create_with_lead'),
    path('interaction/create/', InteractionCreateView.as_view(), name='interaction_create'),
    path('interaction/update/<int:pk>/', InteractionUpdateView.as_view(), name='interaction_update'),

    path('interactiontemplate/create/', InteractionTemplateCreateView.as_view(), name='interactiontemplate_create'),
    path('interactiontemplate/update/<int:pk>/',InteractionTemplateUpdateView.as_view(), name='interactiontemplate_update'),
    path('search/', search_and_add_leads, name='search_and_add_leads'),
]

