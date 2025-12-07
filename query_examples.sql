-- HCI Exam Review Database - Helpful Query Examples
-- Use these queries to explore and study from the database

-- ========================================
-- BASIC QUERIES
-- ========================================

-- 1. View all categories
SELECT * FROM categories ORDER BY order_num;

-- 2. Count terms in each category
SELECT c.name AS category, COUNT(t.id) AS term_count
FROM categories c
LEFT JOIN terms t ON c.id = t.category_id
GROUP BY c.id
ORDER BY c.order_num;

-- 3. View all terms with their categories
SELECT c.name AS category, t.name AS term
FROM terms t
JOIN categories c ON t.category_id = c.id
ORDER BY c.order_num, t.order_num;

-- ========================================
-- STUDYING SPECIFIC TERMS
-- ========================================

-- 4. Get complete information about a specific term (example: "Usability")
SELECT
    t.name AS term,
    t.definition,
    c.name AS category
FROM terms t
JOIN categories c ON t.category_id = c.id
WHERE t.name LIKE '%Usability%';

-- 5. Get all answers for a specific term
SELECT
    t.name AS term,
    q.question_text,
    a.answer_text
FROM terms t
JOIN answers a ON t.id = a.term_id
JOIN questions q ON a.question_id = q.id
WHERE t.name = 'User Experience (UX)'
ORDER BY q.order_num;

-- 6. Get definition and all 7 answers for a term (formatted nicely)
SELECT
    'TERM: ' || t.name AS info
FROM terms t
WHERE t.name = 'Human-Computer Interaction (HCI)'
UNION ALL
SELECT 'DEFINITION: ' || t.definition
FROM terms t
WHERE t.name = 'Human-Computer Interaction (HCI)'
UNION ALL
SELECT q.question_text || ' ' || a.answer_text
FROM terms t
JOIN answers a ON t.id = a.term_id
JOIN questions q ON a.question_id = q.id
WHERE t.name = 'Human-Computer Interaction (HCI)'
ORDER BY info;

-- ========================================
-- BROWSING BY CATEGORY
-- ========================================

-- 7. View all terms in a specific category (example: General)
SELECT t.name AS term, t.definition
FROM terms t
JOIN categories c ON t.category_id = c.id
WHERE c.name = 'General'
ORDER BY t.order_num;

-- 8. View hierarchical terms in a category (showing parent-child relationships)
SELECT
    CASE
        WHEN t.hierarchy_level = 0 THEN t.name
        WHEN t.hierarchy_level = 1 THEN '  → ' || t.name
        WHEN t.hierarchy_level = 2 THEN '    → ' || t.name
        ELSE '      → ' || t.name
    END AS term_hierarchy,
    t.definition
FROM terms t
JOIN categories c ON t.category_id = c.id
WHERE c.name = 'Analysis'
ORDER BY t.order_num;

-- ========================================
-- FINDING RELATED TERMS
-- ========================================

-- 9. Find all sub-terms of a parent term (example: "Design Thinking")
SELECT
    t.name AS sub_term,
    t.definition
FROM terms t
WHERE t.parent_term_id = (
    SELECT id FROM terms WHERE name = 'Design Thinking'
)
ORDER BY t.order_num;

-- 10. Search for terms by keyword
SELECT t.name AS term, t.definition, c.name AS category
FROM terms t
JOIN categories c ON t.category_id = c.id
WHERE t.name LIKE '%persona%' OR t.definition LIKE '%persona%'
ORDER BY c.order_num, t.order_num;

-- ========================================
-- STUDY AIDS
-- ========================================

-- 11. Get random term for flashcard practice
SELECT
    t.name AS term,
    t.definition,
    c.name AS category
FROM terms t
JOIN categories c ON t.category_id = c.id
ORDER BY RANDOM()
LIMIT 1;

-- 12. Quiz yourself: Get just term names, then lookup answers
SELECT name FROM terms ORDER BY RANDOM() LIMIT 10;

-- 13. Get all terms without their definitions (test yourself!)
SELECT c.name AS category, t.name AS term
FROM terms t
JOIN categories c ON t.category_id = c.id
ORDER BY c.order_num, t.order_num;

-- 14. Get specific question answers across all terms (example: "Why is it important?")
SELECT
    t.name AS term,
    a.answer_text AS why_important
FROM terms t
JOIN answers a ON t.id = a.term_id
JOIN questions q ON a.question_id = q.id
WHERE q.question_text = 'Why is it important?'
ORDER BY t.name;

-- ========================================
-- COMPREHENSIVE STUDY SHEETS
-- ========================================

-- 15. Generate study sheet for entire category
SELECT
    t.name AS term,
    t.definition,
    GROUP_CONCAT(q.question_text || ': ' || a.answer_text, ' | ') AS all_answers
FROM terms t
JOIN categories c ON t.category_id = c.id
JOIN answers a ON t.id = a.term_id
JOIN questions q ON a.question_id = q.id
WHERE c.name = 'General'
GROUP BY t.id
ORDER BY t.order_num;

-- 16. Get complete term information (everything about one term)
-- Replace 'Contextual Inquiry' with any term name
SELECT
    '=== ' || t.name || ' ===' AS section,
    '' AS content
FROM terms t WHERE t.name = 'Contextual Inquiry'
UNION ALL
SELECT 'Category:', c.name
FROM terms t
JOIN categories c ON t.category_id = c.id
WHERE t.name = 'Contextual Inquiry'
UNION ALL
SELECT 'Definition:', t.definition
FROM terms t WHERE t.name = 'Contextual Inquiry'
UNION ALL
SELECT '', ''
UNION ALL
SELECT q.question_text, a.answer_text
FROM terms t
JOIN answers a ON t.id = a.term_id
JOIN questions q ON a.question_id = q.id
WHERE t.name = 'Contextual Inquiry'
ORDER BY section;

-- ========================================
-- NIELSEN'S HEURISTICS
-- ========================================

-- 17. Get all of Nielsen's 10 heuristics
SELECT
    t.name AS heuristic,
    t.definition
FROM terms t
WHERE t.parent_term_id = (
    SELECT id FROM terms WHERE name = "Nielsen's Original Heuristics"
)
ORDER BY t.order_num;

-- ========================================
-- EXAM PREPARATION
-- ========================================

-- 18. Get terms most likely on exam (from last two project phases)
-- This shows Prototyping and Evaluation terms
SELECT c.name AS category, t.name AS term, t.definition
FROM terms t
JOIN categories c ON t.category_id = c.id
WHERE c.name IN ('Prototyping', 'Evaluation')
ORDER BY c.order_num, t.order_num;

-- 19. Get all Design-Informing Models (important for analysis)
SELECT
    t.name AS model_type,
    t.definition
FROM terms t
WHERE t.parent_term_id = (
    SELECT id FROM terms WHERE name = 'Design-Informing Models (DIMs)'
)
OR t.id = (SELECT id FROM terms WHERE name = 'Design-Informing Models (DIMs)')
ORDER BY t.order_num;

-- 20. Compare similar terms (example: usability vs usefulness vs UX)
SELECT
    t.name AS term,
    t.definition,
    a.answer_text AS how_it_differs
FROM terms t
JOIN answers a ON t.id = a.term_id
JOIN questions q ON a.question_id = q.id
WHERE t.name IN ('Usability', 'Usefulness', 'User Experience (UX)')
  AND q.question_text = 'How is it similar to or different than related terms?'
ORDER BY t.name;
