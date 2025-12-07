-- HCI Final Exam Review Database Schema
-- This database stores terms, concepts, definitions, and answers for the CS 3205 HCI course

-- Categories table: Main organizational categories
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    order_num INTEGER
);

-- Terms table: All HCI terms and concepts
CREATE TABLE IF NOT EXISTS terms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    parent_term_id INTEGER,
    name TEXT NOT NULL,
    definition TEXT NOT NULL,
    hierarchy_level INTEGER DEFAULT 0,
    order_num INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (parent_term_id) REFERENCES terms(id)
);

-- Questions table: Standard questions to consider for each term
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT NOT NULL,
    order_num INTEGER
);

-- Answers table: Answers to questions for each term
CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    term_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    answer_text TEXT NOT NULL,
    FOREIGN KEY (term_id) REFERENCES terms(id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

-- Examples table: Specific examples for terms
CREATE TABLE IF NOT EXISTS examples (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    term_id INTEGER NOT NULL,
    example_text TEXT NOT NULL,
    FOREIGN KEY (term_id) REFERENCES terms(id) ON DELETE CASCADE
);

-- Relationships table: Connects related terms
CREATE TABLE IF NOT EXISTS term_relationships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    term_id INTEGER NOT NULL,
    related_term_id INTEGER NOT NULL,
    relationship_type TEXT,
    FOREIGN KEY (term_id) REFERENCES terms(id) ON DELETE CASCADE,
    FOREIGN KEY (related_term_id) REFERENCES terms(id) ON DELETE CASCADE
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_terms_category ON terms(category_id);
CREATE INDEX IF NOT EXISTS idx_terms_parent ON terms(parent_term_id);
CREATE INDEX IF NOT EXISTS idx_answers_term ON answers(term_id);
CREATE INDEX IF NOT EXISTS idx_answers_question ON answers(question_id);
CREATE INDEX IF NOT EXISTS idx_examples_term ON examples(term_id);
