from django.shortcuts import render
from .forms import FeedbackForm


def homepage_view(request):
    return render(request, 'website/homepage.html')


def about_us_view(request):
    return render(request, 'website/about-us.html')


def feedback_handler(request):
    if request.method == "GET":
        print("Function: Feedback Get")
        form = FeedbackForm
        context = {
                "form": form,
                }
        return render(request, 'website/about-us.html', context)

    if request.method == "POST":
        print("Function: Feedback Post")
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            print('Form is saved')
            context = {
                    "form": FeedbackForm,
                    "message": "Thankyou for giving us your feedback!"
                    }
            return render(request, "website/about-us.html", context)
        else:
            context = {
                    "message": "Form is Invalid",
                    "form": FeedbackForm
                    }
            return render(request, 'website/about-us.html', context)


def admission_view(request):
    return render(request, 'website/admission.html')


def fee_structure_view(request):
    return render(request, 'website/fee-structure.html')


def gallery_view(request):
    return render(request, 'website/gallery.html')
