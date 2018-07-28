import requests
import re
import time

delay = 1

asins = ["B0725QS78J", "B07BL325JJ"]

keywords = """
chunky puzzle preschool learning toy educational for kids and toddlers - wooden montessori jigsaw board animals cats mouse fish gift box nice colors puzzles toys wood baby boy girl kid cat zigsaw stem fun old top organic best ages large education set art s.t.e.m big age year olds yr 1 2 3 4 5 6 infant table sorting learn brain small shape sorter match color recognition gifts 7 cheap cool boys games birthday girls toddler babies play children game indoor outdoor round
""".split()
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,lt;q=0.8,ru;q=0.7,fr;q=0.6'
}

print(keywords)

for asin in asins:
    indexed = []
    not_indexed = []
    for kw in keywords:
        url = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={}+{}".format(asin, kw)
        # print(url)
        r = requests.get(url, headers = headers)
        # print(r.text)
        pattern = "(\d) result for .+?{} {}".format(asin, kw)
        a = re.findall(pattern, r.text)

        if a and a[0] == '1':
            indexed.append(kw)
        else:
            not_indexed.append(kw)
        time.sleep(delay)
    print("/\/\/\/\/\/\/\/\/")
    print("ASIN: " + asin )
    print("INDEXED:")
    print("\n".join(indexed))
    print("------------")
    print("NOT INDEXED:")
    print("\n".join(not_indexed))
