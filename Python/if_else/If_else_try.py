print("Welcome to Rakki Theatre")
movie = input("Enter the movie name to book ticket")
movie_name = "coolie"
bill = 190
if movie == movie_name:
    print("Movie ticket available for coolie")
    age = int(input("Enter your Age"))
    if age >= 18:
        print("Tickets Available")
        ticket = int(input("Enter No. of tickets Required"))
        if ticket <= 1:
            amount = bill * ticket
            print(f"Tickets Booked total amount will be {amount}")
        elif ticket <=5:
            amount = bill * ticket
            print(f"tickets booked total amount will be  {amount}")
        elif ticket <=9:
            amount = bill * ticket
            print(f"tickets booked total amount will be  {amount}")
        else:
            print("Please tryagain something went wrong")
    else:
        print("You are under age.")
else:
    print("Movie Not available")
