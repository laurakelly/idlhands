# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.url'
        db.delete_column('idlhands_app_image', 'url')

        # Adding field 'Image.image'
        db.add_column('idlhands_app_image', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Image.width'
        db.add_column('idlhands_app_image', 'width',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Image.height'
        db.add_column('idlhands_app_image', 'height',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Image.url'
        db.add_column('idlhands_app_image', 'url',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=200),
                      keep_default=False)

        # Deleting field 'Image.image'
        db.delete_column('idlhands_app_image', 'image')

        # Deleting field 'Image.width'
        db.delete_column('idlhands_app_image', 'width')

        # Deleting field 'Image.height'
        db.delete_column('idlhands_app_image', 'height')


    models = {
        'idlhands_app.date': {
            'Meta': {'object_name': 'Date'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'idlhands_app.image': {
            'Meta': {'object_name': 'Image'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.User']"}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.Project']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        'idlhands_app.project': {
            'Meta': {'object_name': 'Project'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'idlhands_app.show': {
            'Meta': {'object_name': 'Show'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'exhibition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exhibition_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'exhibition_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opening_date': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.Date']"}),
            'opening_end': ('django.db.models.fields.DateTimeField', [], {}),
            'opening_start': ('django.db.models.fields.DateTimeField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'idlhands_app.user': {
            'Meta': {'object_name': 'User'},
            'avatar': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '320'}),
            'gallery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'trendsetter': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'user_since': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'idlhands_app.vote': {
            'Meta': {'object_name': 'Vote'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.Image']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.User']"})
        }
    }

    complete_apps = ['idlhands_app']