from fastapi import FastAPI, UploadFile, File
from ocr import extract_text

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open("temp_image.jpg", "wb") as f:
        f.write(contents)

    text = extract_text("temp_image.jpg")
    return {"extracted_text": text}
