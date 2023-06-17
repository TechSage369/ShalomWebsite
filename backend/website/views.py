from django.shortcuts import render
from .models import FeesStructure


def homepage_view(request):
    return render(request, 'website/homepage.html')


def about_us_view(request):
    return render(request, 'website/about-us.html')


def admission_view(request):
    return render(request, 'website/admission.html')


def fee_structure_view(request):
    data = FeesStructure.objects.all()
    print(data)
    return render(request, 'website/fee-structure.html', {'context': data})


def gallery_view(request):
    return render(request, 'website/gallery.html')


def admission_form(request):
    return render(request, 'website/form.html')
