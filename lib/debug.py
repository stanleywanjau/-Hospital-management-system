from models.Doctor import Doctor, Base, engine
from models.Appointment import Appointment
from models.Patient import Patient



Base.metadata.create_all(engine)

# Instantiate a doctor object for testing
doctor = Doctor()
test_doctor = Doctor(first_name="John", last_name="Doe", department="Cardiology", phone=1234567890)

# Add the doctor to the database
doctor.add_doctor(test_doctor.first_name, test_doctor.last_name,test_doctor.department, test_doctor.phone)

# Retrieve all doctors from the database
all_doctors = doctor.get_doctors()
print("All Doctors:")
for doctor in all_doctors:
    print(doctor)


specific_doctor_id = 2  # Replace with a valid doctor ID


# Get appointments for a specific doctor
appointments = doctor.get_doctor_appointments(specific_doctor_id)
print(f"\nAppointments for Doctor with ID {specific_doctor_id}:")
for appointment in appointments:
    print(appointment)


# Retrieve a doctor by name
retrieved_doctor = doctor.get_doctor_by_name("John", "Doe")
print("\nDoctor retrieved by name:")
print(retrieved_doctor)

print("\ndeleted by id:")
doctor_to_delete_id = 6  # Replace with the actual ID of the doctor you want to delete
doctor.delete_doctor(doctor_to_delete_id)








print("\nDebug script execution completed.")
