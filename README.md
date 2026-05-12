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
