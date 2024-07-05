from fastapi import FastAPI, UploadFile
import os
import uuid

app = FastAPI()

UPLOADS_FOLDER = "uploads"

@app.get("/")
async def home():
    return {"message": "Welcome to Docker tutorial on volume"}

@app.get("/list-files/")
async def list_files():
    try:
        files = os.listdir(UPLOADS_FOLDER)
        return {"files": files}
    except Exception as e:
        return {"message": f"Error while loading files: {str(e)}"}

@app.post("/upload-file")
async def upload_file(file: UploadFile):
    try:
        filename = file.filename
        file_extension = filename.split(".")[1]
        filepath = os.path.join(UPLOADS_FOLDER, f"{str(uuid.uuid4())}.{file_extension}")

        with open(filepath, "wb") as f:
            f.write(file.file.read())

        return {"message": "File uploaded successfully"}
    
    except Exception as e:
        return {"message": f"Error uploading file: {str(e)}"}
