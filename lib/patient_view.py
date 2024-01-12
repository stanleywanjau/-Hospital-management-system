import click
from models.Doctor import Doctor
from models.Patient import Patient
from models.Appointment import Appointment
import tabulate





patients=Patient()

@click.group()
def patient():
    pass


@click.command()

@click.option('--first_name', prompt="Enter first name", help='first name of the patient')
@click.option('--last_name', prompt="Enter last name", help='last name of the patient')
@click.option('--sex', prompt="Enter sex", help='the patients sex')
@click.option('--birth_date', prompt="Enter birth date", help='patient date of the birth')
@click.option('--phone_number', prompt="Enter phone number", help='patient phone number')
@click.option('--email', prompt="Enter email", help='patients emails address')
@click.option('--addmission_date', prompt="Enter date of admission", help='when was the patient admited')
@click.option('--medication', prompt="Enter medictation", help='medictaion given to the patient')
def add(first_name,last_name,sex,birth_date,phone_number,email,addmission_date,medication):
  patient_data = {
        'first_name': first_name,
        'last_name': last_name,
        'sex': sex,
        'birth_date': birth_date,
        'phone_number': phone_number,
        'email': email,
        'addmission_date': addmission_date,
        'medication': medication
    }
  patients.add_patient_data(**patient_data)
  click.echo('patient added successfully!')
@click.command()
@click.option('--name', required=True,prompt="Name to search",help="Enter the name of the patient")
def search_patient(name):
  patient=patients.get_patient_by_name(name)
  if patient is not None:
        headers = ["ID", "First Name", "Last Name", "Sex", "Birth Date", "Phone Number", "Email", "Admission Date", "Medication"]
        rows = [[patient.id, patient.first_name, patient.last_name, patient.sex, patient.birth_date, patient.phone_number, patient.email, patient.addmission_date, patient.medication]]
        table = tabulate.tabulate(rows, headers, tablefmt="fancy_grid")
        click.echo(f"Found patient:\n{table}")
  else:
        click.echo(f"{name} not found")


@click.command()
@click.option('--name', required=True,prompt="Name of patient to delete", help="Name of patient to delete")
def delete(name):
  patients.delete_patient(name)

@click.command()
@click.option('--name', prompt="Enter patient name", help='Name of the patient to update')
@click.option('--update', help='Update patient information in the format key=value', prompt="Enter data to change")
def update(name, update):
    update_data = {}

    # Split the update parameter into key-value pairs
    for item in update.split(','):
        key, value = item.split('=')
        update_data[key] = value

    # Check if any data is provided for update
    if not update_data:
        click.echo("No data provided for update.")
        return

    # Call the update_patient_by_name method
    patients.update_patient_by_name(name, update_data)

    click.echo('Patient updated successfully!')



patient.add_command(add)
patient.add_command(search_patient)
patient.add_command(delete)
patient.add_command(update)

if __name__ == '__main__':
    patient()