#!/usr/bin/env python3
"""
Populate Design Section (Category 5)
This script adds all Design-related terms to the HCI database
"""

import sqlite3

def create_connection():
    """Create a database connection"""
    return sqlite3.connect('hci_exam_review.db')

def insert_term(conn, category_id, name, definition, parent_id=None, hierarchy_level=0, order_num=0):
    """Insert a term and return its ID"""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO terms (category_id, parent_term_id, name, definition, hierarchy_level, order_num)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (category_id, parent_id, name, definition, hierarchy_level, order_num))
    conn.commit()
    return cursor.lastrowid

def insert_answer(conn, term_id, question_num, answer_text):
    """Insert an answer for a specific term and question"""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO answers (term_id, question_id, answer_text)
        VALUES (?, ?, ?)
    """, (term_id, question_num, answer_text))
    conn.commit()

def populate_design_section(conn):
    """Populate the Design category (Category 5) - Part 1: Design Thinking"""
    print("Populating Design section...")
    category_id = 5

    # Main category: Design Thinking
    dt_term_id = insert_term(conn, category_id, "Design Thinking",
        "A human-centered, iterative approach to problem-solving that emphasizes empathy, ideation, and experimentation to create innovative solutions.",
        order_num=1)
    insert_answer(conn, dt_term_id, 1, "Design thinking is a creative problem-solving approach that emphasizes understanding human needs (empathy), generating many ideas (ideation), and learning through making (prototyping/testing). It's iterative, user-centered, and exploratory.")
    insert_answer(conn, dt_term_id, 2, "Design thinking is important because it provides a structured yet flexible approach to innovation, helps teams break free from assumptions, encourages exploration, and keeps focus on real human needs rather than just technical possibilities.")
    insert_answer(conn, dt_term_id, 3, "Design thinking is used throughout the Design phase, particularly in early conceptual design. It's applied when facing complex problems, seeking innovation, or needing to understand user needs deeply.")
    insert_answer(conn, dt_term_id, 4, "Examples: using empathy to understand user frustrations, brainstorming many solutions without judgment, rapidly prototyping ideas to test them, iterating based on feedback, considering emotional and ecological perspectives.")
    insert_answer(conn, dt_term_id, 5, "Design thinking shapes how Design is approached in the UX lifecycle - emphasizing empathy (from Analysis), ideation (generating options), and iteration (through prototyping and evaluation).")
    insert_answer(conn, dt_term_id, 6, "Good design thinking involves: deep empathy with users, divergent thinking (many ideas), deferring judgment, making ideas tangible quickly, testing and learning, iterating based on feedback.")
    insert_answer(conn, dt_term_id, 7, "Design thinking is an approach/mindset (how to think about design), the design-thinking paradigm is a theoretical perspective (phenomenological), and specific methods like ideation are techniques within design thinking.")

    # Sub-term: "Design" (what is it?)
    term_id = insert_term(conn, category_id, "Design (What is it?)",
        "The intentional, creative process of envisioning and planning solutions - in UX, specifically focused on creating user experiences that are usable, useful, and delightful.",
        parent_id=dt_term_id, hierarchy_level=1, order_num=1)
    insert_answer(conn, term_id, 1, "Design is the creative act of envisioning how things should be - planning solutions, making decisions about form and function, imagining possibilities. It's intentional creation guided by understanding and constraints.")
    insert_answer(conn, term_id, 2, "Understanding what design is matters because it clarifies the designer's role (creative problem-solving, not just decoration), the design process (intentional exploration), and design's value (solving problems innovatively).")
    insert_answer(conn, term_id, 3, "Design as an activity occurs throughout the UX lifecycle's Design phase, from conceptual through detailed design. It's the creative, generative work that transforms requirements into solutions.")
    insert_answer(conn, term_id, 4, "Examples of design activities: sketching interface concepts, planning interaction flows, choosing metaphors, making layout decisions, selecting visual styles, designing affordances.")
    insert_answer(conn, term_id, 5, "Design sits between Analysis (understanding) and Implementation (building). It transforms insights from Analysis into specifications for Implementation through creative problem-solving.")
    insert_answer(conn, term_id, 6, "Good design is: intentional (purposeful decisions), user-centered (based on user needs), creative (generating novel solutions), iterative (refining through feedback), and balanced (managing tradeoffs).")
    insert_answer(conn, term_id, 7, "Design is creative/generative (making solutions), while analysis is investigative (understanding problems) and evaluation is critical (judging solutions). Design is the central creative act in UX.")

    # Sub-term: Design Paradigms
    dp_term_id = insert_term(conn, category_id, "Design Paradigms",
        "Different theoretical frameworks for thinking about and approaching design, each emphasizing different aspects - engineering, cognitive, or phenomenological.",
        parent_id=dt_term_id, hierarchy_level=1, order_num=2)
    insert_answer(conn, dp_term_id, 1, "Design paradigms are fundamental frameworks for thinking about design - different perspectives on what matters most. The three paradigms are: engineering (optimizing performance), HIP (cognitive processing), and design-thinking (phenomenological experience).")
    insert_answer(conn, dp_term_id, 2, "Paradigms matter because they shape what designers pay attention to, what questions they ask, what they optimize for, and what methods they use. Different paradigms lead to different design outcomes.")
    insert_answer(conn, dp_term_id, 3, "Paradigms are theoretical frameworks that guide design practice. Understanding them helps designers choose appropriate approaches for different contexts and avoid being limited by one perspective.")
    insert_answer(conn, dp_term_id, 4, "Examples: engineering paradigm optimizing task completion time, HIP paradigm reducing cognitive load, design-thinking paradigm creating delightful emotional experiences.")
    insert_answer(conn, dp_term_id, 5, "Design paradigms provide different lenses for the Design phase - each emphasizing different aspects of UX (performance, cognition, experience). Modern UX often combines insights from all three.")
    insert_answer(conn, dp_term_id, 6, "Effective use of paradigms involves: understanding each perspective's strengths, choosing appropriately for context, combining insights from multiple paradigms, and recognizing when you're operating within a particular paradigm.")
    insert_answer(conn, dp_term_id, 7, "Paradigms are overarching frameworks (theoretical perspectives), while methods are specific techniques (practical tools), and design perspectives (ecological/interaction/emotional) are complementary views within design-thinking.")

    # Design Paradigm sub-items
    term_id = insert_term(conn, category_id, "Engineering Paradigm",
        "A design approach focused on optimizing measurable performance metrics like speed, accuracy, and efficiency through systematic engineering methods.",
        parent_id=dp_term_id, hierarchy_level=2, order_num=1)
    insert_answer(conn, term_id, 1, "The engineering paradigm approaches design as optimization of measurable performance - minimizing time, errors, and effort through systematic engineering methods and quantitative evaluation.")
    insert_answer(conn, term_id, 2, "This paradigm is important for task efficiency and performance. It provides rigorous, measurable approaches to improving productivity and reducing errors, particularly important for work systems.")
    insert_answer(conn, term_id, 3, "The engineering paradigm is applied when performance optimization is critical - enterprise systems, productivity tools, safety-critical systems where efficiency and accuracy matter most.")
    insert_answer(conn, term_id, 4, "Examples: optimizing button placement for fastest clicking, reducing steps in workflows, minimizing error rates through constraints, measuring and improving task completion times.")
    insert_answer(conn, term_id, 5, "The engineering paradigm emphasizes the usability (efficiency/effectiveness) aspect of UX, contributing systematic measurement and optimization methods to the design process.")
    insert_answer(conn, term_id, 6, "Engineering paradigm done well: sets clear performance metrics, measures systematically, optimizes based on data, balances multiple performance criteria, validates improvements empirically.")
    insert_answer(conn, term_id, 7, "Engineering paradigm focuses on performance (speed/accuracy), HIP on cognition (mental processing), design-thinking on experience (emotional/phenomenological). Engineering is most quantitative and optimization-focused.")

    term_id = insert_term(conn, category_id, "Human-Information Processing (HIP) Paradigm",
        "A design approach based on understanding human cognitive processes - perception, attention, memory, decision-making - and designing to support these processes.",
        parent_id=dp_term_id, hierarchy_level=2, order_num=2)
    insert_answer(conn, term_id, 1, "The HIP paradigm approaches design by understanding human cognitive processes (perception, attention, memory, thinking) and creating designs that work with, not against, these processes.")
    insert_answer(conn, term_id, 2, "HIP is important because it grounds design in cognitive science, helps designers understand and support how humans process information, and leads to interfaces that fit natural cognitive abilities and limitations.")
    insert_answer(conn, term_id, 3, "HIP paradigm is applied when cognitive factors are critical - complex information processing, learning systems, attention-demanding contexts, or when designing to minimize cognitive load.")
    insert_answer(conn, term_id, 4, "Examples: using chunking to support memory limitations, visual hierarchy supporting attention, recognition over recall, clear feedback supporting understanding of system state.")
    insert_answer(conn, term_id, 5, "HIP paradigm contributes understanding of cognitive aspects to design, informing guidelines about memory, attention, and perception that improve usability and learnability.")
    insert_answer(conn, term_id, 6, "HIP paradigm done well: applies cognitive principles appropriately, designs for cognitive strengths and limits, reduces unnecessary cognitive load, supports learning and memory.")
    insert_answer(conn, term_id, 7, "HIP focuses on cognition (mental processes), engineering on performance (measurable outcomes), design-thinking on experience (emotional/phenomenological). HIP is most cognitive-science grounded.")

    term_id = insert_term(conn, category_id, "Design-Thinking Paradigm",
        "A design approach emphasizing the phenomenological - lived experience, meaning-making, and holistic human experience beyond just performance or cognition.",
        parent_id=dp_term_id, hierarchy_level=2, order_num=3)
    insert_answer(conn, term_id, 1, "The design-thinking paradigm focuses on phenomenological concerns - the lived, felt experience of using systems, including meaning, emotion, aesthetics, and how technology fits into life holistically.")
    insert_answer(conn, term_id, 2, "This paradigm is important because it addresses aspects of experience that engineering and HIP miss - emotional impact, meaning, aesthetics, values - which are increasingly important for product differentiation and user satisfaction.")
    insert_answer(conn, term_id, 3, "Design-thinking paradigm is applied in consumer products, experiences where emotional connection matters, and when designing for overall life experience rather than just task completion.")
    insert_answer(conn, term_id, 4, "Examples: designing for presence and flow, creating emotionally resonant experiences, considering aesthetic pleasure, designing for meaning and values, thinking ecologically about technology in life context.")
    insert_answer(conn, term_id, 5, "Design-thinking paradigm adds emotional impact and experiential quality to UX, complementing engineering (performance) and HIP (cognition) to create holistic user experiences.")
    insert_answer(conn, term_id, 6, "Design-thinking done well: deeply empathizes with users, considers emotional and aesthetic dimensions, thinks ecologically about technology in life, creates meaningful experiences, balances phenomenological with practical.")
    insert_answer(conn, term_id, 7, "Design-thinking emphasizes experience/phenomenology, HIP emphasizes cognition, engineering emphasizes performance. Design-thinking is most qualitative and holistic, considering human experience beyond tasks.")

    # Phenomenological concerns sub-item
    term_id = insert_term(conn, category_id, "Phenomenological Concerns",
        "Focus on the lived, subjective experience of using technology - how it feels, what it means, and how it fits into life - beyond objective performance or cognitive processing.",
        parent_id=dp_term_id, hierarchy_level=2, order_num=4)
    insert_answer(conn, term_id, 1, "Phenomenological concerns focus on subjective lived experience - how using technology feels, what meaning it has, how it affects presence and consciousness - the qualitative, experiential aspects beyond performance.")
    insert_answer(conn, term_id, 2, "These concerns are important because human experience isn't just cognitive processing or task performance - emotions, meanings, aesthetics, and life impact matter deeply for satisfaction and technology acceptance.")
    insert_answer(conn, term_id, 3, "Phenomenological concerns are considered in the design-thinking paradigm, particularly when designing consumer products, experiences, or any system where emotional impact and life integration matter.")
    insert_answer(conn, term_id, 4, "Examples: designing for sense of presence in VR, creating flow experiences in games, building trust through aesthetics, considering meaning and values, designing for life balance not just productivity.")
    insert_answer(conn, term_id, 5, "Phenomenological concerns shape the design-thinking paradigm's focus on emotional perspective, presence, and holistic experience, complementing task-focused and cognition-focused approaches.")
    insert_answer(conn, term_id, 6, "Addressing phenomenological concerns well: empathizing deeply with lived experience, considering emotional and aesthetic dimensions, thinking about meaning and values, designing for life context not just tasks.")
    insert_answer(conn, term_id, 7, "Phenomenological is subjective/qualitative (how it feels), cognitive is mental-processing (how we think), engineering is objective/measurable (how it performs). Phenomenological addresses experience quality beyond function.")

    # The Phenomenological Concept of Presence
    term_id = insert_term(conn, category_id, "The Phenomenological Concept of Presence",
        "The sense of 'being there' or engaged immersion in an experience - when technology becomes invisible and users feel present in the activity or virtual environment.",
        parent_id=dt_term_id, hierarchy_level=1, order_num=3)
    insert_answer(conn, term_id, 1, "Presence is the phenomenological state where users feel fully immersed and engaged, technology becomes invisible, and they experience direct engagement with the activity or virtual environment without conscious awareness of the interface.")
    insert_answer(conn, term_id, 2, "Presence is important because it represents peak user experience - when technology successfully gets out of the way and users feel directly engaged with their goals, creating flow states and deep satisfaction.")
    insert_answer(conn, term_id, 3, "Presence is a design goal in immersive environments (VR, games), but also valuable in any interface where minimizing friction and maximizing engagement matters.")
    insert_answer(conn, term_id, 4, "Examples: VR experiences where users forget they're wearing a headset, games where players lose track of time, productivity tools that feel invisible, reading experiences where interface disappears.")
    insert_answer(conn, term_id, 5, "Presence represents a goal of good design - when usability, usefulness, and emotional impact combine so well that the interface becomes transparent and users feel directly connected to their activity.")
    insert_answer(conn, term_id, 6, "Designing for presence involves: minimizing friction, creating seamless interactions, reducing cognitive load, providing immediate feedback, maintaining flow, eliminating jarring interruptions.")
    insert_answer(conn, term_id, 7, "Presence is phenomenological (felt immersion), flow is psychological (optimal experience), usability is functional (easy to use). Presence is about consciousness and felt experience; usability enables it but isn't the same.")

    # Design Perspectives
    dpers_term_id = insert_term(conn, category_id, "Design Perspectives",
        "Three complementary viewpoints for design: ecological (technology in life context), interaction (user-system dialogue), and emotional (affective experience).",
        parent_id=dt_term_id, hierarchy_level=1, order_num=4)
    insert_answer(conn, dpers_term_id, 1, "Design perspectives are three complementary lenses for viewing design problems: ecological (how technology fits in life/work context), interaction (the user-system dialogue), and emotional (affective responses).")
    insert_answer(conn, dpers_term_id, 2, "Multiple perspectives are important because looking from different angles reveals different insights and opportunities. Each perspective highlights aspects the others might miss, leading to more complete designs.")
    insert_answer(conn, dpers_term_id, 3, "Perspectives are applied throughout design work, helping designers consider multiple facets of the design problem and ensure they're addressing ecological context, interaction quality, and emotional impact.")
    insert_answer(conn, dpers_term_id, 4, "Examples: ecological view considers work disruption, interaction view considers gesture intuitiveness, emotional view considers delight - same feature examined from three angles.")
    insert_answer(conn, dpers_term_id, 5, "Perspectives structure design thinking within the design-thinking paradigm, ensuring designers consider context, interaction, and emotion - creating holistic solutions.")
    insert_answer(conn, dpers_term_id, 6, "Using perspectives well: deliberately shift between views, ensure all three are considered, recognize which perspective is most critical for specific design problems, integrate insights from all three.")
    insert_answer(conn, dpers_term_id, 7, "Perspectives are complementary viewpoints (ways of looking), paradigms are theoretical frameworks (ways of thinking about design). Perspectives operate within the design-thinking paradigm.")

    # Design Perspectives sub-items
    term_id = insert_term(conn, category_id, "Ecological Perspective",
        "A design viewpoint focusing on how technology fits into the broader context of users' lives, work, and environment - the system in its ecology.",
        parent_id=dpers_term_id, hierarchy_level=2, order_num=1)
    insert_answer(conn, term_id, 1, "The ecological perspective views technology in its broader context - how it fits into users' lives, affects work practices, integrates with other tools, impacts social relationships, and influences overall life balance.")
    insert_answer(conn, term_id, 2, "Ecological perspective is important because technology doesn't exist in isolation - it affects and is affected by work practices, social dynamics, other tools, and life balance. Ignoring ecology leads to adoption failures.")
    insert_answer(conn, term_id, 3, "Ecological perspective is applied when considering technology impact on work practices, integration with existing tools/workflows, social implications, and life balance effects.")
    insert_answer(conn, term_id, 4, "Examples: considering how notifications affect focus, how collaboration tools change team dynamics, how automation affects job satisfaction, how mobile access affects work-life boundaries.")
    insert_answer(conn, term_id, 5, "Ecological perspective informs Analysis (understanding current ecology) and Design (envisioning how new systems fit ecology), ensuring designs work within, not against, broader context.")
    insert_answer(conn, term_id, 6, "Good ecological thinking: considers ripple effects, examines technology in life/work context, anticipates social impacts, thinks about integration with existing practices and tools.")
    insert_answer(conn, term_id, 7, "Ecological views context/environment (technology in life), interaction views dialogue (user-system exchange), emotional views feeling (affective response). Ecological is broadest, most contextual perspective.")

    term_id = insert_term(conn, category_id, "Interaction Perspective",
        "A design viewpoint focusing on the dynamic dialogue between user and system - the back-and-forth exchange of actions and responses.",
        parent_id=dpers_term_id, hierarchy_level=2, order_num=2)
    insert_answer(conn, term_id, 1, "The interaction perspective focuses on the user-system dialogue - how users act, how systems respond, the dynamics of the exchange, the interaction patterns and flows.")
    insert_answer(conn, term_id, 2, "Interaction perspective is crucial because it focuses on the core of HCI - the interaction itself. Quality interaction is fundamental to usability and user experience.")
    insert_answer(conn, term_id, 3, "Interaction perspective is applied when designing interaction patterns, defining system responses, planning feedback, designing gestures/controls, and specifying interaction dynamics.")
    insert_answer(conn, term_id, 4, "Examples: designing how a system responds to user input, planning feedback timing and form, creating intuitive gesture mappings, specifying state transitions, designing conversational flows.")
    insert_answer(conn, term_id, 5, "Interaction perspective bridges user intent and system capability, informing interaction design, conceptual design, and detailed UI specifications throughout the Design phase.")
    insert_answer(conn, term_id, 6, "Good interaction thinking: considers the full interaction loop (user action → system response → user perception), designs for immediate feedback, creates natural mappings, maintains interaction consistency.")
    insert_answer(conn, term_id, 7, "Interaction views dialogue/exchange (dynamic user-system communication), ecological views context (technology in life), emotional views feeling (affective response). Interaction is most focused on the UI level.")

    term_id = insert_term(conn, category_id, "Emotional Perspective",
        "A design viewpoint focusing on affective responses - the emotions, feelings, and emotional impact users experience when interacting with systems.",
        parent_id=dpers_term_id, hierarchy_level=2, order_num=3)
    insert_answer(conn, term_id, 1, "The emotional perspective focuses on affective responses - what emotions the experience evokes, how it makes users feel, emotional impact of aesthetics, tone, and interaction qualities.")
    insert_answer(conn, term_id, 2, "Emotional perspective is important because emotions strongly influence user behavior, satisfaction, and loyalty. Emotional connections differentiate products and create memorable experiences beyond mere functionality.")
    insert_answer(conn, term_id, 3, "Emotional perspective is applied when considering aesthetic choices, tone of voice, animation/delight factors, error message tone, and any aspect that influences emotional response.")
    insert_answer(conn, term_id, 4, "Examples: choosing colors for emotional effect, crafting empathetic error messages, adding delightful animations, selecting friendly vs. professional tone, creating trust through visual design.")
    insert_answer(conn, term_id, 5, "Emotional perspective contributes to the emotional impact component of UX, influencing visual design, copywriting, animation, and all aspects that shape affective response.")
    insert_answer(conn, term_id, 6, "Good emotional thinking: considers intended emotional response, uses appropriate aesthetics and tone, adds delight where appropriate, shows empathy in messaging, builds trust through design.")
    insert_answer(conn, term_id, 7, "Emotional views feelings/affect (how it makes you feel), interaction views dialogue (how you interact), ecological views context (where it fits). Emotional is most focused on subjective affective response.")

    print(f"  Inserted Design Thinking subsection")
    return dt_term_id

def continue_design_section(conn):
    """Continue with remaining design subsections"""
    print("Continuing Design section...")
    category_id = 5

    # Note: Continuing with more design topics in next function
    # This is split to manage file size
    print(f"  Design section part 1 completed - preparing for part 2")

def main():
    """Main function to populate Design section"""
    print("Starting Design section population (Part 1)...")
    print("="*50)

    conn = create_connection()

    try:
        populate_design_section(conn)

        # Get total count
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM terms WHERE category_id = 5")
        design_term_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM terms")
        total_term_count = cursor.fetchone()[0]

        print("="*50)
        print(f"Design section part 1 completed!")
        print(f"Design terms inserted: {design_term_count}")
        print(f"Total terms in database: {total_term_count}")
        print("\nNote: Due to the large size of the Design section,")
        print("additional design topics will be added in continuation scripts.")

    finally:
        conn.close()

if __name__ == "__main__":
    main()
