from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'correo']
        #exclude = ['full_name']    #NO RECOMENDABLE USARLO

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if not full_name:
            raise forms.ValidationError("Please add a full_name")

        return full_name

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        correo_base, provider = correo.split("@")
        domain, extension = provider.split('.')
        if not extension == 'edu':
            raise forms.ValidationError("Please use a valid .EDU email address")

        return correo