import random
import datetime

themes = [
    "Arab calligraphy fusion",
    "Chinese ink landscapes",
    "Wild West USA mythic scenes",
    "Latin American textile motifs",
    "Mexican mural-style abstracts",
    "Pacific Island tribal patterns",
    "African mask-inspired geometry",
    "Southeast Asian temple overlays"
]

def generate_nft_metadata():
    theme = random.choice(themes)
    timestamp = datetime.datetime.utcnow().isoformat()
    metadata = {
        "name": f"{theme} NFT - {timestamp}",
        "description": f"A cultural NFT inspired by {theme}",
        "image": f"https://your-image-generator.com/{theme.replace(' ', '_')}.png",
        "attributes": [{"trait_type": "Culture", "value": theme}]
    }
    print("Generated NFT:", metadata)
    return metadata

if __name__ == "__main__":
    generate_nft_metadata()
