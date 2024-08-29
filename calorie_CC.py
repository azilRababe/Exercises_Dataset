activity_levels = {
    "sedentary": 1.2,
    "lightly": 1.375,
    "moderate": 1.55,
    "active": 1.725,
    "very_active": 1.9
}

def female_calorie_calculator(weight, height, age, activity_level):
    # Calculate BMR
    BMR= 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

    calories = BMR * activity_levels[activity_level]

    calorie_message(calories)

def male_calorie_calculator(weight, height, age, activity_level):
    # Calculate BMR
    BMR= 66.5 + (13.75 * weight) + (5 * height) - (6.75 * age)
   
    calories =  BMR * activity_levels[activity_level]

    calorie_message(calories)

def calorie_message(calories):
    maintenance = f"To maintain your current weight: {round(calories)} calories/day"
    lose_weight = f"To lose weight: {round(calories) - 500} calories/day"
    gain_weight = f"To gain weight: {round(calories) + 500} calories/day"

    for message in [maintenance, lose_weight, gain_weight]:
        print(message)
