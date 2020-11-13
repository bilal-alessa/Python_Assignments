from django.db import models

# Create your models here.


class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

