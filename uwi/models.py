from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MonConductorHistory(models.Model):
    conductor_id = models.BigIntegerField(primary_key=True)
    conductor_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'MON_CONDUCTOR_HISTORY'

class MonTerminalInfo(models.Model):
    rowid = models.CharField(max_length=255,primary_key=True)
    smid = models.CharField(max_length=7)
    hardware_model = models.CharField(max_length=64)
    hardware_serial_number = models.CharField(max_length=64)
    os_version = models.CharField(max_length=64)
    software_name = models.CharField(max_length=64)
    software_version = models.CharField(max_length=64)
    software_sha1 = models.CharField(max_length=40)
    sm_version = models.CharField(max_length=64)
    info_timestamp = models.DateTimeField()
    load_id = models.BigIntegerField()
    create_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mon_terminal_info'

class MonTerminalStates(models.Model):
    rowid = models.CharField(max_length=255,primary_key=True)
    smid = models.CharField(max_length=7)
    route_number = models.CharField(max_length=10, blank=True, null=True)
    trip_number = models.IntegerField(blank=True, null=True)
    conductor = models.ForeignKey(MonConductorHistory, models.DO_NOTHING, blank=True, null=True)
    gsm_signal_value = models.IntegerField()
    battery_life = models.IntegerField()
    contactless_reader_status = models.IntegerField()
    sm_module_status = models.IntegerField()
    sim_module_status = models.IntegerField()
    nsi_update_time = models.DateTimeField()
    nsi_version = models.BigIntegerField()
    config_update_time = models.DateTimeField()
    config_version = models.BigIntegerField()
    main_blacklist_update_time = models.DateTimeField()
    main_blacklist_version = models.BigIntegerField()
    social_blacklist_update_time = models.DateTimeField(blank=True, null=True)
    social_blacklist_version = models.BigIntegerField(blank=True, null=True)
    mps_blacklist_update_time = models.DateTimeField(blank=True, null=True)
    mps_blacklist_version = models.BigIntegerField(blank=True, null=True)
    repl_registry_update_time = models.DateTimeField(blank=True, null=True)
    repl_registry_version = models.BigIntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    state_timestamp = models.DateTimeField()
    load_id = models.BigIntegerField()
    create_date = models.DateField()
