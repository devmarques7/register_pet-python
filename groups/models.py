from django.db import models


class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"<[{self.pk}] - {self.scientific_name}>"
