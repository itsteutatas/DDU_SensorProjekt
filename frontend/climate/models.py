from django.db import models

# Create your models here.
class Collectors(models.Model):
    collectorid = models.AutoField(db_column='collectorID', primary_key=True)  # Field name made lowercase.
    room_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collectors'


class Data(models.Model):
    dataid = models.AutoField(db_column='dataID', primary_key=True)  # Field name made lowercase.
    collectorid = models.ForeignKey(Collectors, models.DO_NOTHING, db_column='collectorID', blank=True, null=True)  # Field name made lowercase.
    humidity = models.IntegerField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    date = models.CharField(blank=True, null=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'data'