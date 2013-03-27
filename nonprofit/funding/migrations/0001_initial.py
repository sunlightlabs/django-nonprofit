# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contribution'
        db.create_table(u'funding_contribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=2013)),
            ('contributor', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_inkind', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'funding', ['Contribution'])

        # Adding model 'Grant'
        db.create_table(u'funding_grant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=2013)),
            ('recipient', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('recipient_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('purpose', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_minigrant', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'funding', ['Grant'])


    def backwards(self, orm):
        # Deleting model 'Contribution'
        db.delete_table(u'funding_contribution')

        # Deleting model 'Grant'
        db.delete_table(u'funding_grant')


    models = {
        u'funding.contribution': {
            'Meta': {'ordering': "('-year', '-amount', 'contributor')", 'object_name': 'Contribution'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'contributor': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_inkind': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2013'})
        },
        u'funding.grant': {
            'Meta': {'ordering': "('-year', '-amount', 'recipient')", 'object_name': 'Grant'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_minigrant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'purpose': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'recipient_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2013'})
        }
    }

    complete_apps = ['funding']