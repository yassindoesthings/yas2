import os 
from selenium import webdriver

songName = input("What is the name of the song you want to play? ")
songArtist = input("Who is the song's artist? ")


PATH = "C:/Users/defaultuser0/Downloads/yas2/os/os main/packages/play music/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/results?search_query=" + songName + "+" + '"' + songArtist + '"' + '"topic"')
