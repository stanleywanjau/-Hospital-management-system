# views/doctor_view.py
import click
from models.Doctor import Doctor
from models.Patient import Patient
from models.Appointment import Appointment
import tabulate

doctor_cls = Doctor()

@click.group()
def doctor():
    pass

@click.command()

@click.option('--first_name', prompt="Enter first name", help='first name of the doctor')
@click.option('--last_name', prompt="Enter last name", help='last name of the doctor')
@click.option('--department', prompt="Enter department", help='the department of the doctor')
@click.option('--phone', prompt="Enter phone number", help='phone number of the doctor')

def add(first_name,last_name,department,phone):
    doctor_cls.add_doctor(first_name,last_name,department,phone)
    click.echo('Doctor added successfully!')

@doctor.command()
def list():
    doctors=doctor_cls.get_doctors()
    if not doctors:
        click.echo("No doctors found.")
    else:
        headers = ["ID", "Name", "Department"]
        rows = [[doctor.id, doctor.full_name(), doctor.department] for doctor in doctors]
        table = tabulate.tabulate(rows, headers, tablefmt="fancy_grid")
        click.echo(table)
@click.command()
@click.option('--name', required=True ,help="enter  name" ,prompt="Enter name")
# @click.option('--last_name', required=True ,help="enter last name" ,prompt="Enter last name")
def search_doctor(name):
    doctor =doctor_cls. get_doctor_by_name(name)
    if doctor is not None:
        headers = ["ID", "Name", "Department"]
        rows = [[doctor.id, doctor.full_name(), doctor.department]]
        table = tabulate.tabulate(rows, headers, tablefmt="fancy_grid")
        click.echo(f"Found Doctor:\n{table}")
    else:
        click.echo(f"{name} not found")

@click.command()
@click.option('--name',required=True,help="Name of the the doctor",prompt="Name of the doctor")
def get_appointment_for_doc(name):
    
    doctor_cls.get_doctor_appointments(name)
    
   
    
@click.command()
@click.option('--name',required=True,help="Name of doctor to delete",prompt="Name of doctor to delete")
def delete (name):
    doctor_cls.delete_doctor(name)
    
    
doctor.add_command(list)
doctor.add_command(add)
doctor.add_command(search_doctor)
doctor.add_command(get_appointment_for_doc)
doctor.add_command(delete)
if __name__ == '__main__':
    doctor()

# @doctor.command()
# @click.option('--id', prompt=True, help='ID of the doctor')
# def appointments(id):
#     doctor = doctor_controller.get_doctor_by_name(id)
#     appointments = doctor_controller.get_doctor_appointments(id)
#     click.echo(f"Appointments for Doctor {doctor.name}:")
#     for appointment in appointments:
#         click.echo(f"Appointment ID: {appointment.id}, Patient: {appointment.patient.name}")

