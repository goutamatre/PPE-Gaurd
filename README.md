# PPE GUARD - PERSONAL PROTECTIVE EQUIPMENT DETECTION  
### AI-Powered Safety Compliance Monitoring System  

---

## Tech Stack
- Python 3.8+
- FastAPI 0.104+
- YOLOv8 (Ultralytics)
---

## 📝 About

**PPE Guard** is an intelligent Personal Protective Equipment detection system powered by the **YOLOv8** deep learning model. It automatically identifies whether individuals are wearing required safety gear including helmets, vests, gloves, boots, and face masks.

Suitable for:
- Construction sites  
- Industrial zones  
- Hazardous work environments  

### Benefits:
- Reduce human error in safety monitoring
- Ensure workplace safety compliance
- Provide instant alerts for missing equipment
- Generate safety compliance reports

---

## ✨ Features

### Core Functionality
- **Real-time Webcam Detection**
- **Image Upload Analysis**
- **High Accuracy YOLOv8 Detection**
- **Near Real-Time GPU/CPU Processing**
- **Confidence Scoring Display**

### User Experience
- Modern Glassmorphism UI
- Fully Responsive Design
- Download Annotated Results
- Privacy First (No external data sharing)

### Technical
- Custom-trained PPE model
- FastAPI Backend
- Adjustable thresholds (Confidence / IoU)
- REST API for easy integration

---

## 📸 Demo

Screenshots:
1. Homepage –
   ![WhatsApp Image 2025-11-05 at 19 28 25_2d0af806](https://github.com/user-attachments/assets/c75c9976-42e0-4300-af80-efbe61402a56)

   
2. Detection Results – Highlighted PPE items with confidence values
   ![WhatsApp Image 2025-11-05 at 19 32 34_bcbe7b3d](https://github.com/user-attachments/assets/cf7cf82e-5e93-4f1b-a9fb-7fc07a1b3483)
  ![WhatsApp Image 2025-11-05 at 19 27 42_eef811b8](https://github.com/user-attachments/assets/0a3cdc9f-1f6f-4500-827c-21c14c75785f)


3. Webcam Detection – Live monitoring feed
   ![WhatsApp Image 2025-11-05 at 19 31 23_c9bcc6ba](https://github.com/user-attachments/assets/c1344b82-dce8-4f2e-a169-48a925532a20)


## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Webcam (optional)

### Installation


1. Clone repository
git clone https://github.com/your-username/ppe-guard.git
cd ppe-guard

2. Create and activate virtual environment
python -m venv myenv

Windows
myenv\Scripts\activate

macOS/Linux
source myenv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Add Trained Model
Download model:
[https://drive.google.com/uc?export=download&id=14jNk69dfp8qO7xJXiaFggttIzH_b6z1Q](https://drive.google.com/file/d/17YlqhMa3o_m1-BGyylcmq-FNNYOsYoHP/view?usp=drive_link)

Place as:
PPE-Guard/app/model.pt

5. Run Application
uvicorn app.main:app --reload

Visit: http://127.0.0.1:8000

🧪 Usage
# Image Upload Detection

1. Click Upload Image
2. Choose an image
3. View detection results & confidence
4. Download annotated image

# Live Webcam Detection

1. Click Live Webcam
2. Allow camera permissions
3. Start detection
4. Stop when finished

``` 
# 📂 Project Structure

PPE-GUARD/
├── app/
│   ├── main.py
│   ├── utils.py
│   ├── model.pt
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── index.html
│       └── webcam.html
├── requirements.txt
├── README.md
└── .gitignore
```
🛡 Supported PPE Classes

1. Safety Helmets
2. Safety Vests / High-Visibility Jackets
3. Safety Boots
4. Safety Gloves
4. Face Masks / Respirators

# 📦 Dependencies

1. FastAPI
2. YOLOv8 (Ultralytics)
3. OpenCV
4. Uvicorn
5. NumPy
6. Pillow
(See requirements.txt)

# 🔮 Future Enhancements

1. Mobile App Version
2. Docker Container Support
3. Cloud Deployment Guide
4. Multi-Camera Support
5. Video File Processing
6. PDF Safety Reports
7. Integration With Security Systems
