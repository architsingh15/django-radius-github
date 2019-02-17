from django.core.management.base import BaseCommand

from issue_tracker.tests import automated_test


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        automated_test()
