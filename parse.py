import requests
from lxml import html
import re

gameerrankings = {}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

with open('xbox-game-pass-console.txt', 'r+') as f:
    lines = (line.rstrip() for line in f)
    lines = (line for line in lines if line)
    for l in lines: 
        if not (l.startswith('Viewing') 
                or l.startswith('CLEAR FILTERS') 
                or l.startswith('Sort') 
                or l.startswith('box shot') 
                or l.startswith('QUICK LOOK') 
                ):
            l = re.sub('[™®]', '', l)
            l = re.sub('Standard Edition', '', l)
            l = re.sub('Full Game', '', l)
            l = re.sub(': The One Edition', '', l)
            l = re.sub(' - Xbox One Edition', '', l)
            l = re.sub(': Special Edition', '', l)
            l = re.sub(': Special Edition', '', l)
            l = re.sub(' - Definitive Edition', '', l)
            l = re.sub(' STANDARD EDITION', '', l)
            l = re.sub(': Console Edition', '', l)
            l = re.sub(' - Xbox', '', l)
            l = re.sub(' - Game Preview', '', l)
            l = re.sub(': Definitive Edition', '', l)
            l = re.sub(' - HD 1.5+2.5 ReMIX -', '', l)
            l = re.sub(': Complete Edition', '', l)
            l = re.sub(' - Definitive Edition', '', l)
            l = re.sub(' - The Complete Season (Episodes 1-5)', '', l)
            l = re.sub(' (Game Preview)', '', l)
            l = re.sub(' (Xbox One)', '', l)
            
            print(l)

            game = l
            url = 'https://www.metacritic.com/search/game/'+game+'/results?search_type=advanced&plats[80000]=1'
            
            print(url)
            
            r = requests.get(url, headers=headers)
            if r is not None and r != '': tree = html.fromstring(r.content)
            else: continue

            positive = tree.xpath('//span[@class="metascore_w medium game positive"]/text()')
            mixed = tree.xpath('//span[@class="metascore_w medium game mixed"]/text()')
            negative = tree.xpath('//span[@class="metascore_w medium game negative"]/text()')
            
            if positive: gameerrankings[game] = int(positive[0])
            elif mixed: gameerrankings[game] = int(mixed[0])
            elif negative: gameerrankings[game] = int(negative[0])
            else: 
                url = 'https://www.metacritic.com/search/game/'+game+'/results?search_type=advanced&plats[2]=1'

                print(url)

                r = requests.get(url, headers=headers)
                if r is not None and r != '': tree = html.fromstring(r.content)
                else: continue

                positive = tree.xpath('//span[@class="metascore_w medium game positive"]/text()')
                mixed = tree.xpath('//span[@class="metascore_w medium game mixed"]/text()')
                negative = tree.xpath('//span[@class="metascore_w medium game negative"]/text()')

                if positive: gameerrankings[game] = int(positive[0])
                elif mixed: gameerrankings[game] = int(mixed[0])
                elif negative: gameerrankings[game] = int(negative[0])
                else: gameerrankings[game] = -1

with open('ea-pass.txt', 'r+') as f:
    lines = (line.rstrip() for line in f)
    lines = (line for line in lines if line)
    for l in lines: 
        if not (l.startswith('Viewing') 
                or l.startswith('CLEAR FILTERS') 
                or l.startswith('Sort') 
                or l.startswith('box shot') 
                or l.startswith('QUICK LOOK') 
                ):
            l = re.sub('[™®]', '', l)
            l = re.sub('EA SPORTS NHL', 'NHL', l)
            l = re.sub('EA SPORTS NBA', 'NBA', l)
            l = re.sub('EA SPORTS FIFA', 'FIFA', l)
            l = re.sub('Standard Edition', '', l)
            l = re.sub('Full Game', '', l)
            l = re.sub(': The One Edition', '', l)
            
            print(l)
            
            game = l
            url = 'https://www.metacritic.com/search/game/'+game+'/results?search_type=advanced&plats[80000]=1'
            
            print(url)
            
            r = requests.get(url, headers=headers)
            if r is not None and r != '': tree = html.fromstring(r.content)
            else: continue

            positive = tree.xpath('//span[@class="metascore_w medium game positive"]/text()')
            mixed = tree.xpath('//span[@class="metascore_w medium game mixed"]/text()')
            negative = tree.xpath('//span[@class="metascore_w medium game negative"]/text()')
            
            if positive: gameerrankings[game] = int(positive[0])
            elif mixed: gameerrankings[game] = int(mixed[0])
            elif negative: gameerrankings[game] = int(negative[0])
            else: 
                url = 'https://www.metacritic.com/search/game/'+game+'/results?search_type=advanced&plats[2]=1'

                print(url)

                r = requests.get(url, headers=headers)
                if r is not None and r != '': tree = html.fromstring(r.content)
                else: continue

                positive = tree.xpath('//span[@class="metascore_w medium game positive"]/text()')
                mixed = tree.xpath('//span[@class="metascore_w medium game mixed"]/text()')
                negative = tree.xpath('//span[@class="metascore_w medium game negative"]/text()')

                if positive: gameerrankings[game] = int(positive[0])
                elif mixed: gameerrankings[game] = int(mixed[0])
                elif negative: gameerrankings[game] = int(negative[0])
                else: gameerrankings[game] = -1

gameerrankings = {k: v for k, v in sorted(gameerrankings.items(), key=lambda item: item[1], reverse=True)}

for k, v in gameerrankings.items():
    print(k, v)

