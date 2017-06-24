print('Welcome to the Mad Lib Generator!\n')

adjective1 = raw_input('Type in an adjective: ')
adjective2 = raw_input('Another adjective: ')
adjective3 = raw_input('And another adjective: ')
adjective4 = raw_input('One more adjective: ')

plural_animal = raw_input('Plural animal (e.g., puppies): ')
verb = raw_input('Now a verb: ')
plural_noun = raw_input('Now a plural noun: ')

name = raw_input('The first name of a woman musician: ')
beverage = raw_input('A beverage: ')
plural_body_part = raw_input('And finally, a plural body part: ')

# adjective1 = 'fearless'
# adjective2 = 'gooey'
# adjective3 = 'sassy'
# adjective4 = 'fancy'
# plural_animal = 'elephants'
# verb = 'skip'
# plural_noun = 'marbles'
# name = 'Ani'
# beverage = 'chocolate milk'
# plural_body_part = 'knees'

print("\nExcellent choices! Here's your story...")
print("--------------------------------")
print("There once was a " + adjective1 + " programmer named " + name)
print("who wanted to build a " + adjective2 + " mobile app to ")
print("help " + adjective3 + " " + plural_animal + " find new homes.")
print("")
print(name + " stayed up all night, drinking lots of ")
print("caffeinated " + beverage + " as she worked and worked")
print("trying to complete her " + adjective4 + " program.")
print("")
print("Whenever " + name + " hit a dead end, she would")
print("exclaim *" + plural_noun + "*!")
print("")
print("But she was not discouraged, and after a quick break ")
print("to " + verb + " and clear her head, she got back to work.")
print("")
print("By morning, when the sun started to rise, she let out a")
print("big yawn and stretched her " + plural_body_part + ".")
print("Finally, she was done. ")
print("--------------------------------")
