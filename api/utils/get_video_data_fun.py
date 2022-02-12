from requests_html import HTMLSession, AsyncHTMLSession
from bs4 import BeautifulSoup as bs 
from pytube import YouTube

# async def get_video_data_fun( video_id):
#     # sample youtube video url
#     video_url = f"https://www.youtube.com/watch?v={video_id}"
#     # init an HTML Session
#     session  = AsyncHTMLSession()
#      # download HTML code
#     response = await session.get(video_url)
#     await response.html.render(sleep=1, keep_page = True, scrolldown = 2)
#     # create beautiful soup object to parse HTML
#     soup = bs(await response.html.html, "html.parser")
#     # open("index.html", "w").write(response.html.html)
#     # initialize the result
#     # print(soup.find_all("meta"))
#     video_name=soup.find("meta", itemprop="name")["content"]
#     video_description=soup.find("meta", itemprop="description")["content"]
#     video_image=soup.find("meta", property="og:image")["content"]
#     video_interactionCount=soup.find("meta", itemprop="interactionCount")["content"]
#     print(video_name)
#     print(video_description)
#     print(video_image)
#     print(video_interactionCount)
#     return {
#         "video_name": video_name,
#         "video_description": video_description,
#         "video_image": video_image,
#         "video_interactionCount": video_interactionCount,
#     }

def get_video_data_fun( video_id):
    # sample youtube video url
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    video=YouTube(video_url)
    return {
        "video_name": video.title,
        "video_description": video.description,
        "video_image": video.thumbnail_url,
        "video_interactionCount": video.rating,
    }