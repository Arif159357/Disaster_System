from django.core.management.base import BaseCommand, CommandError
from scheduler.task import tasks


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.help = 'store images'
        self.task = tasks()

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=str)

    def handle(self, *args, **options):
        if options['poll_ids'][0] == 'scrapy':
            return self.task.annotator_performance()
