from pedalboard import Pedalboard, Reverb
from pedalboard.io import AudioFile
import os
import time

# input and output locations
input_directory = './audio'
output_directory = './output'

# Make a Pedalboard object, containing multiple plugins:
board = Pedalboard([Reverb(room_size=0.5)])

start = time.time()

for filename in os.listdir(input_directory):
    file = os.path.join(input_directory, filename)
    # checking if it is a wav file
    if file.endswith('.wav'):
      print('Converting: ' + file)
      # Read in a whole audio file:
      with AudioFile(file, 'r') as f:
        audio = f.read(f.frames)
        samplerate = f.samplerate

      # Run the audio through this pedalboard
      effected = board(audio, samplerate)

      trimmed_filename = file.replace(input_directory + '/', '')
      trimmed_filename = trimmed_filename.replace('.wav', '')

      # Write the audio back as a wav file into the output directory:
      with AudioFile(output_directory + '/' + trimmed_filename + '_reverb' + '.wav', 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)

end = time.time()

time_elapsed = end - start
print('Completed in ' + str(time_elapsed) + ' seconds.\n')