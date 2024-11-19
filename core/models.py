from django.db import models

class Task(models.Model):
    title = models.CharField("Título", max_length=100, null=False, blank=False)
    created_at =models.DateField("Criação", auto_now_add=True)
    check_task = models.BooleanField("Concluído", default=False)

    def __str__(self):
        return self.title