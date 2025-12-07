#!/usr/bin/env python3
"""
Populate HCI Exam Review Database
This script populates the SQLite database with all HCI terms, definitions, and answers.
"""

import sqlite3
import json

def create_connection():
    """Create a database connection"""
    return sqlite3.connect('hci_exam_review.db')

def insert_questions(conn):
    """Insert the standard questions to consider for each term"""
    questions = [
        (1, "What does it mean?"),
        (2, "Why is it important?"),
        (3, "When and/or where is it used?"),
        (4, "What are some examples?"),
        (5, "If it's part of a process, how does it fit into the process and how does it relate to other parts of the process?"),
        (6, "What does it look like to do this well?"),
        (7, "How is it similar to or different than related terms?")
    ]

    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO questions (order_num, question_text) VALUES (?, ?)",
        questions
    )
    conn.commit()
    print(f"Inserted {len(questions)} questions")

def insert_categories(conn):
    """Insert the main categories"""
    categories = [
        (1, "General", "Foundational HCI and UX concepts"),
        (2, "UX in Software Engineering", "Integration of UX practices in software development"),
        (3, "Overall UX Process", "The UX lifecycle and iterative process"),
        (4, "Analysis", "Methods for understanding users, work, and requirements"),
        (5, "Design", "Design thinking, conceptual design, and design production"),
        (6, "Prototyping", "Creating and testing early versions of designs"),
        (7, "Evaluation", "Methods for assessing and validating UX designs")
    ]

    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO categories (order_num, name, description) VALUES (?, ?, ?)",
        categories
    )
    conn.commit()
    print(f"Inserted {len(categories)} categories")

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

