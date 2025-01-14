from django.shortcuts import render
from django.http import JsonResponse
import MySQLdb  
# import html as cgi


# Define the view that will return a "Hello World" response
def hello_world(request):
    return JsonResponse({'message': 'Hello, World!'})





def test_mysql_connection(request):
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",  # Or your MySQL host
            user="root",
            passwd="root",
            db="helloworld_db"
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Check the connection and print log
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        print(f"Successfully connected to the database: {db_name[0]}")

        # Close the connection
        cursor.close()
        db.close()

        return JsonResponse({"message": "Successfully connected to MySQL database!"})

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        return JsonResponse({"message": "Failed to connect to MySQL database."}, status=500)
