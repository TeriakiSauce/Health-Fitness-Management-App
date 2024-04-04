import psycopg2

# Database connection
#conct = psycopg2.connect(host="", user="", password ="", port=, dbname="")
#cursr = conct.cursor()

    # Function that does operations
    #def sampleFunction():
        #"""
        #Peforms Operation
        #"""
        #cursr.execute("""""")
        #for row in cursr.fetchall():
        #    print(row)
print("Welcome to a Database Management System")
commands=""
print("Enter a number corresponding to your role")
while(commands!= "q"):
    print("""Possible roles are:\n
          1. Member\n
          2. Trainer\n
          3. Admin Staff\n
          q (to quit)\n""")
    commands = input("Enter a command:")
    
    if (commands == "1"):
        #sampleFunction()
        while(commands!= "q"):
            print("""Possible Member operations are:\n
            1. User Registration\n
            2. Profile Management\n
            3. Dashboard Display\n
            4. Schedule Management\n
            q (to quit)\n""")
            commands = input("Pick an operation:")
        
    elif (commands == "2"):
        #sampleFunction()
        while(commands!= "q"):
            print("""Possible Trainer operations are:\n
            1. Schedule Management\n
            2. Member Profile Viewing\n
            q (to quit)\n""")
            commands = input("Pick an operation:")
        
    elif (commands == "3"):
        #sampleFunction()
        while(commands!= "q"):
            print("""Possible Admin Staff operations are:\n
            1. Room Booking Management\n
            2. Equipment Maintenance Monitoring\n
            3. Class Schedule Updating\n
            4. Billing and Payment Processing\n
            q (to quit)\n""")
            commands = input("Pick an operation:")
      
#conct.commit()
#cursr.close()
#conct.close()