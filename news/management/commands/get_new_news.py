from newspaper import Config
from newspaper import Article
import pandas as pd
import newspaper
import news_summarizer
from keras.models import load_model

def get_data():
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'

    config = Config()
    config.browser_user_agent = USER_AGENT
    config.request_timeout = 10

    BASE_URL = {
        "India" : {
            "The Indian Express" : "https://indianexpress.com/",
            "Time Of India" : "https://timesofindia.indiatimes.com/",
            "News 18" : "https://www.news18.com/",
            "NDTV News" : "https://www.ndtv.com/"
        },
        "USA" : {
            "The New York Times" : "https://www.nytimes.com/",
            "NBC News" : "https://www.nbcnews.com/",
            "US News" : "https://www.usnews.com/",
            "ABC USA" : "https://abcnews.go.com/",
            
        },
        "Australia" : {
            "9 News Australia" : "https://www.9news.com.au/",
            "Daily Telegraph" : "https://www.dailytelegraph.com.au/news/breaking-news",
            "SMH | Australian Breaking News" : "https://www.smh.com.au/",
            "ABC Australia" : "https://www.abc.net.au/news/",
            "The Age News Headlines" : "https://www.theage.com.au/",
        },
        "Russia" : {
            "The Moscow Times" : "https://www.themoscowtimes.com/",
            "Reuters" : "https://www.reuters.com/places/russia",
        }
    }

    COLS = ["country_name",
            "newspaper_name",
            "title",
            "summary",
            "post_url",
            "image_url",
            "tags",
            "authors",
            "sentiment"
    ]

    MODEL_URL = "sentiment.h5"
    model = load_model(MODEL_URL)
    DATA = []

    for country in BASE_URL:
        COUNTRY_NAME = country
        for paper in BASE_URL[country]:
            NEWSPAPER_NAME = paper
            NEWS_URL = BASE_URL[country][paper]
            np = newspaper.build(NEWS_URL, config=config, memoize_articles=False, language='en')
            for sub_article in np.article_urls()[0:1]:
                article = Article(sub_article, config=config, memoize_articles=False, language='en')
                article.download()
                article.parse()
                article.nlp()

                ARTICLE_TITLE = article.title
                ARTICLE_TEXT = article.text
                ARTICLE_IMG = str(article.top_image)
                ARTICLE_AUTHORS = str(article.authors)
                ARTICLE_LINK = sub_article
                
                if len(ARTICLE_TEXT) < 100 or ARTICLE_TITLE == "":
                    continue
                
                ARTICLE_SUMMARY, ARTICLE_KEYWORDS = news_summarizer.summarize(ARTICLE_TITLE, ARTICLE_TEXT)

                ARTICLE_SENTIMENT = model.predict(ARTICLE_SENTIMENT)

                DATA.append([COUNTRY_NAME, NEWSPAPER_NAME, ARTICLE_TITLE, ARTICLE_SUMMARY, ARTICLE_LINK, ARTICLE_IMG, ARTICLE_KEYWORDS, ARTICLE_AUTHORS, ARTICLE_SENTIMENT])

    df = pd.DataFrame(DATA, columns=COLS)
    return df