from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = content.decode("utf-8")  
        
        if not text.strip():
            return {"error": "Empty file or unreadable content"}

      
        total_messages = text.count("\n")
        total_words = sum(len(line.split()) for line in text.split("\n"))
        
        return {
            "filename": file.filename,
            "total_messages": total_messages,
            "total_words": total_words
        }
    except Exception as e:
        return {"error": f"Failed to process file: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
