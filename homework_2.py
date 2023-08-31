import sqlite3

with sqlite3.connect('hospital.db') as db:
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Workers (
            ID INTEGER PRIMARY KEY,
            Name VARCHAR(255),
            Surname VARCHAR(255),
            Position VARCHAR(255),
            Phone_Number VARCHAR(255),
            Rate INT
        )
    ''')

    cursor.execute('''
        INSERT INTO Workers (Name, Surname, Position, Phone_Number, Rate)
        VALUES (?, ?, ?, ?, ?)
    ''', ('Andrew', 'Ivanov', 'Manager', '+380123456789', 15000))

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patients (
            ID INTEGER PRIMARY KEY,
            Name VARCHAR(255),
            Surname VARCHAR(255),
            Birth_Date DATE,
            Address TEXT,
            Contacts TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO Patients (Name, Surname, Birth_Date, Address, Contacts)
        VALUES (?, ?, ?, ?, ?)
    ''', ('Harry', 'Tate', '1985-08-25', 'Shevchenko St, 20', '+380987652511'))

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Visits (
            ID INTEGER PRIMARY KEY,
            Patient_ID INTEGER REFERENCES Patients(ID),
            Doctor_ID INTEGER REFERENCES Workers(ID),
            Visit_Date DATE,
            Diagnosis TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO Visits (Patient_ID, Doctor_ID, Visit_Date, Diagnosis)
        VALUES (?, ?, ?, ?)
    ''', (1, 1, '2023-08-31', 'Flu'))

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Appointments (
            ID INTEGER PRIMARY KEY,
            Patient_ID INTEGER REFERENCES Patients(ID),
            Doctor_ID INTEGER REFERENCES Workers(ID),
            Appointment_Date DATE,
            Prescription TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO Appointments (Patient_ID, Doctor_ID, Appointment_Date, Prescription)
        VALUES (?, ?, ?, ?)
    ''', (1, 1, '2023-09-05', 'General checkup'))

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Prescriptions (
            ID INTEGER PRIMARY KEY,
            Patient_ID INTEGER REFERENCES Patients(ID),
            Doctor_ID INTEGER REFERENCES Workers(ID),
            Prescription_Date DATE,
            Medications TEXT,
            Dosage TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO Prescriptions (Patient_ID, Doctor_ID, Prescription_Date, Medications, Dosage)
        VALUES (?, ?, ?, ?, ?)
    ''', (1, 1, '2023-08-31', 'Aspirin', '1 tablet twice a day'))

