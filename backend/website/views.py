from django.shortcuts import render


def homepage_view(request):
    return render(request, 'website/homepage.html')

def about_us_view(request):
    return render(request, 'website/about-us.html')

def admission_view(request):
    return render(request, 'website/admission.html')

def fee_structure_view(request):
    return render(request, 'website/fee-structure.html')

def gallery_view(request):
    return render(request, 'website/gallery.html')