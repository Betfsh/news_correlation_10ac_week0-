# news_correlation_10ac_week0

This repository contains the code and documentation for the News Correlation Analysis project. The project aims to perform exploratory data analysis (EDA), statistical analysis, sentiment analysis, topic modeling, and more on a dataset comprising news articles from various sources.
It will explore the relationship between the news presenting websites and quantify different characterstics by comparison. By conducting this analysis into different aspects and features of these websites,meaningful insights can be obtained.                          
Gathered  data, such as the news articles, domain locations, and website trafficdata will be  compared and analyzed in  various aspects, such as sentiment analysis of article titles, traffic ranks, and domain locations.

Quantifying these characteristics and comparing them across different news presenting websites, interesting patterns or correlations will be shown. This analysis may provide valuable insights into how various factors, like sentiment, traffic, and geographic location, contribute to the success or popularity of news websites.

## Table of Contents

- [Introduction](#introduction)
- [How to get started](#how-to-clone-the-repository)
- [Project Structure](#project-structure)
- [Task Overview](#task-overview)
- [Task 1: Project Setup and EDA](#task-1-project-setup-and-eda)
- [Task 2: Data Science Component Building](#task-2-data-science-component-building)
- [Task 3: PostgreSQL](#task-3-postgresql)
- [Task 4: Dashboards](#task-4-dashboards)
- [Contributions](#contributing)
- [License](#license)

## Introduction

This project is centered around the analysis of news data to reveal valuable insights including top news websites, traffic patterns, sentiment analysis, topic modeling, and other pertinent aspects. The dataset encompasses details about news articles such as their source, author, content, sentiment, and publication date. Through the application of diverse data science methodologies, the goal is to extract actionable insights that provide a deeper understanding of the news landscape.

## How to get started

This section will guide you through cloning the repository and setting up your development environment.

### Prerequisites

Git installed on your system. You can download and install Git from https://git-scm.com/downloads

### Steps

1. Go to terminal window.

2. Navigate to the desired directory on your local machine where you want to clone the repository. You can use the cd command to change directories.:

3. Clone the repository using the following command:

   ``` bash
   git clone git@github.com:Betfsh/news_correlation_10ac_week0-.git
   
   cd news_correlation_10ac_week0
   ```
4. Install the required dependencies:
   
   ```bash
    pip install -r requirements.txt

## Project Structure

The project is structured as follows:

- .github
  - workflows
    - flake8_check.yml
    - unittests.yml
    - docstring_tests.yml
- .vscode
  - settings.json
- model
  - saved_model_weights.h5
- notebooks
  - news_correlation.ipynb
- screenshoots: screenshots of the streamlit dashboard.
- src
  - csv_handler.py
  - database.py
  - loader.py
  - main.py
  - utils.py
- tests
  - __init__.py
- .gitignore
- README.md
- app.py
- config.json
- requirements.txt

## Task Overview

The project is divided into multiple tasks:

1. **Project Setup and EDA**: Setup Python environment, perform exploratory data analysis, and answer specific questions about the data.
2. **Data Science Component Building**: Develop components for machine learning operations (MLOps), conduct time series analysis, classification of headlines, topic modeling, sentiment analysis, and predictive modeling.
3. **PostgreSQL**: Design database schema, load data into PostgreSQL, and utilize it for storing ML features.
4. **Dashboards**: Design and implement a dashboard using Streamlit or React to visualize analysis results.
5. **Deployment**: Deploy the project using GitHub Actions for continuous deployment, and configure environment variables and PostgreSQL database.

## Task 1: Project Setup and EDA

- **Git and GitHub Setup**: Created a GitHub repository and set up version control.
- **Python Environment Setup**: Prepared a Python environment for data analysis.
- **Exploratory Data Analysis (EDA)**: Analyzed the dataset to answer various questions about news articles, including top websites, traffic analysis, sentiment analysis, and more.


