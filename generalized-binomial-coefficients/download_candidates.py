import urllib2
from time import time

# from https://oeis.org/eishelp1.html
sectionLabels = {
            'Identification': '%I',
            'Sequence': '%S',
            'Name': '%N',
            'Detailed References': '%D',
            'Links related to this sequence': '%H',
            'Formula': '%F',
            'Cross-references to other sequences': '%Y',
            'Author': '%A',
            'Maple program': '%p',
            'Mathematica program': '%t',
            'Other program': '%o',
            'Keywords': '%K',
            'Comments': '%C'
           }

def find_between(string, first, last):
    try:
        start = string.index( first ) + len( first )
        end = string.index( last, start )
        return string[start:end]
    except ValueError:
        return ""
        
def GetSectionFromLabel(html, label):
    return find_between(html, label, '\n')
    
def GetSectionLabelFromSectionName(sectionName):
    return sectionLabels[sectionName]
               
def GetSequence(html):
    label = GetSectionLabelFromSectionName('Sequence')
    return GetSectionFromLabel(html, label)
    
def GetName(html):
    label = GetSectionLabelFromSectionName('Name')
    return GetSectionFromLabel(html, label)

def GetFormula(html):
    label = GetSectionLabelFromSectionName('Formula')
    return GetSectionFromLabel(html, label)

    
def get_oeis_url(seq_id):
    url = 'http://oeis.org/%s/internal' % seq_id
    return url

def main():
    file = "candidates.txt"
    start = time()
    count = 0
    with  open('candidates.txt', 'r') as candidates, open('name_and_formulas.txt', 'w') as output:
        for line in candidates:
            count += 1
            seq_id = line.strip()
            url = get_oeis_url(seq_id)
            response = urllib2.urlopen(url)
            html = response.read()
            name = GetName(html)
            formula = GetFormula(html)
            if formula:
                output.write(seq_id + ',' + name + ',' + formula + '\n')
            if count % 100 == 0:
                current_time = time() - start
                print 'Downloaded %s sequences in %s seconds' % (count, current_time)
                print 'This is an average of %s sequences per second' % (float(count) /  current_time)
                
          
    end = time()
    length = round((end-start)/60)
    # 277 minutes at home (3 seqs/sec)
    print 'Downloaded %s sequences in %s minutes!' % (count , length)
        
    
if __name__ == "__main__":
    main()