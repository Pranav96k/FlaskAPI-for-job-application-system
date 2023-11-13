from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Configure MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client.digitalflake  # Use the name of your database

# Define the collections
job_collection = db.yourCollectionName  # Use the name of your collection
user_collection = db.users

# Sample data for initialization
initial_data = [
    {
        'jobRole': 'Software Developer',
        'location': 'City XYZ',
        'startDate': '2023-11-13',
        'transportation': 'Available',
        'timing': '9:00 AM - 5:00 PM',
        'salaryPerHour': 30.50
    },
    # Add more initial data as needed
]

# Initialize the job collection with sample data
job_collection.insert_many(initial_data)

# Routes


@app.route('/jobs', methods=['GET'])
def get_all_jobs():
    jobs = job_collection.find({}, {'_id': 0})
    return jsonify({'jobs': list(jobs)})


@app.route('/register', methods=['POST'])
def register_for_job():
    data = request.get_json()

    # Assuming the request payload includes 'name', 'email', and 'jobRole'
    name = data.get('name')
    email = data.get('email')
    job_role = data.get('jobRole')

    if not name or not email or not job_role:
        return jsonify({'error': 'Name, email, and jobRole are required fields'}), 400

    # Check if the job exists
    job = job_collection.find_one({'jobRole': job_role})
    if not job:
        return jsonify({'error': f'Job with role {job_role} not found'}), 404

    # Register the user for the job
    user_collection.insert_one({
        'name': name,
        'email': email,
        'jobRole': job_role
    })

    return jsonify({'message': f'{name} registered for the job {job_role}'}), 201


@app.route('/joined-jobs/<email>', methods=['GET'])
def get_joined_jobs(email):
    user_jobs = user_collection.find({'email': email}, {'_id': 0, 'email': 0})
    return jsonify({'joinedJobs': list(user_jobs)})


@app.route('/job/<job_role>', methods=['GET'])
def get_job_details(job_role):
    job = job_collection.find_one({'jobRole': job_role}, {'_id': 0})
    if job:
        return jsonify({'jobDetails': job})
    else:
        return jsonify({'error': f'Job with role {job_role} not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
