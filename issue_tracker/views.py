import requests
from django.shortcuts import render, redirect

from issue_tracker.utils import _extract_username_repository_name, _get_issues_data, _count_required_issues, \
    _render_error_page

regex_ = '^(?:http)s?:\/\/(?:github\.com)\/[a-z]*\/[a-z]*$'

# pass constants from view to template


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
        resolvable_url = requests.get(input_url)
        if resolvable_url.status_code is 200:
            split_input_url = input_url.split('/')
            if len(split_input_url) is 5:
                username, repository_name = _extract_username_repository_name(split_input_url)
                issues = _get_issues_data(username, repository_name)
                required_count = _count_required_issues(issues)
                print(required_count)
                return redirect('/add')
            else:
                return _render_error_page('invalid_github', request)
        else:
            return _render_error_page('private_github_repo_invalid', request)
    else:
        return _render_error_page('403', request)
