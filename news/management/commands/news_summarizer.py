import re
import math
from os import path
from collections import Counter
from pprint import pprint

ideal = 20.0
stopwords = set()


def load_stopwords(language="en"):
    """ 
    Loads language-specific stopwords for keyword selection
    """
    global stopwords
    if(language == "en"):
        stopwords = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", 
        "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", 
        "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", 
        "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", 
        "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", 
        "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", 
        "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"])
            
        
def score(sentences, titleWords, keywords):
    """
    Score sentences based on different features like : 
    1. On the basis of title to text relation
    2. On the basis of length of the sentence (too short or too long sentences dont weigh much power)
    3. On the basis of the position of the sentence in the article (sentences in the middle hold little importance when compared to the initial and later sentence)
    4. On the basis of features such as SBS and FBS
    """
    senSize = len(sentences)
    ranks = Counter()
    for i, s in enumerate(sentences):
        sentence = split_words(s)
        titleFeature = title_score(titleWords, sentence)
        sentenceLength = length_score(len(sentence))
        sentencePosition = sentence_position(i + 1, senSize)
        sbsFeature = sbs(sentence, keywords)
        dbsFeature = dbs(sentence, keywords)
        frequency = (sbsFeature + dbsFeature) / 2.0 * 10.0
        totalScore = (titleFeature*1.5 + frequency*2.0 + sentenceLength*1.0 + sentencePosition*1.0) / 4.0
        ranks[(i, s)] = totalScore
    return ranks

# Done
def sbs(words, keywords):
    """
    Feature 1 : Used to meausre the frequency of the words in a sentence when compared with keywords
    """
    score = 0.0
    if (len(words) == 0):
        return 0
    for word in words:
        if word in keywords:
            score += keywords[word]
    return (1.0 / math.fabs(len(words)) * score) / 10.0

# Done
def dbs(words, keywords):
    """
    Feature 2 : Used to meausre the frequency of the words in a sentence when compared with keywords
    """
    if (len(words) == 0):
        return 0
    summ = 0
    first = []
    second = []

    for i, word in enumerate(words):
        if word in keywords:
            score = keywords[word]
            if first == []:
                first = [i, score]
            else:
                second = first
                first = [i, score]
                dif = first[0] - second[0]
                summ += (first[1] * second[1]) / (dif ** 2)
    
    k = len(set(keywords.keys()).intersection(set(words))) + 1
    return (1 / (k * (k + 1.0)) * summ)

# Done
def split_words(text):
    """
    Split a string into array of words after getting rid of all the special characters
    """
    try:
        text = re.sub(r'[^\w ]', '', text)  # strip special chars
        return [x.strip('.').lower() for x in text.split()] # converts into a list of words
    except TypeError:
        return None

# Done
def keywords(text):
    """
    Get the top 10 keywords and their frequency scores ignores blacklisted words in stopwords.
    Counts the number of occurrences of each word
    Sorts them in reverse natural order (so descending) by number of occurrences.
    These are the top 10 most used words o
    """
    NUM_KEYWORDS = 10
    text = split_words(text) # of words before removing blacklist words
    if text:
        num_words = len(text)
        text = [x for x in text if x not in stopwords]
        freq = {} # freq dictonary so we dont repeat words
        for word in text:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        min_size = min(NUM_KEYWORDS, len(freq)) # update min_size in case text has less than 10 words
        keywords = sorted(freq.items(),
                          key=lambda x: (x[1], x[0]),
                          reverse=True)
        keywords = keywords[:min_size]
        keywords = dict((x, y) for x, y in keywords)

        for k in keywords:
            articleScore = keywords[k] * 1.0 / max(num_words, 1)
            keywords[k] = articleScore * 1.5 + 1
        return dict(keywords) # return the top 10 words with their score (influence in the sentence)
    else:
        return dict()

# Done
def split_sentences(text):
    """
    Split a large string into sentences.
    """
    import nltk.data
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    sentences = tokenizer.tokenize(text)
    sentences = [x.replace('\n', '') for x in sentences if len(x) > 10]
    return sentences

# Done
def length_score(sentence_len):
    """
    Returns an int that defines the score of a sentence based solely on its length.
    Ideally sentences contain 20 characters at least.
    Hence more the length of the sentence more would the score be.
    But incase the sentence is terribly long it decreases the score.
    """
    return 1 - math.fabs(ideal - sentence_len) / ideal

