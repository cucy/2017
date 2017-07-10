```python
sh make_migrations.sh 
Migrations for 'assets':
  /opt/jumpserver/apps/assets/migrations/0001_initial.py:
    - Create model AdminUser
    - Create model Asset
    - Create model AssetGroup
    - Create model IDC
    - Create model SystemUser
    - Add field system_users to assetgroup
    - Add field groups to asset
    - Add field idc to asset
    - Add field system_users to asset
    - Alter unique_together for asset (1 constraint(s))
Migrations for 'ops':
  /opt/jumpserver/apps/ops/migrations/0001_initial.py:
    - Create model Task
Migrations for 'perms':
  /opt/jumpserver/apps/perms/migrations/0001_initial.py:
    - Create model AssetPermission
  /opt/jumpserver/apps/perms/migrations/0002_auto_20170510_1637.py:
    - Add field user_groups to assetpermission
    - Add field users to assetpermission
Migrations for 'applications':
  /opt/jumpserver/apps/applications/migrations/0001_initial.py:
    - Create model Terminal
    - Create model TerminalHeatbeat
  /opt/jumpserver/apps/applications/migrations/0002_terminal_user.py:
    - Add field user to terminal
Migrations for 'audits':
  /opt/jumpserver/apps/audits/migrations/0001_initial.py:
    - Create model CommandLog
    - Create model LoginLog
    - Create model ProxyLog
    - Create model RecordLog
Migrations for 'users':
  /opt/jumpserver/apps/users/migrations/0001_initial.py:
    - Create model User
    - Create model AccessKey
    - Create model PrivateToken
    - Create model UserGroup
    - Add field groups to user
    - Add field user_permissions to user
Operations to perform:
  Apply all migrations: applications, assets, audits, auth, captcha, contenttypes, ops, perms, sessions, users
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying users.0001_initial... OK
  Applying applications.0001_initial... OK
  Applying applications.0002_terminal_user... OK
  Applying assets.0001_initial... OK
  Applying audits.0001_initial... OK
  Applying captcha.0001_initial... OK
  Applying ops.0001_initial... OK
  Applying perms.0001_initial... OK
  Applying perms.0002_auto_20170510_1637... OK
  Applying sessions.0001_initial... OK
```

