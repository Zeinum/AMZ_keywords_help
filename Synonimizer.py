import urllib.request
import mtranslate

api_key = "e54fdd67ad5763fddd7ebf663946fee1"

def get_synonims(word):
    resp = urllib.request.urlopen("http://words.bighugelabs.com/api/2/{}/{}/".format(api_key, word)).read()
    resp = resp.decode("utf-8")
    resp = resp.split("\n")
    resp = [r.split("|") for r in resp]
    resp = [r[2] for r in resp if len(r)==3]
    return resp

syns = get_synonims("travel")
for s in syns:
    print(s, "", mtranslate.translate(s, to_language="ru") )
