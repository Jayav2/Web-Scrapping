
# Recommendation based on emotion.
# Import library for web scrapping.
from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP


def main(emotion):
    
    if (emotion == "Sad"):
        urlhere = 'https://www.imdb.com/list/ls052109630/'

    
    elif (emotion == "Excitement"):
        urlhere = 'https://www.imdb.com/search/title/?count=100&genres=action&release_date=2019,2019&title_type=feature'


    
    elif (emotion == "Disgust"):
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'


    
    elif (emotion == "Anger"):
        urlhere = 'https://www.imdb.com/list/ls004108030/'


   
    elif (emotion == "Fear"):
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'


    
    elif (emotion == "Enjoyment"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    
    elif (emotion == ""):
        urlhere = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'

    
    elif (emotion == "Trust"):
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

   
    elif (emotion == "Surprise"):
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

    # HTTP request to get the data
    
    response = HTTP.get(urlhere)
    data = response.text

    # Parsing the data using
    
    soup = SOUP(data, "lxml")

    # Extract movie titles from the
    # data using regex
    title = soup.find_all("a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    return title


# Driver Function
if __name__ == '__main__':

    emotion = input("Enter the emotion: ").title()
    a = main(emotion)

    count = 0

    if (emotion == "Surprise"):

        for i in a:
            
            tmp = str(i).split('>;')

            if (len(tmp) == 3):
                print(tmp[1][:-3])

            if (count > 102):
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split('>')

            if (len(tmp) == 3):
                print(tmp[1][:-3])

            if (count > 100):
                break
            count += 1
