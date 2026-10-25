# Customer Churn Prediction & Retention Analytics

## Project Overview

This project analyzes customer churn in a banking customer dataset and develops a machine-learning classification model to estimate the likelihood that a customer will leave.

The objective is to demonstrate how exploratory data analysis, predictive modeling, and model evaluation can support customer analytics and retention-related decision-making.

## Business Problem

Customer attrition can affect revenue, customer relationships, and long-term business performance. Organizations need to understand which customer characteristics are associated with churn and evaluate whether predictive models can help identify customers who may require further attention.

This project explores these questions using historical customer records.

## Dataset

- **Records:** 10,000
- **Target variable:** `Exited`
- **Observed churn rate:** 20.37%
- **Task:** Binary classification
- **Target interpretation:** `1` indicates a customer exited; `0` indicates a customer did not exit.

The observation period and currency units are not established by the dataset documentation used in this project. They are therefore not assumed here.

## Methodology

1. Define the analytical problem.
2. Inspect the data structure and target distribution.
3. Conduct exploratory data analysis.
4. Prepare the modeling features and target variable.
5. Train and evaluate classification models.
6. Assess model performance using metrics relevant to churn detection.
7. Discuss limitations and possible next steps.

## Model Evaluation

The reproduced Random Forest evaluation used a stratified 80/20 train-test split.

| Metric | Reproduced result |
|---|---:|
| Accuracy | 86.45% |
| ROC-AUC | 85.26% |
| Precision for churn | 78.33% |
| Recall for churn | 46.19% |
| F1-score for churn | 58.11% |

These results must be reproduced from the final notebook before being treated as the definitive published results.

## Interpretation

The model distinguishes between customers who exited and customers who did not exit better than random ranking, as reflected by its ROC-AUC.

However, its reproduced churn recall is 46.19%. This means that it failed to identify more than half of the customers who actually exited in the test set. Accuracy alone would therefore give an incomplete picture of its usefulness.

A practical next step is to investigate the precision-recall trade-off and test alternative decision thresholds.

## Limitations

- Predictive performance does not establish that a retention intervention will prevent churn.
- The dataset does not establish the observation window or currency units used for its financial variables.
- Model performance can change when customer populations or business conditions change.
- The results depend on the preprocessing and evaluation procedure used.
- Retention costs, customer lifetime value, and intervention effectiveness have not been established by this model alone.

## Tools

Python, Pandas, NumPy, scikit-learn, Jupyter Notebook, Matplotlib, and Seaborn. Include other tools only if they are actually used in the final project.

## How to Run

1. Download or clone this repository.
2. Install the packages listed in `requirements.txt`.
3. Open the notebook in Jupyter Notebook or Google Colab.
4. Place the dataset in the documented location.
5. Run the notebook cells in order.

The interactive application, if included in this repository, should have its own run instructions based on its actual entry-point filename.

## Project Links

- **Source code:** [Customer-Churn-Analysis](https://github.com/NematullahAmiri/Customer-Churn-Analysis)
- **Portfolio:** [Nematullah Amiri](https://nematullahamiri.github.io/)

## Disclaimer

This project is for analytical demonstration and learning. Predictions should not be treated as verified causes of churn or as evidence that a particular retention action will work.
