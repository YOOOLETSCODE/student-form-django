from django import forms
from .models import student

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone) != 10:
            raise forms.ValidationError("Phone number must be 10 digits long.")
        return phone

    