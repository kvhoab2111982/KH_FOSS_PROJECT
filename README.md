# HausaMediaLab

HausaMediaLab is a media processing library designed for handling audio and video processing tasks, with a focus on supporting Hausa language transformations and localized features. This library includes functionality for audio extraction, video resizing, watermarking, format conversions, and more. It's designed to empower users to work efficiently with multimedia files in the context of Hausa language media.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Audio Processing**: Extract audio from videos, convert audio formats, apply noise reduction, and more.
- **Video Processing**: Resize videos, add watermarks, convert formats, and extract frames.
- **Utility Functions**: Various helpers for file handling, duration calculation, and unique filename generation.
- **Support for Hausa Language**: Text-to-speech and audio transformation tailored for the Hausa language.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AI-Bauchi/HausaMediaLab.git
   cd HausaMediaLab
   ```

2. **Set up the Environment**:
   Ensure you have Python 3.7+ installed. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. **Install FFMPEG**:
   Many video and audio operations rely on FFMPEG. Install it using:
   - **Mac**: `brew install ffmpeg`
   - **Ubuntu**: `sudo apt update && sudo apt install ffmpeg`
   - **Windows**: Download the installer from [FFmpeg](https://ffmpeg.org/download.html).

## Usage

Example code to use the library's `extract_audio` and `resize_video` functions:

```python
from HausaMediaLab.audio_processing import extract_audio
from HausaMediaLab.video_processing import resize_video

# Extract audio from video
extract_audio("input_video.mp4", "output_audio.mp3")

# Resize video
resize_video("input_video.mp4", "output_resized.mp4", width=1280, height=720)
```

For more detailed examples, refer to the [documentation](docs/README.md) or `example_scripts/`.

## Directory Structure

```
HausaMediaLab/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   ├── task.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── workflows/
│   │   ├── greetings.yml
│   │   ├── pylint.yml
├── CONTRIBUTORS.md
├── LICENSE
├── README.md
├── core/
│   ├── __init__.py
│   ├── audio_processing.py
│   ├── utils.py
│   ├── video_processing.py
├── setup.py
├── tests/
│   ├── __init__.py
│   ├── files/
│   │   ├── test_video.mp4
│   ├── test_audio_processing.py
│   ├── test_utils.py
│   ├── test_video_processing.py
```

## Configuration

Configure your environment variables or settings by creating a `.env` file in the project root. This can include any API keys, file paths, or settings specific to your development or production environment.

## Contributing

We welcome contributions! Follow these steps:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for more details, and see the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to understand our community guidelines.

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

Happy Coding! 😃
