# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'roster_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roster.Student'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roster.Team'])),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('hand', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'roster', ['Player'])

        # Adding model 'School'
        db.create_table(u'roster_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'roster', ['School'])

        # Adding model 'Student'
        db.create_table(u'roster_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('hometown', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('highschool', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'roster', ['Student'])

        # Adding model 'Sport'
        db.create_table(u'roster_sport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'roster', ['Sport'])

        # Adding model 'Team'
        db.create_table(u'roster_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roster.Sport'])),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roster.School'])),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'roster', ['Team'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'roster_player')

        # Deleting model 'School'
        db.delete_table(u'roster_school')

        # Deleting model 'Student'
        db.delete_table(u'roster_student')

        # Deleting model 'Sport'
        db.delete_table(u'roster_sport')

        # Deleting model 'Team'
        db.delete_table(u'roster_team')


    models = {
        u'roster.player': {
            'Meta': {'object_name': 'Player'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'hand': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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