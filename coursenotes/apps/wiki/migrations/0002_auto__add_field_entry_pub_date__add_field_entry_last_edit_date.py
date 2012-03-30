# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.pub_date'
        db.add_column('wiki_entry', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 3, 24, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Entry.last_edit_date'
        db.add_column('wiki_entry', 'last_edit_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 3, 24, 0, 0), blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Entry.pub_date'
        db.delete_column('wiki_entry', 'pub_date')

        # Deleting field 'Entry.last_edit_date'
        db.delete_column('wiki_entry', 'last_edit_date')

    models = {
        'wiki.entry': {
            'Meta': {'object_name': 'Entry'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edit_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['wiki']