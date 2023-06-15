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
<<<<<<< HEAD
            "form": form,
        }
=======
                "form": form,
                }
>>>>>>> 09b208b (feat: add feedback model and feedback form in about us page also create about us page)
        return render(request, 'website/about-us.html', context)

    if request.method == "POST":
        print("Function: Feedback Post")
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            print('Form is saved')
            context = {
<<<<<<< HEAD
                "form": FeedbackForm,
                "message": "Thankyou for giving us your feedback!"
            }
            return render(request, "website/about-us.html", context)
        else:
            context = {
                "message": "Form is Invalid",
                "form": FeedbackForm
            }
=======
                    "form": FeedbackForm,
                    "message": "Thankyou for giving us your feedback!"
                    }
                "form": FeedbackForm,
                "message": "Thankyou for giving us your feedback!"
            }
            return render(request, "website/about-us.html", context)
        else:
            context = {
                    "message": "Form is Invalid",
                    "form": FeedbackForm
                    }
>>>>>>> 09b208b (feat: add feedback model and feedback form in about us page also create about us page)
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
