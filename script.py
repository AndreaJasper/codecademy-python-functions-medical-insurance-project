# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output_message = "The estimated insurance cost for " + name + "  is " + str(estimated_cost) + " dollars."
  return output_message, estimated_cost

def insurance_cost_difference(name1, cost1, name2, cost2):
  cost_difference = abs(cost1 - cost2)
  print("The difference in insurance cost between " + name1 + " and " + name2 + " is " + str(cost_difference) + " dollars.")

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)
maria_output_message, maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)
print(maria_output_message)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)
omar_output_message, omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)
print(omar_output_message)

andrea_insurance_cost = calculate_insurance_cost(name = "Andrea", age = 32, sex = 0, bmi = 26.2, num_of_children = 1, smoker = 0)
andrea_output_message, andrea_insurance_cost = calculate_insurance_cost(name = "Andrea", age = 32, sex = 0, bmi = 26.2, num_of_children = 1, smoker = 0)
print(andrea_output_message)

# Calculate the difference in insurance cost between Maria and Omar
insurance_cost_difference("Maria", maria_insurance_cost, "Omar", omar_insurance_cost)

# Calculate the difference in insurance cost between Maria and Andrea
insurance_cost_difference("Maria", maria_insurance_cost, "Andrea", andrea_insurance_cost)

# Calculate the difference in insurance cost between Andrea and Omar
insurance_cost_difference("Andrea", andrea_insurance_cost, "Omar", omar_insurance_cost, )

