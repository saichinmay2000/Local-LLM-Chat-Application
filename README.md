# Project: Streamlit and FastAPI Integration

## Overview
This project combines the power of Streamlit for interactive user interfaces and FastAPI for building robust backend APIs. It also integrates the Ollama API and Hugging Face Hub for leveraging AI models.

---

## Features
- **Streamlit Frontend**: Provides a user-friendly interface for interacting with backend services.
- **FastAPI Backend**: Handles API requests and serves data to the frontend.
- **Ollama Integration**: Utilizes AI capabilities provided by the Ollama API.
- **Hugging Face Hub**: Accesses pre-trained models and datasets for various AI tasks.
- **Uvicorn**: Serves the FastAPI backend efficiently.

---

## Prerequisites

Ensure you have the following installed:
- Python 3.7+
- `pip` (Python package manager)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/saichinmay2000/Local-LLM-Chat-Application.git
   cd Local-LLM-Chat-Application
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. Start the Streamlit Frontend
Run the Streamlit app:
```bash
streamlit run app/main.py
```
- Replace `main.py` with the filename of your Streamlit application.

---

## Project Structure

```plaintext
.
├── app/main.py           # Streamlit application
├── app/utils.py          # Backend Ollama Integration
├── requirements.txt      # Python dependencies
├── README.md             # Project details
└── ...                   # Additional files/modules
```

---

## Dependencies

The following libraries are used in this project:
- **streamlit**: For building the frontend.
- **fastapi**: For creating backend APIs.
- **uvicorn**: ASGI server for running FastAPI.
- **ollama**: AI model integration.
- **huggingface_hub**: Access to Hugging Face models and datasets.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contribution

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with detailed information.

---

## Contact

For any questions or suggestions, please contact:
- **Email**: [saichinmayt@gmail.com]
- **GitHub**: [https://github.com/saichinmay2000]
