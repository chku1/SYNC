import mysql.connector

# Database connection configuration
config = {
    'user': 'elene',
    'password': 'some_pass',
    'host': '192.168.1.5',
    'port': 3306,
    'database': 'dwh'
}

# Connect to the database
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Fetch procedures from sync_tables
query = """
SELECT procedure_name, ordering
FROM sync_tables
ORDER BY ordering, procedure_name
"""
cursor.execute(query)
procedures = cursor.fetchall()

# Call procedures in order
for procedure in procedures:
    procedure_name = procedure[0]
    print(f"Calling procedure: {procedure_name}")
    cursor.callproc(procedure_name)
    conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("All procedures have been called in the specified order.")
