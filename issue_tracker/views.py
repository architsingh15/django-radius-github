"""The backend processing that receives the request and handles the rendering of the templates with appropriate
data and processing. It's the V in MVT"""
import requests
from django.shortcuts import render, redirect

from issue_tracker.models import Registry
from issue_tracker.utils import _extract_username_repository_name, _get_issues_data, _count_required_issues, \
    _render_error_page


def base(request):
    return render(request, 'issue_tracker/base.html')


def add_to_registry(request):
    return render(request, 'issue_tracker/add_to_registry.html')


def validate_url(request):
    if request.method == 'POST':
        input_url = request.POST.get('input_url')
        resolvable_url = requests.get(input_url)
        if resolvable_url.status_code is 200:
            split_input_url = input_url.split('/')
            if len(split_input_url) is 5:
                username, repository_name = _extract_username_repository_name(split_input_url)
                issues = _get_issues_data(username, repository_name)
                required_count = _count_required_issues(issues)
                registry_obj = Registry(
                    username=username,
                    repository_name=repository_name,
                    total=required_count['total'],
                    last_24_hours=required_count['less_than_24_hours'],
                    between_1_and_7_days=required_count['less_than_7_days'],
                    more_than_7_days=required_count['more_than_7_days'],
                )
                registry_obj.save()

                return redirect('/issue_registry')
            else:
                return _render_error_page('invalid_github', request)
        else:
            return _render_error_page('private_github_repo_invalid', request)
    else:
        return _render_error_page('403', request)


def issue_registry(request):
    return render(request, 'issue_tracker/issue_registry.html', {
        'issues': Registry.objects.all()
    })


def dashboard(request):
    return render(request, 'issue_tracker/dashboard.html')
