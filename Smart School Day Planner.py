day=input("Enter the current day : ").strip().capitalize()
if day in("Saturday,Sunday"):
    print("Day Type: Weekend - Enjoy your free time !")
elif day=="Monday":
    print("Day Type: First day of the week.")
elif day=="Friday":
    print("Day Type: Last day of the school.")
elif day in("Tuesday","Wednesday","Thursday"):
    print("Day Type: Regular School Day.")
else:
    print("Day is not recognized.")


weather=input("What is the weather right now? (sunny/rainy/cloudy) : ").strip().lower()
homework=input("Is your homework done? (yes/no) : ").strip().lower()
if weather== "sunny" and homework=="yes":
    print("It's sunny outside and your homework is done so, you can do whatever you want. ")

if weather=="rainy" or "cloudy":
    print("Take an umbrella with you before heading out.")

if not (homework=="yes") and weather=="rainy":
    print("FINISH YOUR HOMEWORK")
elif weather=="sunny" and homework=="yes" and not (day in("Saturday,Sunday")):
    print("You are ready for tomorrow.")
          


