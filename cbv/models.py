from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Coutries"

    def __str__(self):
        return self.name


class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now_add=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
