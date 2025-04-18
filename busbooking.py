#CODE FOR BOOKING OF SEATS (ONE AT A TIME)

# function which displays the number of seats available.
def view_seats(seats):
    for seat in range(0,len(seats) ) :
        if seats[seat] != 0:
            print(f"seat no-{seat + 1} is available")

# function which is used to book the tickets.
def book_ticket(seats,Traveler):
    print("\n\t\tBELOW ARE THE AVAILABLE SEATS FOR BOOKING..\n")
    view_seats(seats)
    userSeat_choice = int(input("enter the seat you want to book ?"))
    if userSeat_choice > len(seats) or userSeat_choice < 0:
        print("Please enter a valid seat number")  
    elif seats[userSeat_choice  -1] == 0:
        print("--------The seat is booked,Please try booking a differet seat.--------")
    elif seats[userSeat_choice -1 ] != 0:
        seats[userSeat_choice  -1] = 0
        Traveler = {
            "Name" : input("Enter your name : "),
            "Age" : int(input("Enter your age : ")),
            "Destination" : input("Enter your destination : "),
            "Seat-No" : userSeat_choice
        }
        list_of_passengers.append(Traveler)
# function which is used to display all the booked information of each passengers.
def display_status(list_of_passengers):
    for passenger in list_of_passengers:
            print(f"HERE ARE THE DEATAILS FOR PASSENGER-NO {list_of_passengers.index(passenger) + 1}")
            print("NAME : " ,passenger["Name"])
            print("AGE : " ,passenger['Age'])
            print(f"DESTINATION : " ,passenger["Destination"])
            print(f"SEAT_NUMBER : " ,passenger["Seat-No"]) 
            print("")

choice = True
seats = [1,1,1,1,1,1,1,1,1,1]
list_of_passengers = []
Traveler = {}
while choice:
 print("\t\t-----WELCOME DEAR USER-----\n\t\tCHOOSE AN OPTION TO CONTINUE \n1-BOOK TICKET \n2-DISPLAY STATUS \n3-EXIT")
 booking_choice = int(input("ENTER YOUR CHOICE (1-3)?"))
 print("\n")
 match booking_choice:
     case 1:
         book_ticket(seats,Traveler)
     
     case 2:
         display_status(list_of_passengers)

     case 3:
         print("DO YOU WANT TO EXIT ?")
         
 choice = int(input("DO YOU WANT TO CONTINUE ((0 FOR NO) OR (1 FOR YES)) ?"))
print("\t\tTHANKS FOR CHOOSING US\n\t\tHAVE A SAFE JOURNEY.")



