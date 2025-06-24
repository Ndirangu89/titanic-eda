# Titanic Survival Prediction Project

This project explores the Titanic dataset to build a machine learning model that predicts whether a passenger survived or not. It includes data cleaning, visualization, feature engineering, model training, evaluation, and deployment.

---

##  Project Structure

```
titanic-eda/
├── data/                        # Dataset files
├── images/                      # Visualizations (charts, graphs)
├── models/                      # Trained model files (.pkl)
├── notebooks/
│   ├── cleaning.ipynb           # Data cleaning and preprocessing steps
│   ├── visual.ipynb             # Exploratory data visualizations
│   ├── feature_engineering.ipynb # Feature transformation & encoding
│   └── modeling.ipynb           # Model training, evaluation, and tuning
├── predict.py                   # Script to make predictions
├── requirements.txt             # Required Python packages
└── README.md                    # Project overview
```

---

##  Technologies Used

- Python 3.x
- pandas
- numpy
- matplotlib & seaborn
- scikit-learn
- Jupyter Lab / Notebook

---

## How to Run

1. **Clone the repository**

```bash
git clone https://github.com/Ndirangu89/titanic-eda.git
cd titanic-eda
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the notebooks**

Open Jupyter Lab and run the notebooks in this order:

| Notebook                    | Description                             |
| --------------------------- | --------------------------------------- |
| `cleaning.ipynb`            | Handles missing values, drops noise     |
| `visual.ipynb`              | Generates visual insights from the data |
| `feature_engineering.ipynb` | Extracts and encodes features           |
| `modeling.ipynb`            | Builds, tunes, and evaluates models     |

5. **Make predictions using script**

```bash
python predict.py
```

---

## Model Summary

- **Algorithm Used**: Random Forest Classifier (tuned using GridSearchCV)
- **Best Parameters**:\
  `n_estimators=100`, `max_depth=5`, `min_samples_leaf=2`, `min_samples_split=2`
- **Accuracy**: \~83.2% on test data
- **Top Features**: `Sex`, `Title`, `Pclass`, `FamilySize`, `FareBand`

---

## Future Enhancements

- Add XGBoost or Gradient Boosting for better accuracy
- Build a simple web interface using Streamlit or Flask
- Include automated preprocessing pipeline

---

## Acknowledgements

- Kaggle Titanic Dataset
- scikit-learn documentation
- seaborn documentation

---

## Author

**Joshua Ndirangu**\
Student, BSc Mathematics & Computer Science\
Jomo Kenyatta University of Agriculture and Technology (JKUAT)\
GitHub: @Ndirangu89



---

️ If you found this project helpful, feel free to star it!

