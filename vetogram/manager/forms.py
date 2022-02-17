from django import forms
from .models import Owner, Patient
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# CRUD - Create
class OwnerCreateForm(PermissionRequiredMixin, forms.ModelForm):
    permission_required = 'manager.ownercreate'
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'phone','email')

class PatientCreateForm(PermissionRequiredMixin, forms.ModelForm):
    permission_required = 'manager.patientcreate'
    class Meta:
        model = Patient
        fields = ('pet_name', 'animal_type', 'breed', 'age', 'owner')


#CRUD - Update
class OwnerUpdateForm(PermissionRequiredMixin, forms.ModelForm):
    permission_required = 'manager.ownerupdate'
    #form for updating owners
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'phone','email')

class PatientUpdateForm(PermissionRequiredMixin, forms.ModelForm):
    permission_required = 'manager.patientupdate'
    #form for updating patients
    class Meta:
        model = Patient
        fields = ('pet_name', 'animal_type', 'breed', 'age', 'owner','description')