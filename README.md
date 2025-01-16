# Life Expectancy Prediction Using WHO Dataset

This project demonstrates the use of machine learning to predict life expectancy based on various health, social, and economic factors. By leveraging the WHO life expectancy dataset, the project aims to identify significant patterns and build a predictive model using regression techniques.

## Project Overview

The project focuses on:
- **Data Cleaning and Preprocessing**: Handling missing values and selecting relevant features from the dataset.
- **Building a Regression Model**: Training a machine learning model to predict life expectancy using Python and Scikit-learn.
- **Model Evaluation**: Assessing model performance using metrics like Mean Squared Error (MSE) and R-squared.
- **Prediction and Insights**: Using the trained model to predict life expectancy for new data inputs and providing insights into key factors influencing life expectancy.

---

## Dataset

The project uses the WHO life expectancy dataset, which includes data on various features such as:
- GDP
- Healthcare expenditure
- Immunization rates
- Population metrics
- Mortality rates

Make sure to download the dataset and place it in the appropriate directory before running the code.

---

## Installation

To set up and run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/life-expectancy-prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd life-expectancy-prediction
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Jupyter Notebook or Python script to execute the project.

---

## Project Structure

```
.
├── data
│   └── life_expectancy_dataset.csv   # Dataset (to be added by the user)
├── notebooks
│   └── Life_Expectancy_Prediction.ipynb   # Jupyter Notebook with code and explanations
├── src
│   └── model.py   # Python script for training and evaluating the model
├── requirements.txt   # Dependencies for the project
└── README.md   # Project documentation
```

---

## Key Features

- **Data Preprocessing**:
  - Handling missing values.
  - Selecting relevant features for model training.

- **Regression Modeling**:
  - Building a simple Linear Regression model using Scikit-learn.
  - Splitting the dataset into training and testing sets.

- **Model Evaluation**:
  - Evaluating the model's performance with metrics like MSE and R-squared.

- **Visualization**:
  - Visualizing the relationships between features and life expectancy using Matplotlib and Seaborn.

---

## How to Use

1. Prepare the dataset by placing it in the `data/` folder.
2. Run the Jupyter Notebook in the `notebooks/` directory to:
   - Explore the data.
   - Preprocess the data.
   - Train the regression model.
   - Evaluate the model's performance.

3. Optionally, use the `src/model.py` script to automate the model training and evaluation process.

---

## Results and Insights

The regression model provides:
- Predictions of life expectancy based on input factors.
- Insights into the key contributors to life expectancy, such as GDP, healthcare access, and immunization rates.

---

## Future Improvements

- Experimenting with advanced regression models like Random Forest and Gradient Boosting.
- Automating hyperparameter tuning for improved model performance.
- Enhancing data visualization for better interpretation of results.

---

## Technologies Used

- **Python**: Core programming language.
- **Libraries**:
  - `Pandas` and `NumPy` for data manipulation.
  - `Scikit-learn` for machine learning.
  - `Matplotlib` and `Seaborn` for visualization.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- The WHO for providing the life expectancy dataset.
- The open-source community for developing the tools and libraries used in this project.
