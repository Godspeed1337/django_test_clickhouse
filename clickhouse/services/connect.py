import clickhouse_connect
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT = clickhouse_connect.get_client(host=os.environ.get('CLICKHOUSE_HOST', 'localhost'),
                                       username=os.environ.get('CLICKHOUSE_USER', 'username'),
                                       password=os.environ.get('CLICKHOUSE_PASSWORD', 'pass'),
                                       database=os.environ.get('CLICKHOUSE_NAME', 'db_name'))