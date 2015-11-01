from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm


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