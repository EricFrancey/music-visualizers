import librosa
import numpy as np
import cv2
import os
from moviepy.editor import VideoFileClip, AudioFileClip
import math
import random
import argparse
import importlib.util

def load_config_module(use_inverted=False):
    """
    Dynamically load the appropriate config module
    
    Args:
        use_inverted (bool): If True, load config_inverted.py, otherwise load config.py
        
    Returns:
        module: The loaded config module
    """
    config_file = "config_inverted.py" if use_inverted else "config.py"
    
    spec = importlib.util.spec_from_file_location("config", config_file)
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)
    
    return config_module

class SpaceMusicVisualizer:
    def __init__(self, audio_file, output_file="visualizer_output.mp4", palette_name="cool", config_module=None):
        self.audio_file = audio_file
        self.output_file = output_file
        self.palette_name = palette_name
        
        # Load config module if not provided
        if config_module is None:
            config_module = load_config_module()
        self.config = config_module
        
        # Load color palette from config
        self.palette = self.config.get_palette(palette_name)
        self.nebula_colors = self.palette['nebula_colors']
        self.cosmic_colors = self.palette['cosmic_colors']
        self.background_base = self.palette['background_base']
        self.text_color = self.palette['text_color']
        
        self.y, self.sr = librosa.load(audio_file)
        self.duration = len(self.y) / self.sr
        
        # Audio analysis
        self.tempo, self.beats = librosa.beat.beat_track(y=self.y, sr=self.sr)
        self.beat_times = librosa.frames_to_time(self.beats, sr=self.sr)
        
        # Spectral features
        self.stft = librosa.stft(self.y)
        self.magnitude = np.abs(self.stft)
        self.frequencies = librosa.fft_frequencies(sr=self.sr)
        
        # Create frequency bands
        self.freq_bands = self._create_frequency_bands()
        
        # Video settings from config
        self.fps = self.config.VIDEO_SETTINGS['fps']
        self.frame_count = int(self.duration * self.fps)
        self.width = self.config.VIDEO_SETTINGS['width']
        self.height = self.config.VIDEO_SETTINGS['height']
        
        # Space theme settings from config
        self.stars = self._generate_starfield(self.config.VISUAL_SETTINGS['num_stars'])
        
        # Pre-load and resize the space image for performance
        self.space_img = self._load_space_image()
        
    def _create_frequency_bands(self):
        """Create frequency bands for visualization"""
        bands = []
        # Bass (0-250 Hz)
        bass_idx = np.where((self.frequencies >= 0) & (self.frequencies <= 250))[0]
        bands.append(('bass', bass_idx))
        
        # Low mid (250-2000 Hz)
        low_mid_idx = np.where((self.frequencies > 250) & (self.frequencies <= 2000))[0]
        bands.append(('low_mid', low_mid_idx))
        
        # High mid (2000-8000 Hz)
        high_mid_idx = np.where((self.frequencies > 2000) & (self.frequencies <= 8000))[0]
        bands.append(('high_mid', high_mid_idx))
        
        # Treble (8000+ Hz)
        treble_idx = np.where(self.frequencies > 8000)[0]
        bands.append(('treble', treble_idx))
        
        return bands
    
    def _generate_starfield(self, num_stars):
        """Generate a random starfield for the space background"""
        stars = []
        for _ in range(num_stars):
            star = {
                'x': random.randint(0, self.width),
                'y': random.randint(0, self.height),
                'brightness': random.uniform(0.3, 1.0),
                'size': random.randint(1, 3),
                'twinkle_speed': random.uniform(0.02, 0.08)
            }
            stars.append(star)
        return stars
    
    def _load_space_image(self):
        """Load and preprocess the space image for performance"""
        img_path = "img/space_transparent.png"
        if os.path.exists(img_path):
            # Load the image
            space_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
            
            if space_img is not None:
                # Calculate new dimensions (from config, maintain aspect ratio)
                target_width = self.config.VISUAL_SETTINGS['space_image_width']
                height, width = space_img.shape[:2]
                aspect_ratio = height / width
                target_height = int(target_width * aspect_ratio)
                
                # Resize the image once
                resized_img = cv2.resize(space_img, (target_width, target_height))
                return resized_img
        
        return None
    
    def get_band_energy(self, frame_idx):
        """Get energy for each frequency band at a given frame"""
        frame_time = frame_idx / self.fps
        
        # Get the closest STFT frame
        stft_frame = int(frame_time * self.sr / 512)
        stft_frame = min(stft_frame, self.magnitude.shape[1] - 1)
        
        band_energies = {}
        for band_name, band_indices in self.freq_bands:
            if len(band_indices) > 0:
                energy = np.mean(self.magnitude[band_indices, stft_frame])
                band_energies[band_name] = energy
            else:
                band_energies[band_name] = 0
        
        return band_energies
    
    def create_visualization_frame(self, frame_idx):
        """Create a single frame with space theme using OpenCV"""
        # Create deep space background with nebula effect
        frame = self._create_space_background(frame_idx)
        
        # Get current audio data
        band_energies = self.get_band_energy(frame_idx)
        frame_time = frame_idx / self.fps
        
        # Check if we're on a beat
        is_beat = any(abs(beat_time - frame_time) < 0.1 for beat_time in self.beat_times)
        
        center_x, center_y = self.width // 2, self.height // 2
        
        # Create galaxy/planet visualizer
        self._draw_galaxy_center(frame, center_x, center_y, band_energies, is_beat, frame_idx)
        
        # Add cosmic frequency bars (like energy beams)
        self._draw_cosmic_bars(frame, center_x, center_y, band_energies, is_beat, frame_idx)
        
        # Add floating particles
        self._draw_particles(frame, band_energies, frame_idx)
        
        # Add title with space font
        self._draw_title(frame, frame_time)
        
        return frame
    
    def _create_space_background(self, frame_idx):
        """Create a space background with nebula and stars"""
        # Start with background color from palette
        frame = np.full((self.height, self.width, 3), self.background_base, dtype=np.uint8)
        
        # Add nebula effect
        for i in range(3):
            nebula_color = self.nebula_colors[i]
            # Create gradient nebula
            for y in range(0, self.height, 20):
                for x in range(0, self.width, 20):
                    distance = math.sqrt((x - self.width//2)**2 + (y - self.height//2)**2)
                    intensity = max(0, 1 - distance / (self.width//2))
                    intensity *= (0.3 + 0.7 * math.sin(frame_idx * 0.01 + i))
                    
                    if intensity > 0.1:
                        color_intensity = int(intensity * 30)
                        frame[y:y+20, x:x+20] = np.clip(
                            frame[y:y+20, x:x+20] + np.array(nebula_color) * color_intensity // 255,
                            0, 255
                        )
        
        # Add twinkling stars
        for star in self.stars:
            twinkle = 0.5 + 0.5 * math.sin(frame_idx * star['twinkle_speed'])
            brightness = int(star['brightness'] * twinkle * 255)
            color = (brightness, brightness, brightness)
            cv2.circle(frame, (star['x'], star['y']), star['size'], color, -1)
        
        return frame
    
    def _draw_galaxy_center(self, frame, center_x, center_y, band_energies, is_beat, frame_idx):
        """Draw the central galaxy/planet system"""
        # Main central planet (bass)
        bass_energy = band_energies.get('bass', 0)
        planet_radius = int(80 + bass_energy * 150)
        if is_beat:
            planet_radius = int(planet_radius * 1.3)
        
        # Limit maximum radius to prevent filling entire frame
        max_radius = int(min(self.width, self.height) * self.config.VISUAL_SETTINGS['max_planet_radius_ratio'])
        planet_radius = min(planet_radius, max_radius)
        
        # Determine color based on which frequency band has the highest energy
        dominant_band = max(band_energies.items(), key=lambda x: x[1])[0]
        glow_color = self.cosmic_colors[dominant_band]
        
        # Draw planet with glow effect
        for i in range(5, 0, -1):
            alpha = 0.2 * i
            color = tuple(int(c * alpha) for c in glow_color)
            cv2.circle(frame, (center_x, center_y), planet_radius + i*3, color, -1)
        
        # Main planet
        cv2.circle(frame, (center_x, center_y), planet_radius, glow_color, -1)
        
        # Add planet surface details
        cv2.circle(frame, (center_x, center_y), planet_radius, (255, 255, 255), 2)
        
        # Orbiting rings (other frequency bands)
        for i, (band_name, energy) in enumerate(band_energies.items()):
            if band_name == 'bass':
                continue
                
            ring_radius = 120 + i * 60 + energy * 100
            if is_beat:
                ring_radius = int(ring_radius * 1.2)
            
            color = self.cosmic_colors[band_name]
            # Draw ring as dashed circle
            for angle in range(0, 360, 10):
                if angle % 20 < 10:  # Create dashed effect
                    x = int(center_x + ring_radius * math.cos(math.radians(angle)))
                    y = int(center_y + ring_radius * math.sin(math.radians(angle)))
                    cv2.circle(frame, (x, y), 3, color, -1)
    
    def _draw_cosmic_bars(self, frame, center_x, center_y, band_energies, is_beat, frame_idx):
        """Draw cosmic energy bars around the galaxy"""
        num_bars = self.config.VISUAL_SETTINGS['num_cosmic_bars']
        base_radius = 200
        
        for i in range(num_bars):
            angle = 2 * math.pi * i / num_bars + frame_idx * 0.02  # Rotate over time
            
            # Map bar to frequency band
            band_idx = min(i // (num_bars // 4), 3)
            band_names = ['bass', 'low_mid', 'high_mid', 'treble']
            energy = band_energies.get(band_names[band_idx], 0)
            
            bar_length = int(30 + (energy * 300))
            if is_beat:
                bar_length = int(bar_length * 1.5)
            
            # Calculate bar positions
            start_x = int(center_x + base_radius * math.cos(angle))
            start_y = int(center_y + base_radius * math.sin(angle))
            end_x = int(center_x + (base_radius + bar_length) * math.cos(angle))
            end_y = int(center_y + (base_radius + bar_length) * math.sin(angle))
            
            color = self.cosmic_colors[band_names[band_idx]]
            
            # Draw energy beam with glow
            cv2.line(frame, (start_x, start_y), (end_x, end_y), color, 8)
            cv2.line(frame, (start_x, start_y), (end_x, end_y), (255, 255, 255), 2)
    
    def _draw_particles(self, frame, band_energies, frame_idx):
        """Draw floating particles that respond to music"""
        num_particles = self.config.VISUAL_SETTINGS['num_particles']
        treble_energy = band_energies.get('treble', 0)
        
        for i in range(num_particles):
            # Particle position based on time and energy
            x = int(self.width * 0.1 + (i * 37) % (self.width * 0.8))
            y = int(self.height * 0.1 + (i * 23 + frame_idx * 2) % (self.height * 0.8))
            
            # Particle size based on treble energy
            size = int(1 + treble_energy * 5)
            if size > 0:
                # Random cosmic color
                colors = [(255, 255, 255), (0, 191, 255), (138, 43, 226), (255, 215, 0)]
                color = colors[i % len(colors)]
                cv2.circle(frame, (x, y), size, color, -1)
    
    def _draw_title(self, frame, frame_time):
        """Draw the space image in the top left corner"""
        # Use pre-loaded space image for better performance
        if self.space_img is not None:
            # Position in top left corner (50 pixels from edges)
            x_offset, y_offset = 50, 50
            target_height, target_width = self.space_img.shape[:2]
            
            # Handle transparency if the image has an alpha channel
            if self.space_img.shape[2] == 4:  # RGBA image
                # Extract alpha channel
                alpha = self.space_img[:, :, 3] / 255.0
                
                # Extract RGB channels
                rgb = self.space_img[:, :, :3]
                
                # Blend with background
                for c in range(3):
                    frame[y_offset:y_offset+target_height, x_offset:x_offset+target_width, c] = \
                        frame[y_offset:y_offset+target_height, x_offset:x_offset+target_width, c] * (1 - alpha) + \
                        rgb[:, :, c] * alpha
            else:
                # No alpha channel, just overlay
                frame[y_offset:y_offset+target_height, x_offset:x_offset+target_width] = self.space_img
        
        # Add bottom text with audio info
        audio_name = os.path.splitext(os.path.basename(self.audio_file))[0]
        bottom_text = f"{audio_name}"
        
        # Add glow effect to bottom text
        # for i in range(4, 0, -1):
        #     color_intensity = 30 * i
        #     cv2.putText(frame, bottom_text, 
        #                (50 + i, self.height - 50 + i), cv2.FONT_HERSHEY_TRIPLEX, 1.2, 
        #                (color_intensity, color_intensity + 20, color_intensity + 40), 3)
        
        # Main bottom text with color from palette
        cv2.putText(frame, bottom_text, 
                   (50, self.height - 50), cv2.FONT_HERSHEY_DUPLEX, 1.2, self.text_color, 3)
    
    def generate_video(self):
        """Generate the complete video using MoviePy directly"""
        print(f"Generating {self.frame_count} frames...")
        
        # Create temporary directory for frames
        temp_dir = "temp_frames"
        os.makedirs(temp_dir, exist_ok=True)
        
        # Generate frames as images
        for i in range(self.frame_count):
            if i % 30 == 0:  # Progress update every second
                print(f"Generating frame {i}/{self.frame_count}")
            
            frame = self.create_visualization_frame(i)
            # Save as image
            cv2.imwrite(f"{temp_dir}/frame_{i:06d}.png", frame)
        
        print("Creating video from frames...")
        
        # Use MoviePy to create video from images
        from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
        
        # Get all frame files
        frame_files = [f"{temp_dir}/frame_{i:06d}.png" for i in range(self.frame_count)]
        
        # Create video clip from images
        video_clip = ImageSequenceClip(frame_files, fps=self.fps)
        
        # Load audio
        audio_clip = AudioFileClip(self.audio_file)
        
        # Combine video and audio
        print("Combining video with audio...")
        final_video = video_clip.set_audio(audio_clip)
        
        # Write final video
        final_video.write_videofile(
            self.output_file, 
            fps=self.fps, 
            codec=self.config.VIDEO_SETTINGS['codec'], 
            audio_codec=self.config.VIDEO_SETTINGS['audio_codec'],
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )
        
        # Cleanup
        video_clip.close()
        audio_clip.close()
        final_video.close()
        
        # Remove temporary files
        for frame_file in frame_files:
            if os.path.exists(frame_file):
                os.remove(frame_file)
        os.rmdir(temp_dir)
        
        print(f"Video saved as {self.output_file}")

def get_audio_files():
    """Get all audio files from the audio directory"""
    audio_dir = "audio"
    if not os.path.exists(audio_dir):
        print(f"Error: {audio_dir} directory not found!")
        return []
    
    # Supported audio formats
    audio_extensions = ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg']
    audio_files = []
    
    for file in os.listdir(audio_dir):
        if any(file.lower().endswith(ext) for ext in audio_extensions):
            audio_files.append(os.path.join(audio_dir, file))
    
    return audio_files

def main():
    parser = argparse.ArgumentParser(description='Space Music Visualizer with customizable color palettes')
    parser.add_argument('--palette', '-p', 
                       default='cool',
                       help='Color palette to use for visualization')
    parser.add_argument('--list-palettes', '-l', 
                       action='store_true',
                       help='List all available color palettes')
    parser.add_argument('--audio-file', '-a',
                       help='Specific audio file to process (if not provided, processes all files in audio/ directory)')
    parser.add_argument('--inverted', '-i',
                       action='store_true',
                       help='Use inverted color configuration (config_inverted.py)')
    
    args = parser.parse_args()
    
    # Load the appropriate config module
    config_module = load_config_module(use_inverted=args.inverted)
    
    # List palettes if requested
    if args.list_palettes:
        print("Available color palettes:")
        for palette in config_module.list_palettes():
            print(f"  - {palette}")
        return
    
    # Get audio files
    if args.audio_file:
        if not os.path.exists(args.audio_file):
            print(f"Error: Audio file '{args.audio_file}' not found!")
            return
        audio_files = [args.audio_file]
    else:
        audio_files = get_audio_files()
        if not audio_files:
            print("No audio files found in the audio/ directory!")
            print("Supported formats: .mp3, .wav, .flac, .m4a, .aac, .ogg")
            print("Use --audio-file to specify a specific file, or --list-palettes to see available color themes.")
            return
    
    print(f"Found {len(audio_files)} audio file(s) to process:")
    for audio_file in audio_files:
        print(f"  - {audio_file}")
    
    # Validate palette
    try:
        config_module.get_palette(args.palette)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    config_type = "inverted" if args.inverted else "normal"
    print(f"\nUsing {config_type} color configuration with palette: {args.palette}")
    print("Starting space music visualizer generation...")
    
    # Ensure output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    for i, audio_file in enumerate(audio_files, 1):
        # Get the base name without extension for output file naming
        base_name = os.path.splitext(os.path.basename(audio_file))[0]
        output_file = os.path.join(output_dir, f"{base_name}_{args.palette}_Visualizer.mp4")
        
        print(f"\n[{i}/{len(audio_files)}] Processing: {audio_file}")
        print(f"Output will be saved as: {output_file}")
        
        try:
            visualizer = SpaceMusicVisualizer(audio_file, output_file, args.palette, config_module)
            visualizer.generate_video()
            print(f"✓ Completed: {output_file}")
        except Exception as e:
            print(f"✗ Error processing {audio_file}: {str(e)}")
            continue
    
    print(f"\nAll visualizers complete! Processed {len(audio_files)} file(s) with '{args.palette}' palette.")

if __name__ == "__main__":
    main()
