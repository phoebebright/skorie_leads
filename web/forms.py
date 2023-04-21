
from django import forms
from django.utils import timezone

from .models import Lead, Interaction, InteractionTemplate


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead

        exclude = ['created','created_by']

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.creator = self.request.user
        return super().form_valid(form)

class InteractionForm(forms.ModelForm):
    templates = forms.ModelChoiceField(queryset=InteractionTemplate.objects.all(), required=False)
    class Meta:
        model = Interaction
        fields = ['lead', 'interaction_type','notes']


    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.interaction_date = timezone.now()
        # if self.request.user.is_authenticated:
        #     instance.creator = self.request.user
        if commit:
            instance.save()
        return instance

class InteractionTemplateForm(forms.ModelForm):
    class Meta:
        model = InteractionTemplate
        fields = ['name','template_contents']

