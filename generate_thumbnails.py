#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create thumbnails directory if it doesn't exist
os.makedirs('assets/images/thumbnails', exist_ok=True)

# Define week titles and colors
weeks = [
    ("week01", "Reverse\nEngineering", "#c9a86a"),
    ("week03", "Selfie &\nIdentity", "#d9c79a"),
    ("week04", "Comic &\nStorytelling", "#b8aa8d"),
    ("week05", "GIF &\nRemix Culture", "#a89676"),
    ("week06", "Text &\nDistant Reading", "#9b8860"),
    ("week07", "Mapping AI\nWorlds", "#8e7a4a"),
    ("week08", "Networks of\nKnowledge", "#816c34"),
    ("week09", "Bots &\nGenerators", "#7a5c1e"),
    ("week10", "Games &\nPlay", "#c9a86a"),
    ("week11", "AI &\nLabor", "#d9c79a"),
    ("week12", "AI &\nEcology", "#b8aa8d"),
    ("week13", "Futures of AI\n& Humanity", "#a89676"),
]

# Create thumbnails
for week_id, title, color in weeks:
    img = Image.new('RGB', (200, 200), color=color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a decent font, fall back to default
    try:
        font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 18)
    except:
        font = ImageFont.load_default()
    
    # Draw text in center
    draw.text((100, 100), title, fill="#111214", font=font, anchor="mm", align="center")
    
    # Save thumbnail
    img.save(f'assets/images/thumbnails/{week_id}-thumb.jpg')
    print(f"✓ Created {week_id}-thumb.jpg")

print("All thumbnails generated!")
