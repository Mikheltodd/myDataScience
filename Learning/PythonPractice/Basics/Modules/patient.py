class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  # Methods
  # Estimate Insurance Cost
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print(f"{self.name}’s estimated insurance costs is {estimated_cost} dollars.")

  # Update Age
  def update_age(self, new_age):
    self.age = new_age
    print(f"{self.name} is now {self.age} years old.")
    self.estimated_insurance_cost()

  # Update Number of Children
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print(f"{self.name} has {self.num_of_children} child.")
    else: 
      print(f"{self.name} has {self.num_of_children} children.")
    self.estimated_insurance_cost()

  # Patient Info
  def patient_profile(self):
    patient_information = {"Name": self.name, "Age": self.age, "Sex": self.sex, "BMI": self.bmi, "Number of Children": self.num_of_children, "Smoker": self.smoker}
    return patient_information

  # String Representation
  def __repr__(self):
    patient_info = self.patient_profile()
    profile = f"""
    Patient Data
    -------------
    Name: {patient_info['Name']}
    Age: {patient_info['Age']}
    Sex: {patient_info['Sex']}
    BMI: {patient_info['BMI']}
    Number of Children: {patient_info['Number of Children']}
    Smoker: {patient_info['Smoker']}
    """
    return profile
