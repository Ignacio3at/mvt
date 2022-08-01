from django.http import HttpResponse
from django.template import Template, Context 
from django.template import loader
from EntregableApp.models import Familiares 

def first_template(self):
    familiar = Familiares(nombre="Marco", apellido="Motez", fechaDeNacimiento = "1998-7-4", edad = 24 )
    familiar.save()
    diccionario = {"familiar":familiar}
    
    familiar1 = Familiares(nombre="Fausto", apellido="Motez", fechaDeNacimiento = "2013-12-26", edad = 8 )
    familiar1.save()
    diccionario["familiar1"] = familiar1
    
    familiar2 = Familiares(nombre="Mario", apellido="Motez", fechaDeNacimiento = "1954-1-25", edad = 68 )
    familiar2.save()
    diccionario["familiar2"] = familiar2
    
    plantilla = loader.get_template("template02.html")
    documento = plantilla.render(diccionario)
    """documento = f"Curso:{curso.nombre} - Camada: {curso.camada}"""
    return HttpResponse(documento)

