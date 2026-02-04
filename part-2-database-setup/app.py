# =============================================================================
# Part 2: Database Setup
# =============================================================================
# Now we add a database to store data permanently.
# We will learn:
#   1. What is SQLAlchemy (database toolkit)
#   2. How to create database models (tables)
#   3. How to query the database
# =============================================================================

from flask import Flask, render_template
from models import db, User, Todo, init_db

app = Flask(__name__)

# Database configuration
# 'sqlite:///todo.db' creates a file called 'todo.db' in instance/ folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
init_db(app)


# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')


@app.route('/test-db')
def test_db():
    """
    Test route to verify database is working.
    Creates 3 test users and todos if DB is empty.
    """

    # Step 1: Check if any users exist
    users = User.query.all()

    if not users:
        # Step 2: Create multiple users
        user1 = User(
            username='testuser1',
            email='test1@example.com',
            password_hash='temporary'
        )

        user2 = User(
            username='testuser2',
            email='test2@example.com',
            password_hash='temporary'
        )

        user3 = User(
            username='testuser3',
            email='test3@example.com',
            password_hash='temporary'
        )

        # Step 3: Add all users at once
        db.session.add_all([user1, user2, user3])
        db.session.commit()

        # Step 4: Create todos for each user
        todo1 = Todo(task_content='Learn Flask', user_id=user1.id)
        todo2 = Todo(task_content='Learn SQLAlchemy', user_id=user2.id)
        todo3 = Todo(task_content='Build Todo App', user_id=user3.id)

        db.session.add_all([todo1, todo2, todo3])
        db.session.commit()

    # Step 5: Fetch all data to display
    all_users = User.query.all()
    all_todos = Todo.query.all()

    return render_template(
        'test_db.html',
        users=all_users,
        todos=all_todos
    )



# =============================================================================
# RUN THE SERVER
# =============================================================================
if __name__ == '__main__':
    print("\n" + "="*50)
    print("  Part 2: Database Setup")
    print("  Open: http://127.0.0.1:5000")
    print("  Test DB: http://127.0.0.1:5000/test-db")
    print("="*50 + "\n")
    app.run(debug=True)


# ============================================
# SELF-STUDY QUESTIONS
# ============================================
# 1. What is SQLAlchemy and why do we use it?
# 2. What does db.Column(db.String(80)) mean?
# 3. What is the difference between db.session.add() and db.session.commit()?
# 4. What does filter_by() do? How is it different from get()?
# 5. What happens if you delete todo.db file and restart the app?
#
# ============================================
# ACTIVITIES - Try These!
# ============================================
# Activity 1: Add a new field
#   - In models.py, add 'phone' field to User model
#   - Delete todo.db file (so tables are recreated)
#   - Restart the app and check if it works
#
# Activity 2: Query practice
#   - In test_db route, try: User.query.all() (gets all users)
#   - Try: User.query.first() (gets first user)
#   - Try: User.query.count() (counts users)
#
# Activity 3: View database file
#   - Install "DB Browser for SQLite" software
#   - Open instance/todo.db file
#   - See the tables and data inside
#
# Activity 4: Add more test data
#   - Modify test_db() to create 3 users instead of 1
#   - Create different todos for each user
# ============================================
