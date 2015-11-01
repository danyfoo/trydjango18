from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email =  forms.EmailField()
    message = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not extension == 'edu':
            raise forms.ValidationError("Please use a valid .EDU email address")

        return email

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp  #Modelo de datos a usar
        fields = ['full_name', 'email'] #Campos que contendra el formulario
        #exclude = ['full_name']    #NO RECOMENDABLE USARLO

    #Metodos para validar el contenido del formulario
    def clean_full_name(self):  #Por convencion se hace de esta manera: clean_<NOMBRE_DEL_CAMPO>
        full_name = self.cleaned_data.get('full_name')  #Obtenemos el valor del campo
        if not full_name:   #Encaso de que no haiga un full_name, se hace lo siguiente:
            raise forms.ValidationError("Please add a full_name")   #raise publicara en el template un aviso

        return full_name #Regresamos ese nombre

    #NO FUNCIONA CON email
    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not extension == 'edu':
            raise forms.ValidationError("Please use a valid .EDU email address")

        return email