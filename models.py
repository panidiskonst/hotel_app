from app import db

class Hotel_group(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Hotel_group_name = db.Column(db.String(100), nullable=False)
    Number_of_hotels= db.Column(db.Integer,nullable=False)
    address = db.relationship('Hotel_group_address',cascade="delete" , backref=('hotel_group'),lazy='dynamic')
    phones = db.relationship('Hotel_group_phones',cascade="delete" , backref=('hotel_group'),lazy='dynamic')
    hotels = db.relationship('Hotel',cascade="delete" ,backref=('hotel_group'),lazy='dynamic')


class Hotel_group_address(db.Model):




























    id=db.Column(db.Integer, primary_key=True,autoincrement = True)
    Street=db.Column(db.String(100),nullable=False)
    Street_number = db.Column(db.Integer,nullable=False)
    Postal_code = db.Column( db.Integer,nullable=False)
    City = db.Column( db.String(100),nullable=False)
    hotel_groupID = db.Column(db.Integer,db.ForeignKey('hotel_group.id'),nullable=False)


class Hotel_group_phones(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number=db.Column(db.String(100),nullable=False)
    hotel_groupID = db.Column(db.Integer, db.ForeignKey('hotel_group.id'), nullable=False)

    def add_hgroup_phone(id,phone_number):
        hgroup_phone=Hotel_group_phones(hotel_groupID=id,phone_number=phone_number)
        db.session.add(hgroup_phone)
        db.session.commit()

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Hotel_name = db.Column(db.String(100), nullable=False)
    Number_of_rooms = db.Column(db.Integer, nullable=False)
    Stars = db.Column(db.Integer, nullable=False)
    hotel_groupID = db.Column(db.Integer, db.ForeignKey('hotel_group.id'),nullable=False)
    address = db.relationship('Hotel_address',cascade="delete" , backref=('hotel'),lazy='dynamic')
    emails= db.relationship('Hotel_email',cascade="delete" , backref=('hotel'),lazy='dynamic')
    phones= db.relationship('Hotel_phone',cascade="delete" , backref=('hotel'),lazy='dynamic')
    rooms = db.relationship('Hotel_room',cascade="delete" , backref=('hotel'),lazy='dynamic')
    working = db.relationship('Works',cascade="delete" , backref=('hotel'),lazy='dynamic')


class Hotel_address(db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement = True)
    Street=db.Column(db.String(100),nullable=False)
    Street_number = db.Column(db.Integer,nullable=False)
    Postal_code = db.Column( db.Integer,nullable=False)
    City = db.Column( db.String(100),nullable=False)
    hotelID = db.Column(db.Integer,db.ForeignKey('hotel.id'),nullable=False)


class Hotel_email(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_address = db.Column(db.String(100), nullable=False)
    hotelID = db.Column(db.Integer, db.ForeignKey('hotel.id'),nullable=False)

class Hotel_phone(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.String(100), nullable=False)
    hotelID = db.Column(db.Integer, db.ForeignKey('hotel.id'),nullable=False)

class Hotel_room(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Price = db.Column(db.Integer,nullable=False)
    Capacity = db.Column(db.Integer,nullable=False)
    Repairs_needed = db.Column(db.String(100), nullable=False)
    View = db.Column(db.String(100), nullable=True)
    Expandable = db.Column(db.String(100), nullable=True)
    hotelID = db.Column(db.Integer, db.ForeignKey('hotel.id'),nullable=False)
    reserves = db.relationship('Reserve', backref=('hotel_room'),lazy='dynamic')
    rents = db.relationship('Rents', backref=('hotel_room'),lazy='dynamic')



class Customer(db.Model):
    IRS_Number = db.Column(db.Integer, nullable=False, primary_key=True)
    First_name = db.Column(db.String(100), nullable=False)
    Last_name = db.Column(db.String(100), nullable=False)
    Social_security_number = db.Column(db.Integer, nullable=False)
    First_registration=db.Column(db.DateTime, nullable=False)
    address = db.relationship('Customer_address',cascade="delete" , backref=('customer'),lazy='dynamic')
    reserves=db.relationship('Reserve',cascade="delete" , backref=('customer'),lazy='dynamic')
    rents = db.relationship('Rents',cascade="delete" , backref=('customer'),lazy='dynamic')

class Customer_address(db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement = True)
    Street=db.Column(db.String(100),nullable=False)
    Street_number = db.Column(db.Integer,nullable=False)
    Postal_code = db.Column( db.Integer,nullable=False)
    City = db.Column( db.String(100),nullable=False)
    customer_irs = db.Column(db.Integer,db.ForeignKey('customer.IRS_Number'),nullable=False)


class Employee(db.Model):
    IRS_Number = db.Column(db.Integer,nullable=False, primary_key=True)
    First_name = db.Column(db.String(100),nullable=False)
    Last_name = db.Column(db.String(100),nullable=False)
    Social_security_number = db.Column(db.Integer,nullable=False)
    address=db.relationship('Employee_address',cascade="delete" ,backref=('employee'),lazy='dynamic')
    works_as = db.relationship('Works',cascade="delete" ,backref=('employee'),lazy='dynamic')
    checkin_rent = db.relationship('Rents',cascade="delete",backref=('employee'),lazy='dynamic')

class Works(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Start_date = db.Column(db.DateTime, nullable=False)
    Finish_date = db.Column(db.DateTime, nullable=False)
    Position = db.Column(db.String(100),nullable=False)
    employee_irs = db.Column(db.Integer, db.ForeignKey('employee.IRS_Number'), nullable=False)
    hotelID = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)


class Employee_address(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    Street = db.Column(db.String(100),nullable=False)
    Street_number = db.Column(db.Integer,nullable=False)
    Postal_code = db.Column( db.Integer,nullable=False)
    City = db.Column( db.String(100),nullable=False)
    employee_irs = db.Column(db.Integer,db.ForeignKey('employee.IRS_Number'),nullable=False)


class Reserve(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Start_date = db.Column(db.DateTime, nullable=False)
    Finish_date = db.Column(db.DateTime, nullable=False)
    Paid = db.Column(db.DateTime,default=None, nullable=True)
    customer_irs = db.Column(db.Integer, db.ForeignKey('customer.IRS_Number'), nullable=False)
    roomID = db.Column(db.Integer,db.ForeignKey('hotel_room.id'),nullable=True)

class Rents(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Start_date = db.Column(db.DateTime, nullable=False)
    Finish_date = db.Column(db.DateTime, nullable=False)
    customer_irs = db.Column(db.Integer, db.ForeignKey('customer.IRS_Number'), nullable=False)
    roomID = db.Column(db.Integer, db.ForeignKey('hotel_room.id'), nullable=True)
    employee_irs = db.Column(db.Integer, db.ForeignKey('employee.IRS_Number'), nullable=False)
    payment = db.relationship('Payment_transaction',cascade="delete", backref=('rents'),lazy='dynamic')

class Payment_transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Payment_Amount = db.Column(db.String(100),nullable=False)
    Payment_method = db.Column( db.String(100),nullable=False)
    rentID = db.Column(db.Integer, db.ForeignKey('rents.id'), nullable=False)



