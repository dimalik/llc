import datetime

from paper.models import Paper, Journal, Affiliation, Author
from session.models import Session, Location
from participants.models import Participant
from ratings.models import Rating

## participants

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/participants.txt')

for line in f:
    p = Participant()
    p.name = line.strip().split('\t')[1]
    p.save()
    
f.close()

## affiliation

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/affiliations.txt')

for line in f:
    a = Affiliation()
    try:
        a.department = line.strip().split('\t')[1]
    except:
        pass
    try:
        a.university = line.strip().split('\t')[2]
    except:
        pass
    try:
        a.post_details = line.strip().split('\t')[3]
    except:
        pass
    a.save()
    
f.close()

## journal

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/journals.txt')

for line in f:
    a = Journal()
    try:
        a.title = line.strip().split('\t')[1]
    except:
        pass
    try:
        a.url = line.strip().split('\t')[2]
    except:
        pass
    a.save()
    
f.close()

## authors

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/authors.txt')

for line in f:
    a = Author()
    try:
        a.name = line.strip().split('\t')[1]
    except:
        pass
    try:
        a.email = line.strip().split('\t')[2]
    except:
        pass
    a.save()
    
f.close()

## author_affiliation

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/authors_affiliations.txt')

for i, line in enumerate(f, 1):
    if line.strip():
        a = Author.objects.get(pk=i)
        affiliations = map(int, line.strip().split('\t'))
        for a_id in affiliations:
            a.affiliation.add(Affiliation.objects.get(pk=a_id))
f.close()

## papers

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/papers.txt')

for line in f:
    a = Paper()
    try:
        a.title = line.strip().split('\t')[1]
    except:
        pass
    try:
        jid = int(line.strip().split('\t')[2])
        a.journal = Journal.objects.get(pk=jid)
    except:
        pass
    try:
        a.file = line.strip().split('\t')[3]
    except:
        pass
    try:
        a.year = line.strip().split('\t')[4]
    except:
        pass

    vol = line.strip().split('\t')[5]
    if vol != "None":
        a.volume = int(vol)
    try:
        num = line.strip().split('\t')[6]
        if num != "None":
            a.number = line.strip().split('\t')[6]
    except:
        pass
    try:
        pag = line.strip().split('\t')[7]
        if pag != "None":
            a.pages = pag
    except:
        pass
    try:
        ur = line.strip().split('\t')[8]
        if ur != "None":
            a.url = line.strip().split('\t')[8]
    except:
        pass
    a.save()
    
f.close()

## papers_authors

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/papers_authors.txt')

for i, line in enumerate(f, 1):
    if line.strip():
        p = Paper.objects.get(pk=i)
        authors = map(int, line.strip().split('\t'))
        for a_id in authors:
            p.authors.add(Author.objects.get(pk=a_id))
f.close()

## locations

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/locations.txt')

for line in f:
    l = Location()
    try:
        l.name = line.strip().split('\t')[1]
    except:
        pass
    l.save()
    
f.close()

## sessions

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/sessions.txt')
f2 = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/paper_sessions.txt')
d = {}
for i, s in enumerate(f2, 1):
    d[i] = map(int, s.strip().split('\t'))

for line in f:
    s = Session()
    newline = map(int, line.strip().split('\t'))
    day = newline[1]
    month = newline[2]
    year = newline[3]
    loc = newline[4]
    date = datetime.date(year=year, month=month, day=day)
    s.day = date
    s.location = Location.objects.get(pk=loc)
    s.save()
    for i, (k, v) in enumerate(d.iteritems(), 1):
        if s.pk in v:
            s.paper.add(Paper.objects.get(pk=i))
    s.save()
    
f.close()

## ratings

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/ratings.txt')

for line in f:
    r = Rating()
    try:
        pid = line.strip().split('\t')[0]
        r.paper = Paper.objects.get(pk=pid)
    except:
        pass
    try:
        rid = line.strip().split('\t')[1]
        if rid != "None":
            r.rater = Participant.objects.get(pk=rid)
    except:
        pass
    try:
        r.score = float(line.strip().split('\t')[2])
    except:
        pass
    try:
        b = line.strip().split('\t')[3]
        if b == "True":
            r.before = True
        else:
            r.before = False
    except:
        pass
    r.save()
    
f.close()