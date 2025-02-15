from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)  # Заголовок
    title_url = models.URLField(blank=True)  # Ссылка
    date = models.DateField(default=None, blank=True, null=True)
    description = models.CharField(max_length=250)

