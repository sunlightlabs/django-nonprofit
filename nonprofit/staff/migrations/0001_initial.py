# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'staff_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
        ))
        db.send_create_signal(u'staff', ['Location'])

        # Adding model 'Department'
        db.create_table(u'staff_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'staff', ['Department'])

        # Adding model 'Member'
        db.create_table(u'staff_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='members', null=True, to=orm['staff.Department'])),
            ('is_department_head', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_employed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('employment_status', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('primary_location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='members', null=True, to=orm['staff.Location'])),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('github', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('office_phone', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('home_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('emergency_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('emergency_phone', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('emergency_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('guid', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
        ))
        db.send_create_signal(u'staff', ['Member'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'staff_location')

        # Deleting model 'Department'
        db.delete_table(u'staff_department')

        # Deleting model 'Member'
        db.delete_table(u'staff_member')


    models = {
        u'staff.department': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'staff.location': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Location'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'staff.member': {
            'Meta': {'ordering': "('last_name', 'first_name')", 'object_name': 'Member'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'to': u"orm['staff.Department']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'emergency_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'emergency_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'emergency_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'employment_status': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'home_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_department_head': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_employed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'office_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'primary_location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'to': u"orm['staff.Location']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
        }
    }

    complete_apps = ['staff']