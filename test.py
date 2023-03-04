from flask import Flask, render_template, request
import csv
import sqlite3

app = Flask(__name__)

# Connect to the database
conn = sqlite3.connect('example.db')

# Define a route for displaying the data
@app.route('/')
def display_data():
    # Retrieve data from the table
    result = conn.execute("SELECT * FROM users")
    data = []
    for row in result:
        data.append(row)
    # Render a template with the data
    return render_template('data.html', data=data)

# Define a route for inserting data from the CSV file
@app.route('/insert', methods=['POST'])
def insert_data():
    # Read data from the CSV file
    file = request.files['file']
    reader = csv.reader(file.stream)
    next(reader)  # Skip the header row
    for row in reader:
        # Insert data into the table
        conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (row[0], row[1]))
    # Commit the changes
    conn.commit()
    # Redirect to the home page
    return redirect('/')

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)

