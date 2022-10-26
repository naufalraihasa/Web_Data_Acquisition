from bs4 import BeautifulSoup
import requests
import json

semua_judul = []
semua_tanggal = []
semua_link = []
daftar_judul = [semua_judul]
daftar_tanggal = [semua_tanggal]
daftar_link = [semua_link]

def scraping (webpage):
    response = requests.get(webpage)
    unair_news = response.text
    soup = BeautifulSoup(unair_news, "html.parser")
    #judul artikel
    judul_artikel = soup.find_all(name="h3",class_="elementor-post__title")
    # tanggal upload artikel
    tanggal_artikel = soup.find_all(name="span", class_="elementor-post-date")
    # link artikel
    link_artikel = soup.find_all(name="h3", class_="elementor-post__title")


    for x in range(len(judul_artikel)):
        semua_judul.append(judul_artikel[x].getText().strip())
        semua_tanggal.append(tanggal_artikel[x].getText().strip())
    for links in link_artikel:
        link_artikel_a= links.findChildren("a")
        for link in link_artikel_a:
            link_artikel_text = link.get("href")
            semua_link.append(link_artikel_text)

webpage = "https://www.unair.ac.id/news/"
scraping(webpage)
list_ = ['daftar_judul', 'daftar_tanggal', 'daftar_link']
data = {listname: globals()[listname] for listname in list_}
with open('Data_Unair_News_scraping.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)