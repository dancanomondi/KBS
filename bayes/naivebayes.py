from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

# Define the Bayesian Network structure
model = BayesianNetwork([('Fever', 'Flu'),
                         ('Cough', 'Flu'),
                         ('Flu', 'Congestion')])

# Define Conditional Probability Tables (CPTs) for each variable

# CPD for 'Fever'
cpd_fever = TabularCPD(variable='Fever', variable_card=2, values=[[0.7], [0.3]])

# CPD for 'Cough'
cpd_cough = TabularCPD(variable='Cough', variable_card=2, values=[[0.6], [0.4]])

# CPD for 'Flu', which depends on 'Fever' and 'Cough'
cpd_flu = TabularCPD(variable='Flu', variable_card=2, values=[[0.8, 0.1, 0.1, 0.01],
                                                               [0.2, 0.9, 0.9, 0.99]],
                     evidence=['Fever', 'Cough'], evidence_card=[2, 2])

# CPD for 'Congestion', which depends on 'Flu'
cpd_congestion = TabularCPD(variable='Congestion', variable_card=2, values=[[0.9, 0.4],
                                                                           [0.1, 0.6]],
                            evidence=['Flu'], evidence_card=[2])

# Add CPTs to the model
model.add_cpds(cpd_fever, cpd_cough, cpd_flu, cpd_congestion)

# Create an inference object using Variable Elimination algorithm
inference = VariableElimination(model)

# Query the network for diagnosis
evidence = {'Fever': 1, 'Cough': 1}  # Patient has fever and cough
flu_prob = inference.query(variables=['Flu'], evidence=evidence).values[1]
cold_prob = 1 - flu_prob

# Print the probabilities
print("Probability of having Flu:", flu_prob)
print("Probability of having Cold:", cold_prob)

# Draw the Bayesian Network
pos = nx.spring_layout(model, seed=42)
nx.draw(model, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_color='black')

# Show the plot
plt.show()
