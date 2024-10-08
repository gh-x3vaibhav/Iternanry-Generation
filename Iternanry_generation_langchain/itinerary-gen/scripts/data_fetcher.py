import pymysql
import pandas as pd

# Establish connection to AWS RDS MySQL
connection = pymysql.connect(
    host='travalingdatabase.cfu8y0yscmkf.eu-north-1.rds.amazonaws.com',
    user='admin',
    password='vaibhavsonawnae',
    db='travalingdatabase'
)

def fetch_user_data(user_id):
    query = f"SELECT * FROM users WHERE user_id = {user_id}"
    df = pd.read_sql(query, connection)
    return df
