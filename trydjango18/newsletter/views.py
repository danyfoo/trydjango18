from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from .forms import ContactForm, SignUpForm


def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None) #Anadimos un Formulario a nuestra vista que sera identificado por form
                                            #Indicamos que esta puede devolver un valor para Agregar a la DB o Nada

    #Contextos que pueden ser utilizados desde HTML con las etiquetas de JINJA 2
    #EJEMPLO {{ form }} o {{ title }}
    context = {
        "title" : title,    #Titulo del template
        "form" : form      #Formulario que puede ser utilizado en el template
    }

    #Si el formulario es valido, hara lo siguiente:
    if form.is_valid():
        print request.POST
        instance = form.save(commit=False)  #Obtenemos la instancia de guardar los datos de formulario,
                                            #Que es un diccionario de los datos a guardar
                                            #Con commit = false indicamos que no se guardara en la DB
        if not instance.full_name:  #Si no existe datos en full_name hara lo siguiente
            instance.full_name = "Daniel"   #full_name ahora tiene el valor de Daniel
        instance.save() #Guardamos en la DB la instancia
        context = {
            "title" : 'Thank you',  #Modificamos el contexto a Thank You
        }

    return render(request,"home.html",context)  #RENDERIZAMOS UN TTEMPLATE, CON UN REQUEST ESPECIFICO Y UN CONTEXTO

def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form =  ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value

        #PARA PODER ENVIAR EMAIL POR DJANGO
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")

        subject = 'Site contact Form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s: %s via %s" %(
            form_full_name,
            form_message,
            form_email)
        some_html_message = """ <h1>Hello</h1> """
        send_mail(subject,
                  contact_message,
                  from_email,
                  [to_email],
                  html_message=some_html_message,
                  fail_silently=False)

    context = {
        "form" : form,
        "title": title,
        "title_align_center": title_align_center,
    }

    return render(request, "forms.html", context)