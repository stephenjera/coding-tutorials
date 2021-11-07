import os

notes_to_frequency = {
  "D4": 293.66,
  "D#4": 311.13,
  "E4": 329.63,
  "F4": 349.23,
  "F#4": 369.99,
  "G4": 392.00,
  "G#4": 415.30,
  "A4": 440.00,
  "A#4": 466.16,
  "B4": 493.88,
  "C5": 523.25,
  "C#5": 554.37,
  "D5": 587.33,
  "D#5": 622.25,
  "E5": 659.25,
  "F5": 698.46,
  "F#5": 739.99,
  "G5": 783.99,
  "G#5": 830.61,
  "A5": 880.00,
  "A#5": 932.33,
  "B5": 987.77,
  "C6": 1046.50,
  "C#6": 1108.73,
  "D6": 1174.66,
  "D#6": 1244.51,
  "E6": 1318.51,
}



directory = "Simulated_Dataset"

# Parent Directory path
parent_dir = "working_with_files"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
is_dir = os.path.isdir(directory)
print(path)
# print(is_dir)
if not os.path.exists(path):
    os.mkdir(path)
    print("Directory '% s' created" % directory)
else:
    print(directory + " is already a directory")

for key, value in notes_to_frequency.items():
    # create notes directory
    note_path = os.path.join(path, key)
    is_dir = os.path.isfile(note_path)
    # print(is_dir)
    if not os.path.exists(note_path):
        os.mkdir(note_path)
        print("Directory '% s' created" % key)
    else:
        print(key + " is already a directory")

