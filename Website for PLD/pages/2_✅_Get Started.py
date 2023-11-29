import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page 



img = Image.open("logo.png")
st.set_page_config(page_title="VitaVoyage!", page_icon = img , layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



local_css("style/style.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)

# Title



st.title("‎‎‎ VitaVoyage")
st.divider()
st.write(" ")
st.write(" ")
st.write(" ")

# Create two columns with increased width
col1, col2, col3 = st.columns([2, 1, 2])

# Input form (Left Column)
with col1:
    st.subheader("Please provide your information:")
    fitness_level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advance"])

    # Define colors and messages based on fitness level
    color_mapping = {
        "Beginner": ("green", "Great choice for beginners!"),
        "Intermediate": ("yellow", "Keep pushing yourself!"),
        "Advance": ("red", "Challenging level ahead!")}
    
    # Get the selected fitness level color and message
    selected_color, selected_message = color_mapping.get(fitness_level, ("black", "Unknown fitness level"))
    
    if selected_color == "green":
        st.success(selected_message)
    elif selected_color == "yellow":
        st.warning(selected_message)
    elif selected_color == "red":
        st.error(selected_message)
    else:
        st.write(selected_message)
    
    calories_per_day = st.number_input("Average Calories Per Day", min_value=500, max_value=5000)
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10, max_value=50)
    desired_body_type = st.selectbox("Desired Body Type", ["Lose Weight", "Build Muscle", "Maintain"])
# Define colors and messages based on desired body type
    color_mapping = {
        "Lose Weight": ("green", "Achieve a healthy weight through proper diet and exercise."),
        "Build Muscle": ("red", "Focus on strength training and a protein-rich diet to build muscle mass."),
        "Maintain": ("blue", "Sustain current weight through a balanced diet and regular physical activity.")
        }
# Get the selected fitness level color and message
    selected_color, selected_message = color_mapping.get(desired_body_type, ("black", "Unknown desired body type"))
    if selected_color == "green":
        st.success(selected_message)
    elif selected_color == "red":
        st.error(selected_message)
    elif selected_color == "blue":
        st.info(selected_message)
    else:
        st.write(selected_message)

    # Health Records
    st.header("Additional Info")
    skip_health_records = st.button("Skip")

    # Initialize variables
    blood_pressure = None
    heart_rate = None
    sleep_duration = None

    if not skip_health_records:
        # Blood Pressure input with validation
        blood_pressure = st.text_input("Blood Pressure (e.g., 120/80 mmHg)")
        if blood_pressure and not any(char.isdigit() or char in ['/'] for char in blood_pressure):
            st.warning("Please enter a valid blood pressure format (e.g., 120/80 mmHg)")
            st.stop()

        # Resting Heart Rate input with validation
        heart_rate = st.number_input("Resting Heart Rate (bpm)", min_value=30, max_value=200)

        # Average Sleep Duration input with validation
        sleep_duration = st.number_input("Average Sleep Duration (hours)", min_value=1, max_value=24)

with col2:
    st.empty()

# Recommendations (Right Column)
with col3:
    # Additional Health Tips
    st.subheader("Health Records Tips:")
        # Check sleep duration for the average range
    if sleep_duration is not None:
        if sleep_duration < 6:
                st.warning("Your sleep duration is less than the recommended 6-8 hours. Consider adjusting your sleep routine.")
        elif sleep_duration > 8:
                st.warning("Your sleep duration is more than the recommended 6-8 hours. Ensure quality sleep and consider adjusting your sleep routine.")
        else:
                st.success("Great job! Your sleep duration is within the recommended 6-8 hours.")
        st.header("Recommendations:")

    # Meal Plan
    st.subheader("Meal Plan:")

    # Additional content for meal plan based on desired body type
    if desired_body_type == "Lose Weight":
        st.write("Focus on a calorie deficit and choose nutrient-dense, low-calorie foods.")
        st.write("Include plenty of vegetables, lean proteins, and whole grains in your meals.")
        st.write("Stay hydrated and consider smaller, more frequent meals to manage hunger.")
        st.write("Avoid foods containing your allergens.")
    elif desired_body_type == "Build Muscle":
        st.write("Prioritize protein-rich foods to support muscle growth and repair.")
        st.write("Include a mix of complex carbohydrates and healthy fats for energy.")
        st.write("Consider pre- and post-workout nutrition to optimize muscle recovery.")
        st.write("Avoid foods containing your allergens.")
    elif desired_body_type == "Maintain":
        st.write("Maintain a balanced diet with a mix of macronutrients: proteins, carbohydrates, and fats.")
        st.write("Monitor portion sizes to avoid overeating and maintain a stable weight.")
        st.write("Avoid foods containing your allergens.")
    else:
        st.write("Customize your meal plan based on your specific goals and nutritional needs.")

    # Exercise Regime
    st.subheader("Exercise Regime:")
    if fitness_level == "Beginner":
        st.write("Start slowly and build up gradually.")
        st.write("Then speed up to a pace you can continue for five to 10 minutes without getting overly tired. As your stamina improves, gradually increase the amount of time you exercise. Work your way up to 30 to 60 minutes of exercise most days of the week.")
    elif fitness_level == "Intermediate":
        st.write("Aim to up your training to four days a week.")
        st.write("Focus on compound movements like the squat, bench press, or deadlift.")
        st.write("Remember, nutrition matters when it comes to gains in the gym!")
    elif fitness_level == "Advance":
        st.write("Use heavier weights, one set for each exercise, doing them slowly (5 second up, 5 seconds down), and to exhaustion, making sure to have good form on each exercise.")
        st.write("You would have a protein/carb shake before and after the workout, and a small meal of protein/carbs within 60-90 minutes of the workout.")
    else:
        st.write("Advanced fitness level allows for more intense workouts. Focus on both strength and endurance.")

    # Result Alternatives
    st.header("Result Alternatives:")

    if fitness_level == "Beginner" and desired_body_type == "Lose Weight":
        st.write("Cutting carbs, eating more protein, lifting weights, and getting more sleep are all actions that can promote sustainable weight loss.")
        st.write("Focusing on long-term health and habits that you can stick with over time will help improve your health and are more likely to result in lasting weight loss.")
    elif fitness_level == "Intermediate" and desired_body_type == "Lose Weight":
        st.write("While fasted high-intensity weight lifting may have negative results, low-intensity cardio—which runs primarily on fat—before breaking your fast is good.")
        st.write("Some great choices for burning calories include walking, jogging, running, cycling, swimming, weight training, interval training, yoga, and Pilates.")
    elif fitness_level == "Advance" and desired_body_type == "Lose Weight":
        st.write("Move whenever possible.")


        st.write("Snack smarter and add more veggies to every meal.")
        st.write("Drink more water")

    if fitness_level == "Beginner" and desired_body_type == "Build Muscle":
        st.write("Start light, with just 1- or 2-pound weights.")
        st.write("Lift your weights using controlled movement.")
        st.write("Keep breathing during your workout.")
    elif fitness_level == "Intermediate" and desired_body_type == "Build Muscle":
        st.write("Train 4 Days A Week.")
        st.write("Train Each Muscle Group At Least Twice A Week.")
        st.write("Stick With ONE Program For At Least 12 Weeks.")
    elif fitness_level == "Advance" and desired_body_type == "Build Muscle":
        st.write("Perform resistance training by using moderate to heavy loads, combined with relatively high protein intake, remains the only tried-and-true training method for increasing muscle mass.")

    # Additional Tips
    st.subheader("Additional Tips:")
    if desired_body_type == "Lose Weight":
        st.write("Reduce in eating oily food and food that is high in fats")
    elif desired_body_type == "Build Muscle":
        st.write("Eat fish and chicken, whole grains and beans, nuts and seeds, olive oil and avocados, fresh fruits or veggies to build muscle easily.")
    elif desired_body_type == "Maintain":
        st.write("Avoid eating sweets, unhealthy carbohydrates, fried foods, and spicy food. Also less drinking alcohol.")
    else:
        st.write("To maintain, balance your calorie intake with your activity level.")

# Disclaimer
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write("Please consult with a healthcare or fitness professional before starting any new diet or exercise program.")

# End of the app
st.write("Always prioritize your health and well-being!")


show_images_button = st.button("Show Sample Meal Plan")

# Display images based on button click
if show_images_button:
    # Define image paths based on fitness level and body type
    image_paths = {
        ("Beginner", "Lose Weight"): "Images/begginer, lose weight.png",
        ("Beginner", "Build Muscle"): "Images/beginner, build muscle.png",
        ("Beginner", "Maintain"): "Images/begginer, maintain.png",
        ("Intermediate", "Lose Weight"): "Images/Intermediate, Lose weight.png",
        ("Intermediate", "Build Muscle"): "Images/Intermediate, build muscle.png",
        ("Intermediate", "Maintain"): "Images/Intermediate, maintain.png",
        ("Advance", "Lose Weight"): "Images/advance, lose weight.png",
        ("Advance", "Build Muscle"): "Images/advance, build muscle.png",
        ("Advance", "Maintain"): "Images/advance, maintain.png",
        # Add more mappings as needed
    }

    # Get the selected image path
    selected_image_path = image_paths.get((fitness_level, desired_body_type), "images/default_image.jpg")
    
    # Display the selected image
    selected_image = Image.open(selected_image_path)
    st.image(selected_image, caption=f"Image for {fitness_level} - {desired_body_type}", width=600)
    
    close_images_button = st.button("Close Images")

    # Close the image display if the button is clicked
    if close_images_button:
        st.text("Images closed.")
        st.experimental_rerun()
