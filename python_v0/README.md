**DIP Fundamentals**

**What is DIP**

**How Do We Obtain A DI**

**Sample and Quantization**

**Generation of A DI**

**Various Spatial Resolutions**

**Block Arifacts**

**Various Quantization Levels**

**False Contours**

**Aliasing Error**

**Coordinate Systems**

**Neighbors of A Pixel**

**Three Types of Connectivity**

**Distance Measures**

**Sampling Theorem**

**Exercise 1**
- Plot three 7 by 7 matrices by letting each element denote the distance from the element in the center.Three matrices are obtained based on the Euclidean distance, D4 distance, and D8 distance, respectively.

**Assignment from Chapter 1**
1. Obtain a digital image of your face.
2. Change the spatial resolution of it, and comment on the results. (See Chap1_1.m)
3. Change the number of gray levels, and comment on the results. (See Chap1_2.m)
4. Obtain a digital image that shows aliasing error, and comment on it.

- [ ] checking type of image
- [ ] checking size of image
- [ ] size of image property storage

## การเล่นกับ DIP ในรูปเเบบต่างๆ
- [ ] create image
- [ ] check type of image
- [ ] check size of image
- [ ] size of image property storage

## เทคนิคต่างๆ ใน DIP(DIGITAL IMAGE PROCESSING)
- [ ] การปรับขนาดภาพ
- [ ] การเปลี่ยนรูปแบบภาพ
- [ ] การปรับความสว่างและความคมชัด

## Knowledge of DIP(DIGITAL IMAGE PROCESSING)
- [ ] Understand the basic concepts of digital images
- [ ] Learn about different image formats and their properties
- [ ] Explore image representation and storage
- [ ] Grayscale: 1 pixel = 1 byte = 1 channel (0-255)
  - [ ] 0 = black
  - [ ] 255 = white
- [ ] Color || RGB: 1 pixel = 3 bytes = 3 channels (RGB)
  - [ ] R: 0-255
  - [ ] G: 0-255
  - [ ] B: 0-255
- [ ] 0 = black, 255 = white (for mode 8-bit)
- [ ] size of image (width x height x channels)
  - [ ] **example**: 256 x 256 x 3 = 196608 bytes or 1572864 bit or 192 KB or 0.192 MB

## Practices create image with fundamental python libraries
- [ ] create image with pillow
- [ ] create image with numpy
- [ ] create image with cv2