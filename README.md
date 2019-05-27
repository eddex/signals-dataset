# Signals Dataset

This dataset is used to traing a YOLOv3 object detector on signals with different colors and numbers on them.

used for https://github.com/eddex/pren2

## the data

There are 37 different signals.

- 9 Number signals with white font and black background on a high pole (info-signals)
- 9 Number signals with black font and white background on a high pole (info-signals)
- 9 Number signals with white font and black background on a low pole (stop-signals)
- 9 Number signals with black font and white background on a low pole (stop-signals)
- 1 start signal: blue and white striped signal on high pole

## how the data has been collected

- The train was set to full speed (7) and slow driving (2) while taking images.
- The signals have been spilt to 2 sets because not all could fit on the track at the same time.
- Batches of 1000 images have been taken while driving.
- The signals positions were (sometimes) shuffled between batches.
- Images without any signals have been deleted afterwards.

Does this look like a scientific approach on collecting data? 
*WARNING*: The answer might be shocking!

### first set of signals

**signals**
- info white: 2, 4, 5, 6, 8
- info black: 6, 7, 8
- stop white: 1, 3, 4, 5, 6, 7, 9
- stop black: 1, 3, 4, 6, 7, 8, 9
- start

**collected data**
- batch 0 - 999: speed 7
- batch 1000 - 1999: speed 2
- signals shuffled
- batch 2000 - 2999: speed 7
- batch 3000 - 3999: speed 2

### second set of signals

**signals**
- info white: 1, 3, 7, 9
- info black: 1, 2, 3, 4, 5, 9
- stop white: 2, 8
- stop black: 5
- start

**collected data**
- batch 4000 - 4999: speed 7
- signals shuffled
- batch 5000 - 5999: speed 2
- signals shuffled
- batch 6000 - 6999: speed 7
- signals shuffled
- batch 7000 - 7999: speed 2

### third set of signal(s)

**signal(s)**
- stop black: 2

> Because I missed this one...

The signal has been placed in different positions between and during the 4 rounds.

- batch 8000 - 8999: speed 7
- batch 9000 - 9999: speed 2
- batch 10000 - 10999: speed 7
- batch 11000 - 11999: speed 2