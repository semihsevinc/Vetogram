from django.urls import path, include 
from django.conf.urls.static import static
from django.contrib.auth.decorators import permission_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('account/', include('django.contrib.auth.urls'), name="login"),
   path('signup/',views.signup , name='signup'),
   path('owner/list', views.OwnerList.as_view(), name="ownerlist"),
   path('owner/create', views.OwnerCreate.as_view(), name="ownercreate"),
   path('owner/update/<pk>', views.OwnerUpdate.as_view(), name="ownerupdate"),
   path('owner/delete/<pk>', views.OwnerDelete.as_view(), name="ownerdelete"),
   path('patient/list', views.PatientList.as_view(), name="patientlist"),
   path('patient/create', views.PatientCreate.as_view(), name="patientcreate"),
   path('patient/update/<pk>', views.PatientUpdate.as_view(), name="patientupdate"),
   path('patient/delete/<pk>', views.PatientDelete.as_view(), name="patientdelete"),
   path('owner_search/', views.OwnerSearchView.as_view(), name='ownersearch'),
   path('patient_search/', views.PatientSearchView.as_view(), name='patientsearch'),
] 