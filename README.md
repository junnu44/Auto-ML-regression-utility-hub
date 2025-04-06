# Auto-ML-regression-utility-hub
The AutoML regression utility hub project automates the process of building and optimizing machine learning models for regression tasks.
**AutoML Regression Utility Hub**
**Overview**
The AutoML Regression Utility Hub is a powerful Streamlit-based web application that simplifies the process of building and evaluating machine learning regression models. Built using H2O's AutoML, it empowers users—regardless of expertise—to upload datasets, explore data visually, train models automatically, and evaluate model performance with ease.
**Features**
Features
🔍 Automated Data Profiling
Generates detailed exploratory data analysis using ydata-profiling.

⚙️ AutoML Model Training
Uses H2O's AutoML to automatically select and train the best regression models from a wide range of algorithms.

📈 Performance Metrics
Displays key metrics including MAE, MSE, and R² to evaluate model accuracy.

📤 Upload Any CSV Dataset
Just drag and drop your CSV and start training in seconds.

💾 Model Export
Save and download your best trained model for later use.

🖥️ Streamlit UI
User-friendly interface with interactive components to guide you through each step.
**Installation**
🧰 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/automl-regression-hub.git
cd automl-regression-hub
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Running the App
Launch the Streamlit app:

bash
Copy
Edit
streamlit run automl.py

📦 Requirements
The main libraries used include:

streamlit

pandas

ydata-profiling

h2o

scikit-learn

pyarrow & polars (optional but improves performance)

🧪 Usage Example
Upload a CSV dataset.

View data preview and profiling report.

Select the target column for regression.

The app automatically splits data, trains multiple models, and picks the best one.

View model performance metrics.

Optionally, download the trained model.

🤝 Contributing
Contributions are welcome!
Feel free to fork the repository, suggest features, or fix bugs via pull requests.

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

📬 Contact
For feedback, questions, or support, contact:
📧 junaidsheikhjs2003@gmail.com
