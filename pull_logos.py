from bs4 import BeautifulSoup
import io
import urllib.request

urls = [
        'http://www.sportslogos.net/teams/list_by_league/30/NCAA_Division_I_a-c/NCAA_a-c/logos/',
        'http://www.sportslogos.net/teams/list_by_league/31/NCAA_Division_I_d-h/NCAA_d-h/logos/',
        'http://www.sportslogos.net/teams/list_by_league/32/NCAA_Division_I_i-m/NCAA_i-m/logos/',
        'http://www.sportslogos.net/teams/list_by_league/33/NCAA_Division_I_n-r/NCAA_n-r/logos/',
        'http://www.sportslogos.net/teams/list_by_league/34/NCAA_Division_I_s-t/NCAA_s-t/logos/',
        'http://www.sportslogos.net/teams/list_by_league/35/NCAA_Division_I_u-z/NCAA_u-z/logos/'
]

str = io.StringIO()
str.write('[')

for url in urls:

    print('Loading HTML...')
    s = urllib.request.urlopen(url)
    html = s.read()

    soup = BeautifulSoup(html)
    for li in soup.find_all('img'):
        #print(li)
        if li.string is None:
            continue
        team = li.string.strip()
        filename = team.replace(' ','') + '.gif'
        image_url = li['src']

        print('Downloading ' + filename + '...')
        urllib.request.urlretrieve(image_url, filename)

        str.write('{"name":"' + team + '", "logoPath":"/img/logos/' + filename + '"},\n')

outputValue = str.getvalue().rstrip(',\n')
outputValue = outputValue + "]"
print('Writing teams.json')
open('teams.json', 'wt').write(outputValue)