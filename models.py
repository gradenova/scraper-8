from app import db


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    item = db.Column(db.String())
    agency = db.Column(db.String())
    fsg = db.Column(db.String())
    source = db.Column(db.String())
    title = db.Column(db.String())
    keywords = db.Column(db.String())
    url_2 = db.Column(db.String())
    naics_code = db.Column(db.String())
    psc_code = db.Column(db.String())
    contact_info = db.Column(db.String())
    place_of_performance = db.Column(db.String())
    link_of_solicitation = db.Column(db.String())
    description = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)
