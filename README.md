Flask User Management
Objective :- This application demonstrates basic Flask API development, MySQL database interaction, and version control using Git. It includes user listing, adding new users, and viewing specific user details.

Tech Stack
Backend: Python (Flask)
Database: MySQL
Frontend: HTML
Version Control: Git

 Setup Instructions:-
1. Clone the Repository :-
→ git clone https://github.com/singhkajal25/flask_assignment.git
→ cd flask_assignment

2. Create Virtual Environment (Optional but Recommended):- 
→ python -m venv venv
→ .\venv\Scripts\Activate

3. Install required packages:
→ pip install flask mysql-connector-python

4.  Run the Flask app:
→ python app.py

5. Open browser:
→ http://127.0.0.1:5000


 
 ### 🗃️ MySQL Database Details

- Database Name: `users`
- Table: `users`
- Schema:
  - id (INT, Primary Key)
  - name (VARCHAR)
  - email (VARCHAR)
  - role (VARCHAR)

#### Sample SQL Queries

```sql
-- Create Table
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  email VARCHAR(100),
  role VARCHAR(50)
);

-- Insert Sample Data
INSERT INTO users (name, email, role) VALUES
 ('Kajal Singh', 'kajal@example.com', 'Admin'),
 ('Niharika Lakra', 'niharika@example.com', 'Editor'),
 ('Rahul Mehta', 'rahul@example.com', 'Viewer');


-- Fetch All Users
SELECT * FROM users;

-- Fetch User by ID
SELECT * FROM users WHERE id = 1;

### 5. **Routes & Features**
List the Flask routes:

```markdown
### 🌐 Routes Implemented

- `/hello` → returns “Hello World!”
- `/users` → displays all users in an HTML table
- `/new_user` → form to add a new user
- `/users/<id>` → shows details of a specific user
- Error handling → for user not found and other issues

 ###  Git Workflow

- Initialized git repo locally using `git init`
- Created branch `assignment`
- Committed changes as per each task
- Pushed to GitHub
- Created pull request to merge `assignment` branch into `main`


###  Contribution Guidelines

- Fork the repo
- Create a feature branch
- Make changes and commit
- Open a pull request

 
 
 
