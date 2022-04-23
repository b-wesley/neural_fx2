# neural_fx
General Idea: 
- Use deep learning to generate envelopes for partials for oscillators to re-synthesize sounds

Workflow (just a broad, flexible skeleton rn):
- Load audio files into spectrograms
    - currently using regular scipy spectrograms
    - may be advantageous to switch librosa/mel spectrograms
    - also do some data augmentation
- Feed spectrograms into CNN for feature extraction/classification
- The new workflow:
    - Make wet versions of the data
        - prob just slap em in max or a daw and just make analagous files with whichever effect we're going for       
    - xs = dry spectrograms, ys = wet spectrograms
    - start w/autoencoder for encoder training first while working on getting the data together
    - then train encoder/decoder for the effects
    - make a max thing for demoing
        - maybe also for making the wet files, but idk anything about saving max ouputs
    
Backup Ideas:
- Essentially recreate the WaveNet style autoencoder outlined in [this Google paper](https://arxiv.org/pdf/1704.01279.pdf)
- pretty much does all the synthesis in neural net
    - I think it outputs spectrogram, we can inverse FFT it into an audio file
    - load into max, use other parameters to do some kind of stuff for demos, etc.
- Could also do something with deep-learning generated effects and compare them to their max counterparts
    - general effects like chorus, reverb, etc. or amp simulation