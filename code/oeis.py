# The OEIS class contains helper functions
# for analyzing OEIS

# Uses undocumented (?) json API from
# https://oeis.org/wiki/JSON_Format,_Compressed_Files

# Author Michal Adamaszek

import urllib2, json, time

class OEIS(object):
    def __init__(self, fname = 'stripped'):
        seqs = {}

        try:
            with open(fname) as f:
                for l in f.readlines():
                    s = l.split(',')
                    name = s[0].strip()
                    currentseq = [ int(x) for x in s[1:-1] if  x!= '' ]
                    seqs[name] = currentseq
        except:
            print("Could not read the local file")

        self.seqs = seqs

    def searchID(self, id):
        return json.loads(urllib2.urlopen('https://oeis.org/search?fmt=json&q=id:{0}'.format(id)).read())['results']

    def search(self, query):
        return json.loads(urllib2.urlopen('https://oeis.org/search?fmt=json&q={0}'.format(query)).read())

    def printJSON(self, query):
        print(self.search(query))

    def count(self, query):
        return self.search(query)['count']

    def description(self, id):
        return self.searchID(id)[0]['name']

    def pause(self):
        time.sleep(20)