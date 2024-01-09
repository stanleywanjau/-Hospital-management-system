# views/doctor_view.py
import click
from models.Doctor import Doctor

doctor_controller = Doctor()

@click.group()
def doctor():
    pass

@doctor.command()
@click.option('--name', prompt=True, help='Name of the doctor')
def add(name):
    doctor_controller.add_doctor(name)
    click.echo('Doctor added successfully!')

@doctor.command()
def list():
    doctors = doctor_controller.get_doctors()
    for doctor in doctors:
        click.echo(f"Doctor ID: {doctor.id}, Name: {doctor.name}")

@doctor.command()
@click.option('--id', prompt=True, help='ID of the doctor')
def appointments(id):
    doctor = doctor_controller.get_doctor_by_id(id)
    appointments = doctor_controller.get_doctor_appointments(id)
    click.echo(f"Appointments for Doctor {doctor.name}:")
    for appointment in appointments:
        click.echo(f"Appointment ID: {appointment.id}, Patient: {appointment.patient.name}")

