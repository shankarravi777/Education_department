from flask import Flask,render_template
import sqlite3


app=Flask(__name__)

@app.route('/')
def Table():
     conn = sqlite3.connect('education_department_data.db')
     conn.row_factory = sqlite3.Row
     cur = conn.cursor()
     cur.execute("SELECT table1.Transaction_Number, table1.Departmental_Family, table1.Date, table2.Supplier, table2.Amount FROM table1 INNER JOIN table2 ON table1.Transaction_Number = table2.Transaction_Number;")
     rows = cur.fetchall()
     conn.close()
     return render_template('tables.html', rows=rows)

        
