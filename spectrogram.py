from scipy.io import wavfile
import matplotlib.pyplot as plt
import sys
import os

def main():
    if len(sys.argv) != 4:
        print("Usage: spectrogram /source_dir /target_dir <filename>")
        return 1
    if not os.path.isdir(sys.argv[1]) or not os.path.isdir(sys.argv[2]):
        print("Arguments supplied must be: DIR DIR STR")
        return 1

    source = sys.argv[1]
    target = sys.argv[2]
    specname = sys.argv[3]

    file_list = os.scandir(source)
    print(file_list)
    for i, filename in enumerate(file_list):
        plt.rcParams['figure.figsize'] = [3.0, 3.0]
        plt.rcParams['figure.autolayout'] = True
        Fs, aud = wavfile.read(filename)
        aud = aud[:,0]
        plt.specgram(aud, Fs=Fs)
        plt.axis(False)
        plt.savefig(f'{target}/{specname}-{i}.png')

if __name__ == "__main__":
    main()
