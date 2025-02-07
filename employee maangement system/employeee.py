 
import tkinter as tk 
import mysql.connector 
 
# Establish connection to the database 
connection = mysql.connector.connect(host='localhost', user='root', 
password='', database='loyee') 
 
def submit_details(data_type, details): 
    try: 
        cursor = connection.cursor() 
        # Insert data into the corresponding table based on data_type 
        if data_type == "Employee": 
            query = "INSERT INTO employee (Employee_ID, First_Name, 
Last_Name, Contact, Email, Address) VALUES (%s, %s, %s, %s, %s, 
%s)" 
            data = (details["Employee ID"], details["First Name"], 
details["Last Name"], details["Contact"], details["Email"], 
details["Address"]) 
        elif data_type == "Department": 
            query = "INSERT INTO department (Department_ID, 
Department_Name) VALUES (%s, %s)" 
            data = (details["Department ID"], details["Department Name"]) 
        elif data_type == "Attendance": 
            query = "INSERT INTO attendance (Attendance_ID, 
Employee_ID, Attendance_Date, Attendance_Time) VALUES (%s, %s, 
 
%s, %s)" 
            data = (details["Attendance ID"], details["Employee ID"], 
details["Attendance Date"], details["Attendance Time"]) 
        elif data_type == "Leave": 
            query = "INSERT INTO leave_table (Leave_ID, Employee_ID, 
Leave_Type, Start_Date, End_Date) VALUES (%s, %s, %s, %s, %s)" 
            data = (details["Leave ID"], details["Employee ID"], 
details["Leave Type"], details["Start Date"], details["End Date"]) 
        elif data_type == "Salary": 
            query = "INSERT INTO salary (Salary_ID, Employee_ID, Salary, 
Effective_Date) VALUES (%s, %s, %s, %s)" 
            data = (details["Salary ID"], details["Employee ID"], 
details["Salary"], details["Effective Date"]) 
        elif data_type == "Skills": 
            query = "INSERT INTO skills (Skill_ID, Employee_ID, 
Skill_Level, Skill_Name) VALUES (%s, %s, %s, %s)" 
            data = (details["Skill ID"], details["Employee ID"], details["Skill 
Level"], details["Skill Name"]) 
 
        cursor.execute(query, data) 
        connection.commit() 
        cursor.close() 
        show_data(data_type) 
    except mysql.connector.Error as error: 
        print("Error:", error) 
 
def show_data(data_type): 
    data_window = tk.Toplevel(root) 
    data_window.title(f"Submitted {data_type} Data") 
 
    data_label = tk.Label(data_window, text=f"Submitted {data_type} 
Data", font=("Arial", 16, "bold")) 
    data_label.pack() 
 
    try: 
        cursor = connection.cursor() 
 
        # Fetch data from the database based on data_type 
        if data_type == "Employee": 
            query = "SELECT * FROM employee" 
 
        elif data_type == "Department": 
            query = "SELECT * FROM department" 
        elif data_type == "Attendance": 
            query = "SELECT * FROM attendance" 
        elif data_type == "Leave": 
            query = "SELECT * FROM leave_table" 
        elif data_type == "Salary": 
            query = "SELECT * FROM salary" 
        elif data_type == "Skills": 
            query = "SELECT * FROM skills" 
 
        cursor.execute(query) 
        data = cursor.fetchall() 
 
        # Display fetched data 
        for row in data: 
            data_str = ", ".join(str(item) for item in row) 
            data_label = tk.Label(data_window, text=data_str, font=("Arial", 
12)) 
            data_label.pack() 
 
        cursor.close() 
 
    except mysql.connector.Error as error: 
        print("Error:", error) 
 
# Function to create input fields for form details 
def create_form(data_type, fields): 
    form = tk.Toplevel(root) 
    form.title(f"{data_type} Details") 
 
    # Create labels and entry fields for form details 
    entries = {} 
    for i, (field_name, field_label) in enumerate(fields.items()): 
        label = tk.Label(form, text=field_label, font=("Arial", 14)) 
        label.grid(row=i, column=0, sticky="e", padx=10, pady=5) 
        entry = tk.Entry(form, font=("Arial", 14), width=30) 
        entry.grid(row=i, column=1, padx=10, pady=5) 
        entries[field_name] = entry 
 
 
    # Button to submit form details 
    submit_button = tk.Button(form, text="Submit", font=("Arial", 14), 
command=lambda: submit_details(data_type, {field: entry.get() for field, 
entry in entries.items()})) 
    submit_button.grid(row=len(fields), columnspan=2, pady=10) 
 
# Function to verify login credentials 
def verify_login(): 
    username = username_entry.get() 
    password = password_entry.get() 
    if username == "krishna" and password == "909": 
        login_window.destroy() 
        root.deiconify() 
    else: 
        login_error_label.config(text="Invalid username or password") 
 
# Create the login window 
login_window = tk.Tk() 
login_window.title("Login") 
login_window.geometry("300x150") 
 
username_label = tk.Label(login_window, text="Username:", 
font=("Arial", 14)) 
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e") 
username_entry = tk.Entry(login_window, font=("Arial", 14), width=20) 
username_entry.grid(row=0, column=1, padx=10, pady=5) 
 
password_label = tk.Label(login_window, text="Password:", 
font=("Arial", 14)) 
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e") 
password_entry = tk.Entry(login_window, font=("Arial", 14), width=20, 
show="*") 
password_entry.grid(row=1, column=1, padx=10, pady=5) 
 
login_button = tk.Button(login_window, text="Login", font=("Arial", 14), 
command=verify_login) 
login_button.grid(row=2, columnspan=2, pady=10) 
 
login_error_label = tk.Label(login_window, text="", fg="red") 
login_error_label.grid(row=3, columnspan=2) 
# Create the main window 
root = tk.Tk() 
root.title("Employee Management System") 
root.geometry("600x500") 
root.withdraw()  # Hide the main window initially 
# Create a main menu with buttons for each feature 
menu_items = [ 
("Employee", {"Employee ID": "Employee ID:", "First Name": "First 
Name:", "Last Name": "Last Name:", "Contact": "Contact:", "Email": 
"Email:", "Address": "Address:"}), 
("Department", {"Department ID": "Department ID:", "Department 
Name": "Department Name:"}), 
("Attendance", {"Attendance ID": "Attendance ID:", "Employee ID": 
"Employee ID:", "Attendance Date": "Attendance Date:", "Attendance 
Time": "Attendance Time:"}), 
("Leave", {"Leave ID": "Leave ID:", "Employee ID": "Employee ID:", 
"Leave Type": "Leave Type:", "Start Date": "Start Date:", "End Date": 
"End Date:"}), 
("Salary",  {"Salary ID": "Salary ID:", "Employee ID": "Employee ID:", 
"Salary": "Salary:", "Effective Date": "Effective Date:"}), 
("Skills", {"Skill ID": "Skill ID:", "Employee ID": "Employee ID:", 
"Skill Level": "Skill Level:", "Skill Name": "Skill Name:"}) 
] 
for menu_item in menu_items: 
button_text, fields = menu_item 
button = tk.Button(root, text=f"{button_text} Details", font=("Arial", 
16, "bold"), command=lambda data_type=button_text, form_fields=fields: 
create_form(data_type, form_fields)) 
button.pack(pady=10) 
root.mainloop()