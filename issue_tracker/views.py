import requests
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse

regex_ = '^(?:http)s?:\/\/(?:github\.com)\/[a-z]*\/[a-z]*$'

# pass constants from view to template


def _render_error_page(error_name_html, request):
    return TemplateResponse(request, 'issue_tracker/errors/{}.html'.format(error_name_html))


def base(request):
    return render(request, 'issue_tracker/base.html', {})


def add_to_registry(request):
    return render(
        request,
        'issue_tracker/add_to_registry.html',
        {'show_download_button': True}
    )


def validate_url(request):
    if request.method == 'POST':
        input_url = request.POST.get('input_url')
        split_input_url = input_url.split('/')
        if len(split_input_url) is 5:
            repository_name = split_input_url[-1]
            username = split_input_url[-2]
            # call the git hub API here with timestamp
            print(repository_name)
            print(username)
            return redirect('/add')
        else:
            return _render_error_page('invalid_github', request)
    else:
        return _render_error_page('403', request)
