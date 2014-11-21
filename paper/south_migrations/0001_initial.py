# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Affiliation'
        db.create_table(u'paper_affiliation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('post_details', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'paper', ['Affiliation'])

        # Adding model 'Author'
        db.create_table(u'paper_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'paper', ['Author'])

        # Adding M2M table for field affiliation on 'Author'
        m2m_table_name = db.shorten_name(u'paper_author_affiliation')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('author', models.ForeignKey(orm[u'paper.author'], null=False)),
            ('affiliation', models.ForeignKey(orm[u'paper.affiliation'], null=False))
        ))
        db.create_unique(m2m_table_name, ['author_id', 'affiliation_id'])

        # Adding model 'Journal'
        db.create_table(u'paper_journal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'paper', ['Journal'])

        # Adding model 'Paper'
        db.create_table(u'paper_paper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('journal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paper.Journal'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('volume', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pages', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'paper', ['Paper'])


        # Adding SortedM2M table for field authors on 'Paper'
        db.create_table(u'paper_paper_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paper', models.ForeignKey(orm[u'paper.paper'], null=False)),
            ('author', models.ForeignKey(orm[u'paper.author'], null=False)),
            ('sort_value', models.IntegerField())
        ))
        db.create_unique(u'paper_paper_authors', ['paper_id', 'author_id'])
        # Adding M2M table for field session on 'Paper'
        m2m_table_name = db.shorten_name(u'paper_paper_session')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paper', models.ForeignKey(orm[u'paper.paper'], null=False)),
            ('session', models.ForeignKey(orm[u'session.session'], null=False))
        ))
        db.create_unique(m2m_table_name, ['paper_id', 'session_id'])


    def backwards(self, orm):
        # Deleting model 'Affiliation'
        db.delete_table(u'paper_affiliation')

        # Deleting model 'Author'
        db.delete_table(u'paper_author')

        # Removing M2M table for field affiliation on 'Author'
        db.delete_table(db.shorten_name(u'paper_author_affiliation'))

        # Deleting model 'Journal'
        db.delete_table(u'paper_journal')

        # Deleting model 'Paper'
        db.delete_table(u'paper_paper')

        # Removing M2M table for field authors on 'Paper'
        db.delete_table(db.shorten_name(u'paper_paper_authors'))

        # Removing M2M table for field session on 'Paper'
        db.delete_table(db.shorten_name(u'paper_paper_session'))


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