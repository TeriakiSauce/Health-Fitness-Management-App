-- COMP 3005 Project V2 Group 95 DML

-- Insert into Members Table
INSERT INTO Member(FullName, Email, Phone, Height, Weight, WeightGoal, WeightChange)
VALUES ('Robert James', 'Robjames@gmail.com', '234567', '193', '230', '200', '10'),
       ('David Owens', 'Monday, Friday', '177288', '186', '150', '180', '15'),
       ('Alice Smith', 'alice.smith@example.com', '987654', '170', '140', '130', '-5'),
       ('John Doe', 'john.doe@example.com', '123456', '180', '190', '160', '0'),
       ('Emily Johnson', 'emily.johnson@example.com', '456789', '165', '150', '140', '5'),
       ('Michael Brown', 'michael.brown@example.com', '987654', '175', '160', '150', '-8');

-- Insert into Trainers Table
INSERT INTO Trainer(FullName, DaysAvailable, StartTime, EndTime)
VALUES ('Bob Jones', 'Tuesday, Wednesday, Thursday', '09:00:00', '17:00:00'),
       ('Mike Jordan', 'Monday, Friday', '09:00:00', '17:00:00'),
       ('Sarah Lee', 'Monday, Wednesday, Friday', '10:00:00', '18:00:00'),
       ('Chris Evans', 'Tuesday, Thursday', '11:00:00', '19:00:00'),
       ('Emma Watson', 'Monday, Wednesday, Thursday', '08:00:00', '16:00:00'),
       ('Daniel Smith', 'Tuesday, Thursday, Friday', '09:00:00', '17:00:00');

-- Insert into AdministrativeStaff Table
INSERT INTO AdministrativeStaff(FullName, Email)
VALUES ('Marshall Bean', 'admin1@gmail.com'),
       ('Cena John', 'admin2@gmail.com'),
       ('Jessica Miller', 'admin3@gmail.com'),
       ('Alex Johnson', 'admin4@gmail.com'),
       ('Sophia Garcia', 'admin5@gmail.com'),
       ('William Martinez', 'admin6@gmail.com');

-- Insert into Sessions Table
INSERT INTO SessionBooking(MemberID, TrainerID, SessionDay, StartTime, EndTime)
VALUES ('1', '1', 'Tuesday', '10:00:00', '11:00:00'),
       ('2', '4', 'Wednesday', '14:00:00', '15:00:00'),
       ('3', '3', 'Friday', '15:00:00', '16:00:00'),
       ('4', '2', 'Thursday', '13:00:00', '14:00:00'),
       ('5', '5', 'Monday', '11:00:00', '12:00:00'),
       ('6', '6', 'Friday', '16:00:00', '17:00:00');

-- Insert into RoomBookings Table
INSERT INTO RoomBooking(MemberID, BookingDay, StartTime, EndTime)
VALUES ('1', 'Monday', '09:00:00', '10:00:00'),
       ('2', 'Friday', '13:00:00', '14:00:00'),
       ('3', 'Wednesday', '10:00:00', '11:00:00'),
       ('4', 'Monday', '13:00:00', '14:00:00'),
       ('5', 'Thursday', '14:00:00', '15:00:00'),
       ('6', 'Tuesday', '15:00:00', '16:00:00');

-- Insert into Equipments Table
INSERT INTO Equipment(EquipmentName, MaintenanceStatus, Availability)
VALUES ('Barbell', 'Excellent', 'Available'),
       ('Skipping Rope', 'Broken', 'Not Available'),
       ('Dumbbell Set', 'Good', 'Available'),
       ('Exercise Ball', 'Good', 'Available'),
       ('Resistance Bands', 'Good', 'Available'),
       ('Treadmill', 'Broken', 'Not Available');

-- Insert into Classes Table
INSERT INTO Class(ClassName, ClassDay, StartTime, EndTime)
VALUES ('Yoga', 'Tuesday', '09:00:00', '10:00:00'),
       ('Meditation', 'Saturday', '11:00:00', '12:00:00'),
       ('Pilates', 'Thursday', '17:00:00', '18:00:00'),
       ('Spinning', 'Friday', '19:00:00', '20:00:00'),
       ('Boxing', 'Saturday', '10:00:00', '11:00:00'),
       ('CrossFit', 'Sunday', '09:00:00', '10:00:00');
       
-- Insert into Billings Table
INSERT INTO Billing(MemberID, Amount, CardNumber, CardType)
VALUES ('1','60', '1234', 'Debit'),
       ('2','80', '5678', 'Credit'),
       ('3', '70', '9012', 'Credit'),
       ('4', '90', '3456', 'Debit'),
       ('5', '50', '7890', 'Credit'),
       ('6', '75', '2345', 'Debit');

