from bs4 import BeautifulSoup
import requests
import html

def format(url):
    try:
        source = requests.get(url).text
    except:
        return "URL Error"

    try:
        soup = BeautifulSoup(source, "html.parser")
    except:
        return "Parse Error"

    meta = str(soup.meta)
    times = [t.contents for t in soup.find_all(class_="time secondaryText")]

    numlist = []
    namelist = []
    timelist = []

    tracks = ""
    for chunk in meta.split('\n\n'):
        if chunk[0:3] == "1. ":
            tracks = chunk
            break

    for line in tracks.splitlines():
        line = line.split('.')
        numlist.append(line[0])
        namelist.append(html.unescape(html.unescape(line[1][1:])))

    for time in times:
        time = str(time[0])
        time = time.replace(' ', '')
        time = time.replace('\n', '')
        timelist.append(time)

    numtracks = len(numlist)
    if len(namelist) != numtracks or len(timelist) != numtracks:
        return "Length Error"

    formattedlist = ""
    b = " | "
    for t in range(0, numtracks):
        formattedlist += numlist[t] + b + namelist[t] + b + timelist[t] + "\n"

    return formattedlist
