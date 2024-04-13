CREATE TABLE Member (
    MemberID SERIAL PRIMARY KEY,
    FullName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Height NUMERIC NOT NULL,
    Weight NUMERIC NOT NULL,
    WeightGoal NUMERIC NOT NULL
);

CREATE TABLE Trainer (
    TrainerID SERIAL PRIMARY KEY,
    FullName VARCHAR(255) NOT NULL,
    DaysAvailable VARCHAR(255) NOT NULL,
    StartTime VARCHAR(255) NOT NULL,
    EndTime VARCHAR(255) NOT NULL
);

CREATE TABLE AdministrativeStaff (
    AdminID SERIAL PRIMARY KEY,
    FullName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL
);

CREATE TABLE TrainingSession (
    SessionID SERIAL PRIMARY KEY,
    MemberID INTEGER REFERENCES Member(ID),
    TrainerID INTEGER REFERENCES Trainer(ID),
    SessionDay VARCHAR(255) NOT NULL,
    StartTime VARCHAR(255) NOT NULL,
    EndTime VARCHAR(255) NOT NULL,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID)
);

CREATE TABLE RoomBooking (
    RoomID SERIAL PRIMARY KEY,
    BookingDay VARCHAR(255) NOT NULL,
    StartTime VARCHAR(255) NOT NULL,
    EndTime VARCHAR(255) NOT NULL,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (AdminID) REFERENCES AdministrativeStaff(AdminID)
);

CREATE TABLE Equipment (
    EquipmentID SERIAL PRIMARY KEY,
    EquipmentName VARCHAR(255) NOT NULL,
    MaintenanceStatus VARCHAR(255) NOT NULL,
    Availability VARCHAR(255) NOT NULL
);

CREATE TABLE Class (
    ClassID SERIAL PRIMARY KEY,
    ClassName VARCHAR(255) NOT NULL,
    ClassDay VARCHAR(255) NOT NULL,
    StartTime VARCHAR(255) NOT NULL,
    EndTime VARCHAR(255) NOT NULL
);

CREATE TABLE Billing (
    Amount NUMERIC NOT NULL,
    CardNumber VARCHAR(255) NOT NULL,
    CardType VARCHAR(255) NOT NULL,
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
    FOREIGN KEY (AdminID) REFERENCES AdministrativeStaff(AdminID)
);
