from django.core.management.base import BaseCommand

from issue_tracker.tests import automated_test


class Command(BaseCommand):
    help = 'Command to run the automated selenium test'

    def handle(self, *args, **kwargs):
        automated_test()
