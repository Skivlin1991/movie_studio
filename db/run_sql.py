import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []
  
  # try to connect to the database
    try:
      # Get a connection to the database
        conn = psycopg2.connect("dbname='movie_studio'")
      # Get a cursor from the connection
        cur = conn.cursor(cursor_factory=ext.DictCursor)   
      # Execute the SQL that was passed in 
        cur.execute(sql, values)
      # Commit the execution
        conn.commit()
      # Get the results from the SQL query
        results = cur.fetchall()
      # Close the database cursor
        cur.close()     
  # Catch any errors that might have occured      
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
  # Make sure the connection is closed
    finally:
        if conn is not None:
            conn.close()
  # Return the SQL results
    return results