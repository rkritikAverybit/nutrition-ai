from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import uvicorn

app = FastAPI(title="Nutrition AI API", description="API for food scanning and nutritional analysis")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Nutrition AI API"}

@app.post("/analyze")
async def analyze_food(image: UploadFile = File(...)):
    """Analyze food image and return nutritional information"""
    try:
        # TODO: Implement image analysis logic
        return {
            "status": "success",
            "message": "Image analysis functionality coming soon",
            "filename": image.filename
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)