from django.core.management.base import BaseCommand, CommandError
import csv
from datetime import datetime
from IS.models import HeatTreatment


class Command(BaseCommand):
    help = 'Fill tables from csv'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='data.csv',
            help='csv files',
        )

    def handle(self, *args, **options):
        start = datetime.now()
        try:
            filename = options['file']
            with open(filename, 'r') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in spamreader:
                    hardness = row[0]
                    date = datetime.strptime(row[1], '%d %m %Y %H:%M')
                    obj, created = HeatTreatment.objects.get_or_create(final_hardness=hardness, start_date=date)
        except Exception as e:
            raise CommandError(f'failed with "{e}"')
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully loaded file "{filename}"\n '
                f'Time elapsed: {(datetime.now() - start).seconds} seconds')
        )
