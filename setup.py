import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
        return False
    return True

def check_audio_files():
    """Check if audio files exist in the audio directory"""
    audio_dir = "audio"
    if not os.path.exists(audio_dir):
        print("Error: audio/ directory not found!")
        return False
    
    # Supported audio formats
    audio_extensions = ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg']
    audio_files = []
    
    for file in os.listdir(audio_dir):
        if any(file.lower().endswith(ext) for ext in audio_extensions):
            audio_files.append(file)
    
    if not audio_files:
        print("Error: No audio files found in audio/ directory!")
        print("Supported formats: .mp3, .wav, .flac, .m4a, .aac, .ogg")
        return False
    
    print(f"Found {len(audio_files)} audio file(s):")
    for audio_file in audio_files:
        print(f"  - {audio_file}")
    return True

def main():
    print("Music Visualizer Setup")
    print("=" * 30)
    
    if not check_audio_files():
        return
    
    if install_requirements():
        print("\nSetup complete! You can now run:")
        print("python music_visualizer.py")
    else:
        print("\nSetup failed. Please install packages manually.")

if __name__ == "__main__":
    main()
