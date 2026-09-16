# Diabetes Prediction Flask Application

A machine learning-powered web application built with Flask that predicts the likelihood of diabetes based on patient health metrics. The app uses a pre-trained machine learning model to provide quick and accurate predictions.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.7+](https://img.shields.io/badge/Python-3.7+-blue.svg)

## 🌐 Live Demo

Access the deployed application: [https://diabetes-flask-prediction-2.onrender.com/predict](https://diabetes-flask-prediction-2.onrender.com)

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Input Parameters](#input-parameters)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Contributing](#contributing)

## ✨ Features

- **User-Friendly Interface**: Simple and intuitive web interface for entering patient health data
- **Real-Time Predictions**: Get instant diabetes prediction results
- **Pre-trained Model**: Uses a machine learning model trained on diabetes dataset
- **Data Normalization**: Automatic scaling of input features for accurate predictions
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Production-Ready**: Deployed and accessible online

## 📁 Project Structure

```
diabetes-flask-prediction/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── diabetes_model.pkl          # Pre-trained ML model
├── diabetes_scaler.pkl         # Feature scaler for normalization
├── LICENSE                     # MIT License
├── static/                     # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
└── templates/                  # HTML templates
    ├── index.html
    ├── predict.html
    └── result.html
```

## 🔧 Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.7 or higher**
- **pip** (Python package manager)
- **Git** (optional, for cloning the repository)

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Divya-kumari18/diabetes-flask-prediction.git
cd diabetes-flask-prediction
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## 🚀 Usage

1. **Access the Application**: Open your web browser and navigate to `http://localhost:5000`

2. **Enter Patient Information**: Fill in the required health metrics:
   - Number of pregnancies
   - Glucose level
   - Blood pressure
   - Skin thickness
   - Insulin level
   - BMI (Body Mass Index)
   - Diabetes pedigree function
   - Age

3. **Get Prediction**: Click the "Predict" button to receive the diabetes prediction result

4. **View Results**: The application will display whether the person is predicted to have diabetes or not

## 🧠 How It Works

### Architecture Overview

1. **Frontend**: User inputs are collected through an HTML form in the web interface
2. **Data Processing**: Input features are normalized using the pre-trained scaler (`diabetes_scaler.pkl`)
3. **Model Prediction**: The normalized data is passed to the pre-trained machine learning model (`diabetes_model.pkl`)
4. **Result Display**: The prediction result is displayed to the user with probability information

### Model Details

- **Algorithm**: Trained using a machine learning algorithm (typically Logistic Regression, Random Forest, or SVM)
- **Training Data**: Built on diabetes prediction datasets (likely from the Pima Indians Diabetes Database)
- **Accuracy**: Model provides predictions based on 8 health-related features
- **Output**: Binary classification (Positive/Negative for diabetes)

## 📊 Input Parameters

| Parameter | Description | Range/Unit |
|-----------|-------------|-----------|
| Pregnancies | Number of times pregnant | 0-15 |
| Glucose | Plasma glucose concentration | mg/dL |
| BloodPressure | Diastolic blood pressure | mmHg |
| SkinThickness | Triceps skin fold thickness | mm |
| Insulin | 2-hour serum insulin | mu U/ml |
| BMI | Body Mass Index | kg/m² |
| DiabetesPedigreeFunction | Diabetes pedigree function score | 0.0-2.5 |
| Age | Age of the patient | years |

## 🛠️ Technologies Used

### Backend
- **Flask**: Lightweight Python web framework
- **scikit-learn**: Machine learning library for model and scaler
- **pickle**: For model serialization and deserialization
- **NumPy/Pandas**: Data manipulation and processing

### Frontend
- **HTML5**: Markup structure
- **CSS3**: Styling and responsive design
- **JavaScript**: Client-side interactivity
- **Bootstrap** (optional): For enhanced UI components

### Deployment
- **Render**: Cloud platform for hosting the application

## 📝 Requirements

See `requirements.txt` for the complete list of dependencies:

```
Flask>=2.0.0
scikit-learn>=0.24.0
pandas>=1.2.0
numpy>=1.19.0
```

## 🔒 Security Considerations

- The application validates input data before making predictions
- Model predictions are for informational purposes only
- **Disclaimer**: This application should not be used as a substitute for professional medical advice

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Divya Kumari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software")...
```

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact & Support

- **Author**: Divya Kumari
- **Repository**: [GitHub - diabetes-flask-prediction](https://github.com/Divya-kumari18/diabetes-flask-prediction)
- **Live Application**: [Render Deployment](https://diabetes-flask-prediction-2.onrender.com/predict)

## ⚠️ Disclaimer

This diabetes prediction application is for educational and informational purposes only. The predictions made by this model should not be considered as a substitute for professional medical diagnosis or advice. Always consult with a healthcare professional for proper medical evaluation and diagnosis.

## 🎯 Future Enhancements

- [ ] Add data visualization and analytics
- [ ] Implement user authentication and history tracking
- [ ] Add more features for comprehensive health assessment
- [ ] Improve model accuracy with ensemble methods
- [ ] Create API endpoints for third-party integration
- [ ] Add support for multiple languages
- [ ] Implement unit tests and integration tests

## 📊 Project Statistics

- **Stars**: ⭐ 0
- **Forks**: 🍴 0
- **License**: MIT
- **Status**: Active & Deployed

---

**Last Updated**: 2026  
**Python Version**: 3.7+  
**Status**: Production Ready
