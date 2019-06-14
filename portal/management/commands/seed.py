
from django.core.management.base import BaseCommand
from portal.factories import InfraVltgDetailFactory


class Command(BaseCommand):
    """
    """
    help = 'Creating fake data for InfraVltgDetail models'

    def handle(self, *args, **options):

        # clear invites

        InfraVltgDetailFactory.create_batch(100)