# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ApplicationsTerminal(models.Model):
    name = models.CharField(unique=True, max_length=30)
    remote_addr = models.CharField(max_length=39, blank=True, null=True)
    type = models.CharField(max_length=3)
    url = models.CharField(max_length=100)
    is_accepted = models.IntegerField()
    date_created = models.DateTimeField()
    comment = models.TextField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applications_terminal'


class AssetPermission(models.Model):
    name = models.CharField(unique=True, max_length=128)
    is_active = models.IntegerField()
    date_expired = models.DateTimeField()
    created_by = models.CharField(max_length=128)
    date_created = models.DateTimeField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'asset_permission'


class AssetPermissionAssetGroups(models.Model):
    assetpermission = models.ForeignKey(AssetPermission, models.DO_NOTHING)
    assetgroup = models.ForeignKey('AssetsAssetgroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'asset_permission_asset_groups'
        unique_together = (('assetpermission', 'assetgroup'),)


class AssetPermissionAssets(models.Model):
    assetpermission = models.ForeignKey(AssetPermission, models.DO_NOTHING)
    asset = models.ForeignKey('AssetsAsset', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'asset_permission_assets'
        unique_together = (('assetpermission', 'asset'),)


class AssetPermissionSystemUsers(models.Model):
    assetpermission = models.ForeignKey(AssetPermission, models.DO_NOTHING)
    systemuser = models.ForeignKey('AssetsSystemuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'asset_permission_system_users'
        unique_together = (('assetpermission', 'systemuser'),)


class AssetPermissionUserGroups(models.Model):
    assetpermission = models.ForeignKey(AssetPermission, models.DO_NOTHING)
    usergroup = models.ForeignKey('UsersUsergroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'asset_permission_user_groups'
        unique_together = (('assetpermission', 'usergroup'),)


class AssetPermissionUsers(models.Model):
    assetpermission = models.ForeignKey(AssetPermission, models.DO_NOTHING)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'asset_permission_users'
        unique_together = (('assetpermission', 'user'),)


class AssetsAdminuser(models.Model):
    name = models.CharField(unique=True, max_length=128)
    username = models.CharField(max_length=16)
    field_password = models.CharField(db_column='_password', max_length=256, blank=True, null=True)  # Field renamed because it started with '_'.
    field_private_key = models.CharField(db_column='_private_key', max_length=4096, blank=True, null=True)  # Field renamed because it started with '_'.
    become = models.IntegerField()
    become_method = models.CharField(max_length=4)
    become_user = models.CharField(max_length=64)
    become_pass = models.CharField(max_length=128)
    field_public_key = models.CharField(db_column='_public_key', max_length=4096)  # Field renamed because it started with '_'.
    comment = models.TextField()
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_adminuser'


class AssetsAsset(models.Model):
    ip = models.CharField(max_length=39)
    hostname = models.CharField(unique=True, max_length=128)
    port = models.IntegerField()
    is_active = models.IntegerField()
    type = models.CharField(max_length=16, blank=True, null=True)
    env = models.CharField(max_length=8, blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True)
    public_ip = models.CharField(max_length=39, blank=True, null=True)
    remote_card_ip = models.CharField(max_length=16, blank=True, null=True)
    cabinet_no = models.CharField(max_length=32, blank=True, null=True)
    cabinet_pos = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=32, blank=True, null=True)
    vendor = models.CharField(max_length=64, blank=True, null=True)
    model = models.CharField(max_length=54, blank=True, null=True)
    sn = models.CharField(max_length=128, blank=True, null=True)
    cpu_model = models.CharField(max_length=64, blank=True, null=True)
    cpu_count = models.IntegerField(blank=True, null=True)
    cpu_cores = models.IntegerField(blank=True, null=True)
    memory = models.CharField(max_length=64, blank=True, null=True)
    disk_total = models.CharField(max_length=1024, blank=True, null=True)
    disk_info = models.CharField(max_length=1024, blank=True, null=True)
    platform = models.CharField(max_length=128, blank=True, null=True)
    os = models.CharField(max_length=128, blank=True, null=True)
    os_version = models.CharField(max_length=16, blank=True, null=True)
    os_arch = models.CharField(max_length=16, blank=True, null=True)
    hostname_raw = models.CharField(max_length=128, blank=True, null=True)
    created_by = models.CharField(max_length=32, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    comment = models.TextField()
    admin_user = models.ForeignKey(AssetsAdminuser, models.DO_NOTHING, blank=True, null=True)
    idc = models.ForeignKey('AssetsIdc', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets_asset'
        unique_together = (('ip', 'port'),)


class AssetsAssetGroups(models.Model):
    asset = models.ForeignKey(AssetsAsset, models.DO_NOTHING)
    assetgroup = models.ForeignKey('AssetsAssetgroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assets_asset_groups'
        unique_together = (('asset', 'assetgroup'),)


class AssetsAssetSystemUsers(models.Model):
    asset = models.ForeignKey(AssetsAsset, models.DO_NOTHING)
    systemuser = models.ForeignKey('AssetsSystemuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assets_asset_system_users'
        unique_together = (('asset', 'systemuser'),)


class AssetsAssetgroup(models.Model):
    name = models.CharField(unique=True, max_length=64)
    created_by = models.CharField(max_length=32)
    date_created = models.DateTimeField(blank=True, null=True)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'assets_assetgroup'


class AssetsAssetgroupSystemUsers(models.Model):
    assetgroup = models.ForeignKey(AssetsAssetgroup, models.DO_NOTHING)
    systemuser = models.ForeignKey('AssetsSystemuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'assets_assetgroup_system_users'
        unique_together = (('assetgroup', 'systemuser'),)


class AssetsIdc(models.Model):
    name = models.CharField(max_length=32)
    bandwidth = models.CharField(max_length=32)
    contact = models.CharField(max_length=128)
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    intranet = models.TextField()
    extranet = models.TextField()
    date_created = models.DateTimeField(blank=True, null=True)
    operator = models.CharField(max_length=32)
    created_by = models.CharField(max_length=32)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'assets_idc'


class AssetsSystemuser(models.Model):
    name = models.CharField(unique=True, max_length=128)
    username = models.CharField(max_length=16)
    field_password = models.CharField(db_column='_password', max_length=256)  # Field renamed because it started with '_'.
    protocol = models.CharField(max_length=16)
    field_private_key = models.CharField(db_column='_private_key', max_length=8192)  # Field renamed because it started with '_'.
    field_public_key = models.CharField(db_column='_public_key', max_length=8192)  # Field renamed because it started with '_'.
    auth_method = models.CharField(max_length=1)
    auto_push = models.IntegerField()
    sudo = models.TextField()
    shell = models.CharField(max_length=64)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=32)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'assets_systemuser'


class AuditsCommandlog(models.Model):
    proxy_log_id = models.IntegerField()
    user = models.CharField(max_length=48)
    asset = models.CharField(max_length=128)
    system_user = models.CharField(max_length=48)
    command_no = models.IntegerField()
    command = models.CharField(max_length=200)
    output = models.TextField()
    timestamp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'audits_commandlog'


class AuditsProxylog(models.Model):
    date_start = models.DateTimeField()
    user = models.CharField(max_length=32)
    asset = models.CharField(max_length=32)
    system_user = models.CharField(max_length=32)
    login_type = models.CharField(max_length=2, blank=True, null=True)
    terminal = models.CharField(max_length=32, blank=True, null=True)
    is_failed = models.IntegerField()
    is_finished = models.IntegerField()
    date_finished = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audits_proxylog'


class AuditsRecordlog(models.Model):
    proxy_log_id = models.IntegerField()
    output = models.TextField()
    timestamp = models.FloatField()

    class Meta:
        managed = False
        db_table = 'audits_recordlog'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CaptchaCaptchastore(models.Model):
    challenge = models.CharField(max_length=32)
    response = models.CharField(max_length=32)
    hashkey = models.CharField(unique=True, max_length=40)
    expiration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captcha_captchastore'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LoginLog(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    login_type = models.CharField(max_length=2)
    login_ip = models.CharField(max_length=39)
    login_city = models.CharField(max_length=254, blank=True, null=True)
    user_agent = models.CharField(max_length=254, blank=True, null=True)
    date_login = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'login_log'


class OpsTask(models.Model):
    uuid = models.CharField(primary_key=True, max_length=128)
    name = models.CharField(max_length=128)
    date_start = models.DateTimeField()
    date_finished = models.DateTimeField(blank=True, null=True)
    timedelta = models.FloatField(blank=True, null=True)
    is_finished = models.IntegerField()
    is_success = models.IntegerField()
    assets = models.TextField(blank=True, null=True)
    field_modules_args = models.TextField(db_column='_modules_args', blank=True, null=True)  # Field renamed because it started with '_'.
    pattern = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ops_task'


class TerminalHeatbeat(models.Model):
    date_created = models.DateTimeField()
    terminal = models.ForeignKey(ApplicationsTerminal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'terminal_heatbeat'


class UsersAccesskey(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    secret = models.CharField(max_length=32)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_accesskey'


class UsersPrivatetoken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'users_privatetoken'


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(unique=True, max_length=30)
    role = models.CharField(max_length=10)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    wechat = models.CharField(max_length=30)
    phone = models.CharField(max_length=20, blank=True, null=True)
    enable_otp = models.IntegerField()
    secret_key_otp = models.CharField(max_length=16)
    field_private_key = models.CharField(db_column='_private_key', max_length=5000)  # Field renamed because it started with '_'.
    field_public_key = models.CharField(db_column='_public_key', max_length=1000)  # Field renamed because it started with '_'.
    comment = models.TextField()
    is_first_login = models.IntegerField()
    date_expired = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    usergroup = models.ForeignKey('UsersUsergroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'usergroup'),)


class UsersUserUserPermissions(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)


class UsersUsergroup(models.Model):
    is_discard = models.IntegerField()
    discard_time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=128)
    comment = models.TextField()
    date_created = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users_usergroup'
