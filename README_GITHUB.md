# 🧠 HCI Exam Review - Interactive Study Tool

A beautiful, interactive web-based study tool for mastering Human-Computer Interaction (HCI) concepts. Features 5 different study modes, a comprehensive database of 149 HCI terms, and gorgeous visual design.

![Study Modes](https://img.shields.io/badge/Study%20Modes-5-brightgreen)
![Terms](https://img.shields.io/badge/Terms-149-blue)
![Questions](https://img.shields.io/badge/Questions-7%20per%20term-orange)

## ✨ Features

### 🎮 5 Interactive Study Modes

1. **🎴 Flashcards** - Click to flip cards and review terms with definitions
2. **✅ Multiple Choice** - Test your knowledge with instant feedback
3. **✏️ Fill in the Blank** - Type the correct term based on definitions
4. **🔗 Card Matching** - Match terms with their definitions
5. **🗂️ Model Categorization** - Drag & drop terms into model type categories (NEW!)

### 📚 Comprehensive Content

- **149 HCI Terms** with complete definitions
- **7 Categories**: General, UX in SE, UX Process, Analysis, Design, Prototyping, Evaluation
- **7 Questions per term**: Definition, importance, usage, examples, process fit, best practices, comparisons
- **677 Total answers** covering all aspects of each concept

### 🎨 Beautiful Design

- Gradient purple/pink background with twinkling stars
- Glassmorphic (frosted glass) interface elements
- Smooth animations and transitions
- Fully responsive design (desktop and mobile)
- Modern typography with Poppins and Space Grotesk fonts

### 📊 Study Features

- **Topic Selection** - Choose specific categories or study all topics
- **Custom Questions** - Select 5-50 questions per session
- **Progress Tracking** - Visual progress bar and question counter
- **Score Display** - Detailed results with personalized messages
- **Review Answers** - Review all questions with correct/incorrect indicators
- **Instant Feedback** - Immediate visual feedback on all answers

## 🚀 Quick Start

### Option 1: Simple Start (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd HCI_review

# Start the web server
./start_website.sh
```

The website will automatically open at `http://localhost:8000`

### Option 2: Manual Start

```bash
# Start Python HTTP server
python3 -m http.server 8000

# Open in browser
open http://localhost:8000
```

### Option 3: Direct Open

Double-click `index.html` in your file browser (may have CORS issues with some browsers)

## 📁 Project Structure

```
HCI_review/
├── index.html              # Main interactive study website
├── hci_data.json          # Complete database (149 terms, 677 answers)
├── hci_exam_review.db     # SQLite database
├── start_website.sh       # Easy launch script
├── study_tool.py          # Command-line study tool
├── export_to_json.py      # Database to JSON exporter
├── README.md              # Main documentation
├── QUICK_START.md         # Quick reference guide
├── WEBSITE_GUIDE.md       # Detailed website usage
└── query_examples.sql     # SQL query examples

Database Population Scripts:
├── create_database.sql    # Database schema
├── populate_database.py   # Initial data (General, UX in SE, UX Process)
├── populate_analysis.py   # Analysis section
├── populate_design.py     # Design section
└── populate_remaining.py  # Prototyping & Evaluation
```

## 🎯 Study Modes Explained

### 🎴 Flashcards
Perfect for initial learning and quick review. Click to flip between term and definition.

### ✅ Multiple Choice
Test your recall with 4-option quizzes. Instant green/red feedback shows correct answers.

### ✏️ Fill in the Blank
Advanced mode - type the term name based on the definition. Great for testing deep understanding.

### 🔗 Card Matching
Match terms with definitions. Click a term, then click its matching definition.

### 🗂️ Model Categorization ⭐ NEW!
Drag and drop terms into their correct model categories:
- **User Models** (Personas, Work Roles, User Classes, Social Models)
- **Usage Models** (Flow Model, Task Inventory, Scenarios, Interaction Models)
- **Work Environment Models** (Artifact Model, Physical Model)
- **UX Process** (Lifecycle, Iteration, Analysis, Design, Prototyping, Evaluation)
- **Design Paradigms** (Engineering, HIP, Design-Thinking)
- **Evaluation Methods** (Formative/Summative, Analytic/Empirical, Heuristic, RITE)

Perfect for understanding how concepts relate to each other!

## 📖 Database Contents

### Categories

1. **General** (9 terms) - HCI, UX, UI, Design, Usability, etc.
2. **UX in Software Engineering** (4 terms) - Integration and success factors
3. **Overall UX Process** (7 terms) - The UX Lifecycle/Wheel
4. **Analysis** (33 terms) - Contextual inquiry, DIMs, requirements
5. **Design** (73 terms) - Design thinking, affordances, heuristics
6. **Prototyping** (10 terms) - Fidelity, types, tools
7. **Evaluation** (13 terms) - Methods and approaches

### 7 Questions for Each Term

1. What does it mean?
2. Why is it important?
3. When and/or where is it used?
4. What are some examples?
5. How does it fit into the process?
6. What does doing it well look like?
7. How is it similar/different from related terms?

## 🛠️ Technology Stack

- **Frontend**: Pure HTML5, CSS3, JavaScript (ES6+)
- **Database**: SQLite3
- **Data Format**: JSON for web, SQLite for desktop
- **Fonts**: Google Fonts (Poppins, Space Grotesk)
- **No Dependencies**: Works completely offline (except fonts)

## 💡 Usage Tips

1. **Start with Flashcards** to familiarize yourself with terms
2. **Use Multiple Choice** to test recall
3. **Try Fill in Blank** for deeper understanding
4. **Use Matching** to reinforce connections
5. **Practice Categorization** to understand relationships
6. **Focus on weak categories** by selecting specific topics
7. **Review wrong answers** to learn from mistakes

## 🎓 Perfect For

- **CS 3205 HCI Students** - Complete exam review
- **UX/UI Learners** - Comprehensive HCI fundamentals
- **Design Students** - Design thinking and processes
- **Anyone studying HCI** - Professional development

## 📱 Browser Compatibility

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers (iOS/Android)

## 🔧 Advanced Usage

### Using the SQLite Database

```bash
# Open database
sqlite3 hci_exam_review.db

# View all terms
SELECT name FROM terms;

# Search for specific concept
SELECT * FROM terms WHERE name LIKE '%usability%';

# Get all answers for a term
SELECT q.question_text, a.answer_text
FROM terms t
JOIN answers a ON t.id = a.term_id
JOIN questions q ON a.question_id = q.id
WHERE t.name = 'User Experience (UX)';
```

See `query_examples.sql` for 20+ helpful queries!

### Using the Command-Line Tool

```bash
python3 study_tool.py
```

Interactive menu with:
- Browse by category
- Search terms
- Random flashcards
- Quiz mode
- View Nielsen's heuristics

## 🎨 Customization

The website uses CSS variables for easy customization:

```css
:root {
    --primary: #6366f1;      /* Purple */
    --secondary: #ec4899;    /* Pink */
    --accent: #14b8a6;       /* Teal */
    --success: #22c55e;      /* Green */
    --danger: #ef4444;       /* Red */
}
```

## 📝 License

This project is for educational purposes. Feel free to use and modify for your studies!

## 🤝 Contributing

This is a study tool project. Feel free to fork and customize for your needs!

## 📧 Credits

Created for CS 3205 Fall 2025 Final Exam Review
All content based on HCI/UX best practices and course materials

---

**Good luck on your exam!** 🎉📚

Made with ❤️ for HCI students
