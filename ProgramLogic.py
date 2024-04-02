import psycopg2

# Database connection
conct = psycopg2.connect(host="", user="", password ="", port=, dbname="")
cursr = conct.cursor()

# Function that does operations
def sampleFunction():
    """
    Peforms Operation
    """
    cursr.execute("""""")
    for row in cursr.fetchall():
        print(row)

conct.commit()
cursr.close()
conct.close()