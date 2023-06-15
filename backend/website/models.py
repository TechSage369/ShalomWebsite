from django.db import models


class FeedbackModel(models.Model):
    fullname = models.CharField(max_length=30)
    feedback = models.TextField()
    email = models.EmailField(max_length=254, default="")

    class Meta:
        verbose_name = "Feedback"

    def __str__(self):
        return f"{self.fullname} => {self.feedback[:10]}"
