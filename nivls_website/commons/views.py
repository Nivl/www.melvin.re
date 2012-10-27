# -*- coding: utf-8 -*-

import subprocess
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.contrib.sites.models import Site
from django.conf import settings


class TexplainView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(TexplainView, self).get_context_data(**kwargs)
        context['site'] = Site.objects.get_current()
        return context

    def render_to_response(self, context, **kwargs):
        return super(TexplainView, self).render_to_response(
            context,
            content_type='text/plain',
            **kwargs)


def write_pdf(template_src, context_dict, output):
    template = get_template(template_src)
    context = Context(context_dict)
    rendered = template.render(context)

    temp_html_file_name = '/tmp/nivl_temp_template.html'
    file = open(temp_html_file_name, 'w')
    file.write(rendered.encode('utf-8'))
    file.close()

    command_args = '%s --page-size Letter --disable-javascript %s -' % (
        settings.WKHTMLTOPDF_PATH,
        temp_html_file_name)

    popen = subprocess.Popen(command_args,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)
    pdf_contents = popen.communicate()[0]

    response = HttpResponse(pdf_contents, mimetype='application/pdf')
    response['Content-Disposition'] = 'filename=' + output
    return response
