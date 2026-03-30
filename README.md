# PhysioAugment 🫀📈

**A Lightweight, Plug-and-Play 1D Physiological Signal Augmentation Library for Deep Learning.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

Deep learning models for 1D time-series data (like PPG, ECG, or radar phase signals) often suffer from overfitting due to the lack of diverse training data. Unlike images, you cannot simply "crop" or "rotate" a heartbeat signal without destroying its frequency and phase characteristics.

**PhysioAugment** solves this by providing domain-specific, biophysically meaningful data augmentations using pure NumPy. 

## ✨ Key Features
* **Zero Bloat:** Pure Python with only `numpy` and `scipy` dependencies.
* **Plug-and-Play:** API designed to perfectly mimic `torchvision.transforms` and `albumentations`.
* **Domain-Specific:** Simulates real-world sensor noise, including baseline wander, respiration interference, and motion artifacts.

## 🚀 Quick Start

### Installation
*(Currently installable via source, PyPI coming soon)*

```bash
git clone [https://github.com/phish-tech/PhysioAugment.git](https://github.com/phish-tech/PhysioAugment)(https://github.com/phish-tech/PhysioAugment.git)
cd physioaugment
pip install -e .

📊 Visual Demo
Here is what PhysioAugment does to a clean physiological signal under the hood:

💡 Perfect For
Fatigue Monitoring Systems: Augmenting datasets for multi-class fatigue state classification (e.g., using keystroke dynamics or physiological baselines).

Multi-Modal Vitals: Enhancing dual-modality blood pressure estimation models (e.g., combining iPPG and mmWave radar RMS).

Wearable AIoT: Simulating intense motion artifacts for robust continuous monitoring algorithms and adversarial living research.

Neural Interfaces: Injecting low-frequency baseline drifts into contact/non-contact physiological interface data (like metasurface sensor arrays).

🤝 Contributing
Contributions are welcome! If you have ideas for new physiological noise simulations (e.g., 50/60Hz powerline interference, sensor disconnect flats), feel free to open an issue or submit a Pull Request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
