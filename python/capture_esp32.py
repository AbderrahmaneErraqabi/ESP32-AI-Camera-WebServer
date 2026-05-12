import urllib.request
import time
from pathlib import Path

ESP32_CAPTURE_URL = "http://10.0.0.150/capture"

label = input("Class name, example: orange, manette, apple, cucumber, background: ").strip()
count = int(input("How many images do you want to capture? ").strip())
delay = float(input("Delay between each image in seconds: ").strip())

folder = Path(__file__).parent / "dataset" / label
folder.mkdir(parents=True, exist_ok=True)

existing_images = list(folder.glob("*.jpg"))
start_index = len(existing_images)

print()
print(f"Capturing {count} images for class: {label}")
print("Move the object slowly during the capture.")
print()

for i in range(count):
    filename = folder / f"{label}_{start_index + i:04d}.jpg"

    try:
        with urllib.request.urlopen(ESP32_CAPTURE_URL, timeout=5) as response:
            image_data = response.read()

        with open(filename, "wb") as f:
            f.write(image_data)

        print(f"Saved image: {filename}")

    except Exception as e:
        print(f"Error on image {i}: {e}")

    time.sleep(delay)

print()
print("Done.")
