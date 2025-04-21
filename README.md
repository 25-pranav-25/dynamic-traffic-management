# 🚦 Real-Time Traffic Density Estimation with YOLOv8 and Traffic Signal Simulation

This project demonstrates a real-time traffic density estimation system using a fine-tuned YOLOv8 model on top-view traffic images. The estimated density dynamically controls a simulated traffic signal using Python's Turtle module.

## 📌 Project Overview

- **Object Detection Model:** YOLOv8 (Ultralytics)
- **Dataset Used:** [Top-View Vehicle Detection Image Dataset](https://www.kaggle.com/datasets/farzadnekouei/top-view-vehicle-detection-image-dataset)
- **Training Platform:** Kaggle
- **Traffic Signal Simulation:** Turtle graphics
- **Purpose:** Detect vehicle density at an intersection and simulate traffic light behavior accordingly.

---

## 🧠 Key Features

- Fine-tuned YOLOv8 on a top-view traffic dataset.
- Real-time traffic density estimation and classification.
- Visual traffic light simulation based on vehicle count logic.
- Easy-to-run simulation file with your trained model.

---

## 🧾 Folder Structure

```
├── real-time-traffic-density-estimation-with-yolov8.ipynb  # Kaggle notebook
├── simulation_demo.py                                      # Traffic signal simulation with Turtle
├── yolov8n.pt                                       # Trained YOLOv8 model
└── some sample images and videos
```

---

## 📦 Dataset Details

We use the [Top-View Vehicle Detection Image Dataset](https://www.kaggle.com/datasets/farzadnekouei/top-view-vehicle-detection-image-dataset) available on Kaggle, which contains annotated images of vehicles.

---

## ⚙️ How to Run This Project

### 📍 Part 1: Training the YOLOv8 Model
(U can skip this step and directly download trained model from the repositry itself)

1. Open the notebook [`real-time-traffic-density-estimation-with-yolov8.ipynb`](https://www.kaggle.com/code/farzadnekouei/real-time-traffic-density-estimation-with-yolov8) on Kaggle.
2. Upload the dataset or attach it via Kaggle's "Add Data" option.
3. Make sure your `data.yaml` is correctly configured with paths and class names.
4. Run all cells. This will:
   - Load a pre-trained YOLOv8 model (`yolov8n.pt`).
   - Fine-tune it on your dataset.
   - Save the trained model in `/kaggle/working/runs/detect/train`.

### 📍 Part 2: Traffic Signal Simulation

1. Rename or move your trained model weights (`best.pt`) to your current working directory if needed.
2. Locally, run `simulation_demo.py`.
3. Make sure the line loading the model is updated:
   ```python
   model = YOLO('path to the model')
   ```
4. The Turtle window will open and simulate a traffic intersection based on the detected vehicle count from sample images.

---

## 🧠 Simulation Logic (simulation_demo.py)

- Images are passed to the trained YOLOv8 model.
- Detected vehicles are counted lane-wise.
- The lane with the highest vehicle count gets a green signal.
- Signals are updated dynamically in the Turtle simulation.

---

## ✅ Requirements

- Python 3.8+
- Ultralytics YOLOv8 (`pip install ultralytics`)
- OpenCV (`pip install opencv-python`)
- Turtle (built-in with Python)
- Matplotlib, PyYAML, Pandas

---

## 🚀 Future Enhancements

- Add emergency vehicle detection.
- Deploy with live camera feed instead of static images.
- Create a web-based dashboard for traffic stats.
- Add real-time video inference for multi-lane control.


---
