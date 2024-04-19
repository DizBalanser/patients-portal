from flask import Flask, request, jsonify

class PatientAPIController:
    def __init__(self):
        self.app = Flask(__name__)
        self.patient_db = PatientDB()
        self.setup_routes()
        self.run()

    def setup_routes(self):
        self.app.route("/patients", methods=["GET"])(self.get_patients)
        self.app.route("/patients/<int:patient_id>", methods=["GET"])(self.get_patient)
        self.app.route("/patients", methods=["POST"])(self.create_patient)
        self.app.route("/patients/<int:patient_id>", methods=["PUT"])(self.update_patient)
        self.app.route("/patients/<int:patient_id>", methods=["DELETE"])(self.delete_patient)

    def create_patient(self):
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        patient_id = self.patient_db.add_patient(data)
        return jsonify({'patient_id': patient_id}), 200

    def get_patients(self):
        patients = self.patient_db.get_all_patients()
        return jsonify({'patients': patients}), 200

    def get_patient(self, patient_id):
        patient = self.patient_db.get_patient(patient_id)
        if patient:
            return jsonify(patient), 200
        else:
            return jsonify({'error': 'Patient not found'}), 404

    def update_patient(self, patient_id):
        data = request.json
        if not data:
            return jsonify({'error': 'No update data provided'}), 400
        success = self.patient_db.update_patient(patient_id, data)
        if success:
            return jsonify({'message': 'Patient updated'}), 200
        else:
            return jsonify({'error': 'Update failed'}), 400

    def delete_patient(self, patient_id):
        success = self.patient_db.delete_patient(patient_id)
        if success:
            return jsonify({'message': 'Patient deleted'}), 200
        else:
            return jsonify({'error': 'Patient not found or could not be deleted'}), 404

    def run(self):
        self.app.run()

if __name__ == "__main__":
    PatientAPIController()
