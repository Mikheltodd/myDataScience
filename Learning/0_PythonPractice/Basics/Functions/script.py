# # Create calculate_insurance_cost() function below:


# # Initial variables for Maria
# age = 28
# sex = 0
# bmi = 26.2
# num_of_children = 3
# smoker = 0

# # Estimate Maria's insurance cost
# insurance_cost = 250*age - 128*sex + 370*bmi + \
#     425*num_of_children + 24000*smoker - 12500

# print("The estimated insurance cost for Maria is " +
#       str(insurance_cost) + " dollars.")

# # Initial variables for Omar
# age = 35
# sex = 1
# bmi = 22.2
# num_of_children = 0
# smoker = 1

# # Estimate Omar's insurance cost
# insurance_cost = 250*age - 128*sex + 370*bmi + \
#     425*num_of_children + 24000*smoker - 12500

# print("The estimated insurance cost for Omar is " +
#       str(insurance_cost) + " dollars.")

# -------------------------
# Using Functions:
# -------------------------

# Create calculate_insurance_cost() function below:
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + \
        425*num_of_children + 24000*smoker - 12500
    print(
        f"The estimated insurance cost for {name} is {estimated_cost} dollars.")
    return estimated_cost


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(
    name="Maria", age=28, sex=0, bmi=26.2, num_of_children=3, smoker=0)


# Estimate Omar's insurance cost
omar_insurance_cost = calculate_insurance_cost(
    name="Omar", age=35, sex=1, bmi=22.2, num_of_children=0, smoker=1)

# My own insurance cost
mikheltodd_insurance_cost = calculate_insurance_cost(
    name="Mikheltodd", age=28, sex=1, bmi=30, num_of_children=0, smoker=0)
