from django.shortcuts import render
from django.template import RequestContext


def handler404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {},
                      context_instance=RequestContext(request))
    response.status_code = 500
    return response