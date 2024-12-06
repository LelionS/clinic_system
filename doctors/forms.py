from django import forms
from .models import PatientRecord


class PatientForm(forms.ModelForm):
    clock_number = forms.CharField(
        required=False,  
        initial="",  
        label="Clock Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',  
        })
    )

    class Meta:
        model = PatientRecord
        fields = [
            'clock_number', 'name', 'dob', 'gender', 'age', 'relationship', 'vitals', 'medical_history', 'chief_complaints', 'symptoms', 
            'history_of_presenting_illness','medical_remarks', 'examination' ,'date_symptoms_aware', 'previous_complaints', 'previous_complaints_date',
            'treatment_description', 'test_type', 'test_result', 'test_result_pdf', 'description', 'diagnosis', 
            'prescription', 'remarks'
        ]

        
        widgets = {
            'age': forms.NumberInput(attrs={'placeholder': ' '}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'date-picker'}),   
            'date_symptoms_aware': forms.DateInput(attrs={'type': 'date', 'class': 'date-picker'}),
            'previous_complaints_date': forms.DateInput(attrs={'type': 'date', 'class': 'date-picker'}),
            'gender': forms.RadioSelect(choices=[('Male', 'Male'), ('Female', 'Female')]), 
        }



class LabTestResultForm(forms.ModelForm):
    test_result = forms.CharField(
        label='Test Result',
        widget=forms.HiddenInput(),   
        required=False  
    )
    widgets = {
            'test_result_pdf': forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),
        }

    class Meta:
        model = PatientRecord
        fields = ['test_result']


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields = ['prescription']


class PatientRecordForm(forms.ModelForm):
    unique_code = forms.CharField(
        label='Unique Code',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Unique Code',
            'class': 'form-control'
        })
    )
    
    test_result = forms.CharField(
        label='Test Result',
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter Test Result', 
            'rows': 4,
            'class': 'form-control'
        }),
        required=False 
    )

    class Meta:
        model = PatientRecord
        fields = [
            'unique_code', 'clock_number', 'name', 'dob', 'relationship', 'gender', 
            'test_type', 'description', 'diagnosis', 'prescription', 'test_result', 'test_result_pdf',
            'date_symptoms_aware', 'symptoms', 'previous_complaints', 'previous_complaints_date',
            'treatment_description', 'remarks'
        ]

        
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'date-picker'}),
            'date_symptoms_aware': forms.DateInput(attrs={'type': 'date', 'class': 'date-picker'}),
            'previous_complaints_date': forms.DateInput(attrs={'type': 'date', 'class': 'date-picker'}),
            'gender': forms.RadioSelect(choices=[('Male', 'Male'), ('Female', 'Female')]),
        }

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField()





class UploadFileForm(forms.Form):
    file = forms.FileField()
