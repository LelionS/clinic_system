from django.urls import path
from .views import get_name_by_clock_number, doctor_dashboard, lab_technician_view, update_patient_record, export_to_excel, patient_records_by_clock_number
from . import views
from .views import patient_history, human_resource_report, hr_export_to_excel
from .views import get_patient_details, lab_update_record
from .views import renew_session
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_pdf_view
from .views import upload_pdf_view, success_view, save_patient_record
from .views import upload_file
from .views import get_employee
from .views import get_employee_data

urlpatterns = [
    path('', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('get-name-by-clock-number/', get_name_by_clock_number, name='get_name_by_clock_number'),
    path('doctor-dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('lab-technician-dashboard/', lab_technician_view, name='lab_technician_dashboard'),
    path('human_resource_report/', human_resource_report, name='human_resource_report'),
    path('patient-history/', views.patient_history, name='patient_history'),
    path('lab-reports/', views.lab_reports, name='lab_reports'),    
   
    path('update-patient-record/<str:unique_code>/', update_patient_record, name='update_patient_record'),
    path('lab_update_record/<str:unique_code>/', lab_update_record, name='lab_update_record'),
    path('export-to-excel/', export_to_excel, name='export_to_excel'),
    path('hr-export-to-excel/', hr_export_to_excel, name='hr_export_to_excel'),
    path('patient-records/<str:clock_number>/', patient_records_by_clock_number, name='patient_records_by_clock_number'),
    path('check-unique-code/', views.check_unique_code, name='check_unique_code'),
    path('get-patient-details/', get_patient_details, name='get_patient_details'),
    path('logout/', views.logout_view, name='logout'),
    path('auto-logout/', views.auto_logout, name='auto_logout'),
    path('renew_session/', renew_session, name='renew_session'),

    path('upload/', upload_pdf_view, name='upload_pdf'),
    path('save_patient_record', save_patient_record, name='save_patient_record'),
    path('lab_success/', success_view, name='success'),

    path('employee', upload_file, name='upload_file'),

    path('get-employee/<int:clock_number>/', get_employee, name='get_employee'),

    path('get_employee_data/', get_employee_data, name='get_employee_data'),

]



