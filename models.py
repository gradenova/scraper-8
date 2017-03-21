from app import db


class Result(db.Model):
    __tablename__ = 'dod_open_solicitations'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))
    agency = db.Column(db.String(255))
    fsg = db.Column(db.String(255))
    source = db.Column(db.String(255))
    title = db.Column(db.String(255))
    keywords = db.Column(db.String(255))
    url_2 = db.Column(db.String(255))

    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    contract_specialist = db.Column(db.String(255))
    contract_officer = db.Column(db.String(255))

    fsg_description = db.Column(db.String(255))
    set_side = db.Column(db.String(255))

    naics_code = db.Column(db.String(255))
    psc_code = db.Column(db.String(255))
    contact_info = db.Column(db.String(255))
    place_of_performance = db.Column(db.String(255))
    link_to_solicitation = db.Column(db.String(255))
    description = db.Column(db.Text())

    date = db.Column(db.DateTime)

    def __init__(self, *args, **kwargs):

        self.url = kwargs.get('url')
        self.agency = kwargs.get('agency')
        self.fsg = kwargs.get('fsg')
        self.source = kwargs.get('source')
        self.title = kwargs.get('title')
        self.keywords = kwargs.get('keywords')
        self.url_2 = kwargs.get('url_2')
        self.description = kwargs.get('description')

        self.email = kwargs.get('email')
        self.phone = kwargs.get('phone')
        self.contract_specialist = kwargs.get('contract_specialist')
        self.contract_officer = kwargs.get('contract_officer')
        self.fsg_description = kwargs.get('fsg_description')
        self.set_side = kwargs.get('set_side')

        self.naics_code = kwargs.get('naics_code')
        self.item = kwargs.get('item')
        self.psc_code = kwargs.get('psc_code')
        self.contact_info = kwargs.get('contact_info')
        self.place_of_performance = kwargs.get('place_of_performance')
        self.link_to_solicitation = kwargs.get('link_of_solicitation')

        self.date = kwargs.get('date')

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __str__(self):
        return '<id {}>'.format(self.id)
