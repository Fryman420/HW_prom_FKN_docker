from base import Base, engine, SessionLocal, User

def create_users(session):
    # Define users to add
    users = [
        User(login='pavel', email='a@gmail.com', hashed_password='hashed_password1'),
        User(login='yura', email='b@gmail.com', hashed_password='hashed_password2')
    ]
    
    # Add users to the session
    session.add_all(users)
    # Commit the changes
    session.commit()
    print("Users added successfully.")

def main():
    # Create database tables
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
    
    # Initialize a session
    with SessionLocal() as session:
        create_users(session)

if __name__ == "__main__":
    main()
