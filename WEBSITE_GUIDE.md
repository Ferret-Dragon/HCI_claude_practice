# HCI Study Website Guide

## 🎨 Features

Your new interactive study website includes:

### 4 Study Modes

1. **🎴 Flashcards** - Click to flip cards and review terms with definitions
2. **✅ Multiple Choice** - Test your knowledge with quiz questions
3. **✏️ Fill in the Blank** - Type the correct term based on the definition
4. **🔗 Card Matching** - Match terms with their definitions

### Customization Options

- **Topic Selection** - Choose specific categories or study all topics
- **Question Count** - Select how many questions you want (5-50)
- **Progress Tracking** - Visual progress bar and question counter
- **Score Display** - See your results at the end with personalized messages

### Design Features

- **Colorful gradient background** with animated twinkling stars
- **Modern glassmorphism design** with blur effects
- **Smooth animations** and transitions
- **Responsive design** - works on desktop and mobile
- **Beautiful typography** using Poppins and Space Grotesk fonts

## 🚀 How to Use

### Starting the Website

1. **Open in browser:**
   ```bash
   # Option 1: Double-click index.html in Finder

   # Option 2: Open from terminal
   open index.html

   # Option 3: Use a local server (recommended)
   python3 -m http.server 8000
   # Then visit: http://localhost:8000
   ```

2. **Select your study mode** by clicking one of the four mode cards

3. **Choose your topics:**
   - Click "All Topics" to study everything
   - Or select specific categories (General, Design, Analysis, etc.)
   - Multiple categories can be selected

4. **Set number of questions** (default is 10)

5. **Click "Start Studying! 🚀"**

### During Study Session

- **Navigation:**
  - Use "Next →" to move forward
  - Use "← Previous" to go back
  - "Quit" returns to setup (progress is lost)

- **Mode-Specific Controls:**
  - **Flashcards:** Click card to flip
  - **Multiple Choice:** Click an answer to select it (shows correct/wrong immediately)
  - **Fill in Blank:** Type answer and click "Check Answer"
  - **Matching:** Click a term, then click its definition to match

### After Completion

- **View your score** with percentage and message
- **"Study Again"** - Return to setup for another session
- **"Review Answers"** - (Future feature)

## 🎯 Study Tips

1. **Start with Flashcards** to familiarize yourself with terms
2. **Use Multiple Choice** to test recall
3. **Try Fill in Blank** for deeper understanding
4. **Use Matching** to reinforce connections
5. **Focus on weak categories** by selecting specific topics
6. **Gradually increase** the number of questions

## 🎨 Design Details

### Color Scheme
- **Primary (Purple):** `#6366f1`
- **Secondary (Pink):** `#ec4899`
- **Accent (Teal):** `#14b8a6`
- **Success (Green):** `#22c55e`
- **Danger (Red):** `#ef4444`

### Fonts
- **Headings:** Space Grotesk (modern geometric sans-serif)
- **Body:** Poppins (clean, friendly sans-serif)

### Effects
- Glassmorphism cards with backdrop blur
- Gradient backgrounds
- Twinkling stars animation
- Smooth hover transitions
- Card flip animations (flashcards)

## 🔧 Technical Details

### Files Needed
- `index.html` - The main website (self-contained)
- `hci_data.json` - Database export with all terms and definitions

### Browser Compatibility
- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers

### No Internet Required
- All fonts load from Google Fonts (online)
- Works offline if fonts are cached
- All data is local (hci_data.json)

## 🐛 Troubleshooting

### Website won't load
- Make sure `hci_data.json` is in the same folder as `index.html`
- Try using a local server instead of opening file directly

### Data not showing
- Check browser console (F12) for errors
- Ensure JSON file is valid
- Try re-exporting: `python3 export_to_json.py`

### Styling looks broken
- Check internet connection (for Google Fonts)
- Try a different browser
- Clear browser cache

## 📱 Mobile Use

The website is fully responsive and works great on:
- Tablets
- Smartphones
- All screen sizes

Touch interactions work perfectly for all modes!

## 🎓 Best Study Practices

1. **Daily Practice:** 10-15 minutes per day
2. **Spaced Repetition:** Return to topics after a few days
3. **Mix Modes:** Use different study modes for variety
4. **Focus Sessions:** Study one category at a time for deep learning
5. **Before Exam:** Do a full session with all topics

## 🌟 Pro Tips

- Use **matching mode** to learn term-definition pairs quickly
- **Multiple choice** shows correct answers immediately - great for learning
- **Fill in blank** is the most challenging - save for when you're confident
- **Flashcards** are perfect for quick review sessions
- Track your scores over time to see improvement!

---

**Enjoy studying and good luck on your exam!** 🎉📚

Created with ❤️ for HCI students
