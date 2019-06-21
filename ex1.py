print("Hello, World!")
print("Hello dear!")
lucky_number=input("What is your lucky number?")
food = input("What is your favourite food?")
my_name=input("What is your name?")
greeting = "Hello " + my_name

print(greeting)

favourite_place=input("Where would you most like to visit in the World?")
places_to_visit = ["Mexico", "Portugal", "Kenya", "Nepal", "New Zealand"]
places_to_visit.append(favourite_place)
print("Nice! "+favourite_place+" is awesome!")
print(places_to_visit[0] + " is Alice's No 1 place to visit. She will add " + favourite_place + " to her list of favourite places: ")

print(places_to_visit)
print("Alice looks forward to eating " + food + " with you on the " + lucky_number + " of the next month in " + favourite_place)
