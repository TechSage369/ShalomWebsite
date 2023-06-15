from django.forms import ModelForm
from .models import FeedbackModel


class FeedbackForm(ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ["fullname", "feedback"]
