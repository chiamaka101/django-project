from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        illness = request.POST.get('illness')
        prescription = request.POST.get('prescription')
        bill_balance = int(request.POST.get('bill_balance', 0))
        Patient.objects.create(
            name=name,
            illness=illness,
            prescription=prescription,
            bill_balance=bill_balance
        )
        return redirect('home')
    patients = Patient.objects.all()
    context = {'patients': patients}  
    return render(request, 'home.html', context)  

def discharge_patient(request, pk):  
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('home')