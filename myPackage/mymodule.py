import pandas as pd
import numpy as np

# dictionary mapping official municipality twitter handles to municipality name
mun_dict = {
    '@CityofCTAlerts': 'Cape Town',
    '@CityPowerJhb': 'Johannesburg',
    '@eThekwiniM': 'eThekwini',
    '@EMMInfo': 'Ekurhuleni',
    '@centlecutility': 'Mangaung',
    '@NMBmunicipality': 'Nelson Mandela Bay',
    '@CityTshwane': 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords': [
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something',
        'nothing', 'thereupon', 'may', 'why', 'â€™s', 'therefore', 'you',
        'with', 'towards', 'make', 'really', 'few', 'former', 'during', 'mine',
        'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down',
        'seem', 'whereas', 'to', 'their', 'various', 'thereafter', 'â€˜d',
        'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 'at',
        'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein',
        'become', 'last', 'between', 'still', 'was', 'almost', 'twelve',
        'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see',
        'whose', 'everywhere', 'yourselves', 'across', 'myself', 'further',
        'did', 'then', 'is', 'except', 'up', 'take', 'became', 'however',
        'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein',
        'elsewhere', 'behind', 'becomes', 'alone', 'due', 'being', 'neither',
        'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 'forty',
        'what', 'less', 'and', 'please', 'toward', 'about', 'below',
        'hereafter', 'whether', 'yet', 'nor', 'against', 'whereupon', 'top',
        'first', 'three', 'show', 'per', 'five', 'two', 'ourselves',
        'whenever', 'get', 'thereby', 'noone', 'had', 'now', 'everyone',
        'everything', 'nowhere', 'ca', 'though', 'least', 'so', 'both',
        'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly',
        'â€™d', 'under', 'while', 'empty', 'doing', 'besides', 'thus', 'this',
        'anyone', 'its', 'after', 'bottom', 'call', 'nâ€™t', 'name', 'even',
        'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever',
        'out', 'full', 'themselves', 'been', 'in', "'d", 'wherever', 'part',
        'someone', 'therein', 'can', 'seemed', 'hereby', 'others', "'s", "'re",
        'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty',
        'here', 'as', 'nobody', 'also', 'along', 'than', 'anything', 'he',
        'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 'hers',
        'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re',
        'only', 'namely', 'sixty', 'made', "'m", 'always', 'those', 'have',
        'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his',
        'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 'seems', 'â€™m',
        'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless',
        'whom', 'for', 'somehow', 'beforehand', 'just', 'an', 'beyond',
        'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she',
        'never', 'eight', 'no', 'hereupon', 'them', 'whereafter', 'quite',
        'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself',
        'nâ€˜t', 'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such',
        'already', 'several', 'side', 'whence', 'me', 'same', 'were', 'it',
        'every', 'third', 'together'
    ]
}

# function 1:


def dictionary_of_metrics(items):
    """
    Function should allow a list as input:

    Returns:
    It should return a dict with keys 'mean', 'median', 'std', 'var', 'min',
    and 'max',corresponding to the input list, respectively.
    """
    my_dict = {'mean': round(np.mean(items), 2),
               'median': round(np.median(items), 2),
               'var': round(np.var(items, ddof=1), 2),
               'std': round(np.std(items, ddof=1), 2),
               'min': round(np.min(items), 2),
               'max': round(np.max(items), 2)}

    return my_dict

# function 2:


def five_num_summary(items):
    """
    The function takes a list as input.

    Returns:
    The function returns a dictionary with keys 'max', 'median', 'min', 'q1',
    and 'q3'
    corresponding to the maximum, median, minimum, first quartile and
    third quartile, respectively.
    All numerical values are rounded to two decimal places.

        For example:
        welkom = [1,2,3,4,5,6,7]
        five_num_summary(welkom)
        >>> {'max': 7, 'median': 4.0, 'min': 1, 'q1': 2.5, 'q3': 5.5}
    """
    summary = {'max': round(np.max(items), 2),
               'median': round(np.median(items), 2),
               'min': round(np.min(items), 2),
               'q1': round(np.percentile(items, 25, axis=0), 2),
               'q3': round(np.percentile(items, 75, axis=0), 2)}

    return summary

# function 3:


def date_parser(dates):
    """
    The function should take a list of strings as input.
    Each string in the input list is formatted as 'yyyy-mm-dd hh:mm:ss'.

    Returns:
    The function should return a list of strings
    where each element in the returned list contains only the date in the
    'yyyy-mm-dd' format.

    For Example:
    dates[:3] == [ '2015-12-25 11:45:54', '2015-12-25 11:40:03',
                    2015-12-25 11:30:02']

    Output:
           dates[:3] == ['2015-12-25', '2015-12-25', '2015-12-25' ]
    """
    for i in dates:
        i = pd.to_datetime(dates, format='%Y-%m-%d').strftime('%Y-%m-%d')

    return list(i)

# function 4:


def extract_municipality_hashtags(df):
    """
    This function takes in a pandas dataframe:

    Returns:
    A modified dataframe that includes two new columns that contain information
    about the municipality and hashtag of the tweet
    """
    municipality = []

    for i in range(0, len(df)):
        city_found = ''

        for x, y in mun_dict.items():
            v = df.iloc[i][0].find(x)
            if v is not -1:
                city_found = y

            else:
                city_found = np.nan
        municipality.append(city_found)

        df1 = pd.DataFrame(municipality, columns=['municipality'])

        df2 = df.join(df1, lsuffix='Date', rsuffix='municipality')

        H = [list(filter(lambda x: x.startswith('#'),
                  df['Tweets'][i].lower().split()))
             for i in range(len(df.index.values))]
        hashtags = pd.DataFrame([np.nan if x == [] else x for x in H],
                                columns=['hashtags'])

        final = df2.join(hashtags, lsuffix='municipality', rsuffix='hashtags')

    return final

# function 5


def number_of_tweets_per_day(df):
    """
    This function returns the number of tweets per day:

    Parameters: items- dataframe

    Return: num_of_tweets_per_day:
    prints Date: number of tweets

    """
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

    result = df[['Tweets']].groupby(df['Date'].dt.date).count()

    return result

# function 6:


def word_splitter(df):
    """
    This function splits the sentences in a dataframe's column into a list of
    the separate words:

    Returns:
    The function should split the sentences in the 'Tweets' into a list of
    seperate words,
    and place the result into a new column named 'Split Tweets'. The resulting
    words must all be lowercase!
    """
    words = df['Tweets']

    df['Split Tweets'] = [word.lower().split() for word in words]

    return df

# function 7:


def stop_words_remover(df):
    """
    This function removes english stop words from a tweet:

    Returns:
    Provides a modified dataframe that removes all stop words in the tokenised
    list.
    The resulting tokenised list should be placed in a column named
    `"Without Stop Words"`.
    """
    stop_words = stop_words_dict["stopwords"]

    df["Without Stop Words"] = df["Tweets"].str.lower().str.split()

    df["Without Stop Words"] = df["Without Stop Words"].apply(lambda x:
                                                              [word for word in
                                                               x if word not in
                                                               stop_words])

    return df
