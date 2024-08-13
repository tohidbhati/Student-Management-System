# Student-Management-System
This is a SMS Project, Created Using Python and MySQL 
Here’s a detailed description for your GitHub repository, including information on how to use the Student Management System (SMS):

---

# Student Management System (SMS)

## Overview

The Student Management System (SMS) is a desktop application built using Python's Tkinter for the graphical user interface and MySQL for the database management. The system allows users to manage student data efficiently, with functionalities including adding, updating, deleting, and viewing student records. Additionally, the application features an "Export to Excel" function to facilitate data analysis and sharing.

## Features

- **Add Student**: Input and save new student records.
- **Update Student**: Modify existing student records.
- **Delete Student**: Remove student records from the database.
- **View Records**: Display student data in a table format.
- **Export to Excel**: Export student data to an Excel spreadsheet for further analysis.

## Installation

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.x
- MySQL Server
- Required Python libraries (`pymysql`, `pandas`, `tkinter`)

### Setting Up the Database

1. **Install MySQL Server**: Follow the installation instructions for MySQL from the [official website](https://dev.mysql.com/downloads/).

2. **Create a Database and Table**:
   - Open MySQL Workbench or any MySQL client.
   - Execute the following SQL commands to create a database and table:

     ```sql
     CREATE DATABASE stm;

     USE stm;

     CREATE TABLE data (
         roll_no VARCHAR(10) PRIMARY KEY,
         name VARCHAR(100),
         class VARCHAR(10),
         section VARCHAR(10),
         contact VARCHAR(15),
         fathers_name VARCHAR(100),
         address TEXT,
         dob DATE,
         gender VARCHAR(10)
     );
     ```

### Installing Required Libraries

Open your terminal or command prompt and run:

```bash
pip install pymysql pandas
```

### Running the Application

1. **Download or Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage

1. **Adding a Student**:
   - Enter the student's details in the form on the left.
   - Click the "Add" button to save the record.

2. **Updating a Student Record**:
   - Select a student record from the table on the right.
   - Modify the details in the form.
   - Click the "Update" button to save changes.

3. **Deleting a Student Record**:
   - Select a student record from the table on the right.
   - Click the "Delete" button to remove the record.

4. **Clearing the Form**:
   - Click the "Clear" button to reset the form fields.

5. **Exporting Data to Excel**:
   - Click the "Export to Excel" button located in the top-right corner to generate an Excel file with all student records.

## Troubleshooting

- **Connection Issues**: Ensure MySQL Server is running and that the credentials in the `connect_db` function are correct.
- **Missing Libraries**: Install any missing libraries using `pip`.

## Contributing

If you'd like to contribute to the project, please fork the repository and submit a pull request with your changes. Ensure that your changes are well-documented and tested.
