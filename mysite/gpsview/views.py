from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicles
# Create your views here.
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    vehicles = Vehicles.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'index.html', context)

def index2(request):
    return HttpResponse("Hello, world. You're at the index page.")