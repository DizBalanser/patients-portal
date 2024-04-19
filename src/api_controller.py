"""Patient API Controller"""

from flask import Flask
from patient_db import PatientDB


class PatientAPIController:
    def __init__(self):
        self.app = Flask(__name__)
        self.patient_db = PatientDB()
        self.setup_routes()
        self.run()

    def setup_routes(self):
        """
        Sets up the routes for the API endpoints.
        """
        self.app.route("/patients", methods=["GET"])(self.get_patients)
        self.app.route("/patients/<patient_id>", methods=["GET"])(self.get_patient)
        self.app.route("/patients", methods=["POST"])(self.create_patient)
        self.app.route("/patient/<patient_id>", methods=["PUT"])(self.update_patient)
        self.app.route("/patient/<patient_id>", methods=["DELETE"])(self.delete_patient)


    """
    TODO:
    Implement the following methods,
    use the self.patient_db object to interact with the database.

    Every method in this class should return a JSON response with status code
    Status code should be 200 if the operation was successful,
    Status code should be 400 if there was a client error,
    """

    def create_patient(self):
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        patient_id = self.patient_db.add_patient(data)
        if patient_id:
            return jsonify({"message": "Patient created successfully", "patient_id": patient_id}), 201
        else:
            return jsonify({"error": "Failed to create patient"}), 400

    def get_patients(self):
        patients = self.patient_db.get_all_patients()
        return jsonify(patients), 200

    def get_patient(self, patient_id):
        patient = self.patient_db.get_patient_by_id(patient_id)
        if patient:
            return jsonify(patient), 200
        else:
            return jsonify({"error": "Patient not found"}), 404

    def update_patient(self, patient_id):
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        updated = self.patient_db.update_patient_by_id(patient_id, data)
        if updated:
            return jsonify({"message": "Patient updated successfully"}), 200
        else:
            return jsonify({"error": "Failed to update patient"}), 400

    def delete_patient(self, patient_id):
        deleted = self.patient_db.delete_patient_by_id(patient_id)
        if deleted:
            return jsonify({"message": "Patient deleted successfully"}), 200
        else:
            return jsonify({"error": "Failed to delete patient"}), 400

    def run(self):
        """
        Runs the Flask application.
        """
        self.app.run()


PatientAPIController()
