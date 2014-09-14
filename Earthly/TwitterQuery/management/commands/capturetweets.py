from TwitterQuery import twitterhandler
from TwitterQuery.models import HashTag
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = 'test getting tweets'
    can_import_settings = True

    def handle_noargs(self, *args, **options):
    
        hashtags = []
        
        for hash in HashTag.objects.all():
            hashtags.append(hash.text.encode("ascii"));
        
        print hashtags
        
        twitterhandler.get_tweets(hashtags)