def insert_example(conn, term_id, example_text):
    """Insert an example for a term"""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO examples (term_id, example_text)
        VALUES (?, ?)
    """, (term_id, example_text))
    conn.commit()

def populate_general_section(conn):
    """Populate the General category (Category 1)"""
    print("Populating General section...")
    category_id = 1

    # 1. Human-Computer Interaction (HCI)
    term_id = insert_term(conn, category_id, "Human-Computer Interaction (HCI)",
        "An interdisciplinary field focused on the design, evaluation, and implementation of interactive computing systems for human use and the study of major phenomena surrounding them.",
        order_num=1)
    insert_answer(conn, term_id, 1, "HCI is the study and practice of designing, evaluating, and implementing interactive computing systems for human use. It encompasses understanding how people interact with technology and improving those interactions.")
    insert_answer(conn, term_id, 2, "HCI is important because it ensures technology is usable, useful, and provides positive experiences. It bridges the gap between human capabilities/needs and technical possibilities, making technology accessible and effective.")
    insert_answer(conn, term_id, 3, "HCI is used throughout the entire software/product development lifecycle, from initial research and requirements gathering to design, implementation, and evaluation. It's applied in academia, industry, and any context where humans interact with computers.")
    insert_answer(conn, term_id, 4, "Examples include: designing smartphone interfaces, creating accessible websites, developing voice assistants, improving medical device interfaces, and optimizing dashboard displays for cars.")
    insert_answer(conn, term_id, 5, "HCI is the overarching field that encompasses UX, UI design, usability engineering, and interaction design. It provides the theoretical foundation and research methods that inform all these practices.")
    insert_answer(conn, term_id, 6, "Good HCI practice involves user-centered design, empirical evaluation, iterative refinement, consideration of diverse user needs, and applying established principles from psychology, design, and computer science.")
    insert_answer(conn, term_id, 7, "HCI is broader than UX (which focuses on overall experience) and UI (which focuses on interface elements). HCI includes research, theory, and empirical studies, while UX and UI are more practice-oriented. HCI is the academic/research field; UX/UI are professional practices.")

    # 2. User Experience (UX)
    term_id = insert_term(conn, category_id, "User Experience (UX)",
        "The overall experience a person has when interacting with a product, system, or service, encompassing all aspects of the end-user's interaction including usability, usefulness, and emotional impact.",
        order_num=2)
    insert_answer(conn, term_id, 1, "UX encompasses everything users experience when interacting with a product or service - from first impression to long-term satisfaction. It includes functional, emotional, and aesthetic dimensions of the interaction.")
    insert_answer(conn, term_id, 2, "UX is critical because it determines whether users will adopt, continue using, and recommend a product. Good UX leads to user satisfaction, productivity, and business success; poor UX results in frustration, abandonment, and failure.")
    insert_answer(conn, term_id, 3, "UX is considered throughout the entire product lifecycle - from initial concept through design, development, launch, and ongoing improvements. It's practiced in software companies, design agencies, product teams, and any organization creating interactive products.")
    insert_answer(conn, term_id, 4, "Examples include: the seamless experience of using an iPhone, the frustration of a confusing checkout process, the delight of a well-designed game, the efficiency of a professional tool like Adobe Photoshop.")
    insert_answer(conn, term_id, 5, "UX is a holistic concept that results from successfully combining usability, usefulness, and emotional impact. It's informed by HCI research and implemented through UI design, interaction design, and usability engineering practices.")
    insert_answer(conn, term_id, 6, "Excellent UX is invisible - users accomplish their goals effortlessly without thinking about the interface. It involves deep understanding of user needs, thoughtful design decisions, attention to detail, and continuous iteration based on user feedback.")
    insert_answer(conn, term_id, 7, "UX is broader than UI (which is just the visual/interactive elements), more holistic than usability (which focuses on effectiveness/efficiency), and the practical outcome of HCI research. UX includes emotional and value aspects beyond pure functionality.")

    # 3. User Interface (UI)
    term_id = insert_term(conn, category_id, "User Interface (UI)",
        "The visual and interactive elements through which users interact with a system, including screens, pages, buttons, icons, and other visual and interactive components.",
        order_num=3)
    insert_answer(conn, term_id, 1, "UI refers to the specific visual and interactive elements users see and manipulate when using a system - the buttons, menus, forms, icons, typography, colors, and layout that constitute the interface.")
    insert_answer(conn, term_id, 2, "UI is important because it's the primary means through which users interact with functionality. A well-designed UI makes systems intuitive and efficient; a poorly designed UI creates confusion and errors even if underlying functionality is strong.")
    insert_answer(conn, term_id, 3, "UI design occurs during the detailed design phase, after conceptual design is complete. It's implemented in all interactive systems - websites, mobile apps, desktop software, kiosks, smart devices, and embedded systems.")
    insert_answer(conn, term_id, 4, "Examples include: the Windows taskbar and Start menu, iOS home screen and app icons, a website's navigation menu, the controls in a car dashboard, ATM screens and buttons.")
    insert_answer(conn, term_id, 5, "UI is the tangible manifestation of design decisions. It comes after UX research and conceptual design, implementing the interaction design through specific visual and interactive elements. UI is what users actually see and touch.")
    insert_answer(conn, term_id, 6, "Good UI design is consistent, visually clear, follows established conventions while innovating where appropriate, provides clear affordances, gives immediate feedback, and is aesthetically pleasing without sacrificing usability.")
    insert_answer(conn, term_id, 7, "UI is a subset of UX (the visual/interactive layer vs. the overall experience). UI is more concrete than interaction design (which is conceptual). UI focuses on how things look and respond; UX focuses on how things feel and satisfy needs.")

    # 4. Design
    term_id = insert_term(conn, category_id, "Design",
        "The intentional creative process of planning and making decisions about the form, function, and experience of a product or system to solve problems and meet user needs.",
        order_num=4)
    insert_answer(conn, term_id, 1, "Design is the creative, intentional process of envisioning and specifying how something should work and appear to solve problems and meet user needs. It involves making informed decisions about form, function, and experience.")
    insert_answer(conn, term_id, 2, "Design is crucial because it bridges user needs and technical capabilities. Good design makes products usable, useful, and delightful; it can differentiate products in the market and determine success or failure.")
    insert_answer(conn, term_id, 3, "Design occurs throughout the UX lifecycle, from early conceptual design through detailed design and refinement. It's practiced by UX designers, interaction designers, visual designers, and product designers across industries.")
    insert_answer(conn, term_id, 4, "Examples include: sketching wireframes for a new app, creating a storyboard for a user flow, designing the interaction pattern for a gesture, choosing color schemes and typography, planning information architecture.")
    insert_answer(conn, term_id, 5, "Design follows analysis and requirements gathering in the UX process. It involves ideation, conceptual design, iterative prototyping, and refinement. Design decisions are validated through evaluation and inform implementation.")
    insert_answer(conn, term_id, 6, "Good design starts with deep user understanding, explores multiple solutions, iterates rapidly, balances competing constraints, follows established principles while innovating appropriately, and validates decisions with users.")
    insert_answer(conn, term_id, 7, "Design is broader than just UI (visual elements) - it includes conceptual and interaction design. It's more creative and generative than analysis. Design thinking is a specific approach to design that emphasizes empathy, ideation, and iteration.")

    # 5. Usability Engineering
    term_id = insert_term(conn, category_id, "Usability Engineering",
        "A systematic, disciplined approach to developing usable systems through user-centered design methods, empirical measurement, and iterative refinement throughout the development process.",
        order_num=5)
    insert_answer(conn, term_id, 1, "Usability engineering is the systematic application of engineering principles to achieve usability in products. It involves defined processes, measurable goals, empirical testing, and iterative improvement to ensure systems are usable.")
    insert_answer(conn, term_id, 2, "It's important because it provides structure and rigor to UX practice, ensuring usability is achieved through systematic methods rather than intuition alone. It makes UX measurable, trackable, and accountable to stakeholders.")
    insert_answer(conn, term_id, 3, "Usability engineering is used throughout product development, particularly in organizations that need structured processes. It's common in enterprise software, safety-critical systems, and large organizations with defined development methodologies.")
    insert_answer(conn, term_id, 4, "Examples include: setting quantitative usability targets (e.g., '90% of users complete checkout in under 2 minutes'), conducting structured usability tests, tracking metrics over time, creating usability specifications.")
    insert_answer(conn, term_id, 5, "Usability engineering integrates with the software development lifecycle, adding specific UX activities at each phase: user research early, design and prototyping during development, testing before release, and post-launch evaluation.")
    insert_answer(conn, term_id, 6, "Effective usability engineering involves: clear, measurable usability goals; systematic user testing; documented processes; iterative refinement based on data; and integration with engineering workflows and timelines.")
    insert_answer(conn, term_id, 7, "Usability engineering is more structured and measurement-focused than general UX practice. It emphasizes the 'engineering' aspect - processes, metrics, repeatability. It's more formal than design thinking and focuses specifically on usability rather than broader UX.")

    # 6. Usability
    term_id = insert_term(conn, category_id, "Usability",
        "The extent to which a product can be used by specified users to achieve specified goals with effectiveness, efficiency, and satisfaction in a specified context of use.",
        order_num=6)
    insert_answer(conn, term_id, 1, "Usability is the quality of a system that determines how easily and successfully users can accomplish their goals. It encompasses learnability, efficiency, memorability, error prevention/recovery, and satisfaction.")
    insert_answer(conn, term_id, 2, "Usability is fundamental because even the most powerful features are useless if users can't figure out how to use them. High usability leads to productivity, user satisfaction, reduced errors, and lower support costs.")
    insert_answer(conn, term_id, 3, "Usability is evaluated throughout design and development through various methods like usability testing, heuristic evaluation, and cognitive walkthroughs. It's a concern for any interactive system in any domain.")
    insert_answer(conn, term_id, 4, "Examples include: Google's simple search interface (easy to learn and use), keyboard shortcuts in professional software (efficiency for expert users), clear error messages that help recovery, consistent navigation patterns.")
    insert_answer(conn, term_id, 5, "Usability is one component of overall UX, alongside usefulness and emotional impact. It's assessed during evaluation phases and drives design refinements throughout the iterative UX process.")
    insert_answer(conn, term_id, 6, "High usability means: new users learn quickly, experienced users work efficiently, users remember how to use it after breaks, errors are rare and easily corrected, and users are satisfied with the interaction.")
    insert_answer(conn, term_id, 7, "Usability is narrower than UX (which includes emotional and value aspects). It's more objective and measurable than 'user-friendliness'. Usability is a necessary but not sufficient condition for good UX - a system can be usable but not useful or delightful.")

    # 7. Usefulness
    term_id = insert_term(conn, category_id, "Usefulness",
        "The degree to which a product provides the functionality and capabilities needed to accomplish users' actual goals and tasks effectively.",
        order_num=7)
    insert_answer(conn, term_id, 1, "Usefulness refers to whether a system provides the right functionality to help users accomplish their real goals. It's about having features that matter and solve actual problems, not just being easy to use.")
    insert_answer(conn, term_id, 2, "Usefulness is critical because even the most usable system fails if it doesn't do what users need. Users won't adopt products that don't solve their problems, regardless of how well-designed the interface is.")
    insert_answer(conn, term_id, 3, "Usefulness is determined during requirements analysis and validated through user research and evaluation. It's assessed when deciding what features to build and whether the product meets real user needs.")
    insert_answer(conn, term_id, 4, "Examples include: email is useful for communication, GPS navigation is useful for finding directions, spreadsheets are useful for calculations. A beautifully designed app for a problem no one has is not useful.")
    insert_answer(conn, term_id, 5, "Usefulness is determined early in the UX process through contextual inquiry and requirements extraction. It drives what features are designed and implemented. Along with usability and emotional impact, it comprises overall UX.")
    insert_answer(conn, term_id, 6, "High usefulness means: the system solves real user problems, provides necessary functionality, supports actual workflows, delivers value that justifies the effort to use it, and meets or exceeds user expectations for capabilities.")
    insert_answer(conn, term_id, 7, "Usefulness is about 'what' capabilities a system has, while usability is about 'how well' those capabilities work. Both are necessary for good UX. A system can be highly usable but not useful (solves wrong problem) or vice versa (right features, bad interface).")

    # 8. Emotional Impact
    term_id = insert_term(conn, category_id, "Emotional Impact",
        "The affective and emotional response users have when interacting with a product, including feelings of joy, frustration, trust, delight, or anxiety.",
        order_num=8)
    insert_answer(conn, term_id, 1, "Emotional impact refers to the feelings and emotional responses evoked by interacting with a product - whether it delights, frustrates, builds trust, creates anxiety, or generates other emotional responses in users.")
    insert_answer(conn, term_id, 2, "Emotional impact is important because emotions strongly influence user behavior, adoption, loyalty, and recommendations. Products that create positive emotional connections build stronger user relationships and competitive advantages beyond functionality.")
    insert_answer(conn, term_id, 3, "Emotional impact is considered throughout design, particularly in emotional perspective design and aesthetic decisions. It's especially important in consumer products, brands, and experiences where emotional connection differentiates competitors.")
    insert_answer(conn, term_id, 4, "Examples include: Apple products creating feelings of premium quality, video games generating excitement, bank apps building trust through professional design, error messages causing frustration, delightful animations creating joy.")
    insert_answer(conn, term_id, 5, "Emotional impact is one of three pillars of UX (with usability and usefulness). It's shaped by design decisions in visual design, interaction design, and microcopy. It's assessed through qualitative evaluation methods.")
    insert_answer(conn, term_id, 6, "Positive emotional impact comes from: beautiful aesthetics, delightful micro-interactions, personality in copy, smooth animations, exceeding expectations, showing care for details, creating moments of joy, and building trust through consistency.")
    insert_answer(conn, term_id, 7, "Emotional impact goes beyond usability (which is more functional) and usefulness (which is about capability). It's less measurable than usability but equally important for overall UX. It's what makes products 'lovable' rather than just 'usable'.")

    # 9. Interaction Design
    term_id = insert_term(conn, category_id, "Interaction Design",
        "The practice of designing interactive digital products, environments, systems, and services, with particular focus on defining the behavior of the system and how users interact with it.",
        order_num=9)
    insert_answer(conn, term_id, 1, "Interaction design focuses on defining how users interact with a system - the behaviors, flows, responses, and dynamics of the interaction. It's about designing the dialogue between user and system over time.")
    insert_answer(conn, term_id, 2, "Interaction design is crucial because it determines whether users can successfully accomplish their goals through the interface. It bridges user intentions and system capabilities by defining the interactive behaviors.")
    insert_answer(conn, term_id, 3, "Interaction design occurs after conceptual design and before detailed visual design. It's practiced by interaction designers working on any interactive system - apps, websites, devices, installations, or services.")
    insert_answer(conn, term_id, 4, "Examples include: designing swipe gestures for mobile interfaces, defining the behavior of drag-and-drop, creating the flow of a multi-step form, specifying animations and transitions, designing voice interaction patterns.")
    insert_answer(conn, term_id, 5, "Interaction design follows user research and conceptual design, informing UI design and prototyping. It defines the 'how' of user-system interaction, which is then visualized in UI design and tested through prototypes.")
    insert_answer(conn, term_id, 6, "Good interaction design is: responsive and provides immediate feedback, follows user expectations and mental models, is consistent within the system, supports user control, prevents errors, and creates smooth, natural-feeling interactions.")
    insert_answer(conn, term_id, 7, "Interaction design is more behavioral/temporal than UI design (which is visual/spatial). It's more specific than UX (which is holistic) and more detailed than conceptual design (which is high-level). It focuses on the dynamic aspects of the interface.")

    print(f"  Inserted {9} terms for General section")

def populate_ux_in_se_section(conn):
    """Populate the UX in Software Engineering category (Category 2)"""
    print("Populating UX in Software Engineering section...")
    category_id = 2

    # 1. Locus of influence in an organization
    term_id = insert_term(conn, category_id, "Locus of Influence in an Organization",
        "The point or level within an organization's structure where UX professionals have the most impact and decision-making power, ranging from individual contributor to strategic leadership levels.",
        order_num=1)
    insert_answer(conn, term_id, 1, "Locus of influence refers to where in an organizational hierarchy UX practitioners have authority and impact. It can range from tactical (individual projects) to strategic (company-wide vision and culture).")
    insert_answer(conn, term_id, 2, "It's important because the locus of influence determines the scope and impact of UX work - whether UX shapes individual features, entire products, or organizational strategy. Higher locus enables greater impact on business outcomes.")
    insert_answer(conn, term_id, 3, "This concept applies when considering UX maturity in organizations, planning career growth, or advocating for UX. It helps understand and improve how UX integrates into software development organizations.")
    insert_answer(conn, term_id, 4, "Examples include: Junior designer influencing feature design (low locus), senior designer influencing product direction (medium locus), design executive influencing company strategy and culture (high locus).")
    insert_answer(conn, term_id, 5, "Locus of influence affects how UX connects with software engineering - higher locus means UX considerations are integrated earlier and more fundamentally into development processes and business decisions.")
    insert_answer(conn, term_id, 6, "Effective UX influence involves: demonstrating value through metrics, building relationships with stakeholders, communicating in business terms, showing ROI of UX work, and gradually expanding sphere of impact.")
    insert_answer(conn, term_id, 7, "Locus of influence is about organizational power/position, while UX maturity is about organizational capability. Higher locus enables better UX-SE integration but requires organizational buy-in and demonstrated value.")

    # 2. UX-SE Success Components
    term_id = insert_term(conn, category_id, "UX-SE Success Components",
        "The key factors that enable successful integration of UX and software engineering practices, including communication, shared understanding, aligned processes, and mutual respect between disciplines.",
        order_num=2)
    insert_answer(conn, term_id, 1, "UX-SE success components are the critical factors that enable UX and software engineering teams to work together effectively, including communication, timing, shared goals, mutual understanding, and integrated processes.")
    insert_answer(conn, term_id, 2, "These components are vital because UX and SE must collaborate closely to deliver successful products. Without these factors, teams work in silos, leading to miscommunication, wasted effort, and poor product outcomes.")
    insert_answer(conn, term_id, 3, "These components should be established and maintained throughout product development. They're essential in any organization where UX and engineering teams collaborate, especially in agile and iterative development environments.")
    insert_answer(conn, term_id, 4, "Examples include: regular design-dev sync meetings, shared user story definitions, designers participating in sprint planning, developers involved in design reviews, common language and documentation, aligned timelines.")
    insert_answer(conn, term_id, 5, "Success components enable the UX lifecycle to integrate with software development cycles. They ensure design work happens ahead of development, feedback loops function, and both disciplines contribute to better products.")
    insert_answer(conn, term_id, 6, "Success looks like: designers and developers communicating regularly, shared understanding of user needs, design staying ahead of development, smooth handoffs, collaborative problem-solving, and mutual respect for each discipline's expertise.")
    insert_answer(conn, term_id, 7, "Success components are the 'how' of integration, while locus of influence is about 'where' in the organization. Components are tactical practices; challenges are obstacles to achieving them.")

    # 3. Challenge of Connecting SE and UX
    term_id = insert_term(conn, category_id, "Challenge of Connecting SE and UX",
        "The difficulties in integrating UX practices with software engineering processes, including different timescales, methodologies, vocabularies, priorities, and ways of thinking between the disciplines.",
        order_num=3)
    insert_answer(conn, term_id, 1, "The challenges include: different timescales (design needs time ahead of development), different methodologies (design thinking vs. engineering processes), communication gaps, conflicting priorities, and cultural differences between disciplines.")
    insert_answer(conn, term_id, 2, "Understanding these challenges is crucial for addressing them. Unresolved tensions lead to rushed design, implementation that doesn't match design intent, frustrated teams, and poor user experiences.")
    insert_answer(conn, term_id, 3, "These challenges arise throughout product development, particularly during project planning, sprint planning, design handoffs, and when trying to integrate UX into existing engineering-dominated processes.")
    insert_answer(conn, term_id, 4, "Examples include: designers not having enough lead time before development sprints, developers changing designs without UX input, different vocabularies causing miscommunication, pressure to skip user research, tension over technical feasibility.")
    insert_answer(conn, term_id, 5, "These challenges affect the entire UX lifecycle - limiting time for proper research and iteration, forcing compromises in design, and reducing opportunities for evaluation. Addressing them enables better UX-SE integration.")
    insert_answer(conn, term_id, 6, "Successfully addressing challenges involves: building mutual understanding, creating integrated processes with appropriate timing, establishing clear communication channels, respecting both disciplines' needs, and organizational support.")
    insert_answer(conn, term_id, 7, "Challenges are obstacles to overcome, while success components are solutions/practices to implement. Understanding challenges helps identify what success components to establish.")

    # 4. Importance of UX in Software Development
    term_id = insert_term(conn, category_id, "Importance of UX in Software Development",
        "The critical role UX plays in software development success, including impact on user adoption, satisfaction, productivity, business outcomes, and competitive differentiation.",
        order_num=4)
    insert_answer(conn, term_id, 1, "UX importance in software development refers to the significant impact user experience has on product success - affecting user adoption, satisfaction, retention, productivity, brand perception, and ultimately business outcomes.")
    insert_answer(conn, term_id, 2, "UX is critical because software success depends on users actually using it effectively. Poor UX leads to abandoned products, support costs, lost customers, and competitive disadvantage. Good UX drives adoption, loyalty, and business success.")
    insert_answer(conn, term_id, 3, "UX should be considered from project inception through post-launch maintenance. It's important in all software contexts - consumer apps, enterprise systems, internal tools, websites, and embedded software.")
    insert_answer(conn, term_id, 4, "Examples of UX impact: iPhone's success partly due to superior UX, enterprise software adoption rates tied to usability, e-commerce conversion rates affected by checkout UX, app store ratings reflecting UX quality.")
    insert_answer(conn, term_id, 5, "UX importance justifies investing in the full UX lifecycle - research, design, prototyping, and evaluation. It makes the business case for UX resources, tools, and integration into development processes.")
    insert_answer(conn, term_id, 6, "Demonstrating UX importance effectively involves: showing metrics (increased conversion, reduced support calls), user feedback, competitive analysis, ROI calculations, and connecting UX outcomes to business goals.")
    insert_answer(conn, term_id, 7, "Importance is the 'why' (business case for UX), while challenges describe 'what' makes integration difficult, and success components describe 'how' to achieve integration. Understanding importance helps justify addressing challenges.")

    print(f"  Inserted {4} terms for UX in Software Engineering section")

def populate_overall_ux_process(conn):
    """Populate the Overall UX Process category (Category 3)"""
    print("Populating Overall UX Process section...")
    category_id = 3

    # 1. UX Lifecycle, the Wheel
    term_id = insert_term(conn, category_id, "UX Lifecycle, the Wheel",
        "A cyclical model of the UX process showing the iterative phases of analysis, design, prototyping, and evaluation that repeat throughout product development.",
        order_num=1)
    insert_answer(conn, term_id, 1, "The UX Lifecycle (Wheel) is a circular model representing the iterative UX process: Analysis -> Design -> Prototyping -> Evaluation, then back to Analysis. It emphasizes the continuous, cyclical nature of UX work.")
    insert_answer(conn, term_id, 2, "The Wheel is important because it shows UX is not linear but iterative. It guides teams through systematic UX activities while emphasizing continuous refinement based on evaluation feedback.")
    insert_answer(conn, term_id, 3, "The Wheel is used throughout product development, from initial concept through launch and ongoing improvements. It provides structure for UX activities in any project, helping teams plan and sequence their work.")
    insert_answer(conn, term_id, 4, "Example: Start with user research (Analysis), create designs (Design), build prototypes (Prototyping), test with users (Evaluation), refine based on findings (back to Analysis/Design), repeat until launch and beyond.")
    insert_answer(conn, term_id, 5, "The Wheel encompasses the entire UX process. Analysis informs Design, which is realized through Prototyping, validated by Evaluation, leading to insights that drive the next cycle. Each phase connects to and depends on the others.")
    insert_answer(conn, term_id, 6, "Using the Wheel well means: completing each phase appropriately, iterating multiple times, using evaluation to drive improvements, adapting the pace to project needs, and maintaining momentum through the cycle.")
    insert_answer(conn, term_id, 7, "The Wheel shows the overall UX process structure, while specific methodologies (contextual inquiry, heuristic evaluation) are tools used within specific phases. The Wheel is process-level; methods are activity-level.")

    # 2. Iteration
    term_id = insert_term(conn, category_id, "Iteration",
        "The practice of repeatedly cycling through design, prototyping, and evaluation to progressively refine and improve a design based on feedback and learning.",
        order_num=2)
    insert_answer(conn, term_id, 1, "Iteration is the practice of repeating the design-prototype-evaluate cycle multiple times, each time refining the design based on what was learned. It's about progressive improvement through repeated cycles.")
    insert_answer(conn, term_id, 2, "Iteration is crucial because good designs rarely emerge fully formed. It allows learning from mistakes, incorporating feedback, exploring alternatives, and progressively refining until the design meets user needs effectively.")
    insert_answer(conn, term_id, 3, "Iteration happens throughout the UX process, from early conceptual iterations through detailed design refinements. It's used whenever there's uncertainty or room for improvement, which is nearly always in UX work.")
    insert_answer(conn, term_id, 4, "Examples: sketching multiple concepts, testing a prototype, refining based on feedback, testing again; creating wireframes, getting feedback, revising, testing; multiple rounds of usability testing with improvements between rounds.")
    insert_answer(conn, term_id, 5, "Iteration is the mechanism that drives the UX Wheel. Each cycle through Analysis-Design-Prototyping-Evaluation is an iteration. More iterations generally lead to better designs, though diminishing returns eventually occur.")
    insert_answer(conn, term_id, 6, "Effective iteration involves: testing early and often, being open to change, making informed refinements based on data, knowing when to iterate vs. when to move forward, and balancing iteration with project timelines.")
    insert_answer(conn, term_id, 7, "Iteration is a practice/activity, while the UX Wheel is a process model that incorporates iteration. Evaluation drives iteration by providing feedback. Iteration is how designs progressively improve through the Wheel.")

    # 3. Analysis
    term_id = insert_term(conn, category_id, "Analysis",
        "The phase of the UX process focused on understanding users, their work, their environment, and their needs through research and data interpretation to inform design.",
        order_num=3)
    insert_answer(conn, term_id, 1, "Analysis is the UX phase dedicated to understanding the problem space: who users are, what they're trying to accomplish, how they currently work, what problems they face, and what context surrounds their activities.")
    insert_answer(conn, term_id, 2, "Analysis is critical because good design must be based on real user needs and context. Without proper analysis, teams risk building solutions for wrong problems or missing critical user needs and constraints.")
    insert_answer(conn, term_id, 3, "Analysis occurs early in projects and at the start of each iteration. It includes contextual inquiry, contextual analysis, requirements extraction, and creating design-informing models to guide design work.")
    insert_answer(conn, term_id, 4, "Examples: conducting user interviews, observing work practices, analyzing workflows, creating personas, building task models, identifying barriers, extracting requirements from research data.")
    insert_answer(conn, term_id, 5, "Analysis is the first phase in the UX Wheel. It precedes Design by providing the understanding and requirements that inform design decisions. Analysis outputs (personas, scenarios, requirements) feed directly into Design.")
    insert_answer(conn, term_id, 6, "Good analysis involves: direct user engagement, systematic data collection, thorough interpretation, creating useful models and artifacts, extracting actionable insights, and communicating findings effectively to inform design.")
    insert_answer(conn, term_id, 7, "Analysis focuses on understanding (what is/what's needed), while Design focuses on creating (what could be). Analysis is research-oriented and convergent; Design is creative and divergent. Analysis informs Design.")

    # 4. Design (in UX Process context)
    term_id = insert_term(conn, category_id, "Design",
        "The phase of the UX process where creative solutions are generated and refined based on understanding from analysis, progressing from conceptual ideas to detailed specifications.",
        order_num=4)
    insert_answer(conn, term_id, 1, "In the UX process, Design is the phase where teams create solutions based on Analysis findings. It progresses from ideation and conceptual design through intermediate and detailed design to refined specifications ready for implementation.")
    insert_answer(conn, term_id, 2, "The Design phase is essential because it transforms user understanding into concrete solutions. This is where creativity and problem-solving happen, generating ideas that address user needs identified in Analysis.")
    insert_answer(conn, term_id, 3, "Design follows Analysis in the UX Wheel and precedes Prototyping. It occurs throughout product development, from initial concepts to detailed specifications, with iterative refinement based on evaluation.")
    insert_answer(conn, term_id, 4, "Examples: brainstorming solutions, sketching concepts, creating storyboards, designing interaction flows, developing wireframes, creating visual compositions, specifying detailed interactions and behaviors.")
    insert_answer(conn, term_id, 5, "Design sits between Analysis (which provides requirements and understanding) and Prototyping (which realizes designs for testing). Design takes inputs from Analysis and creates outputs that drive Prototyping and eventually implementation.")
    insert_answer(conn, term_id, 6, "Effective Design involves: grounding decisions in Analysis findings, exploring multiple alternatives, progressing from rough to refined, balancing creativity with constraints, and preparing clear specifications for Prototyping/development.")
    insert_answer(conn, term_id, 7, "Design is creative/generative (creating solutions), while Analysis is investigative/interpretive (understanding problems). Prototyping is about realization (making designs tangible). Design is the central creative phase of UX.")

    # 5. Prototyping (in UX Process context)
    term_id = insert_term(conn, category_id, "Prototyping",
        "The phase of creating preliminary versions of the design to explore, communicate, and test ideas before full implementation, varying in fidelity and scope.",
        order_num=5)
    insert_answer(conn, term_id, 1, "Prototyping is the UX phase where designs are made tangible through representations ranging from paper sketches to interactive digital mockups. Prototypes make abstract design ideas concrete and testable.")
    insert_answer(conn, term_id, 2, "Prototyping is crucial because it enables testing and validation before expensive implementation. It helps identify problems early, communicate designs to stakeholders, and explore alternatives cheaply and quickly.")
    insert_answer(conn, term_id, 3, "Prototyping occurs after Design and before Evaluation in the UX Wheel, though it often overlaps with both. It happens throughout development, with increasing fidelity as designs mature and more aspects become validated.")
    insert_answer(conn, term_id, 4, "Examples: paper sketches to test concepts, clickable wireframes to test navigation, interactive mockups to test detailed interactions, Wizard of Oz prototypes to test novel concepts, video prototypes to test concepts.")
    insert_answer(conn, term_id, 5, "Prototyping follows Design (implementing design decisions) and enables Evaluation (providing something to test). Different prototype types serve different purposes across the design progression from conceptual to detailed.")
    insert_answer(conn, term_id, 6, "Good prototyping involves: choosing appropriate fidelity for the questions being asked, creating prototypes quickly, testing the right aspects, avoiding over-investment before validation, and using prototypes to drive learning.")
    insert_answer(conn, term_id, 7, "Prototyping is about realization/representation (making designs tangible), Design is about creation (generating solutions), and Evaluation is about assessment (validating designs). Prototypes are vehicles for learning through evaluation.")

    # 6. Evaluation (in UX Process context)
    term_id = insert_term(conn, category_id, "Evaluation",
        "The phase of assessing designs through various methods to identify problems, validate decisions, and generate insights that drive improvements in the next iteration.",
        order_num=6)
    insert_answer(conn, term_id, 1, "Evaluation is the UX phase where designs are assessed to determine how well they meet user needs and usability standards. It uses various methods to identify issues, validate design decisions, and drive improvements.")
    insert_answer(conn, term_id, 2, "Evaluation is essential because it provides objective feedback on design quality, catches problems before launch, validates assumptions, and generates insights that drive iterative improvement. It prevents shipping poor designs.")
    insert_answer(conn, term_id, 3, "Evaluation occurs after Prototyping in the UX Wheel and feeds back into Analysis/Design for the next iteration. It happens throughout development, from early conceptual validation to pre-launch usability testing.")
    insert_answer(conn, term_id, 4, "Examples: usability testing with real users, heuristic evaluation by experts, cognitive walkthroughs, A/B testing, analytics review, design critiques, accessibility audits.")
    insert_answer(conn, term_id, 5, "Evaluation completes the UX Wheel cycle by assessing Prototypes, identifying issues, and generating insights that inform the next iteration's Analysis and Design. It's the critical feedback mechanism that drives improvement.")
    insert_answer(conn, term_id, 6, "Effective evaluation involves: choosing appropriate methods for questions and stage, testing with representative users, systematic analysis, actionable findings, clear communication of results, and driving improvements in next iteration.")
    insert_answer(conn, term_id, 7, "Evaluation is assessment/validation (judging quality), while Design is creation (generating solutions) and Analysis is investigation (understanding problems). Evaluation provides the feedback that enables iteration and improvement.")

    # 7. Tradeoffs
    term_id = insert_term(conn, category_id, "Tradeoffs",
        "The necessary compromises and balanced decisions made when competing constraints, requirements, or design qualities cannot all be maximally satisfied simultaneously.",
        order_num=7)
    insert_answer(conn, term_id, 1, "Tradeoffs are the compromises made when you can't optimize everything simultaneously - balancing competing needs like speed vs. accuracy, simplicity vs. power, time vs. quality, or different user groups' needs.")
    insert_answer(conn, term_id, 2, "Understanding tradeoffs is critical because design always involves constraints - time, budget, technical limitations, competing user needs. Good designers explicitly consider and make informed tradeoffs rather than ignoring tensions.")
    insert_answer(conn, term_id, 3, "Tradeoff decisions occur throughout the UX process, particularly in Design when balancing requirements, and when scope/timeline pressures require prioritization. They're inherent in any real-world project with constraints.")
    insert_answer(conn, term_id, 4, "Examples: simplifying UI for novices vs. providing power features for experts, spending time on research vs. design, depth vs. breadth in prototypes, innovation vs. familiarity, accessibility features vs. sleek aesthetics.")
    insert_answer(conn, term_id, 5, "Tradeoffs affect all UX phases - how much time for Analysis vs. Design, prototype fidelity vs. speed, evaluation rigor vs. timeline. They're a constant reality that shapes decisions throughout the UX Wheel.")
    insert_answer(conn, term_id, 6, "Managing tradeoffs well involves: making them explicit, understanding implications, using data to inform decisions, considering long-term impact, getting stakeholder input, and documenting rationale for future reference.")
    insert_answer(conn, term_id, 7, "Tradeoffs are necessary compromises in real projects, while ideals are what you'd do with unlimited resources. Constraints create the need for tradeoffs. Different than prioritization, which is choosing what to do; tradeoffs are about balancing competing goods.")

    print(f"  Inserted {7} terms for Overall UX Process section")

def main():
    """Main function to populate the entire database"""
    print("Starting database population...")
    print("="*50)

    conn = create_connection()

    try:
        # Insert foundation data
        insert_questions(conn)
        insert_categories(conn)

        # Populate each section
        populate_general_section(conn)
        populate_ux_in_se_section(conn)
        populate_overall_ux_process(conn)

        # Get count of terms
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM terms")
        term_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM answers")
        answer_count = cursor.fetchone()[0]

        print("="*50)
        print(f"Database population started!")
        print(f"Total terms inserted so far: {term_count}")
        print(f"Total answers inserted so far: {answer_count}")
        print("\nNOTE: This script currently populates the first 3 sections (20 terms).")
        print("The remaining sections (Analysis, Design, Prototyping, Evaluation)")
        print("will be added in subsequent scripts due to the large volume of content.")

    finally:
        conn.close()

if __name__ == "__main__":
    main()
