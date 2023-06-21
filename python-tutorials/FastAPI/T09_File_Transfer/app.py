import uvicorn
from uuid import uuid4
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/file")
async def file(file: UploadFile = File(...)):
    # Create a directory to store the uploaded files
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)

    # Create a target file path
    file_path = upload_dir / file.filename

    # Reject the new file if a file with the same name already exists
    if file_path.exists():
        raise HTTPException(status_code=400, detail="A file with the same name already exists. Please rename the file and try again.")

    # Save the uploaded file to the target file path
    with file_path.open("wb") as buffer:
        buffer.write(file.file.read())

    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run("app:app", reload=False, port=3000)
