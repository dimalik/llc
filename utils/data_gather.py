from participants.models import Participant
from session.models import Session
from paper.models import Affiliation, Journal, Author, Paper
from rating.models import Rating
## participants

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/participants.txt', 'a')

for p in Participant.objects.all().order_by('pk'):
    f.write('\t'.join([str(p.pk), str(p.name.encode('utf-8'))]))
    f.write('\n')
f.close()

## affiliation

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/affiliations.txt', 'a')

for a in Affiliation.objects.all().order_by('pk'):
    f.write('\t'.join([str(a.pk), str(a.department.encode('utf-8')), str(a.university.encode('utf-8')), str(a.post_details.encode('utf-8'))]))
    f.write('\n')
f.close()


## journal

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/journals.txt', 'a')

for j in Journal.objects.all().order_by('pk'):
    f.write('\t'.join([str(j.pk), str(j.title.encode('utf-8')), str(j.url.encode('utf-8'))]))
    f.write('\n')
f.close()


## authors

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/authors.txt', 'a')

for a in Author.objects.all().order_by('pk'):
    try:
        name = str(a.name.encode('utf-8'))
    except:
        name = ''
    try:
        email = str(a.email.encode('utf-8'))
    except:
        email = ''
    f.write('\t'.join([str(a.pk), name, email]))
    f.write('\n')
f.close()

## authors_affiliations

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/authors_affiliations.txt', 'a')

for a in Author.objects.all().order_by('pk'):
    f.write('\t'.join([str(x[0]) for x in a.affiliation.values_list()]))
    f.write('\n')
f.close()

## paper

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/papers.txt', 'a')

for p in Paper.objects.all().order_by('pk'):
    f.write('\t'.join(map(str, [
        p.pk,
        p.title.encode('utf-8'),
        p.journal_id,
        p.file.name.encode('utf-8'),
        p.year,
        p.volume,
        p.number,
        p.pages.encode('utf-8'),
        p.url.decode('utf-8'),
    ])))
    f.write('\n')
f.close()

## papers_authors

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/papers_authors.txt', 'a')

for p in Paper.objects.all().order_by('pk'):
    f.write('\t'.join([str(x[0]) for x in p.authors.values_list()]))
    f.write('\n')
f.close()

## locations

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/locations.txt', 'a')

for l in Location.objects.all().order_by('pk'):
    f.write('\t'.join([str(l.pk), str(l.name.encode('utf-8'))]))
    f.write('\n')
f.close()

## sessions

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/sessions.txt', 'a')

for s in Session.objects.all().order_by('pk'):
    f.write('\t'.join([
        str(s.pk),
        str(s.day.day),
        str(s.day.month),
        str(s.day.year),
        str(s.location_id)
    ]))
    f.write('\n')
f.close()

## paper_sessions

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/paper_sessions.txt', 'a')

for p in Paper.objects.all().order_by('pk'):
    f.write('\t'.join([
        str('\t'.join([str(x[0]) for x in p.session.values_list()])),
    ]))
    f.write('\n')
f.close()


## ratings

f = open('/Users/dimitriosalikaniotis/Sites/llc/llc_site/llc/utils/ratings.txt', 'a')

for r in Rating.objects.all().order_by('pk'):
    f.write('\t'.join(map(str, [
        r.paper_id,
        r.rater_id,
        r.score,
        r.before,
    ])))
    f.write('\n')
f.close()