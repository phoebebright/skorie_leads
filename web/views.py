from django.core.checks import messages
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Lead, Interaction, InteractionTemplate
from .forms import LeadForm, InteractionForm, InteractionTemplateForm
from .search_module import search


def home(request):
    return render(request, 'home.html')


class LeadListView(ListView):
    model = Lead
    template_name = 'lead_list.html'

class InteractionListView(ListView):
    model = Interaction
    template_name = 'interaction_list.html'

class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'lead_form.html'
    success_url = reverse_lazy('lead_list')


class LeadUpdateView(UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'lead_form.html'
    success_url = reverse_lazy('lead_list')

class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'lead_confirm_delete.html'
    success_url = reverse_lazy('lead_list')

class InteractionCreateView(CreateView):
    model = Interaction
    form_class = InteractionForm
    template_name = 'interaction_form.html'
    success_url = reverse_lazy('lead_list')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user

        lead_id = self.kwargs.get('lead_id')
        if lead_id:
            lead = get_object_or_404(Lead, id=lead_id)
            initial['lead'] = lead

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lead'] = Lead.objects.get(id=self.kwargs.get('lead_id'))
        return context

class InteractionUpdateView(UpdateView):
    model = Interaction
    form_class = InteractionForm
    template_name = 'interaction_form.html'
    success_url = reverse_lazy('lead_list')



def search_and_add_leads(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        search_results = search(query)

        existing_leads = Lead.objects.values_list('website', flat=True)
        new_results = [result for result in search_results if result['website'] not in existing_leads]

        context = {
            'search_results': new_results,
        }

        return render(request, 'search_results.html', context)

    return render(request, 'search_form.html')


class InteractionTemplateListView(ListView):
    model = InteractionTemplate
    template_name = 'interactiontemplate_list.html'

class InteractionTemplateCreateView(CreateView):
    model = InteractionTemplate
    form_class = InteractionTemplateForm
    template_name = 'interactiontemplate_form.html'
    success_url = reverse_lazy('interactiontemplate_list')


class InteractionTemplateUpdateView(UpdateView):
    model = InteractionTemplate
    form_class = InteractionTemplateForm
    template_name = 'interactiontemplate_form.html'
    success_url = reverse_lazy('interactiontemplate_list')

class InteractionTemplateDeleteView(DeleteView):
    model = InteractionTemplate
    template_name = 'interactiontemplate_form_confirm_delete.html'
    success_url = reverse_lazy('interactiontemplate_list')