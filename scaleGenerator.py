'''
20/4/2020
Bought a (digital) piano yesterday and thought it would be cool
to learn how scales work and then realised it was a pain to google them
everytime. Maybe this will be helpful?
It was easy to get the right notes but hard to make sure they follow
the music conventions of one of each note.
'''

import sys
db = 0
def debug(msg):
    if db == 1:
        print(msg)
# used to easily print unicode flat sign
flat = "♭"
# An ordering of the keys on the piano using sharps for black keys
keys = [
    "A",
    "A#",
    "B",
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#",
]

keys_with_sharps = {
    "A",
    "C",
    "D",
    "F",
    "G",
}
keys_with_flats = {
    "A",
    "B",
    "D",
    "E",
    "G",
}
def convert_sharp_to_flat(key):
    # Does the same thing but for debugging
    # This case will convert keys like B to Cflat (e.g. for Eflat minor)
    if key[0] not in keys_with_sharps:
        new_flat = keys[(keys.index(key)+1) % 12]
        new_flat += flat
        #error_close("You can't convert {} to a flat".format(key))
    else:
        # Go to the next key, since we must be a sharp to convert to a flat
        # The next key will be a normal key so we can just add the flat symbol
        new_flat = keys[(keys.index(key)+1) % 12]
        new_flat += flat
    #print("Converting {} to {}".format(key, new_flat))
    return new_flat

def error_close(msg):
    print(msg)
    print("=========EXITING========")
    sys.exit(1)

start_key = "C"
major_jumps = [2,2,1,2,2,2,1]
natural_minor_jumps = [2,1,2,2,1,2,2]

scale_types = {
    1: major_jumps,
    2: natural_minor_jumps,
}
try:
    type_of_scale = int(input('''
    Please enter the type of scale by number: 
    1: Major
    2: Minor
    More coming soon
    '''))
except:
    error_close("Not a valid number corresponding to scale type")
    
if type_of_scale not in scale_types:
    error_close("Not a valid number corresponding to scale type")
else:
    jumptype = scale_types[type_of_scale]

input_start_key = input("Please enter your start key (use @ for flats): ").upper()
# The actual key that will be printed, may move from a sharp to a flat etc
start_key = input_start_key
print("Start key is " + input_start_key)

# Invalid key entered. It wasn't a flat or sharp from A-G
if start_key not in keys:
    # Check that the first letter is in keys
    if start_key[0] in keys and start_key[1] in ['#','@']:
        debug("Found a non included sharp or flat, converting!")
        start_key_index = keys.index(input_start_key[0]) - 1
        start_key = keys[start_key_index]
    else:
        error_close("Start key {} not in keys".format(start_key))

# Holds the notes of the scale
scale_notes = []
# Keeps track of the relative position on the piano from A (A = 1)
cur_index = keys.index(start_key)

# The key that will be printed, may be changed from sharp to flat.
key = keys[cur_index]

# This means our program has converted an input flat to a sharp
# We must convert back
if key != input_start_key:
    key = convert_sharp_to_flat(key)

# The first key of the output printed outside the loop
print(key)

# Used to see if the next potential note will be unique from the last, 
# if not, we may have to convert to flat.
old_key = key
# Used to format nicely
format_space = " "

# A jump will be a number representing either a tone (2) or a semitone (1).
for jump in jumptype:
    # Make the jump but loop back to start after going through the whole octave
    cur_index = (cur_index + jump) % 12
    # Get the key based on the current index
    key = keys[cur_index]

    # All keys of a scale should be a unique letter so we convert default sharps to flats
    # If the the letter of the key is the same as the last letter (e.g. G, G# would go to G, A♭)
    if key[0] == old_key[0]:
        key = convert_sharp_to_flat(key)

    print(format_space + key)
    format_space += " "
    old_key = key



