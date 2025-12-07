#!/usr/bin/env python3
"""
HCI Exam Review - Interactive Study Tool
A simple command-line tool for studying HCI concepts
"""

import sqlite3
import random
import sys

class HCIStudyTool:
    def __init__(self, db_path='hci_exam_review.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def show_menu(self):
        print("\n" + "="*50)
        print("HCI EXAM REVIEW - STUDY TOOL")
        print("="*50)
        print("\n1. Browse by Category")
        print("2. Search for a Term")
        print("3. Random Flashcard")
        print("4. Quiz Mode (Random 10 terms)")
        print("5. View Nielsen's Heuristics")
        print("6. View All Categories")
        print("7. Compare Terms")
        print("8. Exit")
        print()

    def browse_by_category(self):
        print("\nCategories:")
        self.cursor.execute("SELECT id, name FROM categories ORDER BY order_num")
        categories = self.cursor.fetchall()

        for i, (cat_id, name) in enumerate(categories, 1):
            print(f"{i}. {name}")

        try:
            choice = int(input("\nSelect category (number): "))
            if 1 <= choice <= len(categories):
                cat_id = categories[choice-1][0]
                self.show_category_terms(cat_id)
        except (ValueError, IndexError):
            print("Invalid choice")

    def show_category_terms(self, cat_id):
        self.cursor.execute("""
            SELECT t.name, t.definition
            FROM terms t
            WHERE t.category_id = ?
            ORDER BY t.order_num
        """, (cat_id,))

        terms = self.cursor.fetchall()
        print(f"\nFound {len(terms)} terms:")

        for i, (name, definition) in enumerate(terms, 1):
            print(f"\n{i}. {name}")
            print(f"   {definition[:100]}..." if len(definition) > 100 else f"   {definition}")

        print("\nOptions:")
        print("- Enter term number for details")
        print("- Press Enter to return to main menu")

        choice = input("\nYour choice: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(terms):
                self.show_term_details(terms[idx][0])

    def search_term(self):
        query = input("\nEnter search term: ").strip()

        self.cursor.execute("""
            SELECT t.name, t.definition, c.name
            FROM terms t
            JOIN categories c ON t.category_id = c.id
            WHERE t.name LIKE ? OR t.definition LIKE ?
            ORDER BY t.name
        """, (f'%{query}%', f'%{query}%'))

        results = self.cursor.fetchall()

        if not results:
            print("No terms found.")
            return

        print(f"\nFound {len(results)} term(s):")
        for i, (name, definition, category) in enumerate(results, 1):
            print(f"\n{i}. {name} ({category})")
            print(f"   {definition[:100]}..." if len(definition) > 100 else f"   {definition}")

        if len(results) == 1:
            self.show_term_details(results[0][0])
        elif len(results) > 1:
            choice = input("\nEnter number for details (or Enter to skip): ").strip()
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(results):
                    self.show_term_details(results[idx][0])

    def show_term_details(self, term_name):
        # Get term info
        self.cursor.execute("""
            SELECT t.name, t.definition, c.name
            FROM terms t
            JOIN categories c ON t.category_id = c.id
            WHERE t.name = ?
        """, (term_name,))

        result = self.cursor.fetchone()
        if not result:
            print("Term not found")
            return

        name, definition, category = result

        print("\n" + "="*50)
        print(f"TERM: {name}")
        print("="*50)
        print(f"Category: {category}")
        print(f"\nDefinition:\n{definition}")

        # Get all 7 answers
        self.cursor.execute("""
            SELECT q.question_text, a.answer_text
            FROM answers a
            JOIN questions q ON a.question_id = q.id
            WHERE a.term_id = (SELECT id FROM terms WHERE name = ?)
            ORDER BY q.order_num
        """, (term_name,))

        answers = self.cursor.fetchall()
        if answers:
            print("\n" + "-"*50)
            for question, answer in answers:
                print(f"\n{question}")
                print(f"{answer}")

        input("\nPress Enter to continue...")

    def random_flashcard(self):
        self.cursor.execute("""
            SELECT name, definition
            FROM terms
            ORDER BY RANDOM()
            LIMIT 1
        """)

        name, definition = self.cursor.fetchone()

        print("\n" + "="*50)
        print("RANDOM FLASHCARD")
        print("="*50)
        print(f"\nTerm: {name}")
        input("\nPress Enter to see definition...")
        print(f"\nDefinition:\n{definition}")

        show_more = input("\nSee all 7 questions? (y/n): ").lower()
        if show_more == 'y':
            self.show_term_details(name)

    def quiz_mode(self):
        self.cursor.execute("""
            SELECT id, name, definition
            FROM terms
            ORDER BY RANDOM()
            LIMIT 10
        """)

        questions = self.cursor.fetchall()
        score = 0

        print("\n" + "="*50)
        print("QUIZ MODE - 10 Random Terms")
        print("="*50)
        print("\nYou'll see a term name. Try to recall:")
        print("1. The definition")
        print("2. Why it's important")
        print("3. When/where it's used")
        input("\nPress Enter to start...")

        for i, (term_id, name, definition) in enumerate(questions, 1):
            print(f"\n{'-'*50}")
            print(f"Question {i}/10")
            print(f"{'-'*50}")
            print(f"\nTerm: {name}")
            input("\nPress Enter to see answer...")

            print(f"\nDefinition:\n{definition}")

            # Show key answers
            self.cursor.execute("""
                SELECT q.question_text, a.answer_text
                FROM answers a
                JOIN questions q ON a.question_id = q.id
                WHERE a.term_id = ? AND q.order_num IN (2, 3)
                ORDER BY q.order_num
            """, (term_id,))

            for question, answer in self.cursor.fetchall():
                print(f"\n{question}")
                print(f"{answer}")

            result = input("\nDid you know this? (y/n): ").lower()
            if result == 'y':
                score += 1

        print("\n" + "="*50)
        print(f"QUIZ COMPLETE!")
        print(f"Score: {score}/10 ({score*10}%)")
        print("="*50)
        input("\nPress Enter to continue...")

    def show_nielsens_heuristics(self):
        print("\n" + "="*50)
        print("NIELSEN'S 10 USABILITY HEURISTICS")
        print("="*50)

        self.cursor.execute("""
            SELECT t.name, t.definition
            FROM terms t
            WHERE t.parent_term_id = (
                SELECT id FROM terms WHERE name = "Nielsen's Original Heuristics"
            )
            ORDER BY t.order_num
        """)

        heuristics = self.cursor.fetchall()

        for i, (name, definition) in enumerate(heuristics, 1):
            print(f"\n{i}. {name}")
            print(f"   {definition}")

        input("\nPress Enter to continue...")

    def view_all_categories(self):
        print("\n" + "="*50)
        print("ALL CATEGORIES")
        print("="*50)

        self.cursor.execute("""
            SELECT c.name, c.description, COUNT(t.id)
            FROM categories c
            LEFT JOIN terms t ON c.id = t.category_id
            GROUP BY c.id
            ORDER BY c.order_num
        """)

        for name, description, count in self.cursor.fetchall():
            print(f"\n{name} ({count} terms)")
            print(f"  {description}")

        input("\nPress Enter to continue...")

    def compare_terms(self):
        print("\n" + "="*50)
        print("COMPARE TERMS")
        print("="*50)

        # Show some common comparisons
        print("\nCommon comparisons:")
        print("1. UX vs UI vs HCI")
        print("2. Usability vs Usefulness vs UX")
        print("3. Formative vs Summative")
        print("4. Analytic vs Empirical")
        print("5. Custom search")

        choice = input("\nSelect comparison (1-5): ").strip()

        comparisons = {
            '1': ['User Experience (UX)', 'User Interface (UI)', 'Human-Computer Interaction (HCI)'],
            '2': ['Usability', 'Usefulness', 'User Experience (UX)'],
            '3': ['Formative vs. Summative'],
            '4': ['Analytic vs. Empirical']
        }

        if choice in comparisons:
            terms = comparisons[choice]
            for term in terms:
                self.cursor.execute("""
                    SELECT name FROM terms WHERE name LIKE ?
                """, (f'%{term}%',))
                result = self.cursor.fetchone()
                if result:
                    self.show_term_details(result[0])
        elif choice == '5':
            term1 = input("Enter first term: ").strip()
            term2 = input("Enter second term: ").strip()
            self.show_term_details(term1)
            self.show_term_details(term2)

    def run(self):
        while True:
            self.show_menu()
            choice = input("Select option (1-8): ").strip()

            if choice == '1':
                self.browse_by_category()
            elif choice == '2':
                self.search_term()
            elif choice == '3':
                self.random_flashcard()
            elif choice == '4':
                self.quiz_mode()
            elif choice == '5':
                self.show_nielsens_heuristics()
            elif choice == '6':
                self.view_all_categories()
            elif choice == '7':
                self.compare_terms()
            elif choice == '8':
                print("\nGood luck on your exam! 📚")
                break
            else:
                print("Invalid choice. Please select 1-8.")

        self.close()

if __name__ == "__main__":
    try:
        tool = HCIStudyTool()
        tool.run()
    except FileNotFoundError:
        print("Error: hci_exam_review.db not found!")
        print("Make sure you're in the correct directory.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nStudy session interrupted. Good luck!")
        sys.exit(0)
