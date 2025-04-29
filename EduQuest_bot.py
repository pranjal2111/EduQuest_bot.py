import telebot
from telebot import types

# Set up your Telegram Bot API
TELEGRAM_BOT_TOKEN = "7637066152:AAE7YBTHNn3n_UY-Jk6rH6G-I0TSZoSxF54"  # Replace with your actual token
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Study materials for different engineering branches
study_materials = {
    "computer science": {
        "Data Structures": "https://www.geeksforgeeks.org/data-structures/",
        "Algorithms": "https://www.geeksforgeeks.org/fundamentals-of-algorithms/",
        "Operating Systems": "https://www.geeksforgeeks.org/operating-systems/",
        "Database Management": "https://www.javatpoint.com/dbms-tutorial",
        "Software Engineering": "https://www.geeksforgeeks.org/software-engineering/",
        "Web Development": "https://www.w3schools.com/",
        "Computer Networks": "https://www.geeksforgeeks.org/computer-network-tutorials/",
        "Theory of Computation": "https://www.geeksforgeeks.org/theory-of-computation/"
    },
    "electrical engineering": {
        "Basic Electrical Engineering": "https://www.electrical4u.com/basic-electrical-engineering/",
        "Circuit Theory": "https://www.electrical4u.com/circuit-theory/",
        "Electrical Machines": "https://www.electrical4u.com/electrical-machines/",
        "Control Systems": "https://www.geeksforgeeks.org/control-systems/",
        "Power Systems": "https://www.electrical4u.com/power-systems/",
        "Signal Processing": "https://www.geeksforgeeks.org/digital-signal-processing/"
    },
    "civil engineering": {
        "Engineering Mechanics": "https://www.civilengineeringnotes.com/engineering-mechanics/",
        "Building Materials": "https://www.civilengineeringnotes.com/building-materials/",
        "Structural Analysis": "https://www.civilengineeringnotes.com/structural-analysis/",
        "Fluid Mechanics": "https://www.civilengineeringnotes.com/fluid-mechanics/"
    },
    "mechanical engineering": {
        "Engineering Mechanics": "https://www.mechanicalc.com/engineering-mechanics/",
        "Thermodynamics": "https://www.mechanicalc.com/thermodynamics/",
        "Fluid Mechanics": "https://www.mechanicalc.com/fluid-mechanics/",
        "Manufacturing Processes": "https://www.mechanicalc.com/manufacturing-processes/"
    },
    "chemical engineering": {
        "Chemical Process Principles": "https://www.chemengonline.com/",
        "Thermodynamics": "https://www.chemengonline.com/",
        "Fluid Mechanics": "https://www.chemengonline.com/",
        "Chemical Reaction Engineering": "https://www.chemengonline.com/"
    }
}

# Programming course links
programming_courses = {
    "Python Programming": "https://www.javatpoint.com/python-tutorial",
    "Java Programming": "https://www.javatpoint.com/java-tutorial",
    "C++ Programming": "https://www.javatpoint.com/cpp-tutorial",
    "JavaScript Programming": "https://www.javatpoint.com/javascript-tutorial"
}

# Career guidance links
career_guidance = {
    "Career after 10th": "https://www.upgrad.com/blog/career-options-after-10th/",
    "Career after 12th": "https://leverageedu.com/blog/career-options-after-12th/",
    "Engineering Internships": "https://internshala.com/internships/engineering-internship",
    "Job Portals": "https://www.naukri.com/"
}

# Power BI Dashboard Link
powerbi_dashboard_link = "https://1drv.ms/i/c/9a60649479305454/EYNO4ahofT5LgH-AtA2-U94BPPQmwHlmGpeYoBKxsIPeng?e=MJfbQc"  # Replace with your actual Power BI dashboard link

# Function to search for keywords in the user's message
def search_keywords(message):
    input_text = message.text.lower()
    response = []

    # Check for study materials
    for branch, subjects in study_materials.items():
        for subject, link in subjects.items():
            if subject.lower() in input_text:
                response.append(f"{subject}: {link}")

    # Check for programming courses
    for course, link in programming_courses.items():
        if course.lower() in input_text:
            response.append(f"{course}: {link}")

    # Check for career guidance
    for career, link in career_guidance.items():
        if career.lower() in input_text:
            response.append(f"{career}: {link}")

    # Check for Power BI dashboard request
    if "power bi" in input_text or "dashboard" in input_text:
        response.append(f"Here is the Power BI dashboard you requested: {powerbi_dashboard_link}")

    return "\n".join(response) if response else "I'm sorry, I couldn't find any relevant information."

