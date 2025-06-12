# 🏥 HealthcareBot - AI-Powered Medical Assistant

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ShoyebRampure/HealthcareBot?style=social)](https://github.com/ShoyebRampure/HealthcareBot/stargazers)

## 📋 Project Overview

HealthcareBot is an intelligent medical chatbot that leverages machine learning to predict diseases based on user-reported symptoms. The system provides comprehensive treatment recommendations, preventive measures, and health insights to assist users in understanding their health conditions better.

### 🎯 Key Features

- **Symptom-Based Disease Prediction**: Analyzes 3 user-input symptoms for accurate disease prediction
- **Intelligent Treatment Recommendations**: Provides evidence-based treatment suggestions
- **Preventive Care Guidance**: Offers personalized precautions and lifestyle recommendations
- **Interactive Web Interface**: User-friendly chatbot experience with real-time responses
- **Machine Learning Powered**: Trained on extensive medical datasets for reliable predictions
- **Comprehensive Health Insights**: Detailed information about predicted conditions and recovery

## 🚀 Live Demo

Experience intelligent healthcare assistance through our interactive chatbot interface. Input three symptoms and receive instant disease predictions with comprehensive treatment recommendations and precautions.

## 🛠️ Technology Stack

**Backend:**
- Python 3.8+
- Flask Web Framework
- Machine Learning (Scikit-learn)
- Pandas & NumPy for data processing

**Frontend:**
- HTML5, CSS3, JavaScript
- Responsive web design
- Interactive chat interface

**Data:**
- CSV datasets containing medical information
- Trained ML models for disease prediction
- Treatment and precaution databases

## 📊 Dataset Information

The chatbot utilizes comprehensive medical datasets including:

- **Symptoms Database**: Extensive symptom combinations and patterns
- **Disease Classification**: Multiple disease categories and conditions  
- **Treatment Protocols**: Evidence-based medical treatments
- **Precautionary Measures**: Preventive care and lifestyle recommendations

## 🔧 Installation & Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShoyebRampure/HealthcareBot.git
   cd HealthcareBot
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv healthcare_env
   
   # Windows
   healthcare_env\Scripts\activate
   
   # macOS/Linux
   source healthcare_env/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the chatbot**
   Open your web browser and navigate to `http://localhost:5000`

## 💻 How to Use

### Basic Workflow

1. **Launch Application**: Start the Flask server and open the web interface
2. **Input Symptoms**: Enter exactly 3 symptoms in the chat interface
3. **Get Prediction**: Receive AI-powered disease prediction with confidence score
4. **View Recommendations**: Access detailed treatment plans and medications
5. **Follow Precautions**: Review preventive measures and lifestyle advice
6. **Health Insights**: Explore additional information about the condition

### Example Interaction

```
🗣️ User: "I have fever, headache, and fatigue"

🤖 HealthcareBot Response:

🔍 **Disease Prediction**: Viral Fever (Confidence: 87%)

💊 **Treatment Recommendations**:
• Complete bed rest for 2-3 days
• Increase fluid intake (water, juices, soups)
• Paracetamol for fever and headache relief
• Light, easily digestible meals

⚠️ **Precautions**:
• Avoid going out in cold weather
• Maintain proper hand hygiene
• Get adequate sleep (8+ hours)
• Monitor temperature regularly

📊 **Health Insights**:
• Expected recovery time: 3-5 days
• Seek medical attention if fever exceeds 102°F
• Watch for additional symptoms like difficulty breathing
```

## 🧠 Machine Learning Model

### Model Architecture
- **Algorithm**: Advanced classification algorithms
- **Training Data**: Comprehensive medical symptom-disease datasets
- **Feature Engineering**: Multi-symptom pattern recognition
- **Validation**: Cross-validation with medical accuracy standards

### Performance Metrics
- High accuracy in disease prediction
- Reliable symptom-disease correlation
- Validated against medical databases
- Continuous model improvement

## 📁 Project Structure

```
HealthcareBot/
│
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
│
├── datasets/               # Medical datasets (CSV files)
│   ├── symptoms.csv        # Symptoms database
│   ├── diseases.csv        # Disease information
│   ├── treatments.csv      # Treatment protocols
│   └── precautions.csv     # Preventive measures
│
├── models/                 # ML models and training
│   ├── disease_model.pkl   # Trained prediction model
│   └── model_training.py   # Model training scripts
│
├── static/                 # Web assets
│   ├── css/
│   │   └── style.css       # Chatbot interface styles
│   └── js/
│       └── chatbot.js      # Frontend functionality
│
├── templates/              # HTML templates
│   └── index.html          # Main chatbot interface
│
└── utils/                  # Utility functions
    ├── data_processor.py   # Data processing
    └── predictor.py        # Prediction logic
```

## 🚀 Deployment Options

### Local Development
```bash
python app.py
# Application runs on http://localhost:5000
```

### Production Deployment

**Using Gunicorn:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

**Docker Deployment:**
```bash
docker build -t healthcarebot .
docker run -p 5000:5000 healthcarebot
```

## 🔧 Configuration

### Environment Setup
Create a `.env` file for configuration:

```env
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key
MODEL_PATH=models/disease_model.pkl
```

### Customization Options
- Modify symptom databases in `datasets/` folder
- Adjust model parameters in training scripts
- Customize UI themes in `static/css/style.css`
- Update treatment protocols as needed

## 📋 API Documentation

### Core Endpoints

**`/predict` (POST)**
Predict disease from symptoms
```json
Request: {
  "symptoms": ["fever", "headache", "cough"]
}

Response: {
  "disease": "Common Cold",
  "confidence": 0.85,
  "treatments": [...],
  "precautions": [...],
  "insights": {...}
}
```

**`/symptoms` (GET)**
Get available symptoms list

**`/health` (GET)**
Application health check

## 🧪 Testing

Run tests to ensure functionality:

```bash
# Install testing dependencies
pip install pytest pytest-cov

# Run all tests
python -m pytest tests/

# Run with coverage report
pytest --cov=. tests/
```

## 🤝 Contributing

We welcome contributions to improve HealthcareBot! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes and test thoroughly**
4. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
5. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Contribution Areas
- Improve disease prediction accuracy
- Add new medical conditions and treatments
- Enhance user interface and experience
- Add multi-language support
- Improve documentation
- Add comprehensive test coverage

## 📋 Future Roadmap

- [ ] **Enhanced AI Models** - Integration of advanced NLP models
- [ ] **Multi-Language Support** - Support for regional languages
- [ ] **Voice Integration** - Voice input and output capabilities
- [ ] **Mobile Application** - Native mobile app development  
- [ ] **Emergency Detection** - Critical symptom identification
- [ ] **Doctor Network** - Integration with healthcare providers
- [ ] **Health Tracking** - Long-term symptom and health monitoring
- [ ] **Telemedicine Integration** - Connect with medical professionals

## ⚠️ Important Medical Disclaimer

**CRITICAL NOTICE**: HealthcareBot is designed for educational and informational purposes only. This system should **NEVER** be used as a substitute for professional medical advice, diagnosis, or treatment.

### Key Limitations:
- AI predictions may not be 100% accurate
- Cannot diagnose rare or complex conditions  
- Emergency situations require immediate medical attention
- Results should always be verified with healthcare professionals
- Not suitable for critical medical decision making

**Always consult qualified healthcare providers for medical concerns.**

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for complete details.

## 👤 Author

**Shoyeb Rampure**
- GitHub: [@ShoyebRampure](https://github.com/ShoyebRampure)
- Repository: [HealthcareBot](https://github.com/ShoyebRampure/HealthcareBot)

## 🙏 Acknowledgments

- Medical dataset contributors and researchers
- Open source machine learning community
- Flask and Python development communities  
- Healthcare professionals providing guidance
- Contributors and testers of this project

## 📞 Support & Contact

- **GitHub Issues**: [Report Issues](https://github.com/ShoyebRampure/HealthcareBot/issues)
- **Feature Requests**: [Request Features](https://github.com/ShoyebRampure/HealthcareBot/issues/new)
- **Discussions**: [Join Discussions](https://github.com/ShoyebRampure/HealthcareBot/discussions)

## 📊 Project Statistics

![Repository Size](https://img.shields.io/github/repo-size/ShoyebRampure/HealthcareBot)
![GitHub issues](https://img.shields.io/github/issues/ShoyebRampure/HealthcareBot)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ShoyebRampure/HealthcareBot)
![GitHub last commit](https://img.shields.io/github/last-commit/ShoyebRampure/HealthcareBot)
![GitHub contributors](https://img.shields.io/github/contributors/ShoyebRampure/HealthcareBot)

---

⭐ **Found this project helpful? Give it a star!** ⭐

🔗 **Share with others who might benefit from AI-powered healthcare assistance**
