import uuid
from datetime import datetime
import logging
from config import VALID_ROOMS, VALID_WARDS, VALID_GENDERS
from patient_db import PatientDB  # Ensure this import is correct

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Patient:
    def __init__(self, name, gender, age):
        self.id = str(uuid.uuid4())
        self.name = name
        self.gender = gender
        self.age = age
        self.checkin = datetime.now()
        self.checkout = None
        self.room = None
        self.ward = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in VALID_GENDERS:
            raise ValueError(f"Gender must be one of {VALID_GENDERS}")
        self._gender = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

    @property
    def checkout(self):
        return self._checkout

    @checkout.setter
    def checkout(self, value):
        if self._checkout is not None:
            raise ValueError("Checkout date can only be set once")
        if not isinstance(value, datetime):
            raise ValueError("Checkout must be a datetime object")
        self._checkout = value

    def update_room_and_ward(self, room, ward):
        if room not in VALID_ROOMS[self.ward]:
            raise ValueError("Invalid room for the ward")
        if ward not in VALID_WARDS:
            raise ValueError("Invalid ward")
        self.room = room
        self.ward = ward

    def commit(self):
        patient_db = PatientDB()
        patient_data = {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'checkin': self.checkin,
            'checkout': self.checkout,
            'room': self.room,
            'ward': self.ward
        }
        try:
            result = patient_db.insert_patient(patient_data)
            if result is None:
                logging.error("Failed to insert patient into the database")
                return None
            return result
        except Exception as e:
            logging.error(f"An error occurred while committing the patient: {e}")
            return None
