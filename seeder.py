from app import app
from models.db import db
from models.user_model import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def seed_data():
    with app.app_context():
        try:
            print("Starting database seeding")

            seed_users = [
                User(
                    fname="Immanuel",
                    lname="Tugade",
                    uname="immanuel28",
                    email="immanueltugade28@gmail.com",
                    pass_word=generate_password_hash("admin123"),
                    birthday="2013-05-15",
                    gender="male",
                    phone_number="09994875529",
                    address="Maunlad St. Brgy.Pinyahan, Quezon City",
                    student_id="2024-31532-MN0",
                ),
                User(
                    fname="Law",
                    lname="Trafalgar",
                    uname="trafalgarlaw28",
                    email="trafalgarlaw@gmail.com",
                    pass_word=generate_password_hash("password123"),
                    birthday="2004-12-25",
                    gender="male",
                    phone_number="09543645213",
                    address="Mapagbigay St. Brgy.Santolan, Davao City",
                    student_id="2023-75345-MN0",
                )
            ]

            for user in seed_users:
                existing_user = User.query.filter_by(email=user.email).first()
                if existing_user:
                    print(f"Skipping existing user: {user.email}")
                    continue
                db.session.add(user)
            
            db.session.commit()
            print("Database seeded successfully")

        except IntegrityError as e:
            db.session.rollback()
            print(f"Integrity error: {e}")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"SQLALCHEMY ERROR: {e}")
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error during seeding: {e}")

        finally:
            db.session.close()

if __name__ == "__main__":
    seed_data()