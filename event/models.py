from django.db import models

# Classe do aniversariante
class UserEvent(models.Model):

    first_name = models.CharField("nome", max_length=50)
    last_name = models.CharField("sobrenome", max_length=50)
    description = models.TextField("descrição", max_length=250, default="")
    birthday = models.CharField("data de aniversário", max_length=50)

    def __str__(self):
        return ("{} {}").format(self.first_name, self.last_name)
