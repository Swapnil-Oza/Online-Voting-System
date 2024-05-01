from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Ballot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    candidates = db.relationship('Candidate', backref='ballot', lazy='dynamic')

    def __repr__(self):
        return '<Ballot {}>'.format(self.title)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    votes = db.Column(db.Integer, default=0)
    ballot_id = db.Column(db.Integer, db.ForeignKey('ballot.id'))

    def __repr__(self):
        return '<Candidate {}>'.format(self.name)
