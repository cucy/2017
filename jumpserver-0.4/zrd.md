资产
    ｉｄ
    资产管理员
    资产系统用户
    资产（中间表）－－》资产组
    
## 创建测试主机   
```python
import json 
from assets.models import Asset
for i in range(30,51):
    a = {'admin_user_id': 1,
'cabinet_no': None,
'cabinet_pos': None,
'comment': '10.10.1.%s',
'cpu_cores': 2,
'cpu_count': 2,
'cpu_model': 'Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz',
'created_by': 'admin',
'disk_info': '{"sda": "120.00 GB"}',
'disk_total': '120.0 G',
'env': 'Test',
'hostname': '%s虚拟机',
'hostname_raw': 'web-office-stg-%s',
'idc_id': 1,
'ip': '10.10.1.%s',
'is_active': True,
'memory': '3.791 G',
'model': 'None',
'number': None,
'os': 'CentOS',
'os_arch': 'x86_64',
'os_version': '7.2.1511',
'platform': 'Linux',
'port': 22,
'public_ip': '10.10.1.%s',
'remote_card_ip': None,
'sn': 'VMware-42 36 3d dd c1 77 71 56-56 30 8c 33 c9 26%s',
'status': 'In use',
'type': 'VM',
'vendor': 'VMware, Inc.'}
    a = json.dumps(a)
    b = a % (i, i, i, i, i,i)
    c = json.loads(b)
    s = Asset(**c)
    s.save()
```

```mysql
BEGIN;
--
-- Create model Project
--
CREATE TABLE `sh_project` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(32) NOT NULL, `path` varchar(200) NOT NULL, `c_time` datetime(6) NOT NULL, `p_project_id` integer NULL);
--


-- Create model ProjectAssert
--
CREATE TABLE `sh_project_asset` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
CREATE TABLE `sh_project_asset_asset` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `projectassert_id` integer NOT NULL, `asset_id` integer NOT NULL);
CREATE TABLE `sh_project_asset_project` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `projectassert_id` integer NOT NULL, `project_id` integer NOT NULL);
ALTER TABLE `sh_project` ADD CONSTRAINT `sh_project_p_project_id_673a5b9f_fk_sh_project_id` FOREIGN KEY (`p_project_id`) REFERENCES `sh_project` (`id`);
ALTER TABLE `sh_project_asset_asset` ADD CONSTRAINT `sh_project_asset_ass_projectassert_id_259b5b01_fk_sh_projec` FOREIGN KEY (`projectassert_id`) REFERENCES `sh_project_asset` (`id`);
ALTER TABLE `sh_project_asset_asset` ADD CONSTRAINT `sh_project_asset_asset_asset_id_2b0255e8_fk_assets_asset_id` FOREIGN KEY (`asset_id`) REFERENCES `assets_asset` (`id`);
ALTER TABLE `sh_project_asset_asset` ADD CONSTRAINT `sh_project_asset_asset_projectassert_id_asset_id_0a4b7e47_uniq` UNIQUE (`projectassert_id`, `asset_id`);
ALTER TABLE `sh_project_asset_project` ADD CONSTRAINT `sh_project_asset_pro_projectassert_id_e7611d62_fk_sh_projec` FOREIGN KEY (`projectassert_id`) REFERENCES `sh_project_asset` (`id`);
ALTER TABLE `sh_project_asset_project` ADD CONSTRAINT `sh_project_asset_project_project_id_6a842632_fk_sh_project_id` FOREIGN KEY (`project_id`) REFERENCES `sh_project` (`id`);
ALTER TABLE `sh_project_asset_project` ADD CONSTRAINT `sh_project_asset_project_projectassert_id_project_b1aedeb6_uniq` UNIQUE (`projectassert_id`, `project_id`);
COMMIT;

```