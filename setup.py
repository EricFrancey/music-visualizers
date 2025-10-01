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

def check_audio_file():
    """Check if the audio file exists"""
    if not os.path.exists("audio/LegendsHorizon.mp3"):
        print("Error: LegendsHorizon.mp3 not found in audio/ directory!")
        return False
    print("Audio file found!")
    return True

def main():
    print("Music Visualizer Setup")
    print("=" * 30)
    
    if not check_audio_file():
        return
    
    if install_requirements():
        print("\nSetup complete! You can now run:")
        print("python music_visualizer.py")
    else:
        print("\nSetup failed. Please install packages manually.")

if __name__ == "__main__":
    main()
