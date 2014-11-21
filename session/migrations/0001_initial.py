# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'session_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'session', ['Location'])

        # Adding model 'Session'
        db.create_table(u'session_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.DateField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['session.Location'], null=True, blank=True)),
        ))
        db.send_create_signal(u'session', ['Session'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'session_location')

        # Deleting model 'Session'
        db.delete_table(u'session_session')


    models = {
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

    complete_apps = ['session']