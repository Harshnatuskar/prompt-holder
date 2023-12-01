from django.db import models

# Create your models here.

class PromptData(models.Model):
    prompt_json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return str(self.created_at)