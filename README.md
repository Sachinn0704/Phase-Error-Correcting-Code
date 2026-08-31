# Phase Encoding Steganography with Error Correction

A Python research-oriented project that combines phase-based image steganography with Error Correction Codes (ECC) to improve recovery of hidden data when the stego-image is affected by errors or noise.

## Project Summary

The workflow converts a secret message into bits, adds redundancy through ECC, embeds the encoded information into image phase data, and later extracts and decodes the message.

## Main Components

- `main.py` — orchestrates the overall workflow.
- `enc.py` — phase-encoding steganography logic for embedding/extraction.
- `ecc.py` — error-correction encoding and decoding logic.
- `graph.png` — project result/analysis visualization.

## Processing Workflow

1. Start with a secret message.
2. Convert the message into a binary representation.
3. Encode the binary data using ECC.
4. Transform the cover image into the frequency domain.
5. Modify selected phase information to embed the encoded bits.
6. Reconstruct the stego-image.
7. Extract the embedded information from the stego-image.
8. Apply ECC decoding to detect/correct recoverable errors.
9. Reconstruct the original message.

## Technology Stack

- Python 3.x
- NumPy
- OpenCV
- Matplotlib
- Python standard library modules used by the implementation

## How to Run

1. Install Python 3.
2. Install the dependencies used by the project, for example:

```bash
pip install numpy opencv-python matplotlib
```

3. Run the main workflow:

```bash
python main.py
```

The exact input files, command-line arguments, and output behavior are defined by the current implementation in `main.py`.

## Project Structure

```text
.
├── LICENSE
├── README.md
├── ecc.py
├── enc.py
├── graph.png
└── main.py
```

## Key Learning Outcomes

- Frequency-domain image processing
- Phase-based steganography
- Binary data encoding and extraction
- Error detection and correction concepts
- Combining multiple algorithms into one processing pipeline

## Future Improvements

- Add a reproducible sample dataset
- Document ECC parameters and measurable recovery rates
- Add automated tests
- Provide PSNR/BER evaluation scripts
- Add configurable embedding strength and noise experiments
