greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

# First way of doing it.
name = "John"
intrupution = f"Hello {name}"

# Second way of doing it.
greet_format = "Hello {}"
formatted = greet_format.format(name)

# Just print both ways.
print(intrupution, formatted)

# Other extension methods?
print(formatted.upper())
print(formatted.lower())

print(formatted.replace("John", "testing"))
