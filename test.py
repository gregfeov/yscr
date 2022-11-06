from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
while True:
    url = input("URL: ")
    video_url = url
    session = HTMLSession()
    response = session.get(video_url)
    response.html.render(sleep=1)
    soup = bs(response.html.html, "html.parser")
    a = soup.find_all("span", class_="style-scope yt-formatted-string bold")
    print(soup.find("meta", itemprop="interactionCount")['content'])