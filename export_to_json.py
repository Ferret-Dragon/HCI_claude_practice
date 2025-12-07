#!/usr/bin/env python3
"""
Export HCI database to JSON for web application
"""

import sqlite3
import json

def export_database():
    conn = sqlite3.connect('hci_exam_review.db')
    cursor = conn.cursor()

    # Get all categories
    cursor.execute("""
        SELECT id, name, description
        FROM categories
        ORDER BY order_num
    """)
    categories = [
        {'id': cat_id, 'name': name, 'description': desc}
        for cat_id, name, desc in cursor.fetchall()
    ]

    # Get all questions
    cursor.execute("""
        SELECT id, question_text, order_num
        FROM questions
        ORDER BY order_num
    """)
    questions = [
        {'id': q_id, 'text': text, 'order': order}
        for q_id, text, order in cursor.fetchall()
    ]

    # Get all terms with their answers
    cursor.execute("""
        SELECT t.id, t.category_id, t.name, t.definition
        FROM terms t
        ORDER BY t.category_id, t.order_num
    """)

    terms = []
    for term_id, cat_id, name, definition in cursor.fetchall():
        # Get all answers for this term
        cursor.execute("""
            SELECT q.id, q.question_text, a.answer_text
            FROM answers a
            JOIN questions q ON a.question_id = q.id
            WHERE a.term_id = ?
            ORDER BY q.order_num
        """, (term_id,))

        answers = {}
        for q_id, q_text, a_text in cursor.fetchall():
            answers[q_text] = a_text

        terms.append({
            'id': term_id,
            'categoryId': cat_id,
            'name': name,
            'definition': definition,
            'answers': answers
        })

    # Create final data structure
    data = {
        'categories': categories,
        'questions': questions,
        'terms': terms
    }

    # Write to JSON file
    with open('hci_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Exported {len(categories)} categories")
    print(f"Exported {len(terms)} terms")
    print(f"Data saved to hci_data.json")

    conn.close()

if __name__ == "__main__":
    export_database()
