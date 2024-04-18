# Patients Portal

## Introduction

Patient Portal is a basic Patient management system, where the user (ie. receptionist) should do the folowing tasks:
- **List Patients:**
- **List Patients with a given name:**
- **Read a Patient with certain id:**
- **Create a Patient:**
- **Update the data of a Patient:**
- **Delete a Patient:**

## Prerequisites

- Install **Python** (recommended version >= 3.10)
- Install **Gitbash** (Optional)

## Downloading 

To install the repository requirements, follow these steps:

You have the option to either fork the repository or clone it.

### Forking the Repository: 

1. **Fork this Repository**

   Visit [https://github.com/gerelee357/patients-portal-for-students](https://github.com/gerelee357/patients-portal-for-students) and click on the "Fork" button.

   Once forked, rename the repository to *patients-portal* and click "Create Fork".

2. **Clone the Forked Repository:**

```bash
git clone https://github.com/<DizBalanser>/patients-portal.git
```



3. **Navigate to the Repository:**
```bash
cd patient-portal
```
This will allow you to download and set up the repository on your local machine.

### Cloning the Repository:

1. **Clone the Repository:**

```bash
git clone https://github.com/gerelee357/patients-portal-for-students
```

2. **Navigate to the Repository:**
```bash
cd patients-portal-for-students
```

This will allow you to download and set up the repository on your local machine.

## Building project environment

1. **Create a virtual environment**
```bash
python -m venv venv
```

2. **Activate the virtual environment**

*In linux (gitbash)*

```bash
source venv/bin/activate
```

*In windows*
```bash
source venv/Scripts/activate
```

3. **Install Python packages to run the application**
```bash
python -m pip install -r requirements.txt
```

## Running server.
   
   First Run the flask server by running the API_CONTROLLER (`src/api_controller.py`) directly or using Linux command:
```bash
python src/api_controller.py
```

With both the server and database now prepared, the next step involves finalizing the API interface by completing the function definition in src/api_controller.py. This interface serves as the bridge between the database and the client, ensuring seamless communication and interaction between the two.  

## TASK: Completing Function Definitions in src/api_controller.py

- Replace the placeholder `pass` statements with the necessary code to fulfill the requirements specified for each function. 
- Make sure your functions handle any potential exceptions.

**Point Allocation:** 

Each function definition is valued at 3 points, totaling 15 points.

Once these functions are properly implemented, the Patient Portal application will be capable of enabling users, such as receptionists, to perform a range of tasks including creating, reading, updating, and deleting patient records.


Next, you can test out the application. You can use the provided scripts or just try it out using a web browser.

### Testing the final application

In Terminal :

First Run the flask server by running the API_CONTROLLER (`src/api_controller.py`) directly or using linux command:
```bash
python src/api_controller.py
```
Once the Flask server is running, open a new terminal and keep the server running in the first one.

Then,
```bash
cd testing-api-templates
```

Then,
```bash
bash create_patient.sh
```

If it returns the patient_id in the response then meaning that Patient has been created successfully and added to the database.

Then for listing the created patients,
```bash
bash list_patients.sh
```

Then for listing the created patients with \*name\* as parameter,
```bash
bash list_patient_by_name.sh
```

Then to get a patient's details with a certain ID,
```bash
bash get_certain_patient.sh
```

Then, to update the patient,
```bash
bash update_patient.sh
```

Finally, to delete the created patient,
```bash
bash delete_patient.sh
```

## NOTE

If you encounter an error stating that port 5000 is already being used by another program when attempting to run a server, you can resolve this by following these steps:

1. Use the `lsof` command to identify the process ID (PID) associated with port 5000:

```bash
lsof -i :5000
```

2. Once you have the PID, you can stop the process using the `kill` command. For example, if the PID is 1234, you would execute:

```bash
kill -9 1234
```

Replace "1234" with the actual PID you obtained from the `lsof` command.

## You can Refer:

Flask Documentation: https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing

Flask Cheatsheet: https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf

Swagger Editor (Playground): https://editor.swagger.io/

Python OOP : https://docs.python.org/3/tutorial/classes.html


## Feedback

If you need more clarification, please ping me. I will update the readme file.


## Task Originator:

This task has been created by Aadarsh Mehdi.

LinkedIn Profile: [Aadarsh Mehdi](https://www.linkedin.com/in/aadarsh-mehdi-73754b13b/)








