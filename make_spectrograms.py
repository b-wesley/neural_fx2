import librosa
import matplotlib.pyplot as plt
import numpy as np



def get_spectrogram_old(note_str, print_stuff=True, save=False, log=True, base_path='/Users/brantwesley/Documents/School/computer_music/neural_fx/'):
    note_path =  base_path + 'nsynth-valid/audio/{}.wav'.format(note_str)
    sample_rate, samples = wav.read(note_path)

    wav_arr = np.array(samples, dtype=float)
    
    freqs, times, spect = spectrogram(samples, sample_rate)
    
    if log:
        spect = np.log(spect)
    
    if print_stuff:
        plt.pcolormesh(times, freqs, spect, shading='gouraud')
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.show()
        
    if save:
        np.save(base_path+'spectrograms_dry/{}_spect.npy'.format(note_str), spect)
        
    return freqs, times, spect


def get_spectrogram_new(note_str, save=False, base_path='/Users/brantwesley/Documents/School/computer_music/neural_fx/', audio_path='nsynth-valid/audio/', save_path='spectrograms_dry/'):
    print(note_str)
    note_path =  base_path + audio_path + "{}.wav".format(note_str)
    print("note path: {}".format(note_path))

    samples, sample_rate = librosa.load(note_path, sr=None)
    
    # regular spectrogram
    spect = librosa.stft(samples)
    #librosa.display.specshow(spect)
    
    # mel spectrogram
    sgram_mag, _ = librosa.magphase(spect)
    mel_scale_sgram = librosa.feature.melspectrogram(S=sgram_mag, sr=sample_rate)
    #librosa.display.specshow(mel_scale_sgram)
    
    # decibel spectrogram
    mel_sgram = librosa.amplitude_to_db(mel_scale_sgram, ref=np.min)
    #librosa.display.specshow(mel_sgram, sr=sample_rate, x_axis='time', y_axis='mel')
    #plt.colorbar(format='%+2.0f dB')
    
    if save:
        np.save(base_path+save_path+'{}_spect.npy'.format(note_str), mel_sgram)
    return mel_sgram

