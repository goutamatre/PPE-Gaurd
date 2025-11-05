from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, StreamingResponse, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import io
import torch
from ultralytics import YOLO
from app.utils import read_imagefile, draw_detections, image_to_bytes


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Mount static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Load YOLO model
model = YOLO("app/model.pt")

# Template renderer
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Validate file
        if not file.filename:
            return Response(content="No file provided", status_code=400)
        
        # Check file type
        allowed_types = ["image/jpeg", "image/jpg", "image/png"]
        if file.content_type not in allowed_types:
            return Response(content="Invalid file type. Only JPG, PNG, JPEG allowed.", status_code=400)
        
        # Read image
        contents = await file.read()
        image = read_imagefile(contents)
        
        if image is None:
            return Response(content="Failed to decode image", status_code=400)
        
        # Run inference with confidence threshold
        results = model(image, conf=0.5, iou=0.45, stream=False)[0]
        
        # Draw detections
        annotated = draw_detections(image, results)
        
        # Convert to bytes
        image_bytes = image_to_bytes(annotated)
        
        return Response(content=image_bytes, media_type="image/jpeg")
    
    except Exception as e:
        print(f"Error in prediction: {e}")
        import traceback
        traceback.print_exc()
        return Response(content=f"Error processing image: {str(e)}", status_code=500)



@app.get("/webcam", response_class=HTMLResponse)
def webcam_ui(request: Request):
    return templates.TemplateResponse("webcam.html", {"request": request})



@app.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": model is not None}
