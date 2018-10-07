from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from v2x_solution.users import models as user_models

@python_2_unicode_compatible
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Car(TimeStampedModel):

    """ Car Model """

    number = models.CharField(max_length=140)
    isFind = models.BooleanField(default=False)
    message = models.CharField(max_length=140, null=True)

    def __str__(self):
        return '{} - {}'.format(self.number, self.isFind)

class CriminalCar(TimeStampedModel):

    """ CriminalCar Model """

    car = models.ForeignKey(Car, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField()
    location = models.CharField(max_length=140, default='', null=True, blank=True)
    creator = models.CharField(max_length=140, default='', null=True, blank=True)
    
    def __str__(self):
        return '{} - {}'.format(self.car.number, self.car.isFind)

class PostCar(TimeStampedModel):

    """ PostCar Model """

    name = models.CharField(max_length=140)
    number = models.CharField(max_length=140)
    owner = models.CharField(max_length=140)
    location = models.CharField(max_length=140)