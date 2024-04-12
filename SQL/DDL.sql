CREATE TABLE Member (
    member_id SERIAL PRIMARY KEY,
    schedule VARCHAR(255) NOT NULL,
    dashboard VARCHAR(255) NOT NULL,
    personal_info VARCHAR(255) NOT NULL,
    health_metrics VARCHAR(255) NOT NULL,
    fitness_goals VARCHAR(255) NOT NULL
);

CREATE TABLE SchedulesWith (
    member_id SERIAL PRIMARY KEY,
    trainer_id INT,
    FOREIGN KEY (trainer_id) REFERENCES Trainer(id)
);

CREATE TABLE SearchesFor (
   member_id SERIAL PRIMARY KEY,
   trainer_id INT,
   FOREIGN KEY (trainer_id) REFERENCES Trainer(id)
);

CREATE TABLE Trainer (
    id SERIAL PRIMARY KEY,
    schedule VARCHAR(255) NOT NULL
);

CREATE TABLE ManagesBilling (
    transaction_id SERIAL PRIMARY KEY,
    admin_id INT,
    amount FLOAT,
    card_type VARCHAR(255) NOT NULL,
    card_num VARCHAR(255) NOT NULL,
    FOREIGN KEY (admin_id) REFERENCES AdministrativeStaff(id)
);

CREATE TABLE AdministrativeStaff (
    id SERIAL PRIMARY KEY,
    rooms VARCHAR(255) NOT NULL,
    fitness_equipment VARCHAR(255) NOT NULL,
    class_schedules VARCHAR(255) NOT NULL
);
