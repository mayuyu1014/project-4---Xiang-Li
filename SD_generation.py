import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler, AutoencoderKL
import io
import base64

images = []

def sd_generate(prompt, details, cues):

    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    print(device)
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to(device)
    generator = torch.Generator(device).manual_seed(7)

    negative_prompt = ""

    if (details):  
        #faster with scheduler 20 to 25 inference steps, default one is 50
        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        #buffer
        negative_prompt = "poorly drawn,cartoon, 2d, sketch, cartoon, drawing, anime, disfigured, bad art, deformed, extra limbs, close up, b&w, weird colors, blurry"

    if (cues):
        #better quality than the default one
        vae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse", torch_dtype=torch.float16).to(device)
        #responsible for encoding and decoding images into and from a latent space representation
        pipe.vae = vae
    
    prompt = prompt

    #details
    prompt += details
    #cues
    prompt += cues
    
    pipe.enable_attention_slicing()                                                                                                                                                                                           
                                                                                                                                                                                                                                                
    image = pipe(prompt, generator=generator, negative_prompt = negative_prompt, num_inference_steps=25).images[0]

    #transfer img data to html
    img_buffer = io.BytesIO()
    image.save(img_buffer, format="png")
    img_data = base64.b64encode(img_buffer.getvalue()).decode("utf-8")
    images.append(img_data)

    return images      