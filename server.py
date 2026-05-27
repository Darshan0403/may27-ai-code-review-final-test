import sqlite3
from flask import Flask, request

app = Flask(__name__)
SECRET_KEY = "super_secret_admin_password_123" 

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE id = {user_id}" 
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return {"data": result}
    except Exception as e:
        return {"error": str(e)} 

if __name__ == "__main__":
    app.run(debug=True)
