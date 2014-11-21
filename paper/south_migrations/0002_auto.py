# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field related_papers on 'Paper'
        m2m_table_name = db.shorten_name(u'paper_paper_related_papers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_paper', models.ForeignKey(orm[u'paper.paper'], null=False)),
            ('to_paper', models.ForeignKey(orm[u'paper.paper'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_paper_id', 'to_paper_id'])


    def backwards(self, orm):
        # Removing M2M table for field related_papers on 'Paper'
        db.delete_table(db.shorten_name(u'paper_paper_related_papers'))


    models = {
        u'paper.affiliation': {
            'Meta': {'object_name': 'Affiliation'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_details': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'paper.author': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Author'},
            'affiliation': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['paper.Affiliation']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'paper.journal': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Journal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'paper.paper': {
            'Meta': {'object_name': 'Paper'},
            'authors': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['paper.Author']", 'symmetrical': 'False'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paper.Journal']"}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'related_papers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_papers_rel_+'", 'to': u"orm['paper.Paper']"}),
            'session': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['session.Session']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        u'session.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'session.session': {
            'Meta': {'ordering': "('-day',)", 'object_name': 'Session'},
            'day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['session.Location']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['paper']