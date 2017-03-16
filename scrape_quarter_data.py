from bs4 import BeautifulSoup
import requests
import csv


def scrape(url, output_name):
    url = "https://en.wikipedia.org/wiki/50_State_Quarters"

    r = requests.get(url)

    page = r.text

    soup = BeautifulSoup(page, "html.parser")


    year = ""
    number = ""
    state = ""
    releasedate = ""
    design = ""
    elementsdepicted = ""
    engraver = ""

    tablesoup = soup.find("table", {"class" : "wikitable sortable" })

    f = open('quartersoup.csv', 'w')

    for row in tablesoup.findAll("tr"):
        cells = row.findAll("td")
        if len(cells) == 6:
            year = cells[0].find(text=True)
            number = cells[1].find(text=True)
            statereleasedate = cells[2].find(text=True)
            design = cells[3].find(text=True)
            elements depicted = cells[4].find(text=True)
            engraver = cells[5].find(text=True)
            write_to_file = year + "," + state + "," + elementsdepicted



    f.close()