# Done
def title_score(title, sentence):
    if title:
        title = [x for x in title if x not in stopwords]
        count = 0.0
        for word in sentence:
            if (word not in stopwords and word in title):
                count += 1.0
        return count / max(len(title), 1)
    else:
        return 0

# Done
def sentence_position(i, size):
    """
    Different sentence positions indicate different probability of being an important sentence.
    Mainly the starting and the ending part of the sentence have the maximum probabilty of having a meaningful meaning.
    Hence the summarization is not only dependent on the occurence of words but also on the position where they occur.
    Probability of .15 is given to the initial and .17 to the sentences at the end of the text.
    The sentences in the middle have an probabilty between .04 to .08.
    The probability is nothing but a parameter that counts the probabilty of effect of its position on the meaning.
    """
    normalized = i * 1.0 / size
    if (normalized > 1.0):
        return 0
    elif (normalized > 0.9):
        return 0.15
    elif (normalized > 0.8):
        return 0.04
    elif (normalized > 0.7):
        return 0.04
    elif (normalized > 0.6):
        return 0.06
    elif (normalized > 0.5):
        return 0.04
    elif (normalized > 0.4):
        return 0.05
    elif (normalized > 0.3):
        return 0.08
    elif (normalized > 0.2):
        return 0.14
    elif (normalized > 0.1):
        return 0.23
    elif (normalized > 0):
        return 0.17
    else:
        return 0

# Done
def summarize(title='', text='', max_sents=5):
    """
    Summarize the text 
    Steps Followed :
    1. Makes use of the title and text of the article to generate a list of keywords
    2. Ranks the sentences from the text on the basis of occurence of the words
    3. Sorts the sentences in the order of their occurence from the text
    """

    load_stopwords("en")

    # return null if there is no text, title or if max_sents is negative
    if not text or not title or max_sents <= 0:
        return []

    summaries = [] # stores the final summary
    sentences = split_sentences(text) # tokenize the article into sentences
    keys = keywords(text) # top 10 keywords from the text according to usage
    titleWords = split_words(title) # tokenize the title into words

    ranks = score(sentences, titleWords, keys).most_common(max_sents) # top 5 sentences selected here

    # append the 5 top sentences from the text into summaries list
    for rank in ranks:
        summaries.append(rank[0])

    # sort them on their basis of occurence
    summaries.sort(key=lambda summary: summary[0])

    # list of sentences as the summary
    lst = [summary[1] for summary in summaries]
    
    # string to store entire summary
    summary_str = ""

    for i in lst:
        summary_str = summary_str + i + " "

    keyword_list = []

    for i in keys:
        keyword_list.append(i)
    
    # return summary
    return summary_str, keyword_list

# title = "Russia-Ukraine War Live Updates: 300 feared dead in Mariupol theatre bombing"
# text = '''Russia-Ukraine War Crisis Live: As many as 300 people are feared dead in the bombing of a theater in the Ukrainian city of Mariupol last week, reported news agency AFP quoting local authorities. “From eyewitnesses, information is emerging that about 300 people died in the Drama Theatre of Mariupol following strikes by a Russian aircraft,” Mariupol city hall wrote on Telegram. On Thursday, Ukraine said its forces had destroyed the Russian landing ship the Orsk at the Russian-occupied port of Berdyansk. Video footage showed smoke rising from a blaze at a dock and the flash of an explosion.
# Subscribe Now: Get Express Premium to access the best Election reporting and analysis
# US President Joe Biden and Western allies have pledged new sanctions and humanitarian aid in response to Vladimir Putins assault on Ukraine, but their offers fell short of the more robust military assistance that President Volodymyr Zelenskyy pleaded for in a pair of live-video appearances.
# India on Thursday again abstained in the UN General Assembly on a resolution by Ukraine and its allies on the humanitarian crisis in war-torn eastern European country. The resolution was adopted with 140 votes in favour, 38 abstentions and five against. Meanwhile, the banking industry is increasingly complaining about blockages in funds transfers and credits during routine transactions between Indian and Russian banks in the absence of formal guidance on banking transactions involving Russian lenders.
# '''

# s, k = summarize(title, text)
# print(s)
# print(k)