-- COMP 3005 Project V2 Group 95 DML

-- Insert into Members Table
INSERT INTO Member(FullName, Email, Phone, Height, Weight, WeightGoal)
VALUES ('Robert James', 'Robjames@gmail.com', '234567', '193', '230', '200'),
       ('David Owens', 'Monday, Friday', '177288', '186', '150', '180');  

-- Insert into Trainers Table
INSERT INTO Trainer(FullName, DaysAvailable, StartTime, EndTime)
VALUES ('Bob Jones', 'Tuesday, Wednesday, Thursday', '09:00:00', '17:00:00'),
       ('Mike Jordan', 'Monday, Friday', '09:00:00', '17:00:00');


-- Insert into AdministrativeStaff Table
INSERT INTO AdministrativeStaff(FullName, Email)
VALUES ('Marshall Bean', 'admin1@gmail.com'),
       ('Cena John', 'admin2@gmail.com');


-- Insert into Sessions Table
INSERT INTO TrainingSession(MemberID, TrainerID, SessionDay, StartTime, EndTime)
VALUES ('1','1', 'Tuesday', '10:00:00', '11:00:00'),
       ('2','2', 'Wednesday', '14:00:00', '15:00:00');


-- Insert into RoomBookings Table
INSERT INTO RoomBooking(RoomID, MemberID, BookingDay, StartTime, EndTime)
VALUES ('1','1', 'Monday', '09:00:00', '10:00:00'),
       ('2','2', 'Friday', '13:00:00', '14:00:00');  

-- Insert into Equipments Table
INSERT INTO Equipment(EquipmentName, MaintenanceStatus, Availability)
VALUES ('Barbell', 'Good', 'Available'),
       ('Skipping Rope', 'Broken', 'Not Available');


-- Insert into Classes Table
INSERT INTO Class(ClassName, Days, StartTime, EndTime)
VALUES ('Yoga', 'Tuesday', '09:00:00', '10:00:00'),
       ('Meditation', 'Saturday', '11:00:00', '12:00:00');
       

-- Insert into Billings Table
INSERT INTO Billing(MemberID, Amount, CardNumber, CardType)
VALUES ('1','60', '1234', 'Debit'),
       ('2','80', '5678', 'Credit');
