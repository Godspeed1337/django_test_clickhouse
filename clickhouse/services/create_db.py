from connect import CLIENT
CLIENT.command('CREATE TABLE IF NOT EXISTS test_table (key UInt32, value String, metric Float64) ENGINE MergeTree ORDER BY key PRIMARY KEY key')


