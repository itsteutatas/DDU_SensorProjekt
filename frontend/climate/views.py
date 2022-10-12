from django.http import HttpResponse
from django.template import loader
from .models import Data
from django.contrib.auth.decorators import login_required
from .datacollector import collect


@login_required(login_url='/login/')
def index(request):
  if request.method == 'POST' and 'run_script' in request.POST:
    collect(10)

  data = Data.objects.all().values()
  template = loader.get_template('climate.html')
  context = {
    'data': data,
  }
  return HttpResponse(template.render(context, request))

