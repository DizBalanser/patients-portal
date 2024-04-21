from flask import Flask, request, jsonify
from patient_db import PatientDB

class PatientAPIController:
    def __init__(self):
        self.app = Flask(__name__)
        self.patient_db = PatientDB()
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/patients", methods=["GET"])(self.get_patients)
        self.app.route("/patients/<patient_id>", methods=["GET"])(self.get_patient)
        self.app.route("/patients", methods=["POST"])(self.create_patient)
        self.app.route("/patient/<patient_id>", methods=["PUT"])(self.update_patient)
        self.app.route("/patient/<patient_id>", methods=["DELETE"])(self.delete_patient)

    def create_patient(self):
        data = request.json
        try:
            patient_id = self.patient_db.insert_patient(data)
            if patient_id:
                return jsonify({"id": patient_id}), 201
            else:
                return jsonify({"error": "Patient could not be created."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def get_patients(self):
        try:
            patients = self.patient_db.select_all_patients()
            return jsonify(patients), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def get_patient(self, patient_id):
        try:
            patient = self.patient_db.select_patient(patient_id)
            if patient:
                return jsonify(patient), 200
            else:
                return jsonify({"error": "Patient not found."}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def update_patient(self, patient_id):
        data = request.json
        try:
            updated = self.patient_db.update_patient(patient_id, data)
            if updated:
                return jsonify({"success": True}), 200
            else:
                return jsonify({"error": "Patient could not be updated."}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def delete_patient(self, patient_id):
        try:
            deleted = self.patient_db.delete_patient(patient_id)
            if deleted:
                return jsonify({"success": True}), 200
            else:
                return jsonify({"error": "Patient not found."}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    controller = PatientAPIController()
    controller.run()
