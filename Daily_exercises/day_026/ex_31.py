sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split(' ')
print(words)

result = {word:len(word) for word in words}
print(result)