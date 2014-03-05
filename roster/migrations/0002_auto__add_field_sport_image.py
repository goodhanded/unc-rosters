# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sport.image'
        db.add_column(u'roster_sport', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sport.image'
        db.delete_column(u'roster_sport', 'image')


    models = {
        u'roster.player': {
            'Meta': {'object_name': 'Player'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'hand': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roster.Student']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roster.Team']"})
        },
        u'roster.school': {
            'Meta': {'ordering': "('name',)", 'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'roster.sport': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Sport'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'roster.student': {
            'Meta': {'ordering': "('last_name', 'first_name')", 'object_name': 'Student'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'highschool': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'weight': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'roster.team': {
            'Meta': {'object_name': 'Team'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roster.School']"}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roster.Sport']"})
        }
    }

    complete_apps = ['roster']