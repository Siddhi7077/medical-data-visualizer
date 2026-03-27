import csv
import random

# Define headers
headers = ["age","height","weight","gender","ap_hi","ap_lo","cholesterol","gluc","smoke","alco","active","cardio"]

# Open file
with open("medical_examination.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)

    # Generate 350 random records
    for _ in range(350):
        age = random.randint(15000, 25000)   # age in days (~41–68 years)
        height = random.randint(150, 190)    # cm
        weight = random.randint(50, 120)     # kg
        gender = random.choice([1, 2])       # 1=female, 2=male
        ap_hi = random.randint(100, 180)     # systolic
        ap_lo = random.randint(60, 120)      # diastolic
        cholesterol = random.choice([1, 2, 3])
        gluc = random.choice([1, 2, 3])
        smoke = random.choice([0, 1])
        alco = random.choice([0, 1])
        active = random.choice([0, 1])
        cardio = random.choice([0, 1])

        writer.writerow([age, height, weight, gender, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio])
