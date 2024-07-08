from Quality import create_app, db

app = create_app()

# Create an application context
with app.app_context():
    # Create all tables
    db.create_all()
    db.session.commit()
    print("Tables created!")
