# Adjective Counter by Age Group – Women’s E-Commerce Clothing Reviews

This project investigates how women from different age groups describe their clothing purchases in online reviews. Using a dataset of nearly 23,500 women’s clothing reviews from Kaggle, I developed a Python program to extract and count adjectives and analyze their distribution across age groups.

🧪 This was completed as a final project for the *Methods in Computational Linguistics I* course at the CUNY Graduate Center (Fall 2024).

## 📊 Research Goal

Do women of different ages prioritize different clothing characteristics—and can this be observed through their use of adjectives?

By examining adjective frequency across eight age groups (18–29 through 90–99), this project explores possible sociolinguistic insights into how language use reflects consumer preferences across generations.

## 🗂 Dataset

- Source: [Women’s E-Commerce Clothing Reviews (Kaggle)](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews)
- 23,486 reviews (cleaned to 22,643)
- Grouped into 8 age intervals: 18–29, 30–39, ..., 90–99

## 🛠️ Program Design

The script:
- Reads text data and converts it to lowercase
- Counts adjective frequency using Python dictionaries
- Normalizes adjective counts by the number of reviews per age group
- Outputs both raw and normalized tables of adjective use

## 📈 Key Findings

- "Soft" and "comfortable" were consistently among the most used adjectives across all age groups
- Unexpected patterns emerged—for example, the word "sexy" peaked among reviewers aged 80–89
- Adjectives like "trendy" and "versatile" also showed distinct age-related patterns

These patterns could have implications for intergenerational marketing and sociolinguistic studies of consumer language.

## 🧠 Limitations & Reflections

- Sentiment context (positive vs. negative) was not considered—for example, "too sexy" vs. "very sexy"
- Future versions could dynamically group and analyze data without needing separate text files per age group
- Expanding to sentiment analysis or broader word categories could enrich the results

## 📁 Repo Contents

AdjectiveCounter_AgeGroup/
├── Womens Clothing E-Commerce Reviews.csv # Cleaned dataset
├── counter.py # Python script for adjective counting
├── counter_results.xlsx # Normalized and raw count tables
├── counter_WriteUp.pdf # Final project report (term paper)
├── README.md # Project overview
└── .gitignore

## 📚 Acknowledgments

This project was developed under the guidance of Prof. Spencer Caplan at the Graduate Center, CUNY.

