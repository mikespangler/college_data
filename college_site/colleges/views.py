from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import College, Interview

class IndexView(generic.ListView):
  template_name = 'colleges/index.html'
  context_object_name = 'college_list'

  def get_queryset(self):
    return College.objects.order_by('updated_at')