# Handle commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Study Materials"))
    markup.add(types.KeyboardButton("Programming Courses"))
    markup.add(types.KeyboardButton("Career Guidance"))
    markup.add(types.KeyboardButton("Power BI Dashboard"))

    welcome_message = (
        "🙏 Namaste! 👋 Welcome to the Study Bot! 🎓\n\n"
        "I'm here to assist you with various resources related to your studies and career. Here's what I can help you with:\n\n"
        
        "📚 Study Materials\n"
        "You can ask for specific study materials related to different engineering branches. For example:\n"
        "- Computer Science: 'Data Structures', 'Algorithms', 'Operating Systems'\n"
        "- Electrical Engineering: 'Circuit Theory', 'Control Systems'\n"
        "- Civil Engineering: 'Fluid Mechanics', 'Structural Analysis'\n\n"
        
        " 💻 Programming Courses\n"
        "Inquire about programming courses to enhance your coding skills. You can ask about:\n"
        "- Python Programming\n"
        "- Java Programming\n"
        "- C++ Programming\n"
        "- JavaScript Programming\n\n"
        
        " 🎓 Career Guidance\n"
        "Seek advice on career options and guidance after your studies. You can ask about:\n"
        "- Career after 10th\n"
        "- Career after 12th\n"
        "- Internship Opportunities\n"
        "- Job Portals\n\n"
        
        " 📊 Power BI Dashboard\n"
        "- Request access to the Power BI dashboard for data visualization and insights. Just ask:\n"
        "- Show me the Power BI dashboard\n\n"
        
        " 💡 How to Use Me\n"
        " Just type your question or request in the chat, and I'll do my best to assist you! 😊"
    )
    bot.reply_to(message, welcome_message, reply_markup=markup)

# Handle user input
@bot.message_handler(func=lambda message: True)
def handle_input(message):
    if message.text == "Study Materials":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Computer Science"))
        markup.add(types.KeyboardButton("Electrical Engineering"))
        markup.add(types.KeyboardButton("Civil Engineering"))
        markup.add(types.KeyboardButton("Mechanical Engineering"))
        markup.add(types.KeyboardButton("Chemical Engineering"))
        markup.add(types.KeyboardButton("Back"))

        bot.reply_to(message, "Select an engineering branch:", reply_markup=markup)

    elif message.text == "Programming Courses":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Python Programming"))
        markup.add(types.KeyboardButton("Java Programming"))
        markup.add(types.KeyboardButton("C++ Programming"))
        markup.add(types.KeyboardButton("JavaScript Programming"))
        markup.add(types.KeyboardButton("Back"))

        bot.reply_to(message, "Select a programming course:", reply_markup=markup)

    elif message.text == "Career Guidance":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Career after 10th"))
        markup.add(types.KeyboardButton("Career after 12th"))
        markup.add(types.KeyboardButton("Engineering Internships"))
        markup.add(types.KeyboardButton("Job Portals"))
        markup.add(types.KeyboardButton("Back"))

        bot.reply_to(message, "Select a career guidance option:", reply_markup=markup)

    elif message.text == "Power BI Dashboard":
        bot.reply_to(message, f"Here is the Power BI dashboard you requested: {powerbi_dashboard_link}")

    elif message.text == "Back":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Study Materials"))
        markup.add(types.KeyboardButton("Programming Courses"))
        markup.add(types.KeyboardButton("Career Guidance"))
        markup.add(types.KeyboardButton("Power BI Dashboard"))

        bot.reply_to(message, "Welcome back! What can I help you with?", reply_markup=markup)

    elif message.text in study_materials:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for subject in study_materials[message.text]:
            markup.add(types.KeyboardButton(subject))
        markup.add(types.KeyboardButton("Back"))

        bot.reply_to(message, f"Select a subject in {message.text}:", reply_markup=markup)

    elif message.text in programming_courses:
        bot.reply_to(message, f"Here is the link to {message.text}: {programming_courses[message.text]}")

    elif message.text in career_guidance:
        bot.reply_to(message, f"Here is the link to {message.text}: {career_guidance[message.text]}")

    else:
        response = search_keywords(message)
        bot.reply_to(message, response)

# Run the bot
print("Bot is running...")
bot.polling()