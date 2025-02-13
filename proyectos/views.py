from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, Herramienta
from .forms import ProyectoForm, HerramientaForm

# Vista de inicio (Redirige a lista de proyectos)
def home(request):
    return redirect('lista_proyectos')  # Redirige a la lista de proyectos

# CRUD para Proyectos
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

def agregar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'formulario_proyecto.html', {'form': form})

def editar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'formulario_proyecto.html', {'form': form})

def eliminar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'eliminar_proyecto.html', {'proyecto': proyecto})

# CRUD para Herramientas
def lista_herramientas(request):
    herramientas = Herramienta.objects.all()
    return render(request, 'lista_herramientas.html', {'herramientas': herramientas})

def agregar_herramienta(request):
    if request.method == 'POST':
        form = HerramientaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_herramientas')
    else:
        form = HerramientaForm()
    return render(request, 'formulario_herramienta.html', {'form': form})

def eliminar_herramienta(request, id):
    herramienta = get_object_or_404(Herramienta, id=id)
    if request.method == 'POST':
        herramienta.delete()
        return redirect('lista_herramientas')
    return render(request, 'eliminar_herramienta.html', {'herramienta': herramienta})
