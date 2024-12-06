import random
import string
from django.db import models

def generate_unique_code(length=8):
    """Generate a unique code consisting of uppercase letters and digits."""
    characters = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choices(characters, k=length))
        if not PatientRecord.objects.filter(unique_code=code).exists():
            return code

class PatientRecord(models.Model):
    unique_code = models.CharField(max_length=12, unique=True, default=generate_unique_code)
    clock_number = models.CharField(max_length=100,  null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    medical_history=models.TextField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    vitals= models.TextField(max_length=200, blank=True, null=True)
    chief_complaints = models.TextField(max_length=200, blank=True, null=True)
    history_of_presenting_illness = models.TextField(max_length=200, blank=True, null=True)
    examination = models.TextField(max_length=200, blank=True, null=True)
    medical_remarks = models.TextField(max_length=100, blank=True, null=True)

    dob = models.DateField(blank=True, null=True)
    relationship = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    test_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    prescription = models.TextField(blank=True, null=True)
    test_result = models.TextField(blank=True, null=True)
    test_result_pdf = models.FileField(upload_to='test_results/', blank=True, null=True)

    date_symptoms_aware = models.DateField(blank=True, null=True) 
    symptoms = models.TextField(blank=True, null=True)
    previous_complaints = models.BooleanField(default=False)  
    previous_complaints_date = models.DateField(blank=True, null=True) 
    treatment_description = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.clock_number}'



class ExtractedData(models.Model):
    content = models.TextField()  
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Extracted Data from PDF on {self.uploaded_at}"


class Employee(models.Model):
    payroll_number = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=255, null=True)
    department = models.CharField(max_length=255, null=True)
    designation = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=True, null=False)

    def __str__(self):
        return f"{self.name} (Payroll No: {self.payroll_number})"
