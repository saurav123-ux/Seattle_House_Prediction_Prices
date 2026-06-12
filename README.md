# 🏠 Seattle House Price Prediction

> *Can we predict what a house in Seattle will sell for — before it hits the market?*  
> This project says **yes** — and shows you how.

A complete end-to-end **Machine Learning project** on the King County, Seattle housing dataset.  
Multiple regression models were trained, compared, and evaluated to find the best predictor of house prices.

---

## 📌 Project Overview

| | |
|---|---|
| 📍 **City** | Seattle, King County, USA |
| 📦 **Dataset** | `kc_house_data.csv` |
| 🎯 **Goal** | Predict house sale prices using ML regression models |
| 🧪 **Models Tested** | Linear Regression, Decision Tree, Random Forest, SVR |
| 🛠️ **Tools** | Python, Jupyter Notebook, Scikit-learn, Pandas, Matplotlib |

---

## 📂 Repository Structure

```
Seattle_House_Prediction_Prices/
│
├── kc_house_data.csv              # Raw dataset (King County housing data)
├── SHP.ipynb                      # Main analysis & ML notebook
├── ML__House_Prediction.ipynb     # Model training & comparison notebook
│
├── Code/SHP/                      # Supporting code files
├── Seattle_House/                 # Additional project files
├── House_Predictor_website/       # Website screenshots & demo video
│
├── House Price Seattle.pptx       # Project presentation
└── Project 14 House Sales...pdf   # Detailed project report
```

---

## 🗃️ About the Dataset

The `kc_house_data.csv` contains **house sale records from King County, Seattle**.

Key features include:

| Feature | Description |
|---|---|
| `price` | 🎯 Target — Sale price of the house |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `sqft_living` | Square footage of living space |
| `sqft_lot` | Square footage of the lot |
| `floors` | Number of floors |
| `waterfront` | Waterfront view (0/1) |
| `grade` | Overall grade of the house |
| `yr_built` | Year the house was built |
| `zipcode` | Location ZIP code |

---

## 🔬 ML Models Trained & Compared

| Model | Type |
|---|---|
| 📈 Linear Regression | Baseline regression model |
| 🌳 Decision Tree Regressor | Non-linear, tree-based model |
| 🌲 Random Forest Regressor | Ensemble of decision trees |
| 🔷 SVR (Support Vector Regressor) | Kernel-based regression |

**Evaluation Metrics used:** R² Score, MAE, RMSE

---

## 🚀 How to Run

**1. Clone the repo**
```bash
git clone https://github.com/saurav123-ux/Seattle_House_Prediction_Prices.git
cd Seattle_House_Prediction_Prices
```

**2. Install dependencies**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

**3. Launch Jupyter Notebook**
```bash
jupyter notebook
```

**4. Open and run**
- Start with `SHP.ipynb` for EDA & preprocessing
- Then `ML__House_Prediction.ipynb` for model training & comparison

---

## 📊 Dashboard Preview

> 📸 Add your screenshots here
```markdown
![Model Comparison](House_Predictor_website(img_video)/screenshot.png)
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---

## 👤 Author

**Saurav Labade**  
Data Analyst | ClickHouse Specialist  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_PROFILE)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/saurav123-ux)

---

## 📄 License

This project is for learning and portfolio purposes only.  
Dataset sourced from publicly available King County housing records.
