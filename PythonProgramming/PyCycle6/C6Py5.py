class Time:
    def __init__(self, hour, minute, second):
        # Initialize private attributes
        self._hour = hour
        self._minute = minute
        self._second = second

    def __add__(self, other):
        # Overloading the + operator to add two Time objects
        total_seconds = (self._hour * 3600 + self._minute * 60 + self._second) + \
                        (other._hour * 3600 + other._minute * 60 + other._second)
        
        # Convert total seconds back to hours, minutes, and seconds
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        return Time(hours, minutes, seconds)

    def display_time(self):
        # Method to display time in a readable format
        print(f"Time: {self._hour:02}:{self._minute:02}:{self._second:02}")


# Getting user input for the first time object
print("Enter details for the first time (hour, minute, second):")
hour1 = int(input("Enter hour: "))
minute1 = int(input("Enter minute: "))
second1 = int(input("Enter second: "))
time1 = Time(hour1, minute1, second1)

# Getting user input for the second time object
print("\nEnter details for the second time (hour, minute, second):")
hour2 = int(input("Enter hour: "))
minute2 = int(input("Enter minute: "))
second2 = int(input("Enter second: "))
time2 = Time(hour2, minute2, second2)

# Adding the two times using overloaded + operator
sum_time = time1 + time2

# Displaying the times
print("\nTime 1:")
time1.display_time()

print("Time 2:")
time2.display_time()

print("Sum of Time 1 and Time 2:")
sum_time.display_time()
