import MySQLdb as MySQL

config = {}

####
# config database
####
config['MYSQL_HOST'] = '127.0.0.1'
config['MYSQL_USER'] = 'username'
config['MYSQL_PASSWORD'] = 'password'
config['MYSQL_DB'] = 'db_name'

#### 
# Membuat Koneksi Kedatabase
####
def create_conn():
    return MySQL.connect(host=config['MYSQL_HOST'], 
                user=config['MYSQL_USER'], 
                passwd=config['MYSQL_PASSWORD'], 
                db=config['MYSQL_DB'])
