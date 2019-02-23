"""Helper functions to be used during backend processing"""
import datetime
import re

import dateutil.parser
import requests
from django.shortcuts import redirect
from django.template.response import TemplateResponse

auth_token = 'f819a77c821d2ed58b8caff812e7a860ea09988d'

def _render_error_page(error_name_html, request):
    """Renders a custom made error page"""
    return TemplateResponse(request, 'issue_tracker/errors/{}.html'.format(error_name_html))


def _get_issues_data(username, repository_name):
    """Makes the API call to GitHub API server for the issues data for the username and repository name"""
    issues_data = requests.get(
        'https://api.github.com/repos/{}/{}/issues?state=open&page=1&per_page=100&access_token={}'.format(username, repository_name, auth_token)
    )
    if issues_data.status_code is 200:
        last_index = 1
        paginated_link_info = issues_data.headers.get('Link', None)

        if paginated_link_info:
            if paginated_link_info.find('last') > -1:
                split_list = paginated_link_info.split(',')
                for element in split_list:
                    if 'last' in element:
                        splitted_list = element.split('&')
                        last_index = splitted_list[1].strip('page=')
        payload = list()

        for index in range(1, int(last_index) + 1):
            issues_data = requests.get(
                'https://api.github.com/repos/{}/{}/issues?per_page=100&page={}&access_token={}'.format(username, repository_name, str(index), auth_token)
            )

            if issues_data.status_code is 200:
                if issues_data:
                    data = issues_data.json()
                    payload += data

        return payload


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

