import psycopg2

# Database connection
conct = psycopg2.connect(host="localhost", user="user1", password ="1234", port=5432, dbname="Comp3005Project")
cursr = conct.cursor()

# All Member Operations
# Update Profile Info
def updateProfileInfo():
    """
    # Updates profile with provided input
    """
    print("Current profile info")
    cursr.execute("""SELECT * FROM member""")
    for row in cursr.fetchall():
        print(row)
    print("\n")
    
def memberOperations(command):
    if (command!= "q"):
            print("""Possible Member operations are:\n
            1. User Registration\n
            2. Profile Management\n
            3. Dashboard Display\n
            4. Schedule Management\n
            q (to quit)\n""")
            command = input("Pick an operation:")
            
            # Choosing a user registration operation
            if (command == "1"):
                if (command!= "q"):
                    print("""Possible User registration operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
            
            # Choosing a profile operation
            elif (command == "2"):                
                if (command!= "q"):
                    print("""Possible Profile operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
    
            # Choosing a dashboard operation
            elif (command == "3"):                
                if (command!= "q"):
                    print("""Possible Dashboard operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
            
            # Choosing a schedule operation
            else:                
                if (command!= "q"):
                    print("""Possible Schedule operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")

# All Trainer Operations
# Schedule Management
def viewSchedule(name):
    """
    # Views current schedule
    """
    print("Your Schedule")
    parameters = (name, )
    statement = ("""SELECT * FROM Trainer WHERE FullName = %s""")
    cursr.execute(statement, parameters)
    for row in cursr.fetchall():
        print(row)
    print("\n")
    
def updateSchedule(name):
    """
    # Update Trainer schedule
    """
    days = input("What days are you available?")
    startTime = input("What time do you start?")
    endTime = input("What time do you finish?")
    parameters = (days, startTime, endTime, name)
    
    statement = """UPDATE Trainer SET DaysAvailable = %s, StartTime = %s, EndTime = %s WHERE FullName = %s"""
    cursr.execute(statement, parameters)
    for row in cursr.fetchall():
        print(row)
    print("\n")

# Member Profile Viewing
def viewMemberProfile():
    """
    # Views the profile of the specified Member
    """
    name = input("What is the full name of the Member")
    print(name, "'s Profile")
    parameters = (name, )
    statement = ("""SELECT * FROM Member WHERE FullName = %s""")
    cursr.execute(statement, parameters)
    for row in cursr.fetchall():
        print(row)
    print("\n")

def trainerOperations(command):
    if (command!= "q"):
            print("""Possible Trainer operations are:\n
            1. Schedule Management\n
            2. Member Profile Viewing\n
            q (to quit)\n""")
            command = input("Pick an operation:")
            name = input("What is your full name?")
            
            # Choosing a schedule operation
            if (command == "1"):
                if (command!= "q"):
                    print("""Possible Schedule operations are:\n
                    1. View your current schedule\n
                    2. Update your schedule\n
                    q (to quit)\n""")
                    
                    if (command == "1"):
                        viewSchedule(name)
                    elif (command == "2"):
                        updateSchedule(name)
            
            # Choosing a profile operation
            elif (command == "2"):                
                if (command!= "q"):
                    print("""Possible Profile operations are:\n
                    1. View the profile of a member\n
                    q (to quit)\n""")
                    
                    if (command == "1"):
                        viewMemberProfile()

# All Admin Staff Operations
# Room Management
def viewRooms():
    """
    # Views all rooms
    """
    print("All Rooms")
    cursr.execute("""SELECT * FROM RoomBooking""")
    for row in cursr.fetchall():
        print(row)
    print("\n")
    
def manageRooms():
    """
    # Edit a room
    """
    id = input("Type the ID of the Room you would like to edit")
    startTime = input("What time would you like to update the room to start?")
    endTime = input("What time would you like to update the room to end?")
    parameters = (startTime, endTime, id)
    
    statement = """UPDATE RoomBooking SET StartTime = %s, EndTime = %s WHERE RoomID = %s"""
    cursr.execute(statement, parameters)
    for row in cursr.fetchall():
        print(row)
    print("\n")
    
# Equipment Management
def viewEquipment():
    """
    # Views all Equipment
    """
    print("All Equipment")
    cursr.execute("""SELECT * FROM Equipment""")
    for row in cursr.fetchall():
        print(row)
    print("\n")
    
def updateEquipmentStatus():
    """
    # Edit the status of a piece of Equipment
    """
    id = input("Type the ID of the Equipment you would like to edit")
    status = input("What is the status of the Equipment?")
    availability = input("Is the equipment available to use?")
    parameters = (status, availability, id)
    
    statement = """UPDATE Equipment SET MaintenanceStatus = %s, Availability = %s WHERE ID = %s"""
    cursr.execute(statement, parameters)
    for row in cursr.fetchall():
        print(row)
    print("\n")

# Class Schedule Management
def viewClasses():
    """
    # Views all classes
    """
    print("All classes")
    cursr.execute("""SELECT * FROM Class""")
    for row in cursr.fetchall():
        print(row)
    print("\n")
    
def manageClasSchedules():
    """
    # Edit a room
    """
    id = input("Type the ID of the Class you would like to edit")
    day = input("What day would you like to update the class to?")
    startTime = input("What time would you like to update the class to start?")
    endTime = input("What time would you like to update the class to end?")
    parameters = (day, startTime, endTime, id)
    
    statement = """UPDATE Class SET ClassDay %s, StartTime = %s, EndTime = %s WHERE RoomID = %s"""
    cursr.execute(statement, parameters)
    for row in cursr.fetchall():
        print(row)
    print("\n")
    
# Billing Management
def viewTransactions():
    """
    # Views all Transactions
    """
    print("All transactions")
    cursr.execute("""SELECT * FROM Billing""")
    for row in cursr.fetchall():
        print(row)
    print("\n")
    
def processNewTransaction():
    """
    # Add a new Transaction
    """
    id = input("What is the ID of the member making the transaction?")
    amount = input("What is the amount of the transaction?")
    cardNum = input("What is the card number?")
    cardType = input("What is the card type?")
    parameters = (id, amount, cardNum, cardType)
    
    statement = """INSERT INTO Billing (MemberID, Amount, CardNumber, CardType) VALUES (%s, %s, %s, %s);"""
    cursr.execute(statement, parameters)
    for row in cursr.fetchall():
        print(row)
    print("\n")

def adminOperations(command):
    if (command!= "q"):
            print("""Possible Admin Staff operations are:\n
            1. Room Booking Management\n
            2. Equipment Maintenance Monitoring\n
            3. Class Schedule Updating\n
            4. Billing and Payment Processing\n
            q (to quit)\n""")
            command = input("Pick an operation:")

            # Choosing a room booking operation
            if (command == "1"):
                if (command!= "q"):
                    print("""Possible Room Booking operations are:\n
                    1. View all Rooms\n
                    2. Edit Room Details\n
                    q (to quit)\n""")
                    
                    if (command == "1"):
                        viewRooms()
                    elif (command == "2"):
                        manageRooms()
            
            # Choosing an equipment operation
            elif (command == "2"):
                if (command!= "q"):
                    print("""Possible Equipment Maintenance operations are:\n
                    1. View Equipment Status\n
                    2. Update Equipment Status\n
                    q (to quit)\n""")
                    
                    if (command == "1"):
                        viewEquipment()
                    elif (command == "2"):
                        updateEquipmentStatus()
            
            # Choosing a class operation
            elif (command == "3"):                
                if (command!= "q"):
                    print("""Possible Class Schedule operations are:\n
                    1. View Class Schedule\n
                    2. Update Class Schedule\n
                    q (to quit)\n""")

                    if (command == "1"):
                        viewClasses()
                    elif (command == "2"):
                        manageClasSchedules()
                    
            # Choosing a billing operation
            else:
                if (command!= "q"):
                    print("""Possible Billing operations are:\n
                    1. View all Transactions\n
                    2. Process new Payment\n
                    q (to quit)\n""")
                        
                    if (command == "1"):
                        viewTransactions()
                    elif (command == "2"):
                        processNewTransaction()

# Main App Logic
def main():         
    print("Welcome to the Health and Fitness Management System!")
    command=""

    # Choosing your role
    print("Enter a number corresponding to your role.")
    if (command!= "q"):
        print("""Possible roles are:\n
            1. Member\n
            2. Trainer\n
            3. Admin Staff\n
            q (to quit)\n""")
        command = input("Enter a command:")
        
        # Choosing a member operation
        if (command == "1"):
            memberOperations(command)
                        
        # Choosing a trainer operation    
        elif (command == "2"):
            trainerOperations(command)
        
        # Choosing an admin staff operation    
        elif (command == "3"):
            adminOperations(command)
                        
    conct.commit()
    cursr.close()
    conct.close()
    
main()