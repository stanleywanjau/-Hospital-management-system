# Hospital-management-system

This project is a Hospital Management System implemented in Python using SQLAlchemy for database management.

## Features

- Manage doctors, patients, and appointments.
- Add, view, update, and delete doctors, patients, and appointments.
- View appointments for a specific doctor.
- Search for doctors and patients.
  
## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3
- SQLite database (Hospital.db) created
- cd to lib and run:
  
```bash
  python seed.py
  ```

  this will add some data in the database

- Required Python packages installed .

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:stanleywanjau/-Hospital-management-system.git
    ```

2. Install dependencies:

    ```bash
    pipenv install
    ```

## Usage

### Doctor Commands

- **Add Doctor:**

    ```bash
    python doctor_view.py add
    ```

- **List Doctors:**

    ```bash
    python doctor_view.py list
    ```

- **Search Doctor:**

    ```bash
    python doctor_view.py search-doctor
    ```

- **Get Appointments for Doctor:**

    ```bash
    python doctor_view.py get-appointment-for-doc
    ```

- **Delete Doctor:**

    ```bash
    python python doctor_view.py delete
    ```

### Patient Commands

- **Add Patient:**

    ```bash
    python patient_view.py add
    ```

- **Search Patient:**

    ```bash
    python patient_view.py search-patient
    ```

- **Delete Patient:**

    ```bash
    python patient_view.py delete
    ```

- **Update Patient:**

    ```bash
    python patient_view.py update
    ```

### Appointment Commands

- **List Appointments:**

    ```bash
    python appointment-view.py list-appointments
    ```

- **Add Appointment:**

    ```bash
    python appointment-view.py add
    ```

- **Delete Appointment:**

    ```bash
    python appointment-view.py delete
    ```

## Support and Contact Details

Incase of any query, need for collaboration or issues with this code, feel free to reach me at
<stanley.muiruri@student.moringaschool.com>

## License

MIT License

Copyright &copy; 2023 Stanley Wanjau

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
