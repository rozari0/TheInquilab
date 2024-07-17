from django.db import models


# Create your models here.
class Personality(models.Model):
    name = models.CharField(verbose_name="Person's Name", max_length=100)

    class Sides(models.TextChoices):
        Favor = ("FAVOR", "In Favor")
        Against = ("AGAINST", "Opposed")
        Coward = ("COWARD", "Hasn't shared their view")

    side = models.CharField(
        verbose_name="Stand on this Protest", choices=Sides, max_length=10
    )
    cause = models.TextField(verbose_name="What did they do?", null=True, blank=True)

    def __str__(self):
        return str(self.id) + ". " + self.name
