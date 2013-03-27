# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JobListing'
        db.create_table(u'helpwanted_joblisting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('position_description', self.gf('django.db.models.fields.TextField')()),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('organization_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('is_filled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('published_until', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'helpwanted', ['JobListing'])


    def backwards(self, orm):
        # Deleting model 'JobListing'
        db.delete_table(u'helpwanted_joblisting')


    models = {
        u'helpwanted.joblisting': {
            'Meta': {'ordering': "['-date_published', 'position']", 'object_name': 'JobListing'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_filled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'organization_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position_description': ('django.db.models.fields.TextField', [], {}),
            'position_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'published_until': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['helpwanted']