"""
Configuration file for Space Music Visualizer
Contains color palettes and other visual settings
"""

# Color palette definitions
COLOR_PALETTES = {
    'warm': {
        'nebula_colors': [
            (0, 69, 255),      # Red orange
            (0, 140, 255),     # Dark orange
            (0, 215, 255),     # Gold
            (71, 99, 255),     # Tomato
            (122, 160, 255)    # Light salmon
        ],
        'cosmic_colors': {
            'bass': (0, 69, 255),      # Red orange
            'low_mid': (0, 140, 255),  # Dark orange
            'high_mid': (0, 215, 255), # Gold
            'treble': (255, 255, 255)  # White
        },
        'background_base': (5, 10, 20),  # Dark warm brown
        'text_color': (50, 200, 255)    # Warm yellow
    },
    
    'cool': {
        'nebula_colors': [
            (200, 100, 0),     # Deep blue
            (255, 150, 0),     # Light blue
            (255, 200, 100),   # Sky blue
            (200, 200, 0),     # Cyan
            (255, 200, 150)    # Light cyan
        ],
        'cosmic_colors': {
            'bass': (200, 100, 0),      # Deep blue
            'low_mid': (255, 150, 0),   # Light blue
            'high_mid': (255, 200, 100), # Sky blue
            'treble': (255, 255, 255)   # White
        },
        'background_base': (20, 10, 5),  # Dark cool blue
        'text_color': (255, 200, 100)   # Sky blue
    },
    
    'futuristic': {
        'nebula_colors': [
            (100, 255, 0),     # Bright green
            (200, 255, 100),   # Light green
            (255, 255, 0),     # Cyan
            (255, 100, 200),   # Purple
            (255, 100, 255)    # Magenta
        ],
        'cosmic_colors': {
            'bass': (100, 255, 0),      # Bright green
            'low_mid': (200, 255, 100), # Light green
            'high_mid': (255, 255, 0),  # Cyan
            'treble': (255, 255, 255)   # White
        },
        'background_base': (10, 20, 5),  # Dark green
        'text_color': (100, 255, 0)     # Bright green
    },
    
    'modern': {
        'nebula_colors': [
            (255, 144, 30),    # Dodger blue
            (180, 130, 70),    # Steel blue
            (237, 149, 100),   # Cornflower blue
            (235, 206, 135),   # Sky blue
            (222, 196, 176)    # Light steel blue
        ],
        'cosmic_colors': {
            'bass': (255, 144, 30),     # Dodger blue
            'low_mid': (180, 130, 70),  # Steel blue
            'high_mid': (237, 149, 100), # Cornflower blue
            'treble': (255, 255, 255)   # White
        },
        'background_base': (35, 25, 15), # Dark modern blue
        'text_color': (255, 144, 30)    # Dodger blue
    },
    
    'gothic': {
        'nebula_colors': [
            (130, 0, 75),      # Indigo
            (128, 0, 128),     # Purple
            (139, 0, 139),     # Dark magenta
            (139, 61, 72),     # Dark slate blue
            (205, 90, 106)     # Slate blue
        ],
        'cosmic_colors': {
            'bass': (130, 0, 75),       # Indigo
            'low_mid': (128, 0, 128),   # Purple
            'high_mid': (139, 0, 139),  # Dark magenta
            'treble': (255, 255, 255)   # White
        },
        'background_base': (15, 5, 10),  # Dark purple
        'text_color': (128, 0, 128)     # Purple
    },
    
    'rustic': {
        'nebula_colors': [
            (19, 69, 139),     # Saddle brown
            (45, 82, 160),     # Sienna
            (63, 133, 205),    # Peru
            (135, 184, 222),   # Burlywood
            (179, 222, 245)    # Wheat
        ],
        'cosmic_colors': {
            'bass': (19, 69, 139),      # Saddle brown
            'low_mid': (45, 82, 160),   # Sienna
            'high_mid': (63, 133, 205), # Peru
            'treble': (255, 255, 255)   # White
        },
        'background_base': (10, 15, 20), # Dark brown
        'text_color': (63, 133, 205)    # Peru
    },
    
    'metal': {
        'nebula_colors': [
            (105, 105, 105),   # Dim gray
            (128, 128, 128),   # Gray
            (169, 169, 169),   # Dark gray
            (192, 192, 192),   # Silver
            (211, 211, 211)    # Light gray
        ],
        'cosmic_colors': {
            'bass': (105, 105, 105),    # Dim gray
            'low_mid': (128, 128, 128), # Gray
            'high_mid': (169, 169, 169), # Dark gray
            'treble': (255, 255, 255)   # White
        },
        'background_base': (15, 15, 15), # Dark gray
        'text_color': (192, 192, 192)   # Silver
    },
    
    'steel': {
        'nebula_colors': [
            (180, 130, 70),    # Steel blue
            (237, 149, 100),   # Cornflower blue
            (235, 206, 135),   # Sky blue
            (222, 196, 176),   # Light steel blue
            (250, 230, 230)    # Lavender
        ],
        'cosmic_colors': {
            'bass': (180, 130, 70),     # Steel blue
            'low_mid': (237, 149, 100), # Cornflower blue
            'high_mid': (235, 206, 135), # Sky blue
            'treble': (255, 255, 255)   # White
        },
        'background_base': (30, 25, 20), # Dark steel
        'text_color': (235, 206, 135)   # Sky blue
    },
    
    'gold': {
        'nebula_colors': [
            (0, 215, 255),     # Gold
            (0, 223, 255),     # Golden yellow
            (7, 193, 255),     # Amber
            (0, 152, 255),     # Orange
            (34, 87, 255)      # Deep orange
        ],
        'cosmic_colors': {
            'bass': (0, 215, 255),      # Gold
            'low_mid': (0, 223, 255),   # Golden yellow
            'high_mid': (7, 193, 255),  # Amber
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 20, 25),  # Dark gold
        'text_color': (0, 215, 255)     # Gold
    },
    
    'silver': {
        'nebula_colors': [
            (192, 192, 192),   # Silver
            (211, 211, 211),   # Light gray
            (220, 220, 220),   # Gainsboro
            (230, 230, 230),   # Light gray
            (245, 245, 245)    # White smoke
        ],
        'cosmic_colors': {
            'bass': (192, 192, 192),    # Silver
            'low_mid': (211, 211, 211), # Light gray
            'high_mid': (220, 220, 220), # Gainsboro
            'treble': (255, 255, 255)   # White
        },
        'background_base': (20, 20, 20), # Dark gray
        'text_color': (192, 192, 192)   # Silver
    },
    
    'diamond': {
        'nebula_colors': [
            (255, 255, 255),   # White
            (255, 248, 240),   # Alice blue
            (250, 230, 230),   # Lavender
            (245, 240, 255),   # Lavender blush
            (255, 248, 248)    # Ghost white
        ],
        'cosmic_colors': {
            'bass': (255, 255, 255),    # White
            'low_mid': (255, 248, 240), # Alice blue
            'high_mid': (250, 230, 230), # Lavender
            'treble': (255, 255, 255)   # White
        },
        'background_base': (15, 10, 10), # Dark blue-gray
        'text_color': (255, 255, 255)   # White
    },
    
    'blood': {
        'nebula_colors': [
            (0, 0, 139),       # Dark red
            (34, 34, 178),     # Fire brick
            (60, 20, 220),     # Crimson
            (0, 0, 255),       # Red
            (0, 69, 255)       # Red orange
        ],
        'cosmic_colors': {
            'bass': (0, 0, 139),        # Dark red
            'low_mid': (34, 34, 178),   # Fire brick
            'high_mid': (60, 20, 220),  # Crimson
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 5, 20),   # Dark red
        'text_color': (60, 20, 220)     # Crimson
    },
    
    'sea': {
        'nebula_colors': [
            (0, 100, 0),       # Dark green
            (128, 128, 0),     # Teal
            (255, 191, 0),     # Deep sky blue
            (208, 224, 64),    # Turquoise
            (212, 255, 127)    # Aquamarine
        ],
        'cosmic_colors': {
            'bass': (0, 100, 0),        # Dark green
            'low_mid': (128, 128, 0),   # Teal
            'high_mid': (255, 191, 0),  # Deep sky blue
            'treble': (255, 255, 255)   # White
        },
        'background_base': (20, 15, 5),  # Dark sea blue
        'text_color': (255, 191, 0)     # Deep sky blue
    },
    
    'black-and-white': {
        'nebula_colors': [
            (64, 64, 64),      # Dark gray
            (128, 128, 128),   # Gray
            (192, 192, 192),   # Silver
            (224, 224, 224),   # Light gray
            (255, 255, 255)    # White
        ],
        'cosmic_colors': {
            'bass': (64, 64, 64),       # Dark gray
            'low_mid': (128, 128, 128), # Gray
            'high_mid': (192, 192, 192), # Silver
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 5, 5),    # Black
        'text_color': (255, 255, 255)   # White
    },
    
    'grays': {
        'nebula_colors': [
            (79, 79, 47),      # Dark slate gray
            (105, 105, 105),   # Dim gray
            (128, 128, 128),   # Gray
            (169, 169, 169),   # Dark gray
            (211, 211, 211)    # Light gray
        ],
        'cosmic_colors': {
            'bass': (79, 79, 47),       # Dark slate gray
            'low_mid': (105, 105, 105), # Dim gray
            'high_mid': (128, 128, 128), # Gray
            'treble': (255, 255, 255)   # White
        },
        'background_base': (15, 15, 15), # Dark gray
        'text_color': (169, 169, 169)   # Dark gray
    },
    
    'greens': {
        'nebula_colors': [
            (0, 100, 0),       # Dark green
            (0, 128, 0),       # Green
            (0, 255, 0),       # Lime
            (50, 205, 50),     # Lime green
            (144, 238, 144)    # Light green
        ],
        'cosmic_colors': {
            'bass': (0, 100, 0),        # Dark green
            'low_mid': (0, 128, 0),     # Green
            'high_mid': (0, 255, 0),    # Lime
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 20, 5),   # Dark green
        'text_color': (0, 255, 0)       # Lime
    },
    
    'purples': {
        'nebula_colors': [
            (75, 0, 130),      # Indigo
            (128, 0, 128),     # Purple
            (138, 43, 226),    # Blue violet
            (147, 112, 219),   # Medium slate blue
            (186, 85, 211)     # Medium orchid
        ],
        'cosmic_colors': {
            'bass': (75, 0, 130),       # Indigo
            'low_mid': (128, 0, 128),   # Purple
            'high_mid': (138, 43, 226), # Blue violet
            'treble': (255, 255, 255)   # White
        },
        'background_base': (10, 5, 20),  # Dark purple
        'text_color': (138, 43, 226)    # Blue violet
    },
    
    'yellows': {
        'nebula_colors': [
            (184, 134, 11),    # Dark goldenrod
            (255, 215, 0),     # Gold
            (255, 255, 0),     # Yellow
            (255, 255, 224),   # Light yellow
            (255, 250, 205)    # Lemon chiffon
        ],
        'cosmic_colors': {
            'bass': (184, 134, 11),     # Dark goldenrod
            'low_mid': (255, 215, 0),   # Gold
            'high_mid': (255, 255, 0),  # Yellow
            'treble': (255, 255, 255)   # White
        },
        'background_base': (20, 20, 5),  # Dark yellow-brown
        'text_color': (255, 255, 0)     # Yellow
    },
    
    'coral': {
        'nebula_colors': [
            (255, 127, 80),    # Coral
            (255, 99, 71),     # Tomato
            (255, 69, 0),      # Red orange
            (255, 160, 122),   # Light salmon
            (255, 192, 203)    # Pink
        ],
        'cosmic_colors': {
            'bass': (255, 127, 80),     # Coral
            'low_mid': (255, 99, 71),   # Tomato
            'high_mid': (255, 69, 0),   # Red orange
            'treble': (255, 255, 255)   # White
        },
        'background_base': (20, 10, 5),  # Dark coral
        'text_color': (255, 127, 80)    # Coral
    },
    
    'bright': {
        'nebula_colors': [
            (255, 0, 255),     # Magenta
            (0, 255, 255),     # Cyan
            (255, 255, 0),     # Yellow
            (0, 255, 0),       # Lime
            (255, 0, 0)        # Red
        ],
        'cosmic_colors': {
            'bass': (255, 0, 255),      # Magenta
            'low_mid': (0, 255, 255),   # Cyan
            'high_mid': (255, 255, 0),  # Yellow
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 5, 5),    # Black
        'text_color': (255, 255, 255)   # White
    },
    
    'strong': {
        'nebula_colors': [
            (139, 0, 0),       # Dark red
            (0, 0, 139),       # Dark blue
            (0, 100, 0),       # Dark green
            (128, 0, 128),     # Purple
            (255, 140, 0)      # Dark orange
        ],
        'cosmic_colors': {
            'bass': (139, 0, 0),        # Dark red
            'low_mid': (0, 0, 139),     # Dark blue
            'high_mid': (0, 100, 0),    # Dark green
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 5, 5),    # Black
        'text_color': (255, 255, 255)   # White
    }
}

