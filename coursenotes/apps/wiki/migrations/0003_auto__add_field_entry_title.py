# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.title'
        db.add_column('wiki_entry', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Entry.title'
        db.delete_column('wiki_entry', 'title')

    models = {
        'wiki.entry': {
            'Meta': {'ordering': "['-last_edit_date']", 'object_name': 'Entry'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edit_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['wiki']