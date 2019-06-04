# Signals Dataset

This dataset is used to traing a YOLOv3 object detector on signals with different colors and numbers on them.

used for https://github.com/eddex/pren2

## annotations

**bounding-boxes-digits**

Bounding boxes around digits, no distinction between different colors.

Total number of annotations: 540

class        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | start
-------------|---|---|---|---|---|---|---|---|---|---
annotations  | 32 | 18 | 63 | 81 | 62 | 68 | 113 | 60 | 31 | 12
distribution | 5.9% | 3.3% | 11.7% | 15.0% | 11.5% | 12.6% | 20.9% | 11.1% | 5.7% | 2.2%

**bounding-boxes-digits-infolks**

Bounding boxes around digits, no distinction between different colors. Annotation done by [INFOLKS](http://www.infolks.info/).

Total number of annotations: 5687

class        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | start
-------------|---|---|---|---|---|---|---|---|---|---
annotations  | 534 | 494 | 716 | 612 | 690 | 503 | 779 | 617 | 456 | 286
distribution | 9.4% | 8.7% | 12.6% | 10.8% | 12.1% | 8.8% | 13.7% | 10.8% | 8.0% | 5.0%

## the data

There are 37 different signals.

- 9 Number signals with white font and black background on a high pole (info-signals)
- 9 Number signals with black font and white background on a high pole (info-signals)
- 9 Number signals with white font and black background on a low pole (stop-signals)
- 9 Number signals with black font and white background on a low pole (stop-signals)
- 1 start signal: blue and white striped signal on high pole

## camera settings

```
camera = PiCamera()
camera.exposure_mode = 'off'
camera.resolution = (416, 416)
camera.brightness = 55
camera.framerate = 15
camera.shutter_speed = 3100
camera.rotation = 0
camera.iso = 1200
```

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
