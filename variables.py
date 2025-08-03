x=15
price=9.99


discount=0.2

result=price*(1-discount)

print(result)


# Strings
name="Suresh"

print(name)

print(type(name))

names="Bob"
# f string allow you to embed variables in strings
greeting=f"Hello {name}"

print(greeting)


greeting="Hello , {}"
with_name=greeting.format(name)

longer_phrase="Today is {} & tomorrow is {}"

print(longer_phrase.format("Monday","Tuesday"))


