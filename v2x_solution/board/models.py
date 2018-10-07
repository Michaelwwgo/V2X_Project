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
class Board(TimeStampedModel):

    """ Board Model """

    title = models.CharField(max_length=1000, null=True)
    message = models.CharField(max_length=1000)
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} - {}'.format(self.message, self.creator)

@python_2_unicode_compatible
class Comment(TimeStampedModel):

    """ Comment Model """

    comment = models.CharField(max_length=1000)
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} - {}'.format(self.comment, self.creator)

