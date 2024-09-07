import mysql.connector
from mysql.connector import Error


pswd = input(str("Enter the Password to access the main database: "))
if pswd == "pantheon321":
    print("Successfully granted access to database. \n You can use the following commands : create_connection(), add_drug(id, drug_name,expiry_date, original_quantity, present_quantity, cost), get_all_drugs(), update_drug(id, drug_name =None,expiry_date=None, original_quantity=None, present_quantity=None, cost=None), delete_drug(id) ")
    def create_connection():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',  
                password='sheero766',
                database='root-database'
            )
            if connection.is_connected():
                print("Connection successful")
                return connection
        except Error as e:
            print(f"Error: {e}")
            return None


        def add_drug(id, drug_name,expiry_date, original_quantity, present_quantity, cost):
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                query = "INSERT INTO drugs (id, drug_name,expiry_date, original_quantity, present_quantity, cost) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (id, drug_name,expiry_date, original_quantity, present_quantity, cost)
                cursor.execute(query, values)
                connection.commit()
                print("Drug added successfully")
                cursor.close()
                connection.close()


        def get_all_drugs():
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                query = "SELECT * FROM drugs"
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                cursor.close()
                connection.close()



        def update_drug(id, drug_name =None,expiry_date=None, original_quantity=None, present_quantity=None, cost=None):
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                query = "UPDATE drugs SET "
                updates = []
                values = []
                if drug_name is not None:
                    updates.append("drug_name = %s")
                    values.append(drug_name)
                if original_quantity is not None:
                    updates.append("original_quantity = %s")
                    values.append(original_quantity)
                if present_quantity is not None:
                    updates.append("present_quantity = %s")
                    values.append(present_quantity)
                if expiry_date is not None:
                    updates.append("expiry_date = %s")
                    values.append(expiry_date)
                if cost is not None:
                    updates.append("cost = %s")
                    values.append(cost)
                query += ', '.join(updates)
                query += " WHERE id = %s"
                values.append(id)
                cursor.execute(query, tuple(values))
                connection.commit()
                print("Drug updated successfully")
                cursor.close()
                connection.close()



        def delete_drug(id):
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                query = "DELETE FROM drugs WHERE id = %s"
                cursor.execute(query, (id,))
                connection.commit()
                print("Drug deleted successfully")
                cursor.close()
                connection.close()

else:
    print("Sorry, wrong password, you are not authorized access to this database.")