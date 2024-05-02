from flask import Flask, render_template, request, session, redirect, url_for
import webQuery
import json
import sqlite3


app = Flask(__name__)

# Database setup
conn = sqlite3.connect('reservations.db')
cursor = conn.cursor()

from flask_sqlalchemy import SQLAlchemy 
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'  # Set a secret key for session management



# Generate a secure random string of 24 bytes
secret_key = secrets.token_hex(24)

app.secret_key = secret_key

@app.route('/')
def main_menu():
    return render_template('main_menu.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Query the database to check if the provided username and password are valid
        # You'll need to use your preferred method to interact with the SQLite database,
        # such as SQLite3 or Flask-SQLAlchemy.
        # Here's an example using SQLite3:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM admin WHERE username = ? AND password = ?", (username, password))
        admin = cursor.fetchone()

        if admin:
            # If the admin exists in the database, store their id in the session and redirect to the admin dashboard
            session['admin_id'] = admin['id']
            return redirect(url_for('admin_dashboard'))
        else:
            # If the credentials are incorrect, display an error message
            error = "Invalid username or password. Please try again."
            return render_template('admin_login.html', error=error)
    else:
        return render_template('admin_login.html')

@app.route('/result', methods=['GET','POST'])
def reserve_seat():
    if request.method == 'POST':
        # Handle seat reservation
        # Save reservation data to database
        return redirect(url_for('main_menu'))
    else:
        # Display reservation form
        return render_template('reservation_form.html')
    
@app.route('/admin/portal')
def admin_portal():
    # Check if admin is logged in
    # Fetch seating chart and total sales data
    
    return render_template('admin_portal.html')
    

'''def result():
    symbol = request.form['symbol']
    chart_data = webQuery.get_stock_data(symbol)
    if chart_data is None:
        return "No data available for the selected stock symbol."
    dates = chart_data['dates']
    prices = chart_data['prices']
    return render_template('result.html', symbol=symbol, dates=json.dumps(dates), prices=json.dumps(prices))
'''

if __name__ == '__main__':
    app.run(debug=True)

'''
Function to generate cost matrix for flights
Input: none
Output: Returns a 12 x 4 matrix of prices
'''
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix