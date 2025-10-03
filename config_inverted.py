"""
Configuration file for Space Music Visualizer
Contains color palettes and other visual settings
"""

# Color palette definitions
COLOR_PALETTES = {
    'warm': {
        'nebula_colors': [
            (255, 69, 0),      # Red orange
            (255, 140, 0),     # Dark orange
            (255, 215, 0),     # Gold
            (255, 99, 71),     # Tomato
            (255, 160, 122)    # Light salmon
        ],
        'cosmic_colors': {
            'bass': (255, 69, 0),      # Red orange
            'low_mid': (255, 140, 0),  # Dark orange
            'high_mid': (255, 215, 0), # Gold
            'treble': (255, 255, 255)  # White
        },
        'background_base': (20, 10, 5),  # Dark warm brown
        'text_color': (255, 200, 50)    # Warm yellow
    },
    
    'cool': {
        'nebula_colors': [
            (0, 100, 200),     # Deep blue
            (0, 150, 255),     # Light blue
            (100, 200, 255),   # Sky blue
            (0, 200, 200),     # Cyan
            (150, 200, 255)    # Light cyan
        ],
        'cosmic_colors': {
            'bass': (0, 100, 200),      # Deep blue
            'low_mid': (0, 150, 255),   # Light blue
            'high_mid': (100, 200, 255), # Sky blue
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 10, 20),  # Dark cool blue
        'text_color': (100, 200, 255)   # Sky blue
    },
    
    'futuristic': {
        'nebula_colors': [
            (0, 255, 100),     # Bright green
            (100, 255, 200),   # Light green
            (0, 255, 255),     # Cyan
            (200, 100, 255),   # Purple
            (255, 100, 255)    # Magenta
        ],
        'cosmic_colors': {
            'bass': (0, 255, 100),      # Bright green
            'low_mid': (100, 255, 200), # Light green
            'high_mid': (0, 255, 255),  # Cyan
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 20, 10),  # Dark green
        'text_color': (0, 255, 100)     # Bright green
    },
    
    'modern': {
        'nebula_colors': [
            (30, 144, 255),    # Dodger blue
            (70, 130, 180),    # Steel blue
            (100, 149, 237),   # Cornflower blue
            (135, 206, 235),   # Sky blue
            (176, 196, 222)    # Light steel blue
        ],
        'cosmic_colors': {
            'bass': (30, 144, 255),     # Dodger blue
            'low_mid': (70, 130, 180),  # Steel blue
            'high_mid': (100, 149, 237), # Cornflower blue
            'treble': (255, 255, 255)   # White
        },
        'background_base': (15, 25, 35), # Dark modern blue
        'text_color': (30, 144, 255)    # Dodger blue
    },
    
    'gothic': {
        'nebula_colors': [
            (75, 0, 130),      # Indigo
            (128, 0, 128),     # Purple
            (139, 0, 139),     # Dark magenta
            (72, 61, 139),     # Dark slate blue
            (106, 90, 205)     # Slate blue
        ],
        'cosmic_colors': {
            'bass': (75, 0, 130),       # Indigo
            'low_mid': (128, 0, 128),   # Purple
            'high_mid': (139, 0, 139),  # Dark magenta
            'treble': (255, 255, 255)   # White
        },
        'background_base': (10, 5, 15),  # Dark purple
        'text_color': (128, 0, 128)     # Purple
    },
    
    'rustic': {
        'nebula_colors': [
            (139, 69, 19),     # Saddle brown
            (160, 82, 45),     # Sienna
            (205, 133, 63),    # Peru
            (222, 184, 135),   # Burlywood
            (245, 222, 179)    # Wheat
        ],
        'cosmic_colors': {
            'bass': (139, 69, 19),      # Saddle brown
            'low_mid': (160, 82, 45),   # Sienna
            'high_mid': (205, 133, 63), # Peru
            'treble': (255, 255, 255)   # White
        },
        'background_base': (20, 15, 10), # Dark brown
        'text_color': (205, 133, 63)    # Peru
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
            (70, 130, 180),    # Steel blue
            (100, 149, 237),   # Cornflower blue
            (135, 206, 235),   # Sky blue
            (176, 196, 222),   # Light steel blue
            (230, 230, 250)    # Lavender
        ],
        'cosmic_colors': {
            'bass': (70, 130, 180),     # Steel blue
            'low_mid': (100, 149, 237), # Cornflower blue
            'high_mid': (135, 206, 235), # Sky blue
            'treble': (255, 255, 255)   # White
        },
        'background_base': (20, 25, 30), # Dark steel
        'text_color': (135, 206, 235)   # Sky blue
    },
    
    'gold': {
        'nebula_colors': [
            (255, 215, 0),     # Gold
            (255, 223, 0),     # Golden yellow
            (255, 193, 7),     # Amber
            (255, 152, 0),     # Orange
            (255, 87, 34)      # Deep orange
        ],
        'cosmic_colors': {
            'bass': (255, 215, 0),      # Gold
            'low_mid': (255, 223, 0),   # Golden yellow
            'high_mid': (255, 193, 7),  # Amber
            'treble': (255, 255, 255)   # White
        },
        'background_base': (25, 20, 5),  # Dark gold
        'text_color': (255, 215, 0)     # Gold
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
            (240, 248, 255),   # Alice blue
            (230, 230, 250),   # Lavender
            (255, 240, 245),   # Lavender blush
            (248, 248, 255)    # Ghost white
        ],
        'cosmic_colors': {
            'bass': (255, 255, 255),    # White
            'low_mid': (240, 248, 255), # Alice blue
            'high_mid': (230, 230, 250), # Lavender
            'treble': (255, 255, 255)   # White
        },
        'background_base': (10, 10, 15), # Dark blue-gray
        'text_color': (255, 255, 255)   # White
    },
    
    'blood': {
        'nebula_colors': [
            (139, 0, 0),       # Dark red
            (178, 34, 34),     # Fire brick
            (220, 20, 60),     # Crimson
            (255, 0, 0),       # Red
            (255, 69, 0)       # Red orange
        ],
        'cosmic_colors': {
            'bass': (139, 0, 0),        # Dark red
            'low_mid': (178, 34, 34),   # Fire brick
            'high_mid': (220, 20, 60),  # Crimson
            'treble': (255, 255, 255)   # White
        },
        'background_base': (20, 5, 5),   # Dark red
        'text_color': (220, 20, 60)     # Crimson
    },
    
    'sea': {
        'nebula_colors': [
            (0, 100, 0),       # Dark green
            (0, 128, 128),     # Teal
            (0, 191, 255),     # Deep sky blue
            (64, 224, 208),    # Turquoise
            (127, 255, 212)    # Aquamarine
        ],
        'cosmic_colors': {
            'bass': (0, 100, 0),        # Dark green
            'low_mid': (0, 128, 128),   # Teal
            'high_mid': (0, 191, 255),  # Deep sky blue
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 15, 20),  # Dark sea blue
        'text_color': (0, 191, 255)     # Deep sky blue
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
            (47, 79, 79),      # Dark slate gray
            (105, 105, 105),   # Dim gray
            (128, 128, 128),   # Gray
            (169, 169, 169),   # Dark gray
            (211, 211, 211)    # Light gray
        ],
        'cosmic_colors': {
            'bass': (47, 79, 79),       # Dark slate gray
            'low_mid': (105, 105, 105), # Dim gray
            'high_mid': (128, 128, 128), # Gray
            'treble': (255, 255, 255)   # White
        },
        'background_base': (15, 15, 15), # Dark gray
        'text_color': (169, 169, 169)   # Dark gray
    },

     'greens': {
        'nebula_colors': [
            (0, 100, 0),       # Dark green (BGR)
            (0, 128, 0),       # Green (BGR)
            (0, 255, 0),       # Lime (BGR)
            (50, 205, 50),     # Lime green (BGR)
            (144, 238, 144)    # Light green (BGR)
        ],
        'cosmic_colors': {
            'bass': (0, 100, 0),        # Dark green (BGR)
            'low_mid': (0, 128, 0),     # Green (BGR)
            'high_mid': (0, 255, 0),    # Lime (BGR)
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 20, 5),   # Dark green (BGR)
        'text_color': (0, 255, 0)       # Lime (BGR)
    },
    
    'purples': {
        'nebula_colors': [
            (130, 0, 75),      # Indigo (BGR)
            (128, 0, 128),     # Purple (BGR)
            (226, 43, 138),    # Blue violet (BGR)
            (219, 112, 147),   # Medium slate blue (BGR)
            (211, 85, 186)     # Medium orchid (BGR)
        ],
        'cosmic_colors': {
            'bass': (130, 0, 75),       # Indigo (BGR)
            'low_mid': (128, 0, 128),   # Purple (BGR)
            'high_mid': (226, 43, 138), # Blue violet (BGR)
            'treble': (255, 255, 255)   # White
        },
        'background_base': (20, 5, 10),  # Dark purple (BGR)
        'text_color': (226, 43, 138)    # Blue violet (BGR)
    },
    
    'yellows': {
        'nebula_colors': [
            (11, 134, 184),    # Dark goldenrod (BGR)
            (0, 215, 255),     # Gold (BGR)
            (0, 255, 255),     # Yellow (BGR)
            (224, 255, 255),   # Light yellow (BGR)
            (205, 250, 255)    # Lemon chiffon (BGR)
        ],
        'cosmic_colors': {
            'bass': (11, 134, 184),     # Dark goldenrod (BGR)
            'low_mid': (0, 215, 255),   # Gold (BGR)
            'high_mid': (0, 255, 255),  # Yellow (BGR)
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 20, 20),  # Dark yellow-brown (BGR)
        'text_color': (0, 255, 255)     # Yellow (BGR)
    },
    
    'coral': {
        'nebula_colors': [
            (80, 127, 255),    # Coral (BGR)
            (71, 99, 255),     # Tomato (BGR)
            (0, 69, 255),      # Red orange (BGR)
            (122, 160, 255),   # Light salmon (BGR)
            (203, 192, 255)    # Pink (BGR)
        ],
        'cosmic_colors': {
            'bass': (80, 127, 255),     # Coral (BGR)
            'low_mid': (71, 99, 255),   # Tomato (BGR)
            'high_mid': (0, 69, 255),   # Red orange (BGR)
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 10, 20),  # Dark coral (BGR)
        'text_color': (80, 127, 255)    # Coral (BGR)
    },
    
    'bright': {
        'nebula_colors': [
            (255, 0, 255),     # Magenta (BGR)
            (255, 255, 0),     # Cyan (BGR)
            (0, 255, 255),     # Yellow (BGR)
            (0, 255, 0),       # Lime (BGR)
            (0, 0, 255)        # Red (BGR)
        ],
        'cosmic_colors': {
            'bass': (255, 0, 255),      # Magenta (BGR)
            'low_mid': (255, 255, 0),   # Cyan (BGR)
            'high_mid': (0, 255, 255),  # Yellow (BGR)
            'treble': (255, 255, 255)   # White
        },
        'background_base': (5, 5, 5),    # Black
        'text_color': (255, 255, 255)   # White
    },
    
    'strong': {
        'nebula_colors': [
            (0, 0, 139),       # Dark red (BGR)
            (139, 0, 0),       # Dark blue (BGR)
            (0, 100, 0),       # Dark green (BGR)
            (128, 0, 128),     # Purple (BGR)
            (0, 140, 255)      # Dark orange (BGR)
        ],
        'cosmic_colors': {
            'bass': (0, 0, 139),        # Dark red (BGR)
            'low_mid': (139, 0, 0),     # Dark blue (BGR)
            'high_mid': (0, 100, 0),    # Dark green (BGR)
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
