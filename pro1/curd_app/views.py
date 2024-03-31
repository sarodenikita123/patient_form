from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient
from django.http import HttpResponse


def create_view(request):
    template_name = "curd_app/create.html"
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("register successfully!!!")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = Patient.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def updated_view(request, pk):
    template_name = "curd_app/create.html"
    obj = Patient.objects.get(id=pk)
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def cancel_view(request, pk):
    template_name = "curd_app/confirm.html"
    obj = Patient.objects.get(id=pk)
    form = PatientForm(instance=obj)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)



