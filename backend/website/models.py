from django.db import models
import uuid


class FeedbackModel(models.Model):
    fullname = models.CharField(max_length=30)
    feedback = models.TextField()
    email = models.EmailField(max_length=254, default="")

    class Meta:
        verbose_name = "Feedback"

    def __str__(self):
        return f"{self.fullname} => {self.feedback[:10]}"


class FeeStructure(models.Model):
    pdf_file = models.FileField(
        upload_to="Fees-structure/")
    created = models.DateField(auto_now_add=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
