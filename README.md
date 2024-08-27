# MRI-Scan-Image-Segmentation-YOLOv10

This project uses a YOLOv5 model for detecting brain tumors in MRI scans. The model has been trained to identify regions in brain images that likely contain tumors.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The goal of this project is to provide a tool for early detection of brain tumors using deep learning techniques. The YOLOv5 model is used to detect and annotate possible tumor regions in MRI scans.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/vindhyaregonda/brain-tumor-detection.git
    ```
2. Change directory to the project folder:
    ```
    cd brain-tumor-detection
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Ensure that the YOLOv5 model file (`your_model_file.pt`) is in the project directory.

2. Run the Streamlit app:
    ```
    streamlit run Brain_Tumor_Detection_Updated.ipynb
    ```

3. Upload an MRI scan image when prompted. The model will detect and highlight any tumor regions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
