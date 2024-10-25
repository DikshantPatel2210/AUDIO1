import librosa
#import soundfile
import numpy as np
#123456789952

def open_audio_file(path: str, sample_rate=48000, offset=0.0, duration=None):
    a, sr = librosa.load(path, sr=sample_rate, mono=True, offset=offset, duration=duration)
    return a, sr

#def save_signal(data= a , samplerate= 4800):
#    data, samplerate = soundfile.read('/home/sarkar/Desktop/sci_camp/birdnet_mini/testdata/test_1min.wav')
#    soundfile.write()

def split_signal(signal: np.ndarray, rate: int, seconds: float, overlap:float, min_len:float) -> list[np.ndarray]:
    # signal = NumPy Array formate
    # rate = samplerate
    # seconds = desired length of the chunk
    # overlap = determined the overlapping of chunk. 
    # value is between 0.0(no overlapped) and 1.0(full overlapped)
    # min_len = the minimum length of the chunk
    
    chunk_size = int(seconds * rate)
    step_size = int(chunk_size * (1 - overlap))
    min_samples = int(min_len * rate)
    
    chunks = []
    for start in range(0, len(signal), step_size):
        end = start + chunk_size
        chunk = signal[start:end]
        
        if len(chunk) < min_samples:
            break
        
        chunks.append(chunk)
    
    return chunks

#def plotting_signal(filename:str, samplerate=48000):
#    plot = librosa.display.AdaptiveWaveplot(filename, sr=samplerate)
#    return plot