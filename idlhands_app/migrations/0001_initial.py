# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('idlhands_app_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('info', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=320)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('trendsetter', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('gallery', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('avatar', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('user_since', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('idlhands_app', ['UserProfile'])

        # Adding model 'Project'
        db.create_table('idlhands_app_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idlhands_app.UserProfile'])),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('media', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal('idlhands_app', ['Project'])

        # Adding model 'Image'
        db.create_table('idlhands_app_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idlhands_app.UserProfile'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idlhands_app.Project'])),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('idlhands_app', ['Image'])

        # Adding model 'Vote'
        db.create_table('idlhands_app_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idlhands_app.UserProfile'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idlhands_app.Image'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('idlhands_app', ['Vote'])

        # Adding model 'Date'
        db.create_table('idlhands_app_date', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('idlhands_app', ['Date'])

        # Adding model 'Show'
        db.create_table('idlhands_app_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exhibition', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('opening_date', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idlhands_app.Date'])),
            ('opening_start', self.gf('django.db.models.fields.DateTimeField')()),
            ('opening_end', self.gf('django.db.models.fields.DateTimeField')()),
            ('exhibition_start', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('exhibition_end', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idlhands_app.UserProfile'])),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('location_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('idlhands_app', ['Show'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('idlhands_app_userprofile')

        # Deleting model 'Project'
        db.delete_table('idlhands_app_project')

        # Deleting model 'Image'
        db.delete_table('idlhands_app_image')

        # Deleting model 'Vote'
        db.delete_table('idlhands_app_vote')

        # Deleting model 'Date'
        db.delete_table('idlhands_app_date')

        # Deleting model 'Show'
        db.delete_table('idlhands_app_show')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'idlhands_app.date': {
            'Meta': {'object_name': 'Date'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'idlhands_app.image': {
            'Meta': {'object_name': 'Image'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.UserProfile']"}),
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
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.UserProfile']"}),
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
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.UserProfile']"}),
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
        'idlhands_app.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'avatar': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '320'}),
            'gallery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'trendsetter': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'user_since': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'idlhands_app.vote': {
            'Meta': {'object_name': 'Vote'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.Image']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['idlhands_app.UserProfile']"})
        }
    }

    complete_apps = ['idlhands_app']