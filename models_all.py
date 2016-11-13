# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AqTlvtrmtraceQtabG(models.Model):
    msgid = models.TextField()  # This field type is a guess.
    subscriber_field = models.FloatField(db_column='subscriber#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30)
    address_field = models.FloatField(db_column='address#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sign = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbs_sign = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_tlvtrmtrace_qtab_g'
        unique_together = (('msgid', 'subscriber_field', 'name', 'address_field'),)


class AqTlvtrmtraceQtabH(models.Model):
    msgid = models.TextField()  # This field type is a guess.
    subscriber_field = models.FloatField(db_column='subscriber#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30)
    address_field = models.FloatField(db_column='address#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dequeue_time = models.DateTimeField(blank=True, null=True)
    transaction_id = models.CharField(max_length=30, blank=True, null=True)
    dequeue_user = models.CharField(max_length=30, blank=True, null=True)
    propagated_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    retry_count = models.FloatField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)  # This field type is a guess.
    spare = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_tlvtrmtrace_qtab_h'
        unique_together = (('msgid', 'subscriber_field', 'name', 'address_field'),)


class AqTlvtrmtraceQtabI(models.Model):
    subscriber_field = models.FloatField(db_column='subscriber#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30)
    queue_field = models.FloatField(db_column='queue#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    msg_enq_time = models.DateTimeField()
    msg_step_no = models.FloatField()
    msg_chain_no = models.FloatField()
    msg_local_order_no = models.FloatField()
    msgid = models.TextField()  # This field type is a guess.
    hint = models.TextField(blank=True, null=True)  # This field type is a guess.
    spare = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_tlvtrmtrace_qtab_i'
        unique_together = (('subscriber_field', 'name', 'queue_field', 'msg_enq_time', 'msg_step_no', 'msg_chain_no', 'msg_local_order_no', 'msgid'),)


class AqTlvtrmtraceQtabL(models.Model):
    msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    subscriber_field = models.FloatField(db_column='subscriber#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30, blank=True, null=True)
    address_field = models.FloatField(db_column='address#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dequeue_time = models.DateTimeField(blank=True, null=True)
    transaction_id = models.CharField(max_length=30, blank=True, null=True)
    dequeue_user = models.CharField(max_length=30, blank=True, null=True)
    flags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_tlvtrmtrace_qtab_l'


class AqTlvtrmtraceQtabS(models.Model):
    subscriber_id = models.FloatField(primary_key=True)
    queue_name = models.CharField(max_length=128)
    name = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    protocol = models.FloatField(blank=True, null=True)
    subscriber_type = models.FloatField(blank=True, null=True)
    rule_name = models.CharField(max_length=128, blank=True, null=True)
    trans_name = models.CharField(max_length=261, blank=True, null=True)
    ruleset_name = models.CharField(max_length=261, blank=True, null=True)
    negative_ruleset_name = models.CharField(max_length=261, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    deletion_time = models.DateTimeField(blank=True, null=True)
    scn_at_remove = models.FloatField(blank=True, null=True)
    scn_at_add = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aq$_tlvtrmtrace_qtab_s'


class AqTlvtrmtraceQtabT(models.Model):
    next_date = models.DateTimeField()
    txn_id = models.CharField(max_length=30)
    msgid = models.TextField()  # This field type is a guess.
    action = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aq$_tlvtrmtrace_qtab_t'
        unique_together = (('next_date', 'txn_id', 'msgid'),)


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=510, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=256, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=300, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=508, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DicTlvTags(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tlv_tag = models.CharField(max_length=20, blank=True, null=True)
    format = models.CharField(max_length=30, blank=True, null=True)
    project = models.CharField(max_length=30, blank=True, null=True)
    xml_tag = models.CharField(max_length=40, blank=True, null=True)
    root_id = models.BigIntegerField(blank=True, null=True)
    order_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dic_tlv_tags'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=400, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=510, blank=True, null=True)
    name = models.CharField(max_length=510, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=80)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MonAdditionalParameters(models.Model):
    name = models.CharField(max_length=127)
    value = models.CharField(max_length=4000)
    event_timestamp = models.DateTimeField()
    load_id = models.BigIntegerField()
    create_date = models.DateField()
    smid = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'mon_additional_parameters'


class MonCardOperations(models.Model):
    smid = models.CharField(max_length=7)
    card_uid = models.CharField(max_length=14)
    sak = models.CharField(max_length=2)
    card_type = models.CharField(max_length=2)
    status = models.CharField(max_length=4)
    pan = models.CharField(max_length=19, blank=True, null=True)
    category = models.CharField(max_length=12, blank=True, null=True)
    ms_elapsed = models.BigIntegerField(blank=True, null=True)
    event_timestamp = models.DateTimeField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    load_id = models.BigIntegerField()
    create_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mon_card_operations'


class MonConductorHistory(models.Model):
    conductor_id = models.BigIntegerField(primary_key=True)
    conductor_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'mon_conductor_history'


class MonEquipmentFailure(models.Model):
    smid = models.CharField(max_length=7)
    device_code = models.IntegerField()
    error_code = models.CharField(max_length=4)
    ext_info = models.CharField(max_length=256, blank=True, null=True)
    event_timestamp = models.DateTimeField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    load_id = models.BigIntegerField()
    create_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mon_equipment_failure'


class MonProcessingSessions(models.Model):
    smid = models.CharField(max_length=7)
    service_code = models.IntegerField()
    operation_code = models.IntegerField()
    operation_status = models.BigIntegerField(blank=True, null=True)
    ext_info = models.CharField(max_length=255, blank=True, null=True)
    event_timestamp = models.DateTimeField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    load_id = models.BigIntegerField()
    create_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mon_processing_sessions'


class MonTerminalInfo(models.Model):
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

    class Meta:
        managed = False
        db_table = 'mon_terminal_states'


class MonTerminalTracking(models.Model):
    smid = models.CharField(max_length=7, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location_timestamp = models.DateTimeField()
    load_id = models.BigIntegerField()
    create_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mon_terminal_tracking'


class MonUserActions(models.Model):
    smid = models.CharField(max_length=7)
    action_code = models.IntegerField()
    ext_info = models.CharField(max_length=255, blank=True, null=True)
    event_timestamp = models.DateTimeField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    load_id = models.BigIntegerField()
    create_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mon_user_actions'


class StgProcessErrors(models.Model):
    load_id = models.BigIntegerField()
    category = models.CharField(max_length=40)
    subcategory = models.CharField(max_length=40)
    num = models.BigIntegerField()
    data = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stg_process_errors'
        unique_together = (('load_id', 'category', 'subcategory', 'num'),)


class StgTerminalCorruptLog(models.Model):
    smid = models.CharField(max_length=7)
    data = models.TextField(blank=True, null=True)
    error_code = models.BigIntegerField(blank=True, null=True)
    create_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'stg_terminal_corrupt_log'


class StgTerminalEventLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    smid = models.CharField(max_length=7)
    create_date = models.DateField()
    data = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    error_code = models.BigIntegerField(blank=True, null=True)
    queue_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stg_terminal_event_log'
# Unable to inspect table 'sys_iot_over_92270'
# The error was: ORA-25191: cannot reference overflow table of an index-organized table



class TlvtrmtraceQtab(models.Model):
    q_name = models.CharField(max_length=30, blank=True, null=True)
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)
    delay = models.DateTimeField(blank=True, null=True)
    expiration = models.FloatField(blank=True, null=True)
    time_manager_info = models.DateTimeField(blank=True, null=True)
    local_order_no = models.FloatField(blank=True, null=True)
    chain_no = models.FloatField(blank=True, null=True)
    cscn = models.FloatField(blank=True, null=True)
    dscn = models.FloatField(blank=True, null=True)
    enq_time = models.DateTimeField(blank=True, null=True)
    enq_uid = models.CharField(max_length=30, blank=True, null=True)
    enq_tid = models.CharField(max_length=30, blank=True, null=True)
    deq_time = models.DateTimeField(blank=True, null=True)
    deq_uid = models.CharField(max_length=30, blank=True, null=True)
    deq_tid = models.CharField(max_length=30, blank=True, null=True)
    retry_count = models.FloatField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    step_no = models.FloatField(blank=True, null=True)
    recipient_key = models.FloatField(blank=True, null=True)
    dequeue_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sender_name = models.CharField(max_length=30, blank=True, null=True)
    sender_address = models.CharField(max_length=1024, blank=True, null=True)
    sender_protocol = models.FloatField(blank=True, null=True)
    user_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_prop = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tlvtrmtrace_qtab'
