import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import pandas as pd  # Import pandas for Excel export functionality
import bcrypt  # For password hashing

# Function to connect to the database securely
def connect_db():
    return pymysql.connect(host="localhost", user="root", password="", database="stm", charset='utf8mb4')

# Function to export data as an Excel sheet
def export_data():
    try:
        conn = connect_db()
        query = "SELECT * FROM data"
        df = pd.read_sql(query, conn)
        # Exporting data to Excel
        df.to_excel("student_data.xlsx", index=False)
        messagebox.showinfo("Exported", "Data has been exported successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error exporting data: {str(e)}")
    finally:
        conn.close()

# Function to create the main window
def main_window():
    win = tk.Tk()
    win.geometry("1360x1090+0+0")
    win.title("Student Management System")

    # Title Label
    title_label = tk.Label(win, text="Student Management System", font=("Arial", 30, "bold"), border=12, relief=tk.GROOVE, bg="lightgrey")
    title_label.pack(side=tk.TOP, fill=tk.X)

    # Export Button in the top-right corner
    export_btn = tk.Button(win, text="Export to Excel", font=("Arial", 12, "bold"), bg="lightgrey", command=export_data)
    export_btn.place(x=1210, y=20)  # Adjust the position as needed

    detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial", 20), bd=12, bg="lightgrey")
    detail_frame.place(x=20, y=90, width=420, height=570)

    data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
    data_frame.place(x=470, y=90, width=810, height=575)

    # ===========ENTRY==========#

    Rollno_lbl = tk.Label(detail_frame, text="Roll No", font=('Arial', 15), bg="lightgrey")
    Rollno_lbl.grid(row=0, column=0, padx=2, pady=2)

    Rollno_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
    Rollno_ent.grid(row=0, column=1, padx=2, pady=2)

    name_lbl = tk.Label(detail_frame, text="Name", font=('Arial', 15), bg="lightgrey")
    name_lbl.grid(row=1, column=0, padx=2, pady=2)

    name_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
    name_ent.grid(row=1, column=1, padx=2, pady=2)

    class_lbl = tk.Label(detail_frame, text="Class", font=('Arial', 15), bg="lightgrey")
    class_lbl.grid(row=2, column=0, padx=2, pady=2)

    class_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
    class_ent.grid(row=2, column=1, padx=2, pady=2)

    section_lbl = tk.Label(detail_frame, text="Section", font=('Arial', 15), bg="lightgrey")
    section_lbl.grid(row=3, column=0, padx=2, pady=2)

    section_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
    section_ent.grid(row=3, column=1, padx=2, pady=2)

    contact_lbl = tk.Label(detail_frame, text="Contact", font=('Arial', 15), bg="lightgrey")
    contact_lbl.grid(row=4, column=0, padx=2, pady=2)

    contact_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
    contact_ent.grid(row=4, column=1, padx=2, pady=2)

    fathersnm_lbl = tk.Label(detail_frame, text="Father's Name", font=('Arial', 15), bg="lightgrey")
    fathersnm_lbl.grid(row=5, column=0, padx=2, pady=2)

    fathersnm_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
    fathersnm_ent.grid(row=5, column=1, padx=2, pady=2)

    address_lbl = tk.Label(detail_frame, text="Address", font=('Arial', 15), bg="lightgrey")
    address_lbl.grid(row=6, column=0, padx=2, pady=2)

    address_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
    address_ent.grid(row=6, column=1, padx=2, pady=2)

    gender_lbl = tk.Label(detail_frame, text="Gender", font=('Arial', 15), bg="lightgrey")
    gender_lbl.grid(row=7, column=0, padx=2, pady=2)

    gender_ent = ttk.Combobox(detail_frame, font=("Arial", 15), state="readonly")
    gender_ent['values'] = ("Male", "Female", "Others")
    gender_ent.grid(row=7, column=1, padx=2, pady=2)

    dob_lbl = tk.Label(detail_frame, text="D.O.B", font=('Arial', 15), bg="lightgrey")
    dob_lbl.grid(row=8, column=0, padx=2, pady=2)

    dob_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
    dob_ent.grid(row=8, column=1, padx=2, pady=2)

    # ============BUTTON-FRAME========================

    btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
    btn_frame.place(x=28, y=390, width=340, height=115)

    add_btn = tk.Button(btn_frame, bg="lightgrey", text="Add", bd=7, font=("arial", 13), width=15, command=lambda: add_data())
    add_btn.grid(row=0, column=0, padx=2, pady=2)

    update_btn = tk.Button(btn_frame, bg="lightgrey", text="Update", bd=7, font=("arial", 13), width=15, command=lambda: update_data())
    update_btn.grid(row=0, column=1, padx=3, pady=2)

    delete_btn = tk.Button(btn_frame, bg="lightgrey", text="Delete", bd=7, font=("arial", 13), width=15, command=lambda: delete_data())
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    clear_btn = tk.Button(btn_frame, bg="lightgrey", text="Clear", bd=7, font=("arial", 13), width=15, command=lambda: clear_data())
    clear_btn.grid(row=1, column=1, padx=2, pady=2)

    # =======================Treeview and Scrollbars=========================#

    main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

    student_table = ttk.Treeview(main_frame, columns=("Roll No", "Name", "Class", "Section", "Contact", "Father's Name", "Address", "D.O.B", "Gender"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=student_table.yview)
    x_scroll.config(command=student_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    student_table.heading("Roll No", text="Roll No")
    student_table.heading("Name", text="Name")
    student_table.heading("Class", text="Class")
    student_table.heading("Section", text="Section")
    student_table.heading("Contact", text="Contact")
    student_table.heading("Father's Name", text="Father's Name")
    student_table.heading("Address", text="Address")
    student_table.heading("D.O.B", text="D.O.B")
    student_table.heading("Gender", text="Gender")

    student_table['show'] = 'headings'

    student_table.column("Roll No", width=100)
    student_table.column("Name", width=100)
    student_table.column("Class", width=100)
    student_table.column("Section", width=100)
    student_table.column("Contact", width=100)
    student_table.column("Father's Name", width=100)
    student_table.column("Address", width=150)
    student_table.column("D.O.B", width=100)
    student_table.column("Gender", width=100)

    student_table.pack(fill=tk.BOTH, expand=True)

    # =======================Functions=========================#

    def fetch_data():
        conn = connect_db()
        curr = conn.cursor()
        curr.execute("SELECT * FROM data")
        rows = curr.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', 'end', values=row)
            conn.commit()
        conn.close()

    def add_data():
        conn = connect_db()
        curr = conn.cursor()
        curr.execute("INSERT INTO data (roll_no, name, class, section, contact, fathers_name, address, dob, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                     (Rollno_ent.get(), name_ent.get(), class_ent.get(), section_ent.get(), contact_ent.get(), fathersnm_ent.get(), address_ent.get(), dob_ent.get(), gender_ent.get()))
        conn.commit()
        fetch_data()
        clear_data()
        conn.close()

    def update_data():
        conn = connect_db()
        curr = conn.cursor()
        curr.execute("UPDATE data SET name=%s, class=%s, section=%s, contact=%s, fathers_name=%s, address=%s, dob=%s, gender=%s WHERE roll_no=%s",
                     (name_ent.get(), class_ent.get(), section_ent.get(), contact_ent.get(), fathersnm_ent.get(), address_ent.get(), dob_ent.get(), gender_ent.get(), Rollno_ent.get()))
        conn.commit()
        fetch_data()
        clear_data()
        conn.close()

    def delete_data():
        conn = connect_db()
        curr = conn.cursor()
        curr.execute("DELETE FROM data WHERE roll_no=%s", Rollno_ent.get())
        conn.commit()
        fetch_data()
        clear_data()
        conn.close()

    def clear_data():
        Rollno_ent.delete(0, tk.END)
        name_ent.delete(0, tk.END)
        class_ent.delete(0, tk.END)
        section_ent.delete(0, tk.END)
        contact_ent.delete(0, tk.END)
        fathersnm_ent.delete(0, tk.END)
        address_ent.delete(0, tk.END)
        dob_ent.delete(0, tk.END)
        gender_ent.set('')

    fetch_data()

    win.mainloop()

if __name__ == "__main__":
    main_window()
