from TwitterQuery import twitterhandler
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = 'test getting tweets'
    can_import_settings = True

    def handle_noargs(self, *args, **options):
        twitterhandler.get_tweets('#love')