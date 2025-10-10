# Music Visualizer Usage Examples

## Basic Usage

### Process all audio files with default palette (cool)
```bash
python music_visualizer.py
```

### Process all audio files with a specific palette
```bash
python music_visualizer.py --palette warm
python music_visualizer.py --palette gothic
python music_visualizer.py --palette blood
```

### Process a specific audio file
```bash
python music_visualizer.py --audio-file "audio/my_song.wav" --palette futuristic
```

### List all available color palettes
```bash
python music_visualizer.py --list-palettes
```

### Use inverted color configuration
```bash
python music_visualizer.py --inverted --palette cool
python music_visualizer.py --inverted --list-palettes
```

## Available Color Palettes

- **warm**: Red, orange, and gold tones
- **cool**: Blue and cyan tones (default)
- **futuristic**: Bright green, cyan, and neon colors
- **modern**: Modern blue tones
- **gothic**: Purple and indigo tones
- **rustic**: Brown and earth tones
- **metal**: Gray and silver tones
- **steel**: Steel blue tones
- **gold**: Gold and amber tones
- **silver**: Silver and light gray tones
- **diamond**: White and light tones
- **blood**: Red and crimson tones
- **sea**: Teal and aqua tones
- **black-and-white**: Monochrome tones
- **grays**: Various gray tones

## Output Files

Output files are automatically named with the palette used:
- `song_name_cool_Visualizer.mp4`
- `song_name_warm_Visualizer.mp4`
- `song_name_gothic_Visualizer.mp4`

## Configuration

The color palettes and other settings can be customized in `config.py` or `config_inverted.py`. Each palette includes:
- `nebula_colors`: Colors for the background nebula effect
- `cosmic_colors`: Colors for different frequency bands (bass, low_mid, high_mid, treble)
- `background_base`: Base background color
- `text_color`: Color for text overlays

### Configuration Files
- **config.py**: Default color configuration (used by default)
- **config_inverted.py**: Alternative color configuration (use with `--inverted` flag)

## Examples

### Create a warm-toned visualizer
```bash
python music_visualizer.py --palette warm --audio-file "audio/epic_song.mp3"
```

### Create multiple versions with different palettes
```bash
python music_visualizer.py --palette gothic --audio-file "audio/dark_song.wav"
python music_visualizer.py --palette blood --audio-file "audio/dark_song.wav"
python music_visualizer.py --palette futuristic --audio-file "audio/dark_song.wav"
```

### Process all files with a specific theme
```bash
python music_visualizer.py --palette sea
```

### Create visualizers with inverted configuration
```bash
python music_visualizer.py --inverted --palette warm --audio-file "audio/epic_song.mp3"
python music_visualizer.py --inverted --palette gothic
```

### Compare normal vs inverted configurations
```bash
# Create with normal config
python music_visualizer.py --palette cool --audio-file "audio/song.wav"

# Create with inverted config
python music_visualizer.py --inverted --palette cool --audio-file "audio/song.wav"
```
