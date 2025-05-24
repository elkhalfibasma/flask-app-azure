from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Connexion à la base Azure SQL
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=tcp:your-server.database.windows.net,1433;"
    "Database=MyDB;"
    "Uid=azureuser;"
    "Pwd=Password123!;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

@app.route('/')
def index():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM SampleTable")  # Remplace par ta table
        names = [row[0] for row in cursor.fetchall()]
        return render_template('index.html', names=names)
    except Exception as e:
        return f"Erreur : {e}"

if __name__ == '__main__':
    app.run()
