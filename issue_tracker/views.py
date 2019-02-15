from django.shortcuts import render


def base(request):
    return render(request, 'issue_tracker/base.html', {})
