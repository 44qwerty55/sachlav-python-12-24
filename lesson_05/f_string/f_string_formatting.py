name = "Alexander"
surname = "Komanov"
age = 36

# formatted_string = "Hello " + name + " " + surname + "! My age is: " + str(age)

formatted_string = f"Hello {name} {surname}! My age is: {age}"
print(formatted_string)

BASE_URL = "https://www.reqres.in"
CASES_API = f"{BASE_URL}/cases"
USERS_API = f"{BASE_URL}/users"
USER_API = f"{BASE_URL}/users/{name}"