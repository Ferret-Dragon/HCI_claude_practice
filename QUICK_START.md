# Quick Start Guide

## Easiest Way to Study: Use the Interactive Tool

```bash
python3 study_tool.py
```

This launches an interactive menu with options:
1. Browse by Category
2. Search for a Term
3. Random Flashcard
4. Quiz Mode (Random 10 terms)
5. View Nielsen's Heuristics
6. View All Categories
7. Compare Terms
8. Exit

## Quick Command-Line Queries

### View all categories
```bash
sqlite3 hci_exam_review.db "SELECT * FROM categories ORDER BY order_num;"
```

### Search for a term
```bash
sqlite3 hci_exam_review.db "SELECT name, definition FROM terms WHERE name LIKE '%usability%';"
```

### Get complete info about a term
```bash
sqlite3 hci_exam_review.db "SELECT t.name, t.definition, q.question_text, a.answer_text FROM terms t JOIN answers a ON t.id = a.term_id JOIN questions q ON a.question_id = q.id WHERE t.name = 'User Experience (UX)' ORDER BY q.order_num;"
```

### Random flashcard
```bash
sqlite3 hci_exam_review.db "SELECT name, definition FROM terms ORDER BY RANDOM() LIMIT 1;"
```

### View Nielsen's heuristics
```bash
sqlite3 hci_exam_review.db "SELECT t.name FROM terms t WHERE t.parent_term_id = (SELECT id FROM terms WHERE name = \"Nielsen's Original Heuristics\") ORDER BY t.order_num;"
```

## Study Tips

1. **Start with categories you're weakest in**
   - Use the interactive tool to browse by category

2. **Use flashcard mode daily**
   - Quick review of random terms

3. **Take quiz mode multiple times**
   - Tests recall of definitions and key points

4. **Focus on relationships**
   - Pay attention to Question 7 (how terms differ)

5. **Review Nielsen's heuristics thoroughly**
   - These are frequently tested

6. **Understand the UX Lifecycle**
   - Know how phases connect

## Files Created

- `hci_exam_review.db` - Main database (149 terms, 677 answers)
- `study_tool.py` - Interactive study tool
- `query_examples.sql` - 20+ example queries
- `README.md` - Complete documentation
- `QUICK_START.md` - This file

## Sample Output

Try this to see a full term:

```bash
sqlite3 hci_exam_review.db << 'EOF'
.mode line
SELECT 'TERM: ' || t.name AS info, '' AS value
FROM terms t WHERE t.name = 'Usability'
UNION ALL
SELECT 'DEFINITION:', t.definition FROM terms t WHERE t.name = 'Usability'
UNION ALL
SELECT q.question_text, a.answer_text
FROM terms t
JOIN answers a ON t.id = a.term_id
JOIN questions q ON a.question_id = q.id
WHERE t.name = 'Usability'
ORDER BY info;
EOF
```

Good luck on your exam! 📚
