import psycopg2

# Database connection
conct = psycopg2.connect(host="localhost", user="user1", password ="1234", port=5432, dbname="Comp3005Project")
cursr = conct.cursor()

# Function that does operations
def viewTable():
    """
    #Peforms Operation
    """
    print("Trying to print")
    cursr.execute("""SELECT * FROM administrativestaff""")
    for row in cursr.fetchall():
        print(row)
    print("\n")
        
print("Welcome to the Health and Fitness Management System!")
commands=""

# Choosing your role
print("Enter a number corresponding to your role.")
if (commands!= "q"):
    print("""Possible roles are:\n
          1. Member\n
          2. Trainer\n
          3. Admin Staff\n
          q (to quit)\n""")
    commands = input("Enter a command:")
    
    # Choosing a member operation
    if (commands == "1"):
        if (commands!= "q"):
            print("""Possible Member operations are:\n
            1. User Registration\n
            2. Profile Management\n
            3. Dashboard Display\n
            4. Schedule Management\n
            q (to quit)\n""")
            commands = input("Pick an operation:")
            
            # Choosing a user registration operation
            if (commands == "1"):
                if (commands!= "q"):
                    print("""Possible User registration operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
            
            # Choosing a profile operation
            elif (commands == "2"):                
                if (commands!= "q"):
                    print("""Possible Profile operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
    
            # Choosing a dashboard operation
            elif (commands == "3"):                
                if (commands!= "q"):
                    print("""Possible Dashboard operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
            
            # Choosing a schedule operation
            else:                
                if (commands!= "q"):
                    print("""Possible Schedule operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
                    
    # Choosing a trainer operation    
    elif (commands == "2"):
        if (commands!= "q"):
            print("""Possible Trainer operations are:\n
            1. Schedule Management\n
            2. Member Profile Viewing\n
            q (to quit)\n""")
            commands = input("Pick an operation:")
            
            # Choosing a schedule operation
            if (commands == "1"):
                if (commands!= "q"):
                    print("""Possible Schedule operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
            
            # Choosing a profile operation
            elif (commands == "2"):                
                if (commands!= "q"):
                    print("""Possible Profile operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
    
    # Choosing an admin staff operation    
    elif (commands == "3"):
        if (commands!= "q"):
            print("""Possible Admin Staff operations are:\n
            1. Room Booking Management\n
            2. Equipment Maintenance Monitoring\n
            3. Class Schedule Updating\n
            4. Billing and Payment Processing\n
            q (to quit)\n""")
            commands = input("Pick an operation:")

            # Choosing a room booking operation
            if (commands == "1"):
                if (commands!= "q"):
                    print("""Possible Room Booking operations are:\n
                    1. View Available Rooms\n
                    2. Book a new Room\n
                    q (to quit)\n""")
            
            # Choosing an equipment operation
            elif (commands == "2"):
                if (commands!= "q"):
                    print("""Possible Equipment Maintenance operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
            
            # Choosing a class operation
            elif (commands == "3"):                
                if (commands!= "q"):
                    print("""Possible Class Schedule operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
            
            # Choosing a billing operation
            else:
                if (commands!= "q"):
                    print("""Possible Billing operations are:\n
                    1. \n
                    2. \n
                    q (to quit)\n""")
                    
                    
conct.commit()
cursr.close()
conct.close()