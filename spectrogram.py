from scipy.io import wavfile
import matplotlib.pyplot as plt
import os

def main():
    file_list = os.scandir('not_hammerons')
    print(file_list)
    for i, filename in enumerate(file_list):
        plt.rcParams['figure.figsize'] = [3.0, 3.0]
        plt.rcParams['figure.autolayout'] = True
        Fs, aud = wavfile.read(filename)
        aud = aud[:,0]
        plt.specgram(aud, Fs=Fs)
        plt.axis(False)
        plt.savefig(f'false-first-iter/false-classical-{i}.png')

if __name__ == "__main__":
    main()