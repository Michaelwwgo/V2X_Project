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
class Road(TimeStampedModel):

    """ Road Model """

    name = models.CharField(max_length=140)
    location = models.CharField(max_length=140)
    speed = models.SmallIntegerField(null=True)
    
    def __str__(self):
        return '{} - {}'.format(self.name, self.location)

@python_2_unicode_compatible
class Situation(TimeStampedModel):

    """ Situation Model """

    road = models.ForeignKey(Road, null=True, on_delete=models.CASCADE)
    isimpassable = models.BooleanField()
    message = models.CharField(max_length=140)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.isimpassable, self.message)
