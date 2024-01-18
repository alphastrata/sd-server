from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import logging
from diffusers import AutoPipelineForText2Image
import torch
import io

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Initialize FastAPI app
app = FastAPI()

# Load the SDXL Turbo model
pipeline_text2image = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sdxl-turbo", 
    torch_dtype=torch.float16, 
    variant="fp16"
)
pipeline_text2image = pipeline_text2image.to("cuda")

@app.get("/sdxl/api/{prompt}")
async def generate_image(prompt: str):
    logging.info(f"Received prompt: {prompt}")  # Log the received prompt
    try:
        # Generate the image
        image = pipeline_text2image(prompt=prompt, guidance_scale=0.0, num_inference_steps=1).images[0]

        # Convert image to bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Return the image as a response
        return StreamingResponse(io.BytesIO(img_byte_arr), media_type="image/png")
    except Exception as e:
        logging.error(f"Error generating image: {e}")
        raise HTTPException(status_code=500, detail="Error generating image")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9201)
