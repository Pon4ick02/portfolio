from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)  # Заголовок
    date = models.DateField(default=None, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title