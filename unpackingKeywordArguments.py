# It collects all named arguments & puts them into a dictionary
def named(**kwargs):
    print(kwargs)


def named2(name,age):
    print(name, age)

named(name="Bob",age=25)

details={"name":"Bob","age":25}
# Given as named arguments
named2(**details)