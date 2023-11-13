# FlaskAPI-for-job-application-system

# Job Management API

This Flask-based REST API allows you to manage job details, user registrations, and job applications.

## Prerequisites

- Python installed (version 3.x)
- MongoDB installed and running on `localhost:27017`

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/job-management-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd job-management-api
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. Ensure that MongoDB is running on `localhost:27017`.

2. Open a MongoDB shell and execute the following script to add sample data:

    ```javascript
    var citiesInIndia = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Surat", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Pimpri-Chinchwad", "Patna", "Vadodara"];
    var jobRoles = ["Software Developer", "Data Analyst", "Network Engineer", "UX Designer", "Project Manager", "System Administrator", "Business Analyst", "QA Tester", "Technical Writer", "Database Administrator", "DevOps Engineer", "Frontend Developer", "Backend Developer", "Security Analyst", "Mobile App Developer", "Cloud Architect", "AI/ML Engineer", "UI Developer", "Full Stack Developer", "Product Manager"];

    var records = [];

    for (var i = 0; i < 20; i++) {
        var city = citiesInIndia[Math.floor(Math.random() * citiesInIndia.length)];
        var jobRole = jobRoles[Math.floor(Math.random() * jobRoles.length)];
        var salary = 2000 + Math.random() * 1000; // Random salary between 2000 and 3000
        salary = salary.toFixed(2); // Keep two decimal places

        records.push({
            jobRole: jobRole,
            location: city,
            startDate: ISODate("2023-11-13T00:00:00Z"),
            transportation: "Available",
            timing: "9:00 AM - 5:00 PM",
            salaryPerHour: parseFloat(salary)
        });
    }

    db.yourCollectionName.insertMany(records);
    ```

    Ensure to replace `yourCollectionName` with the actual name of your collection.

## Running the Application

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. The API will be accessible at `http://127.0.0.1:5000`.

## Endpoints

- GET `/jobs`: Retrieve details of all jobs.
- POST `/register`: Register for a job (provide name, email, and jobRole in the request payload).
- GET `/joined-jobs/<email>`: Retrieve a list of jobs joined by a user (replace `<email>` with the user's email).
- GET `/job/<job_role>`: Retrieve details of a specific job by job role (replace `<job_role>` with the desired job role).

Feel free to explore and test the API using a tool like Postman.
