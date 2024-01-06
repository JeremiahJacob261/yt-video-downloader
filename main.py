import requests
import json
from pytube import YouTube
from bs4 import BeautifulSoup

def Download(link):
   youtubeObject = YouTube(link)
   youtubeObject = youtubeObject.streams.get_highest_resolution()
   try:
       youtubeObject.download()
   except:
       print("An error has occurred")
   print("Download is completed successfully")

link = input("Enter the YouTube video URL: ")
Download(link)
