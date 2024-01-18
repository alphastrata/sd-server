#!/bin/bash

# Array of sample prompts
prompts=(
    "A cinematic shot of a baby racoon wearing an intricate Italian priest robe"
    "A futuristic city skyline at sunset"
    "A portrait of a robot playing chess in a medieval setting"
    "An astronaut riding a horse on the moon"
    "A landscape of a forest made of crystal"
    "A surreal painting of a cat with wings flying over mountains"
    "An underwater scene with mermaids and a sunken pirate ship"
		"A photo of a bedazzled mint green sports car"
    "A digital art of a cyberpunk marketplace"
    "A fantasy map of an unexplored island"
)

# Loop through the prompts and make curl requests
for i in {0..9}; do
	  # Replace spaces with '%20'
    encoded_prompt=$(echo "${prompts[i]}" | sed -e 's/ /%20/g')
    
    curl "http://localhost:9201/sdxl/api/${encoded_prompt}" -o "$i.png"
	
	  firefox $i.png
done

