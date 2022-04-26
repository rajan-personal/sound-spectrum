# for data transformation 
import numpy as np 
# for visualizing the data 
import matplotlib.pyplot as plt 
# for opening the media file 
import scipy.io.wavfile as wavfile


Fs, aud = wavfile.read('drum.wav') 
aud = aud[:,0] # select left channel only
first = aud[:int(Fs*20)] # trim the first 125 seconds

powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
# plt.show()

print("powerSpectrum", len(powerSpectrum), len(powerSpectrum[0]), powerSpectrum)
print("frequenciesFound", len(frequenciesFound), frequenciesFound)
print("time", len(time), time)
print("imageAxis", imageAxis)


def powerSpectrumParser(t):
    return [int(i[t]) for i in powerSpectrum]

import csv

# open the file in the write mode
f = open('csv_file.csv', 'w')

# create the csv writer
writer = csv.writer(f)

writer.writerow([0.000000] + [int(i) for i in frequenciesFound])
# write a row to the csv file
count = 0
for t in range(len(time)):
    count += 1
    if count%5 ==0:
        writer.writerow([round(time[t],3)]+ powerSpectrumParser(t))
f.close()
