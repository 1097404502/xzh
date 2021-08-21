import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import text
from pprint import pprint


engine = create_engine(
    "mysql+pymysql://cinder:cinder_dbpass@192.168.41.10/cinder", echo=True
)


def version():
    print(sqlalchemy.__version__)

def open_conn(f):
    def x(*a,**ka):
        with engine.connect() as conn:
            res = f(*a,**ka)
        return res
    return x

def show_sql_str(f):
    def x(*a,**ka):
        with engine.connect() as conn:
            sql_str = f(*a,**ka)
            result = conn.execute(text(sql_str))
        pprint(result.fetchall())
    return x

@show_sql_str
def hellow_world():
    return "select 'hello world'"


# [('backend_storages',),
#  ('backups',),
#  ('ceph_osd_host',),
#  ('cgsnapshots',),
#  ('consistencygroups',),
#  ('driver_initiator_data',),
#  ('encryption',),
#  ('image_volume_cache_entries',),
#  ('iscsi_targets',),
#  ('migrate_version',),
#  ('quality_of_service_specs',),
#  ('quota_classes',),
#  ('quota_usages',),
#  ('quotas',),
#  ('reservations',),
#  ('services',),
#  ('snapshot_metadata',),
#  ('snapshots',),
#  ('transfers',),
#  ('volume_admin_metadata',),
#  ('volume_attachment',),
#  ('volume_glance_metadata',),
#  ('volume_metadata',),
#  ('volume_type_extra_specs',),
#  ('volume_type_projects',),
#  ('volume_types',),
#  ('volumes',)]
@show_sql_str
def get_all_table():
    return "select table_name from information_schema.tables where table_schema='cinder' and table_type='base table';"

# [('created_at',),
#  ('updated_at',),
#  ('deleted_at',),
#  ('deleted',),
#  ('id',),
#  ('host',),
#  ('binary',),
#  ('topic',),
#  ('report_count',),
#  ('disabled',),
#  ('availability_zone',),
#  ('disabled_reason',),
#  ('modified_at',),
#  ('rpc_current_version',),
#  ('rpc_available_version',),
#  ('object_current_version',),
#  ('object_available_version',),
#  ('replication_status',),
#  ('frozen',),
#  ('active_backend_id',)]
@show_sql_str
def get_all_fields():
    return """select column_name from information_schema.columns where table_schema='cinder' and table_name='services'"""

@show_sql_str
def get_all_service():
    return """ select host,disabled,deleted,frozen from services """
    # select column_name from information_schema.columns where table_schema='csdb' and table_name='users'

@show_sql_str
def delete_down_service():
    return """  """

if __name__ == "__main__":
    version()
    # hellow_world()
    get_all_table()
    get_all_fields()
    get_all_service()
