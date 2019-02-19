"""Helper functions to be used during backend processing"""
import datetime

import dateutil.parser
import requests
from django.template.response import TemplateResponse


def _render_error_page(error_name_html, request):
    """Renders a custom made error page"""
    return TemplateResponse(request, 'issue_tracker/errors/{}.html'.format(error_name_html))


def _get_issues_data(username, repository_name):
    """Makes the API call to GitHub API server for the issues data for the username and repository name"""
    issues_data = requests.get(
        'https://api.github.com/repos/{}/{}/issues?state=open'.format(username, repository_name)
    )
    if issues_data:
        data = issues_data.json()
        return data
    else:
        return None


def _extract_username_repository_name(split_input_url):
    """Extracts the username and the repository name of a valid GitHub URL"""
    repository_name = split_input_url[-1]
    username = split_input_url[-2]
    return username, repository_name


def _subtract_number_of_days(now, days):
    """Returns a date time object subtracting the number of days given in the argument"""
    return now - datetime.timedelta(days=days)


def _count_required_issues(issues_dict):
    """Returns a dictionary with the processed data that we need to display on Issue Registry"""
    issues_count_dict = dict.fromkeys(["total", "less_than_24_hours", "less_than_7_days", "more_than_7_days"], 0)
    if not issues_dict:
        return issues_count_dict
    for dict_obj in issues_dict:
        if 'pull_request' not in dict_obj:
            issues_count_dict['total'] += 1
            issue_date = dict_obj['created_at']
            issue_date = issue_date.strip('Z')
            issue_date_datetime = dateutil.parser.parse(issue_date)

            now = datetime.datetime.today().replace(microsecond=0)
            one_day_ago = _subtract_number_of_days(now, 1)
            seven_days_ago = _subtract_number_of_days(now, 7)

            if one_day_ago < issue_date_datetime < now:
                issues_count_dict['less_than_24_hours'] += 1
            elif seven_days_ago < issue_date_datetime < one_day_ago:
                issues_count_dict['less_than_7_days'] += 1
            elif issue_date_datetime < seven_days_ago:
                issues_count_dict['more_than_7_days'] += 1
            else:
                pass
    return issues_count_dict

