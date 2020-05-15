from django.shortcuts import render
from django.template import RequestContext

handler400 = 'captain_console.views.bad_request'
handler403 = 'captain_console.views.permission_denied'
handler404 = 'captain_console.views.page_not_found'
handler500 = 'captain_console.views.server_error'

def bad_request(request, exception):
    return render(request, 'errors/400.html', locals())


def permission_denied(request, exception):
    return render(request, 'errors/403.html', locals())


def page_not_found(request, exception):
    return render(request, 'errors/404.html', locals())


def server_error(request):
    return render(request, 'errors/500.html', locals())


#### THE ORIGINAL WITH RENDER_TO_RESPONSE
""""
from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404_RENDER(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler404_RENDER_2(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500_RENDER(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
"""