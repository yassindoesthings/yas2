import os 
from selenium import webdriver

songName = input("What is the name of the song you want to play? ")
songArtist = input("Who is the song's artist? ")


PATH = ""
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/results?search_query=" + songName + "+" + '"' + songArtist + '"' + '"topic"')
