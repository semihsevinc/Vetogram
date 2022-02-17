from django.shortcuts import render,redirect
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from manager.signup import SignUpForm
from django.db.models import Q


from .models import Owner, Patient
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, PatientUpdateForm

# Create your views here.

def home(request):
   context = {"name": request.user}
   return render(request, 'manager/home.html', context)

# CRUD - (R)ead
class OwnerList(LoginRequiredMixin, ListView):
   model = Owner
    
    
class PatientList(LoginRequiredMixin, ListView):
    model = Patient


class OwnerCreate(PermissionRequiredMixin, CreateView):
   permission_required = 'manager.ownercreate'
   model = Owner
   template_name = 'manager/owner_create_form.html'
   form_class = OwnerCreateForm

class PatientCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'manager.patientcreate'
    model=Patient
    template_name = 'manager/patient_create_form.html'
    form_class = PatientCreateForm

# CRUD - (U)pdate
class OwnerUpdate(PermissionRequiredMixin, UpdateView):
   permission_required = 'manager.ownerupdate'
   model = Owner
   template_name = 'manager/owner_update_form.html'
   form_class = OwnerUpdateForm

   def save_form(self, form):
       form.save()
       pass
class PatientUpdate(PermissionRequiredMixin, UpdateView):
   permission_required = 'manager.patientupdate'
   model = Patient
   template_name = 'manager/patient_update_form.html'
   form_class = PatientUpdateForm


# CRUD - (D)elete
class OwnerDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'manager.ownerdelete'
    model = Owner
    template_name = 'manager/owner_delete_form.html'
    success_url = '/owner/list'

class PatientDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'manager.patientdelete'
    model = Patient
    template_name = 'manager/patient_delete_form.html'
    success_url = '/patient/list'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'manager/signup.html', {'form': form})


class OwnerSearchView(ListView):
    model = Owner
    template_name = 'manage/owner_list.html'
    context_object_name = 'owner_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Owner.objects.filter(Q(first_name__icontains=query) | Q(email__icontains=query))

class PatientSearchView(ListView):
    model = Patient
    template_name = 'manage/patient_list.html'
    context_object_name = 'patient_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Patient.objects.filter(Q(pet_name__icontains=query) | Q(owner__first_name__icontains=query))

#def search_owner(request:
#    if request.method == "POST":
#        searched = request.POST["searched"]
#        owners = Owner.objects.filter(name)
