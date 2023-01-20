# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ports(models.Model):
    code = models.TextField(primary_key=True)
    name = models.TextField()
    parent_slug = models.ForeignKey('Regions', models.DO_NOTHING, db_column='parent_slug')

    class Meta:
        db_table = 'ports'


class Prices(models.Model):
    orig_code = models.ForeignKey(Ports, models.DO_NOTHING, db_column='orig_code')
    dest_code = models.ForeignKey(Ports, models.DO_NOTHING, db_column='dest_code')
    day = models.DateField()
    price = models.IntegerField()

    class Meta:
        db_table = 'prices'


class Regions(models.Model):
    slug = models.TextField(primary_key=True)
    name = models.TextField()
    parent_slug = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_slug', blank=True, null=True)

    class Meta:
        db_table = 'regions'
