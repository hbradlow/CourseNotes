# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Webcast'
        db.create_table('wiki_webcast', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(default='', max_length=500)),
        ))
        db.send_create_signal('wiki', ['Webcast'])

        # Adding M2M table for field webcasts on 'Entry'
        db.create_table('wiki_entry_webcasts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm['wiki.entry'], null=False)),
            ('webcast', models.ForeignKey(orm['wiki.webcast'], null=False))
        ))
        db.create_unique('wiki_entry_webcasts', ['entry_id', 'webcast_id'])

    def backwards(self, orm):
        # Deleting model 'Webcast'
        db.delete_table('wiki_webcast')

        # Removing M2M table for field webcasts on 'Entry'
        db.delete_table('wiki_entry_webcasts')

    models = {
        'wiki.entry': {
            'Meta': {'ordering': "['-last_edit_date']", 'object_name': 'Entry'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edit_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'webcasts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wiki.Webcast']", 'symmetrical': 'False'})
        },
        'wiki.webcast': {
            'Meta': {'object_name': 'Webcast'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'})
        }
    }

    complete_apps = ['wiki']