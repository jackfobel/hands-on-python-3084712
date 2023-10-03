NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

## Remember; :2 we start counting from the left, 2: we start counting from the right....

# Slice - Get names to the left of <=:2 (left of George is: John and Paul)
JOHN_PAUL = NAMES[:2]
#print(JOHN_PAUL)

# Slice - Get names to the right of 2:=> (right of Paul: George and Ringo )
GEORGE_RINGO = NAMES[2:]
#print(GEORGE_RINGO)

# ['Ringo', 'George', 'Paul', 'John']
REVERSE1 = NAMES[::-1]

# [start:stop:step]
# start at 2 from left = George, go forward 1 and stop = Ringo, take backwards -1 value = George
REVERSE2 = NAMES[2:1:-1]
#print(REVERSE2) # George

# skip every other.
EVERY_OTHER = NAMES[::2]
print(EVERY_OTHER)

#print(sum(AGES))
#print(min(AGES))
#print(max(AGES))
