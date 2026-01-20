import wave
import numpy as np
import struct

def wavToFloat(wave_file):
    w = wave.open(wave_file)
    astr = w.readframes(w.getnframes())

    # convert binary chunks to short
    a = struct.unpack("%ih" % (w.getnframes() * w.getnchannels()), astr)

    a = [float(val) / np.log(2) for val in a]
    # a = [float(val) for val in a]

    return a


def writeSignal(signal):
    outputFile = open('./data/generated/signal.txt', 'w')

    for dataPoint in signal:
        outputFile.write(f'{dataPoint}\n')

    outputFile.close()


def main():
    signal = wavToFloat(r'/home/volt/code/filter-coffee/data/raw/raw-input.wav')

    signalLength = len(signal)

    print("# Frames Read:", len(signal))
    print(f"Range of Values: [{str(min(signal))}, {str(max(signal))}]")
    print(type(signal))

    writeSignal(signalLength)

    print("Generated signal written to output file!")

if __name__ == '__main__':
    main()
