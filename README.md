# IFCO Data Engineering Challenge

### Project Description
Welcome to the IFCO Data Engineering Challenge! The goal of this project is to analyze business data and solve five defined scenarios that cover data transformation, integration and analysis. The provided data originates from a CSV file (*orders*) and a JSON file (*invoicing data*) and is processed using Python. Also, unit tests are provided for each scenario to ensure the reliability, accuracy, and correctness of the code. This project demonstrates skills in data manipulation, transformation logic, and test-driven development using Python.


### Project Structure
ifco-data-challenge/  
├── data/  
│   ├── orders.csv  
│   └── invoicing_data.json  
├── src/  
│   ├── functions.py  
│   └── main.py  
├── tests/  
│   └── test_functions.py  
├── requirements.txt  
└── README.md  

- **data/**: Contains input files (orders.csv and invoicing_data.json).
- **src/**: Contains the main scripts for data processing and analysis.
- **main.py**: Entry point for running the solution.
- **functions.py**: Contains utility functions for data loading, transformation, and analysis.
- **tests/**: Contains unit tests using `unittest`.
- **requirements.txt**: Contains dependencies needed to run the solution.
- **README.md**: Project documentation.


### Requirements
The project requires Python 3.8+ and the following libraries:  

- `pandas`
- `json`
- `unittest`

To install the dependencies, run:  
    ```pip install -r requirements.txt```


### Instructions for Execution
1. Clone the repository and navigate to the project folder:  
    ```git clone <https://github.com/mschaberger/ifco-data-challenge-ms.git>```

2. Ensure that the input files (orders.csv and invoicing_data.json) are present in the **data/** directory.

3. To run the main script:  
    ```python src/main.py```

4. To run the unit tests:  
    ```python -m unittest discover -s tests/```


### Detailed Tasks and Solutions
- Distribution of Crate Type per Company: Computes the distribution of crate types per company using **get_crate_distribution_per_company()**.
- DataFrame of Orders with Contact Full Name: Creates a DataFrame with the full name of contacts using **create_contact_full_name()**.
- DataFrame of Orders with Contact Address: Generates a DataFrame with formatted contact addresses using **create_contact_address()**.
- Calculation of Sales Team Commissions: Computes sales commissions for sales owners based on net invoice values using **calculate_commissions()**.
- DataFrame of Companies with Sales Owners: Creates a DataFrame listing unique sales owners for each company using **create_company_salesowners_df()**.

### Unit Testing
The tests/test_functions.py file contains unit tests for all implemented functions. Tests cover typical scenarios, edge cases, and unexpected data conditions to ensure correctness and reliability.
