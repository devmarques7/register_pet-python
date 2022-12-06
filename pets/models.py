from django.db import models


class PetSex(models.TextChoices):
    MALE = "Male"
    FEMALE = "Famale"
    DEFAULT = "Not Informed"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=12, choices=PetSex.choices, default=PetSex.DEFAULT
    )
    group = models.ForeignKey(
        "groups.Group", on_delete=models.CASCADE, related_name="group"
    )
    traits = models.ManyToManyField("traits.Trait", related_name="traits")

    def __repr__(self) -> str:
        return f"<[{self.pk}] - {self.name}>"
