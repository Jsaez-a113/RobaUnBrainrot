from django.db import models


class BrainrotItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    img = models.ImageField(upload_to='brainrot_images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name