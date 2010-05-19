from google.appengine.ext import db
from google.appengine.ext.db import polymodel  

class User(db.Model):
    login_name = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    type = db.StringProperty(choices=set(['admin', 'priviledged_user', 'user', 'guest']), default='guest')

class Party(polymodel.PolyModel):
    name = db.StringProperty(required=True)
    contact_mechanisms = db.ListProperty(db.Key)    # list of keys from the Contact model

class Person(Party):
    first_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    middle_name = db.StringProperty()
    ssn = db.StringProperty()
    drivers_license = db.StringProperty()
    birth_date = db.DateTimeProperty(required=True)
    death_date = db.DateTimeProperty()
    marital_status = db.StringProperty(choices=set(['Single', 'Married', 'Divorced', 'Separated', 'Unknown']), default='Unknown')
    gender = db.StringProperty(choices=set(['Male', 'Female', 'Unknown']), default='Unknown')
    ethnicity = db.StringProperty(choices=set(['Caucasian', 'Hispanic', 'Asian', 'Native-American', 'African-American']))
    languages = db.StringListProperty()    #['English', 'Spanish', 'French', 'German', 'Chinese']
    user = db.ReferenceProperty(User)
    photo = db.ListProperty(db.Blob)
    type = db.StringProperty(choices=set(['Patient', 'Provider', 'Referring-Provider', 'Other']), default='Other')
    spouse_partner = db.SelfReferenceProperty()

class Facility(db.Model):
    description = db.StringProperty()
    party = db.ReferenceProperty(Party, collection_name='facilities')

class Organization(Party):
    description = db.StringProperty()
    type = db.StringProperty(choices=set(['Practice', 'Clinic', 'Hospital', 'Employer', 'Pharmacy', 'Other']), default='Other')
    party = db.ReferenceProperty(Party, collection_name='organizations')

class Qualification(db.Model):
    description = db.StringListProperty()
    party = db.ReferenceProperty(Party, collection_name='qualifications')

class ContactMechanism(polymodel.PolyModel):
    type = db.StringProperty(choices=set(['Address', 'Phone', 'Email', 'Other']), default='Other')
    description = db.StringProperty()
    
class Address(ContactMechanism):
    street1 = db.StringProperty()
    street2 = db.StringProperty()
    city = db.StringProperty()
    county = db.StringProperty()
    state_province = db.StringProperty()
    zip_code = db.StringProperty()
    country = db.StringProperty()
    party = db.ReferenceProperty(Party, collection_name='postal_addresses')

class Phone(ContactMechanism):
    number = db.PhoneNumberProperty()
    extension = db.StringProperty()
    party = db.ReferenceProperty(Party, collection_name='phone_numbers')

class Email(ContactMechanism):
    email = db.ListProperty(db.Email())
    party = db.ReferenceProperty(Party, collection_name='email_addresses')
