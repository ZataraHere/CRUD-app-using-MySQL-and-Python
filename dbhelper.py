import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="hit-db-demo"
            )
            self.mycursor = self.conn.cursor()
        except:
            print(f"Some error occured. Could not connect to database")
        else:
            print("✅ Connected to the Database")

    def register(self, name, email, password):

        try:

            query = "INSERT INTO users (name, email, password) VALUES (%s,%s,%s)"
            values = (name, email, password)
            self.mycursor.execute(query, values)
            self.conn.commit()

        except:
            return -1
        else:
            return  1
