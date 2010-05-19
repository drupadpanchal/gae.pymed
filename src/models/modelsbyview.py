from google.appengine.ext import db

class Personal(db.Model):
    name = db.StringProperty(required=True)
    spouse_partner = db.SelfReferenceProperty()
    ssn_sin = db.StringProperty()
    occupation = db.StringProperty()
    employer = db.StringProperty()
    drivers_license = db.StringProperty()
    referred_by = db.StringProperty()
    parent_name = db.StringProperty()

class Demographic(db.Model):
    dob = db.DateTimeProperty()
    marital_status = db.StringProperty()
    perferred_language = db.StringProperty()
    gender = db.StringProperty()
    race = db.StringProperty()
    ethnicity = db.StringProperty()

class Location(db.Model):
    street_address_1 = db.StringProperty()
    street_address_2 = db.StringProperty()
    city = db.StringProperty()
    county = db.StringProperty()
    state_province = db.StringProperty()
    country = db.StringProperty()
    zip_postal = db.StringProperty()

class Contact(db.Model):
    home_phone = db.StringProperty()
    cell_phone = db.StringProperty()
    work_phone = db.StringProperty()
    email = db.StringProperty()
    emergency_contact_name = db.StringProperty()
    emergency_contact_phone = db.StringProperty()
    emergency_contact_cell_phone = db.StringProperty()
    emergency_contact_work_phone = db.StringProperty()
    emergency_contact_address = db.StringProperty()
    emergency_contact_relation = db.StringProperty()

class Insurance(db.Model):
    type = db.StringProperty()
    insurance_company = db.StringProperty()
    company_address = db.StringProperty()
    name_of_insured = db.StringProperty()
    relation_to_patient = db.StringProperty()
    group_number = db.StringProperty()
    effective_date = db.DateProperty()
    benefit_code = db.StringProperty()
    id = db.StringProperty()
    medicare_id = db.StringProperty()
    medicaid_id = db.StringProperty()
    perscription_drug_plan  = db.StringProperty()
    other_coverages = db.StringProperty()
    
class Administration(db.Model):
    date = db.DateProperty()
    co_pay = db.StringProperty()
    doctor = db.StringProperty()
    access_control = db.StringProperty()
    emergency_access = db.StringProperty()

class FamilyMedicalHistory(db.Model):
    epilepsy = db.StringProperty()
    migraine = db.StringProperty()
    mental_illness = db.StringProperty()
    glaucoma = db.StringProperty()
    diabetes = db.StringProperty()
    tyroid = db.StringProperty()
    hayfever = db.StringProperty()
    asthma = db.StringProperty()
    anemia = db.StringProperty()
    bleeds_easily = db.StringProperty()
    osteoporosis = db.StringProperty()
    arthritis = db.StringProperty()
    heart_disease = db.StringProperty()
    stroke = db.StringProperty()
    high_blood_pressure = db.StringProperty()
    high_cholesterol = db.StringProperty()
    alcoholism = db.StringProperty()
    hepatitis = db.StringProperty()
    cancer = db.StringProperty()
    other = db.StringProperty()

class PersonalMedicalHistory(db.Expando):
    # Long List of choices -- what is most appropriate to display will vary greatly depending on the kind of practice -- perhaps this is blank by default and must be configured by the practice the first time to sign-up?
    smoking_status = db.StringProperty()

class PriorHospitalAdmissions(db.Model):
    year = db.DateProperty()
    illness_operation = db.StringProperty()

class CurrentMedications(db.Expando):
    # Long List of choices -- what is most appropriate to display will vary greatly depending on the kind of practice -- perhaps this is blank by default and must be configured by the practice the first time to sign-up?
    description  = db.StringProperty()

class Allergies(db.Expando):
    # Long List of choices -- what is most appropriate to display will vary greatly depending on the kind of practice -- perhaps this is blank by default and must be configured by the practice the first time to sign-up?
    description = db.StringProperty()

class Vaccinations(db.Model):
    tetanus_year = db.StringProperty()
    influenza_year = db.StringProperty()
    pneumonia_year = db.StringProperty()
    hep_a = db.StringProperty()
    hep_b = db.StringProperty()
    hep_c = db.StringProperty()
    whooping_c = db.StringProperty()
    meningitis = db.StringProperty()
    chicken_pox = db.StringProperty()
