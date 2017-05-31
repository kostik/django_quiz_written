from django.contrib.auth.views import login
from django.shortcuts import render_to_response
from django.template import RequestContext


def login_form_page(request, template_name='page_home.html'):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print ip

    if request.user.is_authenticated():
        return render_to_response(template_name, context_instance=RequestContext(request))
    return login(request, template_name=template_name)
