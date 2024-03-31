from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

        widgets = {
            "date": forms.DateInput(),
            "patient_name": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(),
            "phone": forms.NumberInput(),
            "dob": forms.DateInput(),
            "marital_status": forms.RadioSelect()
        }
