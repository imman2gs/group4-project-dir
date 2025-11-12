from models.db import db 
from datetime import datetime, timezone

class Student(db.Model):
    __tablename__- 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    email = db.Column(db.String(255), unique=True)
    pass_word= db.Column(db.String(255), unique=True, nullable=False)
    birthday = db.Column(db.String(db.date))
    gender = db.Column(db.String(10))
    phone_number = db.Column(db.String(11))
    address = db.Column(db.String(255))
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Student {self.student_id if self.student_id else "No ID"}: {self.last_name}, {self.first_name}>'