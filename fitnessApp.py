  
def health_tracker():
    # Take user inputs for weight, height, and age
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters (e.g., 175 for 175 cm): "))
    age = float(input("Enter your age in years: "))
    
    def bmiCheck(weight, height):
        # Convert height from centimeters to meters
        height_in_meters = height / 100

        # Calculate BMI
        heightSq = height_in_meters * height_in_meters
        bmi = weight / heightSq

        # Display the result
        print(f"\nYour BMI (Body Mass Index) is: {bmi:.2f}")
        return bmi

    def bmi_output_rating(bmi):
        if bmi < 18.5:
            print("You are underweight")
        elif 18.5 <= bmi < 24.9:
            print("You are healthy!!! Keep it up!")
        elif 25 <= bmi <= 29.9:
            print("You are overweight! Consider improving your fitness.")
        elif bmi >= 30:
            print("You are obese. Focus on improving your health.")

    def bmr_ratio(weight, height, age):
        gender = input("Enter your gender to know the BMR (enter 'man' or 'woman'): ").strip().lower()
        if gender == "man":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        elif gender == "woman":
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        else:
            print("Invalid input for gender. Please enter 'man' or 'woman'.")
            return None

        print(f"\nYour Basal Metabolic Rate (BMR) is: {bmr:.2f} calories/day")
        return bmr

    def total_daily_cal(bmr):
        print("""
        Please select your activity level:
        Enter "Sedentary" for little or no exercise.
        Enter "Light" for light exercise.
        Enter "Moderate" for moderately active days.
        Enter "Active" for very active days.
        Enter "Extra Active" for heavily active schedules.
        ----------------------------------------------------------------
        """)
        
        # Take user input and normalize case
        user_input = input("Enter your activity level: ").strip().capitalize()
        
        # Calculate daily calorie needs based on activity level
        if user_input == "Sedentary":
            daily_calories = bmr * 1.2
        elif user_input == "Light":
            daily_calories = bmr * 1.375
        elif user_input == "Moderate":
            daily_calories = bmr * 1.55
        elif user_input == "Active":
            daily_calories = bmr * 1.725
        elif user_input == "Extra Active":
            daily_calories = bmr * 1.9
        else:
            print("Invalid input. Please enter a valid activity level.")
            return None

        print(f"Your daily calorie need based on your activity level is: {daily_calories:.2f} calories/day.")
        return daily_calories

    def target_weight_to_achieve(current_weight, target_weight, time_frame_days, bmr, activity_level_calories):
        # Calculate the total weight difference (kg)
        weight_difference = current_weight - target_weight
        total_calories_needed = weight_difference * 7700  # 7700 calories per kg

        # Calculate the daily calorie deficit or surplus needed
        daily_calories_needed = total_calories_needed / time_frame_days

        # Calculate the target daily calorie intake
        target_daily_calories = activity_level_calories - daily_calories_needed

        print(f"\nTo achieve your target weight of {target_weight} kg in {time_frame_days} days,")
        print(f"You will need a daily calorie deficit or surplus of {daily_calories_needed:.2f} calories.")
        print(f"Your target daily calorie intake should be: {target_daily_calories:.2f} calories/day.")
    
    # Main flow of the health tracker function
    bmi = bmiCheck(weight, height)
    bmi_output_rating(bmi)
    bmr = bmr_ratio(weight, height, age)
    activity_level_calories = total_daily_cal(bmr)

    target_weight = float(input("\nEnter your target weight in kilograms: "))
    time_frame_days = int(input("Enter your target time frame in days: "))

    # Call the target weight function
    target_weight_to_achieve(weight, target_weight, time_frame_days, bmr, activity_level_calories)

# Call the health_tracker function to run the program
health_tracker()
