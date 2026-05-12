# ESP32 AI Camera Web Server

An embedded computer vision project using an **ESP32 Wrover camera**, a **web streaming interface**, and an **Edge Impulse image classification model** to recognize everyday objects in real time.

This project combines live video streaming, on-device AI classification, custom dataset collection, and deployment of a trained machine learning model on an ESP32 camera module.

## Demo

[Watch the project demo on YouTube](https://youtube.com/shorts/_FmC6DXuqRQ?feature=share)

## Project Overview

The goal of this project was to build a small AI camera system capable of recognizing objects directly from an ESP32 camera.

The system can:

- stream the camera feed through a local web server
- capture images using the ESP32 camera
- classify objects using an Edge Impulse model
- run predictions directly on the ESP32
- display prediction results through the Serial Monitor

The final model was trained to classify five classes:

- apple
- orange
- cucumber
- manette
- background

## Features

- Live ESP32 camera stream in a browser
- Real-time object classification
- Edge Impulse image classification model
- Python script for automatic dataset collection
- Static IP configuration for stable local access
- On-device inference using an ESP32 camera board
- Lightweight embedded AI pipeline

## Hardware Used

- ESP32 Wrover Module
- ESP32 camera
- USB cable
- WiFi network
- Objects used for testing:
  - apple
  - orange
  - cucumber
  - controller

## Software Used

- Arduino IDE
- Edge Impulse
- Python 3
- ESP32 Arduino board package
- ESP32 Camera WebServer example

## Repository Structure

```text
ESP32-AI-Camera-WebServer/
│
├── arduino/
│   └── CameraWebServer_AI/
│       ├── CameraWebServer.ino
│       ├── app_httpd.cpp
│       ├── board_config.h
│       ├── camera_index.h
│       ├── camera_pins.h
│       ├── ci.yml
│       └── partitions.csv
│
├── python/
│   └── capture_esp32.py
│
├── media/
│   └── demo-link.txt
│
├── README.md
├── .gitignore
└── LICENSE
```

## How It Works

### 1. Camera Stream

The ESP32 hosts a local web server that allows the user to view the camera stream from a browser.

Example local address:

```text
http://10.0.0.150
```

### 2. Dataset Collection

A Python script was used to collect training images directly from the ESP32 camera endpoint.

The script sends requests to:

```text
http://10.0.0.150/capture
```

and saves the images into folders based on their class label.

### 3. Model Training

The dataset was uploaded to Edge Impulse.

The model was trained as an image classification model using images from five classes:

```text
apple
orange
cucumber
manette
background
```

The image input size used was:

```text
96 x 96
```

The model was exported as a quantized int8 Arduino library.

### 4. ESP32 Deployment

The exported Edge Impulse Arduino library was installed in Arduino IDE and integrated into the ESP32 camera web server code.

The ESP32 runs the camera stream and AI classification together. The stream is available in the browser, while predictions are printed in the Serial Monitor.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AbderrahmaneErraqabi/ESP32-AI-Camera-WebServer.git
```

### 2. Open the Arduino Project

Open this file in Arduino IDE:

```text
arduino/CameraWebServer_AI/CameraWebServer.ino
```

### 3. Install ESP32 Board Support

In Arduino IDE, install the ESP32 board package if it is not already installed.

Then select:

```text
ESP32 Wrover Module
```

### 4. Install the Edge Impulse Arduino Library

Export your trained Edge Impulse model as an Arduino library.

In Arduino IDE:

```text
Sketch → Include Library → Add .ZIP Library
```

Then select the exported Edge Impulse ZIP file.

### 5. Add WiFi Credentials

In `CameraWebServer.ino`, replace the placeholders with your own WiFi information:

```cpp
const char *ssid = "YOUR_WIFI_NAME";
const char *password = "YOUR_WIFI_PASSWORD";
```

Do not upload real WiFi credentials to GitHub.

### 6. Upload the Code

Connect the ESP32 camera board to your computer and upload the sketch.

### 7. Open the Serial Monitor

Use:

```text
115200 baud
```

The ESP32 should print the local IP address for the camera stream.

Example:

```text
Camera Ready! Use 'http://10.0.0.150' to connect
```

## Python Dataset Capture Script

The Python script is located here:

```text
python/capture_esp32.py
```

It was used to collect images from the ESP32 camera.

Run it with:

```bash
python capture_esp32.py
```

The script asks for:

- class name
- number of images to capture
- delay between each image

It then saves the captured images into a local dataset folder.

## Dataset

The full dataset is not included in this repository because it contains several thousand images.

The dataset was collected manually using the ESP32 camera and included different:

- lighting conditions
- object angles
- object distances
- backgrounds
- hand positions
- empty background scenes

The background class was important because it helped the model learn when no target object was present.

## Model Information

The model was trained using Edge Impulse.

Main model settings:

```text
Model type: Image classification
Input size: 96 x 96
Resize mode: Squash
Deployment: Arduino Library
Optimization: Quantized int8
```

Classes:

```text
apple
orange
cucumber
manette
background
```

## Results

The project successfully demonstrated an end-to-end embedded AI pipeline:

- dataset collection from the ESP32 camera
- training an image classification model
- deploying the model to a microcontroller
- running real-time predictions
- streaming live video through a web interface

The final demo showed the ESP32 recognizing multiple objects in front of the camera.

## License

This project is shared for educational and portfolio purposes.
