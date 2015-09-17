from django.db import models

class Student(models.Model):

  name = models.CharField(max_length=100, blank=False)
  major = models.CharField(max_length=80)
  gpa = models.FloatField(default=0.0)
  updated_at = models.DateTimeField(auto_now=True)
  colleges = models.ManyToManyField('colleges.College')


  def __str__(self):
    return self.name

class TestScore(models.Model):

  def __str__(self):
    return "({1} - {0})".format(self.test_type, self.student.name)

  TEST_TYPES = [
    ('s1', 'SAT I'),
    ('s2', 'SAT II'),
    ('a','ACT')
  ]
  test_type = models.CharField(choices=TEST_TYPES, default = 'a',max_length=2)
  score = models.IntegerField()
  student = models.ForeignKey(Student, blank=False)

