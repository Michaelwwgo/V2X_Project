from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from v2x_solution.road import models as road_models
from v2x_solution.users import models as user_models

@python_2_unicode_compatible
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Event(TimeStampedModel):

    """ Event Model """

    # 1. 이벤트 명
    name = models.CharField(max_length=140)
    # 2. 시각
    time = models.DateTimeField()
    # 3. 장소
    road = models.ForeignKey(road_models.Road, null=True, on_delete=models.CASCADE)
    # 4. 이벤트 내용
    detail = models.CharField(max_length=140)
    # 5. 작성자
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.road, self.detail)
