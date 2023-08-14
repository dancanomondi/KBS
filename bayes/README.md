# Bayesian Network for Medical Diagnosis

This Python code demonstrates the use of Bayesian networks for medical diagnosis. It uses the `pgmpy` library to create a simplified Bayesian network to diagnose whether a patient has a cold or the flu based on their symptoms.

## Requirements

- Python 3.x
- `pgmpy` library (can be installed using `pip install pgmpy`)

## Usage

1. Install the required library by running the following command:

   ```bash
   pip install pgmpy
   ```

2. Run the bayes.py script to perform medical diagnosis using the Bayesian network:

bash

###

python3 bayes.py

###

The script will calculate and display the probabilities of having the flu and having a cold given the patient's symptoms (fever and cough).

Code Explanation
Importing Required Libraries
The script begins by importing the necessary classes from the pgmpy library. These classes include BayesianNetwork for defining the structure of the network, TabularCPD for creating conditional probability tables, and VariableElimination for performing probabilistic inference.

Defining the Bayesian Network Structure
We define the structure of the Bayesian network using the BayesianNetwork class. In our example, the nodes ('Fever', 'Cough', 'Flu', 'Congestion') are connected with edges indicating conditional dependencies.

Defining Conditional Probability Tables (CPTs)
Conditional Probability Tables (CPTs) are defined using the TabularCPD class. Each CPT specifies the probabilities of different states of a variable given the states of its parent variables. For example, cpd_fever defines the probabilities of having or not having a fever.

Adding CPTs to the Model
The defined CPTs are added to the Bayesian network using the add_cpds() method. This associates the probabilities with the network's structure.

Performing Probabilistic Inference
An instance of the VariableElimination class is created to perform probabilistic inference on the network. This class provides methods for querying the network based on observed evidence.

Querying the Network for Diagnosis
We specify evidence for our query (in this case, the patient's symptoms: fever and cough) using the evidence dictionary. The query() method is used to calculate the probabilities of having the flu and having a cold based on the given evidence.

Displaying Results
Finally, the calculated probabilities of having the flu and having a cold are displayed to the user.

Example Output

Probability of having Flu: 0.5475
Probability of having Cold: 0.4525
Disclaimer
This example is a simplified demonstration of Bayesian networks for educational purposes. Real-world medical diagnosis involves more complex factors and considerations.
