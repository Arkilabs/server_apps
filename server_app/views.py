from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from config_generator import ConfigGenerator


def home(request):
    #generator = ConfigGenerator("garitas_co")
    return render_to_response("home.haml")


def start(request):
    response = {'result': True}
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')


def stop(request):
    response = {'result': True}
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
