db = {
    'user': 'root',
    'password': 'root',
    'host': '61.252.113.28',
    'port': 3306,
    'database': 'flector'
}

db_url = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?collation=utf8mb4_unicode_ci"
