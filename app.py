from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/') # for home page
def home():
    # Logic to fetch user's fitness data (workout summary, calories burned, goals achieved)
    workout_summary = "Summary"
    calories_burned = "Calories burned"
    goals_achieved = "Goals achieved"
    return render_template('home.html', summary=workout_summary, calories=calories_burned, goals=goals_achieved)

@app.route('/workout_log')
def workout_log():
    # Logic to fetch and display workout log
    return render_template('workout_log.html')

@app.route('/goals')
def goals():
    # Logic to fetch and display goals
    return render_template('goals.html')

@app.route('/profile')
def profile():
    # Logic to fetch and display user profile
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