# Default palette
DEFAULT_PALETTE = 'cool'

# Video settings
VIDEO_SETTINGS = {
    'fps': 30,
    'width': 1280,
    'height': 720,
    'codec': 'libx264',
    'audio_codec': 'aac'
}

# Visual settings
VISUAL_SETTINGS = {
    'num_stars': 200,
    'num_particles': 50,
    'num_cosmic_bars': 48,
    'max_planet_radius_ratio': 0.25,  # Max planet radius as fraction of smallest dimension
    'space_image_width': 200
}

def get_palette(palette_name):
    """
    Get a color palette by name
    
    Args:
        palette_name (str): Name of the palette to retrieve
        
    Returns:
        dict: Color palette configuration
        
    Raises:
        ValueError: If palette_name is not found
    """
    if palette_name not in COLOR_PALETTES:
        available_palettes = ', '.join(COLOR_PALETTES.keys())
        raise ValueError(f"Palette '{palette_name}' not found. Available palettes: {available_palettes}")
    
    return COLOR_PALETTES[palette_name]

def list_palettes():
    """
    List all available color palettes
    
    Returns:
        list: List of palette names
    """
    return list(COLOR_PALETTES.keys())

def get_default_palette():
    """
    Get the default color palette
    
    Returns:
        dict: Default color palette configuration
    """
    return get_palette(DEFAULT_PALETTE)
