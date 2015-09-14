from django.db import models

class College(models.Model):

  QUARTER = 'q'
  SEMESTER = 's'
  FOURONEFOUR = '4'
  ACADEMIC_CAL_CHOICES = [
    (QUARTER, 'Quarter'),
    (SEMESTER, 'Semester'),
    (FOURONEFOUR, '4-1-4'),
  ]

  name = models.CharField(max_length=100, blank=False)
  updated_at = models.DateTimeField(auto_now=True) # set every time it's updated
  grad_enrollment = models.IntegerField(default=None, blank=True)
  undergrad_enrollment = models.IntegerField(default=None, blank=True)
  location = models.CharField(max_length=100)
  setting  = models.CharField(max_length=100)
  admit_rate = models.IntegerField()
  lchs_gpa = models.FloatField()
  lchs_act = models.IntegerField()
  lchs_sat = models.IntegerField()
  academic_calendar = models.CharField(max_length=1,
                                      choices=ACADEMIC_CAL_CHOICES,
                                      default=SEMESTER)

  def __str__(self):
    return self.name

class Interview(models.Model):
  college    = models.ForeignKey(College, default=0)
  blurb      = models.CharField(max_length=1000)
  location   = models.CharField(max_length=200)
  timing     = models.CharField(max_length=300)
  link       = models.CharField(max_length=200)
  updated_at = models.DateTimeField(auto_now=True) # set every time it's updated

  def __str__(self):
    return self.college.__str__
