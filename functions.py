# Function - Reusable collection of code that performs a particular task
foo = 'bar'

# Declare a function
def greet(name, age, country="Australia"):
    print(f'Hello, {name}! You are {age} years old.')
    print(f'{name} lives in {country}')


# Call the function. "Call" means "execute" or "run" the code in the function, then
# come back here when the function finishes
greet(age=52, name='Matt')

greet('Mary', 21, "New Zealand")
