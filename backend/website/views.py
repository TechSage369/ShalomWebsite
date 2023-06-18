from django.shortcuts import render
from .forms import FeedbackForm


def homepage_view(request):
    return render(request, 'website/homepage.html')


def about_us_view(request):
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
            return render(request, "website/about-us.html", context)

    if request.method == "GET":
        print("Function: Feedback Get")
        form = FeedbackForm
        context = {
            "form": form,
        }
        return render(request, 'website/about-us.html', context)


def admission_view(request):
    return render(request, 'website/admission.html')


def annual_planner_view(request):
    return render(request, 'website/annual_planner.html')


def gallery_view(request):
    return render(request, 'website/gallery.html')


def principle_letter(request):
    return render(request, 'website/principle-letter.html')


def vision_and_mission_view(request):
    return render(request, 'website/vision-and-mission.html')


def admission_form(request):
    return render(request, 'website/form.html')


def rules_and_regulations_view(request):
    return render(request, 'website/rules-and-regulations.html')


def administration_view(request):
    return render(request, 'website/administration.html')


'''
teachers day
childrens day
investiture ceremony
environment day

sports day
independence day
school activities
christmas day
'''


def gallery_details_view(request):
    return render(request, 'website/gallery-details-view.html')


def gallery_teachers_day_view(request):
    return render(request, 'website/gallery-teachers-day.html')


def gallery_childrens_day_view(request):
    return render(request, 'website/gallery-childrens-day.html')


def gallery_investiture_ceremony_view(request):
    return render(request, 'website/gallery-investiture-ceremony.html')


def gallery_environment_day_view(request):
    return render(request, 'website/gallery-environment-day.html')


def gallery_sports_day_view(request):
    return render(request, 'website/gallery-sports-day.html')


def gallery_independence_day_view(request):
    return render(request, 'website/gallery-independence-day.html')


def gallery_school_activities_view(request):
    return render(request, 'website/gallery-students-activities.html')


def gallery_christmas_day_view(request):
    return render(request, 'website/gallery-christmas-day.html')










