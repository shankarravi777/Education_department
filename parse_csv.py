
import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('education_department_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS table1')
print("table dropped successfully");
conn.execute('DROP TABLE IF EXISTS table2')
print("table dropped successfully");


# create table again
conn.execute('CREATE TABLE table1 (Departmental_Family Text, Entity Text, Date Integer, Transaction_Number Integer)')
print("table created successfully");
conn.execute('CREATE TABLE table2 (Expense_Type_Lookup Text, Expense_Area_Lookup TEXT, Supplier TEXT, Transaction_Number Integer,Amount FLOAT)')
print("table created successfully");



# open the file to read it into the database
with open('educationdata/dfe_20spend_20_20_20april_202010_20to_2011th_20may_202010 (1).csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:

        Departmental_Family = row[0]
        Entity = row[1]
        Date = row[2]
        Expense_Type_Lookup = row[3]
        Expense_Area_Lookup = row[4]
        Supplier = row[5]
        Transaction_Number = int(row[6])
        Amount  = float(row[7])

        cur.execute('INSERT INTO table1 VALUES (?,?,?,?)', (Departmental_Family, Entity, Date,  Transaction_Number))
        cur.execute('INSERT INTO table2 VALUES (?,?,?,?,?)', ( Expense_Type_Lookup, Expense_Area_Lookup, Supplier, Transaction_Number,Amount))
        conn.commit()
print("data parsed successfully");

conn.close()

