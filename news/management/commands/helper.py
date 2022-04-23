from django.core.management.base import BaseCommand
from news.models import News
import get_new_news as gnn

class Command(BaseCommand):
    def handle(self, *args, **options):
        # get data from APIs converted into dataframe with preprocessing, summarization and sentiment analysis
        dataframe = gnn.get_data()
        
        # delete current data from the database
        News.objects.all().delete()

        # add new data into the database
        for index, row in dataframe.iterrows():
            country_name = row['country_name']
            newspaper_name = row['newspaper_name']
            title = row['title']
            summary = row['summary']
            post_url = row['post_url']
            image_url = row['image_url']
            tags = row['tags']
            authors = row['authors']
            sentiment = row['sentiment']
            form = News(country_name = country_name,
                        newspaper_name = newspaper_name,
                        title = title,
                        summary = summary,
                        post_url = post_url,
                        image_url = image_url,
                        tags = tags,
                        authors = authors,
                        sentiment = sentiment)
            form.save()