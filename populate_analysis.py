#!/usr/bin/env python3
"""
Populate Analysis Section (Category 4)
This script adds all Analysis-related terms to the HCI database
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

def populate_analysis_section(conn):
    """Populate the Analysis category (Category 4)"""
    print("Populating Analysis section...")
    category_id = 4

    # Main category: Contextual Inquiry
    ci_term_id = insert_term(conn, category_id, "Contextual Inquiry",
        "A user research method involving going into the user's environment to observe and interview them while they work, gathering rich contextual data about work practices and needs.",
        order_num=1)
    insert_answer(conn, ci_term_id, 1, "Contextual inquiry is a field research method where researchers observe and interview users in their actual work environment while they perform real tasks, gathering rich, contextual understanding of work practices.")
    insert_answer(conn, ci_term_id, 2, "It's important because it reveals how people actually work (vs. how they say they work), uncovers tacit knowledge, identifies unarticulated needs, and provides authentic context that lab studies miss.")
    insert_answer(conn, ci_term_id, 3, "Contextual inquiry is used early in the UX process during the Analysis phase, before design begins. It's appropriate when you need deep understanding of user work, particularly for complex domains or existing workflows.")
    insert_answer(conn, ci_term_id, 4, "Examples: observing nurses using hospital systems during shifts, watching developers use code editors in their workspace, observing retail workers using POS systems during customer interactions.")
    insert_answer(conn, ci_term_id, 5, "Contextual inquiry is the primary data collection method in the Analysis phase. Its outputs (observations, interviews, artifacts) feed into contextual analysis, which creates models that inform design.")
    insert_answer(conn, ci_term_id, 6, "Good contextual inquiry involves: minimal disruption to natural work, active observation and note-taking, asking clarifying questions, collecting artifacts, focusing on work practice rather than opinions, and capturing rich detail.")
    insert_answer(conn, ci_term_id, 7, "Contextual inquiry differs from lab studies (natural vs. controlled environment), surveys (observation vs. self-report), and interviews alone (watching work vs. talking about work). It's ethnographic and context-rich.")

    # Sub-terms of Contextual Inquiry
    term_id = insert_term(conn, category_id, "System Concept Statement",
        "A brief statement defining the high-level idea of what system or solution will support the work being studied, providing initial focus for inquiry.",
        parent_id=ci_term_id, hierarchy_level=1, order_num=1)
    insert_answer(conn, term_id, 1, "A system concept statement is a brief, high-level description of the envisioned system or product that will support the work domain being studied. It provides initial direction without constraining the inquiry.")
    insert_answer(conn, term_id, 2, "It's important because it focuses the contextual inquiry effort on relevant aspects of work while remaining open to discovery. It helps researchers know what to pay attention to without biasing findings.")
    insert_answer(conn, term_id, 3, "The system concept statement is developed before beginning contextual inquiry and refined as understanding grows. It guides what work domains and practices to study.")
    insert_answer(conn, term_id, 4, "Examples: 'A mobile app to help field technicians access repair manuals and report issues,' 'A system to support collaborative scientific data analysis,' 'A tool for managing patient care coordination.'")
    insert_answer(conn, term_id, 5, "The system concept statement initiates the Analysis phase by defining the problem space. It focuses contextual inquiry efforts, though findings may refine or challenge the initial concept.")
    insert_answer(conn, term_id, 6, "A good system concept statement is: brief (1-2 sentences), focused on supporting work (not specific features), open enough to allow discovery, and refined based on early findings if needed.")
    insert_answer(conn, term_id, 7, "Unlike detailed requirements (which are specific), the system concept is high-level and conceptual. Unlike design ideas (which are solutions), it describes the problem space and general intent.")

    term_id = insert_term(conn, category_id, "Ethnography",
        "The study of people and cultures through immersion in their environment, adapted in HCI to understand users' work practices, social context, and culture.",
        parent_id=ci_term_id, hierarchy_level=1, order_num=2)
    insert_answer(conn, term_id, 1, "Ethnography is a research approach from anthropology involving immersing yourself in users' environments to understand their culture, practices, and context through observation and participation over extended periods.")
    insert_answer(conn, term_id, 2, "It's important in HCI because it reveals deep cultural and social factors affecting technology use, uncovers implicit norms and practices, and provides holistic understanding that survey/lab methods miss.")
    insert_answer(conn, term_id, 3, "Ethnographic approaches are used when deep cultural understanding is needed, particularly for complex social/organizational contexts, unfamiliar domains, or when designing systems that affect work culture.")
    insert_answer(conn, term_id, 4, "Examples: spending weeks in a hospital to understand clinical culture before designing medical software, embedding with a sales team to understand their communication patterns, observing classroom culture for educational technology.")
    insert_answer(conn, term_id, 5, "Ethnography is a foundational approach for contextual inquiry. It emphasizes cultural and social aspects of work, providing depth that informs all subsequent analysis and design work.")
    insert_answer(conn, term_id, 6, "Good ethnography involves: extended time in the field, building rapport with participants, observing without judging, noting cultural norms, understanding social relationships, and being open to unexpected findings.")
    insert_answer(conn, term_id, 7, "Ethnography is longer-term and more immersive than standard contextual inquiry, more focused on culture than task analysis, and more interpretive than quantitative research methods.")

    term_id = insert_term(conn, category_id, "Work, Work Practice, Work Domain",
        "Key concepts in contextual inquiry: work (user activities/tasks), work practice (how work is actually done), and work domain (the field/area where work occurs).",
        parent_id=ci_term_id, hierarchy_level=1, order_num=3)
    insert_answer(conn, term_id, 1, "Work is what users do (tasks/activities), work practice is how they do it (methods, tools, collaboration, workarounds), and work domain is the field/context where it happens (nursing, software development, retail, etc.).")
    insert_answer(conn, term_id, 2, "These concepts are important because they structure thinking about users: what they're trying to accomplish (work), how they currently accomplish it (practice), and where/why (domain). Understanding all three is essential for good design.")
    insert_answer(conn, term_id, 3, "These concepts frame contextual inquiry and analysis. Researchers study the work domain, observe work practices, and decompose work into understandable units for analysis and design.")
    insert_answer(conn, term_id, 4, "Examples: Domain=healthcare, Work=reviewing patient records and prescribing medication, Practice=using EMR system, checking with nurses, writing notes. Domain=software dev, Work=debugging, Practice=using debuggers/logs/print statements.")
    insert_answer(conn, term_id, 5, "Understanding work domain provides context, identifying specific work defines scope and goals, and studying work practice reveals how current tools/processes support or hinder work - all informing design.")
    insert_answer(conn, term_id, 6, "Good analysis distinguishes: the work itself (goals/outcomes), how it's currently done (practice - which may be inefficient), and domain constraints/culture. This helps identify improvement opportunities vs. necessary domain characteristics.")
    insert_answer(conn, term_id, 7, "Work is what needs accomplishing (goals), work practice is current methods (which designs might change), work domain is the context (which designs must fit). Work is stable, practice varies, domain provides constraints.")

    term_id = insert_term(conn, category_id, "Interviews",
        "Structured or semi-structured conversations with users to understand their work, needs, preferences, and experiences, often conducted during contextual inquiry.",
        parent_id=ci_term_id, hierarchy_level=1, order_num=4)
    insert_answer(conn, term_id, 1, "Interviews are structured conversations where researchers ask users about their work, needs, experiences, and opinions. In contextual inquiry, they're often semi-structured and conducted while observing work.")
    insert_answer(conn, term_id, 2, "Interviews are important because they reveal user perspectives, motivations, preferences, and explanations for observed behaviors. They provide the 'why' behind the 'what' observed in field studies.")
    insert_answer(conn, term_id, 3, "Interviews are used during contextual inquiry (alongside observation), during requirements gathering, and sometimes during evaluation. They're appropriate when you need to understand user perspectives, not just observe behaviors.")
    insert_answer(conn, term_id, 4, "Examples: asking nurses why they use a particular workaround, having developers explain their debugging process, asking users to walk through their decision-making, conducting post-task interviews about experience.")
    insert_answer(conn, term_id, 5, "In contextual inquiry, interviews complement observation - you watch users work, then ask questions to understand their thinking. Interview data combines with observations and artifacts in contextual analysis.")
    insert_answer(conn, term_id, 6, "Good interviewing involves: open-ended questions, active listening, avoiding leading questions, asking for specific examples, following interesting threads, being comfortable with silence, and focusing on actual behaviors not hypotheticals.")
    insert_answer(conn, term_id, 7, "Interviews gather self-reported data (what people say), while observation captures actual behavior (what people do). Contextual inquiry combines both, since they often differ. Interviews alone miss tacit knowledge and actual practice.")

    term_id = insert_term(conn, category_id, "Observations",
        "Systematic watching and recording of users performing their work in natural settings to understand actual work practices and identify usability issues.",
        parent_id=ci_term_id, hierarchy_level=1, order_num=5)
    insert_answer(conn, term_id, 1, "Observations involve systematically watching users perform their work in natural settings, carefully noting what they do, how they do it, tools they use, interactions with others, and problems they encounter.")
    insert_answer(conn, term_id, 2, "Observations are critical because people often can't articulate their own practices (tacit knowledge), may describe idealized rather than actual behavior, and perform workarounds they don't consider worth mentioning.")
    insert_answer(conn, term_id, 3, "Observations are central to contextual inquiry, occurring in users' actual work environments during real work activities. They're used whenever understanding actual practice (vs. reported practice) is important.")
    insert_answer(conn, term_id, 4, "Examples: watching a user struggle with a form, noting efficient keyboard shortcuts an expert uses, observing informal collaboration between coworkers, seeing workarounds users have developed.")
    insert_answer(conn, term_id, 5, "Observations generate raw data during contextual inquiry. This data is captured in work activity notes, later analyzed to create flow models and work activity affinity diagrams, ultimately informing design.")
    insert_answer(conn, term_id, 6, "Good observation involves: minimal interference with natural work, detailed note-taking, noticing both smooth and problematic moments, watching the whole context (not just screen), and asking clarifying questions without disrupting flow.")
    insert_answer(conn, term_id, 7, "Observations capture actual behavior (what happens), while interviews capture reported behavior (what users say happens). Observations are more objective but need interpretation; interviews provide subjective context and explanations.")

    term_id = insert_term(conn, category_id, "Work Activity Data",
        "The raw information collected during contextual inquiry, including observations, interview responses, artifacts, and notes about work practices and context.",
        parent_id=ci_term_id, hierarchy_level=1, order_num=6)
    insert_answer(conn, term_id, 1, "Work activity data is all the raw information gathered during contextual inquiry: observation notes, interview transcripts, photos, collected artifacts, sketches, and any other records of what was learned about user work.")
    insert_answer(conn, term_id, 2, "This data is important because it's the foundation for all subsequent analysis. Rich, detailed work activity data enables creation of accurate models, extraction of real requirements, and deep understanding that informs design.")
    insert_answer(conn, term_id, 3, "Work activity data is collected during contextual inquiry sessions and becomes the input for contextual analysis activities like creating work activity notes, flow models, and affinity diagrams.")
    insert_answer(conn, term_id, 4, "Examples: notes about a nurse's workflow, photos of a technician's workspace, a printed form users annotate, quotes from interviews, timing notes about task duration, sketches of physical layouts.")
    insert_answer(conn, term_id, 5, "Work activity data flows from contextual inquiry into contextual analysis. It's the raw material that gets organized, interpreted, and synthesized into useful models and requirements that guide design.")
    insert_answer(conn, term_id, 6, "Quality work activity data is: detailed and specific, captures context, includes verbatim quotes, records both successes and problems, notes emotional responses, and covers diverse situations and users.")
    insert_answer(conn, term_id, 7, "Work activity data is raw and uninterpreted, while work activity notes are organized interpretations. Data is the direct capture; analysis involves organizing and making sense of it.")

    term_id = insert_term(conn, category_id, "Work Artifacts",
        "Physical or digital objects users create or interact with during their work, such as forms, documents, tools, notes, or output products.",
        parent_id=ci_term_id, hierarchy_level=1, order_num=7)
    insert_answer(conn, term_id, 1, "Work artifacts are the physical and digital objects that are part of users' work - forms they fill out, documents they create, tools they use, notes they keep, Post-its on monitors, checklists, reports, etc.")
    insert_answer(conn, term_id, 2, "Artifacts are important because they reveal actual work practices, show what information users need, demonstrate workarounds, and provide concrete examples of work inputs/outputs that systems must support.")
    insert_answer(conn, term_id, 3, "Artifacts are collected during contextual inquiry (photographed, copied, or noted), then analyzed to understand their role in work. They contribute to artifact models and inform requirements.")
    insert_answer(conn, term_id, 4, "Examples: Post-it notes with passwords, printed forms users annotate, spreadsheets used for tracking, email templates, handwritten logs, checklists taped to monitors, customized tool configurations.")
    insert_answer(conn, term_id, 5, "Artifacts are discovered during contextual inquiry, inform artifact models in design-informing models, and reveal requirements about information needs and workflows that must be supported in design.")
    insert_answer(conn, term_id, 6, "Analyzing artifacts well involves: collecting/documenting them, understanding their purpose in work, noting modifications users make, identifying information they contain, and recognizing what needs they fulfill.")
    insert_answer(conn, term_id, 7, "Artifacts are concrete objects (things), while work activity data includes observations and notes (information about things and behaviors). Artifacts are physical/digital evidence of work practices.")

    # Main category: Contextual Analysis
    ca_term_id = insert_term(conn, category_id, "Contextual Analysis",
        "The process of organizing, interpreting, and synthesizing work activity data to create structured representations and extract insights about user work.",
        order_num=2)
    insert_answer(conn, ca_term_id, 1, "Contextual analysis is the systematic process of organizing and making sense of work activity data by creating structured representations like work activity notes, flow models, and work activity affinity diagrams.")
    insert_answer(conn, ca_term_id, 2, "It's important because raw data alone doesn't drive design - it must be organized, interpreted, and synthesized to reveal patterns, identify barriers, and extract actionable insights about user needs.")
    insert_answer(conn, ca_term_id, 3, "Contextual analysis follows contextual inquiry in the Analysis phase. It transforms raw observations and interviews into organized, interpretable representations that inform requirements and design.")
    insert_answer(conn, ca_term_id, 4, "Examples: organizing field notes into work activity notes, drawing flow models from observed workflows, building affinity diagrams to find themes, identifying common barriers users face.")
    insert_answer(conn, ca_term_id, 5, "Contextual analysis sits between data collection (contextual inquiry) and design. It processes raw work activity data into models and insights that inform requirements extraction and design-informing models.")
    insert_answer(conn, ca_term_id, 6, "Effective contextual analysis involves: systematic organization of data, collaborative interpretation, creation of visual models, identification of patterns across users, and extraction of actionable design insights.")
    insert_answer(conn, ca_term_id, 7, "Contextual inquiry is data collection (gathering), while contextual analysis is data interpretation (making sense). Inquiry is field research; analysis is synthesis work typically done after returning from the field.")

    # Sub-terms of Contextual Analysis
    term_id = insert_term(conn, category_id, "Work Activity Notes",
        "Organized, cleaned-up notes from contextual inquiry sessions that structure observations and findings into a usable format for analysis.",
        parent_id=ca_term_id, hierarchy_level=1, order_num=1)
    insert_answer(conn, term_id, 1, "Work activity notes are cleaned-up, organized versions of raw field notes from contextual inquiry, structured to highlight key observations, quotes, insights, and findings in a usable format.")
    insert_answer(conn, term_id, 2, "They're important because raw field notes are often messy and hard for others to use. Work activity notes make findings accessible to the team and provide organized input for further analysis.")
    insert_answer(conn, term_id, 3, "Work activity notes are created shortly after contextual inquiry sessions while memories are fresh. They're used as input for creating flow models, affinity diagrams, and requirements extraction.")
    insert_answer(conn, term_id, 4, "Examples: organized notes with sections for workflow observed, pain points, quotes, artifacts seen, context description, and researcher interpretations/questions.")
    insert_answer(conn, term_id, 5, "Work activity notes are the first step in contextual analysis, transforming raw data into organized form. They feed into all subsequent analysis activities and become reference material throughout the project.")
    insert_answer(conn, term_id, 6, "Good work activity notes are: organized clearly, capture key quotes verbatim, distinguish observation from interpretation, include enough context for others to understand, and are created while memory is fresh.")
    insert_answer(conn, term_id, 7, "Work activity notes are organized interpretations of raw data (which is messy/incomplete), more detailed than flow models (which are visual summaries), and input for creating affinity diagrams (which synthesize across sessions).")

    term_id = insert_term(conn, category_id, "Flow Model",
        "A diagram showing the flow of information, artifacts, and communication between people, systems, and groups in a work process.",
        parent_id=ca_term_id, hierarchy_level=1, order_num=2)
    insert_answer(conn, term_id, 1, "A flow model is a visual diagram showing how information, artifacts, and communication flow between people, roles, and systems during work processes. It shows who talks to whom, what information is shared, and what artifacts move between actors.")
    insert_answer(conn, term_id, 2, "Flow models are important because they reveal communication patterns, information bottlenecks, coordination requirements, and collaboration structures that systems must support or improve.")
    insert_answer(conn, term_id, 3, "Flow models are created during contextual analysis based on observations from contextual inquiry. They're also used as design-informing models and can show both current and envisioned situations.")
    insert_answer(conn, term_id, 4, "Examples: diagram showing doctor->nurse->pharmacy medication order flow, showing sales->engineering->customer communication patterns, showing how bug reports flow through a development team.")
    insert_answer(conn, term_id, 5, "Flow models are created during contextual analysis and also appear in design-informing models as usage models. They help identify communication needs that designs must address.")
    insert_answer(conn, term_id, 6, "Good flow models: clearly show actors/roles, indicate information/artifact flows with labeled arrows, note breakdowns or bottlenecks, distinguish different types of communication, and focus on relevant work aspects.")
    insert_answer(conn, term_id, 7, "Flow models show information/communication flows (between entities), while hierarchical task inventories show task decomposition (within work). Flow models are social/collaborative; task models are individual work-focused.")

    term_id = insert_term(conn, category_id, "Work Activity Affinity Diagram (WAAD)",
        "A hierarchical organization of observations from multiple contextual inquiry sessions, grouping related findings to reveal patterns and themes across users.",
        parent_id=ca_term_id, hierarchy_level=1, order_num=3)
    insert_answer(conn, term_id, 1, "A WAAD is created by writing individual observations on notes, then collaboratively grouping related notes into clusters, creating hierarchical categories that reveal themes and patterns across multiple contextual inquiry sessions.")
    insert_answer(conn, term_id, 2, "WAADs are important because they synthesize findings across users, revealing common patterns and needs rather than individual quirks. They help teams build shared understanding and identify design priorities.")
    insert_answer(conn, term_id, 3, "WAADs are created during contextual analysis after collecting data from multiple users. The team collaboratively builds them, then uses resulting themes to inform requirements and design.")
    insert_answer(conn, term_id, 4, "Examples: grouping notes about workflow problems, clustering observations about information needs, organizing findings about collaboration patterns, identifying common barriers users face.")
    insert_answer(conn, term_id, 5, "WAADs synthesize work activity notes from multiple contextual inquiry sessions, revealing patterns that inform requirements extraction and design-informing models. They help teams see the forest, not just trees.")
    insert_answer(conn, term_id, 6, "Effective WAAD creation involves: individual notes capturing single observations, bottom-up grouping, team collaboration to build shared understanding, hierarchical organization revealing themes, and labeling that captures meaning.")
    insert_answer(conn, term_id, 7, "WAADs synthesize across sessions (finding patterns), while work activity notes document individual sessions. WAADs are hierarchical and thematic; flow models are structural diagrams. WAADs reveal what; flow models show how.")

    term_id = insert_term(conn, category_id, "Barriers",
        "Obstacles, problems, or difficulties users encounter in their work that impede efficiency, effectiveness, or satisfaction - key targets for design solutions.",
        parent_id=ca_term_id, hierarchy_level=1, order_num=4)
    insert_answer(conn, term_id, 1, "Barriers are obstacles users face during their work - inefficient processes, confusing interfaces, missing information, communication gaps, system limitations, or any factors that impede work accomplishment.")
    insert_answer(conn, term_id, 2, "Identifying barriers is crucial because they represent opportunities for improvement. Designs that remove or reduce barriers directly improve user experience and work effectiveness.")
    insert_answer(conn, term_id, 3, "Barriers are identified during contextual inquiry (observation), highlighted in contextual analysis, and become primary drivers for requirements and design solutions.")
    insert_answer(conn, term_id, 4, "Examples: waiting for system responses, hunting for needed information, switching between multiple applications, manual data re-entry, unclear error messages, inadequate access to expert knowledge.")
    insert_answer(conn, term_id, 5, "Barriers identified in Analysis directly inform Design by highlighting what problems must be solved. They appear in requirements and drive design decisions about what functionality and interaction patterns to include.")
    insert_answer(conn, term_id, 6, "Good barrier analysis involves: documenting specific instances, understanding root causes not just symptoms, assessing impact and frequency, and identifying which barriers designs can realistically address.")
    insert_answer(conn, term_id, 7, "Barriers are problems (what's wrong), while requirements specify solutions (what's needed). Identifying barriers is descriptive (current state); requirements are prescriptive (desired state). Barriers drive requirement creation.")

    # Main category: Requirements
    req_term_id = insert_term(conn, category_id, "Requirements",
        "Specifications of what the system must do or provide to meet user needs and support their work effectively, derived from analysis of user work.",
        order_num=3)
    insert_answer(conn, req_term_id, 1, "Requirements are specific statements about what a system must do or provide to meet user needs. They specify capabilities, functions, qualities, and constraints that designs must satisfy.")
    insert_answer(conn, req_term_id, 2, "Requirements are critical because they bridge analysis and design - translating user needs into actionable specifications that guide what to build. They ensure designs address real user needs.")
    insert_answer(conn, req_term_id, 3, "Requirements are extracted during the Analysis phase after contextual inquiry and analysis. They guide Design activities and provide criteria for Evaluation.")
    insert_answer(conn, req_term_id, 4, "Examples: 'System must support collaborative editing,' 'Users must be able to filter results by date,' 'Response time must be under 2 seconds,' 'Must work offline with sync capability.'")
    insert_answer(conn, req_term_id, 5, "Requirements are extracted from analysis findings (observations, barriers, user needs). They guide design by specifying what must be included, and drive evaluation by providing success criteria.")
    insert_answer(conn, req_term_id, 6, "Good requirements are: specific and clear, derived from real user needs (with rationale), testable/verifiable, prioritized by importance, and focused on what (not how - that's design).")
    insert_answer(conn, req_term_id, 7, "Requirements specify what systems must do (functional) or what qualities they must have (non-functional). Unlike design decisions (which specify how), requirements specify the must-haves that designs must satisfy.")

    # Sub-terms of Requirements
    term_id = insert_term(conn, category_id, "Requirements Extraction",
        "The process of deriving specific system requirements from analysis of user work, using deductive reasoning to identify what the system must provide.",
        parent_id=req_term_id, hierarchy_level=1, order_num=1)
    insert_answer(conn, term_id, 1, "Requirements extraction is the systematic process of deriving specific requirements from analysis findings - examining observations, barriers, and user needs to determine what capabilities the system must have.")
    insert_answer(conn, term_id, 2, "It's important because it ensures requirements are grounded in actual user needs rather than assumptions. It creates the bridge from 'what we learned' (analysis) to 'what we must build' (design).")
    insert_answer(conn, term_id, 3, "Requirements extraction occurs during the Analysis phase, after contextual inquiry and analysis have been completed. It uses those findings to derive specific system requirements.")
    insert_answer(conn, term_id, 4, "Examples: from observing users switching between apps, extract requirement for integrated interface; from users struggling to find information, extract requirement for robust search functionality.")
    insert_answer(conn, term_id, 5, "Requirements extraction takes contextual analysis outputs (barriers, work activity patterns) and transforms them into requirements that drive design decisions and evaluation criteria.")
    insert_answer(conn, term_id, 6, "Effective extraction involves: using deductive reasoning, tracing requirements to specific findings, including rationale, being specific about needs, distinguishing must-haves from nice-to-haves.")
    insert_answer(conn, term_id, 7, "Extraction is the process (how you derive requirements), while requirements are the output (the specifications themselves). Extraction uses deductive reasoning; analysis uses inductive pattern-finding.")

    term_id = insert_term(conn, category_id, "Deductive Reasoning",
        "Logical reasoning from general observations to specific conclusions, used in requirements extraction to derive specific requirements from general findings.",
        parent_id=req_term_id, hierarchy_level=1, order_num=2)
    insert_answer(conn, term_id, 1, "Deductive reasoning in UX involves starting with general observations or findings and logically deriving specific requirements or design implications. It's reasoning from general to specific.")
    insert_answer(conn, term_id, 2, "It's important because it creates logical connections between what was observed and what's needed, ensuring requirements are justified by evidence rather than hunches.")
    insert_answer(conn, term_id, 3, "Deductive reasoning is used during requirements extraction and when making design decisions based on research findings. It helps justify design choices with logical arguments from evidence.")
    insert_answer(conn, term_id, 4, "Examples: 'Users frequently switch between email and calendar (observation) → System must integrate email and calendar (requirement).' 'Users forget passwords (observation) → Must provide password reset (requirement).'")
    insert_answer(conn, term_id, 5, "Deductive reasoning connects analysis findings to requirements and design decisions, providing logical justification throughout the UX process.")
    insert_answer(conn, term_id, 6, "Good deductive reasoning: makes logical connections explicit, checks that conclusions follow from premises, considers alternative interpretations, and documents the reasoning chain.")
    insert_answer(conn, term_id, 7, "Deductive reasoning goes from general to specific (findings → requirements), while inductive reasoning (used in analysis) goes from specific to general (observations → patterns). Both are used in UX.")

    term_id = insert_term(conn, category_id, "Rationale",
        "The justification or reasoning explaining why a requirement or design decision is necessary, linking it back to user needs and research findings.",
        parent_id=req_term_id, hierarchy_level=1, order_num=3)
    insert_answer(conn, term_id, 1, "Rationale is the explanation of why a requirement or design decision is necessary - the user needs, observations, or business reasons that justify it. It connects decisions to their evidence base.")
    insert_answer(conn, term_id, 2, "Rationale is critical because it: enables evaluation of requirements, helps prioritization, prevents arbitrary changes, educates stakeholders, and preserves understanding when team members change.")
    insert_answer(conn, term_id, 3, "Rationale should be documented with every requirement and major design decision. It's referenced during design reviews, when prioritizing, and when stakeholders question decisions.")
    insert_answer(conn, term_id, 4, "Examples: 'Requirement: Offline mode. Rationale: Field technicians often work in areas without connectivity (observed in sessions 3, 5, 7).' 'Design: Large buttons. Rationale: Primary users wear gloves (contextual inquiry finding).'")
    insert_answer(conn, term_id, 5, "Rationale connects analysis findings to requirements and design decisions, creating traceability throughout the UX process. It justifies decisions and enables informed tradeoffs.")
    insert_answer(conn, term_id, 6, "Good rationale is: specific and detailed, references evidence (user quotes, observation notes), explains the user need or problem, and is documented clearly for future reference.")
    insert_answer(conn, term_id, 7, "Rationale explains 'why' (justification), while requirements state 'what' (specifications) and designs show 'how' (solutions). Rationale is the reasoning that connects research to decisions.")

    print(f"  Inserted terms for Analysis section (part 1: Contextual Inquiry, Contextual Analysis, Requirements)")

    # Note: Design-Informing Models section will be added in a separate function due to its size
    return ci_term_id, ca_term_id, req_term_id

def populate_design_informing_models(conn):
    """Populate Design-Informing Models (DIMs) section"""
    print("Populating Design-Informing Models section...")
    category_id = 4

    # Main category: Design-Informing Models (DIMs)
    dim_term_id = insert_term(conn, category_id, "Design-Informing Models (DIMs)",
        "Structured representations of users, their work, and context that guide and inform design decisions, including user models, usage models, and work environment models.",
        order_num=4)
    insert_answer(conn, dim_term_id, 1, "DIMs are structured representations created during analysis that capture understanding of users, their work, and context in forms specifically intended to guide design decisions. They include user models, usage models, and work environment models.")
    insert_answer(conn, dim_term_id, 2, "DIMs are crucial because they translate research findings into actionable design guidance. They help designers empathize with users, understand work context, and make informed decisions throughout design.")
    insert_answer(conn, dim_term_id, 3, "DIMs are created during the Analysis phase after contextual inquiry/analysis, then used throughout Design to guide decisions. They remain reference materials throughout the project.")
    insert_answer(conn, dim_term_id, 4, "Examples: personas describing user types, scenarios showing how work flows, hierarchical task inventories breaking down work structure, artifact models showing tools used, flow models showing communication.")
    insert_answer(conn, dim_term_id, 5, "DIMs conclude the Analysis phase by organizing findings into design-useful forms. They feed directly into Design activities, helping designers understand who they're designing for and what contexts they must support.")
    insert_answer(conn, dim_term_id, 6, "Effective DIMs are: based on real research data, organized for design use, detailed enough to inform decisions, communicated clearly to designers, and actually referenced during design work.")
    insert_answer(conn, dim_term_id, 7, "DIMs are structured for design use (not just documentation), more actionable than raw analysis findings, and include multiple model types (user/usage/environment) providing complementary perspectives on the design space.")

    # Current situation
    term_id = insert_term(conn, category_id, "Current Situation",
        "Design-informing models representing how users currently work, including existing tools, processes, and problems - the 'as-is' state.",
        parent_id=dim_term_id, hierarchy_level=1, order_num=1)
    insert_answer(conn, term_id, 1, "Current situation models represent how users currently accomplish their work, including existing tools, workflows, problems, and workarounds - providing the 'as-is' baseline for understanding what needs improvement.")
    insert_answer(conn, term_id, 2, "Understanding current situation is important because it reveals what works (to preserve), what doesn't (to fix), and contextual constraints (to respect). You can't improve what you don't understand.")
    insert_answer(conn, term_id, 3, "Current situation models are created from contextual inquiry data during Analysis. They provide baseline understanding that informs envisioned situation models and design decisions.")
    insert_answer(conn, term_id, 4, "Examples: flow models of current communication patterns, task models of current workflows, personas based on current user characteristics, scenarios describing current work practices.")
    insert_answer(conn, term_id, 5, "Current situation models form the foundation for design by establishing baseline understanding. They're compared with envisioned situation models to articulate the design vision and intended improvements.")
    insert_answer(conn, term_id, 6, "Good current situation models: accurately represent actual practice (not idealized), include both successful and problematic aspects, capture enough detail to inform design, and note barriers/pain points.")
    insert_answer(conn, term_id, 7, "Current situation shows 'as-is' (what exists now), while envisioned situation shows 'to-be' (what designs will enable). Current is descriptive; envisioned is prescriptive. Comparing them reveals design impact.")

    # Envisioned situation
    term_id = insert_term(conn, category_id, "Envisioned Situation",
        "Design-informing models representing how users will work with the new system, showing the improved 'to-be' state that design aims to achieve.",
        parent_id=dim_term_id, hierarchy_level=1, order_num=2)
    insert_answer(conn, term_id, 1, "Envisioned situation models represent how work will be performed with the new system - the 'to-be' state showing improved workflows, solved problems, and new capabilities that design will enable.")
    insert_answer(conn, term_id, 2, "Envisioned situation models are important because they articulate the design vision, guide design decisions toward intended improvements, and help stakeholders understand planned changes and benefits.")
    insert_answer(conn, term_id, 3, "Envisioned situation models are created during design thinking and early design phases, building on current situation understanding. They guide detailed design and help evaluate whether designs achieve the vision.")
    insert_answer(conn, term_id, 4, "Examples: scenarios showing improved workflows with new system, flow models showing streamlined communication, task models showing simplified processes, personas in contexts using new capabilities.")
    insert_answer(conn, term_id, 5, "Envisioned models bridge analysis and design - informed by current situation understanding, they articulate the design vision that guides detailed design work and provides criteria for evaluation.")
    insert_answer(conn, term_id, 6, "Effective envisioned models: show realistic improvements (not fantasy), clearly differ from current situation, demonstrate value to users, are specific enough to guide design, and address identified barriers.")
    insert_answer(conn, term_id, 7, "Envisioned situation is the vision (what should be), current situation is the baseline (what is), and design is the solution (how to get there). Envisioned guides design goals; design realizes the envisioned state.")

    # User Models (sub-category of DIMs)
    um_term_id = insert_term(conn, category_id, "User Models",
        "Design-informing models that characterize the users - their roles, characteristics, goals, and behaviors - including work roles, user classes, and personas.",
        parent_id=dim_term_id, hierarchy_level=1, order_num=3)
    insert_answer(conn, um_term_id, 1, "User models are DIMs that characterize who the users are - their roles, responsibilities, characteristics, goals, skills, and needs. They include work roles, user classes, social models, and personas.")
    insert_answer(conn, um_term_id, 2, "User models are critical because understanding users is fundamental to user-centered design. They help designers empathize with users, make decisions from user perspective, and ensure designs fit user characteristics.")
    insert_answer(conn, um_term_id, 3, "User models are created during Analysis from contextual inquiry data, refined during design, and referenced throughout design and evaluation to keep focus on user needs and characteristics.")
    insert_answer(conn, um_term_id, 4, "Examples: personas describing primary user types, work role descriptions, user classes segmented by expertise level, social models showing team structures and relationships.")
    insert_answer(conn, um_term_id, 5, "User models are one category of DIMs (alongside usage and environment models). They answer 'who are we designing for?' while usage models answer 'what do they do?' and environment models answer 'where do they work?'")
    insert_answer(conn, um_term_id, 6, "Effective user models: based on real user research, capture relevant characteristics, help designers empathize, are specific enough to guide decisions, and are actually used during design work.")
    insert_answer(conn, um_term_id, 7, "User models describe people (who), usage models describe activities (what/how), environment models describe context (where/with what). User models are about user characteristics; usage models are about user behaviors.")

    # User Models sub-items
    term_id = insert_term(conn, category_id, "Work Roles",
        "Distinct functional positions or jobs users occupy, each with specific responsibilities, goals, and work patterns relevant to system design.",
        parent_id=um_term_id, hierarchy_level=2, order_num=1)
    insert_answer(conn, term_id, 1, "Work roles are distinct job functions or positions users occupy (nurse, doctor, administrator), each with specific responsibilities, authority, goals, and work patterns that affect system needs.")
    insert_answer(conn, term_id, 2, "Work roles matter because different roles have different needs, permissions, workflows, and goals. Systems must support the distinct requirements of each role appropriately.")
    insert_answer(conn, term_id, 3, "Work roles are identified during contextual inquiry, documented as part of user models, and used to guide design decisions about functionality, permissions, interfaces, and workflows for different role types.")
    insert_answer(conn, term_id, 4, "Examples: in healthcare - doctors, nurses, administrators, technicians; in development - developers, testers, project managers, designers; each role has distinct system needs and usage patterns.")
    insert_answer(conn, term_id, 5, "Work roles inform user class definitions and persona creation. They help structure functionality around role-based needs and appear in usage scenarios showing role-specific workflows.")
    insert_answer(conn, term_id, 6, "Good work role analysis: identifies all relevant roles, understands each role's goals and responsibilities, recognizes role interactions, and informs role-appropriate design decisions.")
    insert_answer(conn, term_id, 7, "Work roles are job-based categories (organizational), user classes can cross roles (skill-based), and personas are specific examples (individual). Roles are formal positions; personas are representative individuals.")

    term_id = insert_term(conn, category_id, "User Classes",
        "Groups of users with similar characteristics, needs, or usage patterns, often based on expertise level, frequency of use, or goals.",
        parent_id=um_term_id, hierarchy_level=2, order_num=2)
    insert_answer(conn, term_id, 1, "User classes are groups of users sharing similar characteristics, needs, or usage patterns - often categorized by expertise (novice/expert), usage frequency (occasional/frequent), or domain knowledge.")
    insert_answer(conn, term_id, 2, "User classes are important because different classes have different needs - novices need learnability, experts need efficiency, occasional users need memorability. Designs must serve appropriate classes.")
    insert_answer(conn, term_id, 3, "User classes are identified during Analysis based on observed variations in user characteristics, then used in Design to make appropriate tradeoffs (e.g., prioritizing novice vs. expert needs).")
    insert_answer(conn, term_id, 4, "Examples: novice vs. expert users, occasional vs. frequent users, technical vs. non-technical users, power users vs. casual users - each class has distinct design implications.")
    insert_answer(conn, term_id, 5, "User classes inform persona creation (personas often represent specific classes), guide design tradeoffs (which class to optimize for), and appear in scenarios showing class-appropriate usage.")
    insert_answer(conn, term_id, 6, "Effective user class definition: based on meaningful distinctions, captures variations that matter for design, helps prioritize features appropriately, and guides interaction design choices.")
    insert_answer(conn, term_id, 7, "User classes are analytical categories (groupings by similarity), personas are synthetic individuals (specific examples), work roles are job-based (organizational). Classes segment users; personas exemplify them.")

    term_id = insert_term(conn, category_id, "Social Models",
        "Representations of social structures, relationships, communication patterns, and collaborative work among users and groups.",
        parent_id=um_term_id, hierarchy_level=2, order_num=3)
    insert_answer(conn, term_id, 1, "Social models represent the social aspects of work: organizational structures, team relationships, communication patterns, collaboration practices, and social dynamics that affect system use.")
    insert_answer(conn, term_id, 2, "Social models are important because work is inherently social. Systems must support communication, collaboration, coordination, and social practices. Ignoring social aspects leads to adoption failures.")
    insert_answer(conn, term_id, 3, "Social models are created from contextual inquiry observations of collaboration and communication, then used to design features supporting teamwork, sharing, and coordination.")
    insert_answer(conn, term_id, 4, "Examples: organizational charts showing reporting structures, communication networks showing who talks to whom, collaboration patterns showing shared work practices, team models showing interdependencies.")
    insert_answer(conn, term_id, 5, "Social models complement individual user models by showing how users work together. They inform design of collaborative features, communication tools, and shared workflows.")
    insert_answer(conn, term_id, 6, "Good social models: capture actual (not formal) communication patterns, show collaboration needs, identify coordination points, reveal social practices that systems must support or change.")
    insert_answer(conn, term_id, 7, "Social models focus on groups and relationships (collective), while personas focus on individuals (singular), and flow models show information exchange (flows). Social models emphasize human relationships.")

    term_id = insert_term(conn, category_id, "User Personas",
        "Rich, realistic descriptions of archetypal users, bringing research findings to life through specific, relatable characters representing user classes.",
        parent_id=um_term_id, hierarchy_level=2, order_num=4)
    insert_answer(conn, term_id, 1, "Personas are detailed, realistic descriptions of specific archetypal users, including their background, goals, frustrations, behaviors, and characteristics. They make research findings tangible and relatable.")
    insert_answer(conn, term_id, 2, "Personas are crucial because they help teams empathize with users, make user-centered decisions, resolve design disagreements by reference to user needs, and communicate user understanding across teams.")
    insert_answer(conn, term_id, 3, "Personas are created during Analysis based on research, refined during design thinking, and referenced throughout design and evaluation to maintain user focus.")
    insert_answer(conn, term_id, 4, "Examples: 'Sarah, the busy emergency room nurse who needs quick access to patient data between interruptions,' 'Alex, the new developer who's unfamiliar with the codebase and needs clear documentation.'")
    insert_answer(conn, term_id, 5, "Personas are central user models that appear in usage scenarios, inform design decisions, and provide the 'who' for design thinking. They're derived from user research and represent distinct user classes.")
    insert_answer(conn, term_id, 6, "Effective personas are: based on real research (not stereotypes), rich and sticky (memorable), include relevant details, represent distinct user classes, and are actually used in design decisions.")
    insert_answer(conn, term_id, 7, "Personas are specific examples (individuals), user classes are general categories (groups), work roles are job-based (positions). Personas bring user classes to life; they're design tools, not documentation.")

    # Usage Models (sub-category of DIMs)
    usm_term_id = insert_term(conn, category_id, "Usage Models",
        "Design-informing models that characterize user activities, tasks, and workflows, including flow models, task inventories, scenarios, and interaction models.",
        parent_id=dim_term_id, hierarchy_level=1, order_num=4)
    insert_answer(conn, usm_term_id, 1, "Usage models are DIMs that characterize what users do - their tasks, workflows, activities, and interactions. They include flow models, hierarchical task inventories, usage scenarios, and task interaction models.")
    insert_answer(conn, usm_term_id, 2, "Usage models are essential because understanding what users do and how they do it is fundamental to designing supportive systems. They reveal workflow requirements and interaction needs.")
    insert_answer(conn, usm_term_id, 3, "Usage models are created during Analysis from work observations, then used throughout Design to ensure systems support actual work tasks and workflows appropriately.")
    insert_answer(conn, usm_term_id, 4, "Examples: scenarios describing task completion, hierarchical task inventories showing task structure, flow models showing information exchange, step-by-step task interaction models showing detailed interactions.")
    insert_answer(conn, usm_term_id, 5, "Usage models are one category of DIMs (alongside user and environment models). They answer 'what do users do?' while user models answer 'who are they?' and environment models answer 'where/with what?'")
    insert_answer(conn, usm_term_id, 6, "Effective usage models: based on observed actual work, capture relevant task details, show both successful and problematic workflows, and provide actionable guidance for supporting work.")
    insert_answer(conn, usm_term_id, 7, "Usage models describe activities/behaviors (what users do), user models describe characteristics (who users are), environment models describe context (where/with what). Usage focuses on action.")

    # Usage Models sub-items
    term_id = insert_term(conn, category_id, "Flow Model (in Usage Models context)",
        "A usage model showing how information, communication, and artifacts flow through a work process - same concept as in contextual analysis, used here as a design-informing model.",
        parent_id=usm_term_id, hierarchy_level=2, order_num=1)
    insert_answer(conn, term_id, 1, "As a usage model, flow models show how information, communication, and artifacts flow through work processes - visualizing coordination and information exchange that systems must support.")
    insert_answer(conn, term_id, 2, "Flow models are important usage models because they reveal communication requirements, information dependencies, coordination needs, and collaboration patterns that designs must facilitate.")
    insert_answer(conn, term_id, 3, "Flow models are created during contextual analysis and refined as DIMs. They're used during design to ensure systems support necessary information flows and communication.")
    insert_answer(conn, term_id, 4, "Examples: showing how patient information flows from admission through discharge, how customer requests flow through support organization, how code changes flow through review and deployment.")
    insert_answer(conn, term_id, 5, "Flow models in usage models context show workflow information flows, complementing hierarchical task inventories (task structure), scenarios (narrative task descriptions), and interaction models (detailed steps).")
    insert_answer(conn, term_id, 6, "Effective flow models as usage models: show key information exchanges, highlight bottlenecks or breakdowns, indicate communication needs, and inform design of collaborative features.")
    insert_answer(conn, term_id, 7, "Flow models show inter-personal flows (between people/systems), while hierarchical task inventories show task decomposition (within work), and interaction models show user-system interaction (detailed steps).")

    term_id = insert_term(conn, category_id, "Hierarchical Task Inventory",
        "A structured breakdown of work tasks into hierarchical levels, showing main tasks decomposed into subtasks and steps, revealing task structure.",
        parent_id=usm_term_id, hierarchy_level=2, order_num=2)
    insert_answer(conn, term_id, 1, "A hierarchical task inventory breaks work down into hierarchical levels: high-level goals decompose into tasks, tasks into subtasks, subtasks into steps - creating a structured view of work organization.")
    insert_answer(conn, term_id, 2, "It's important because it reveals task structure, dependencies, and organization - helping designers understand work complexity and ensure systems support complete task sequences.")
    insert_answer(conn, term_id, 3, "Task inventories are created during Analysis by decomposing observed work, then used in Design to organize functionality and ensure all necessary task steps are supported.")
    insert_answer(conn, term_id, 4, "Examples: 'Process patient' breaks into 'check-in,' 'examination,' 'treatment,' 'checkout'; 'check-in' breaks into 'verify identity,' 'update information,' 'assign room,' etc.")
    insert_answer(conn, term_id, 5, "Task inventories complement scenarios (which tell stories) by providing structured task decomposition. They inform navigation design, feature organization, and workflow support.")
    insert_answer(conn, term_id, 6, "Good task inventories: capture complete task sequences, show appropriate level of detail, reveal task organization and dependencies, and help designers understand task complexity.")
    insert_answer(conn, term_id, 7, "Task inventories show task structure/decomposition (hierarchical), scenarios show task narratives (stories), interaction models show detailed steps (procedural). Inventories are structural; scenarios are narrative.")

    term_id = insert_term(conn, category_id, "Usage Scenarios",
        "Narrative descriptions of how users accomplish tasks or goals, providing context-rich stories about work that bring user models and usage patterns to life.",
        parent_id=usm_term_id, hierarchy_level=2, order_num=3)
    insert_answer(conn, term_id, 1, "Usage scenarios are narrative descriptions of users accomplishing work - stories about specific users (often personas) achieving goals in context, including actions, decisions, and outcomes.")
    insert_answer(conn, term_id, 2, "Scenarios are crucial because they provide context-rich, relatable descriptions of work that help designers understand and empathize with user situations and make user-centered decisions.")
    insert_answer(conn, term_id, 3, "Scenarios are created during Analysis (current situation) and Design (envisioned situation), used throughout design to maintain user focus, and referenced in evaluation.")
    insert_answer(conn, term_id, 4, "Examples: 'Sarah arrives for her shift, checks patient assignments, reviews the first patient's chart, notices a medication conflict, contacts the doctor...' - a story showing workflow in context.")
    insert_answer(conn, term_id, 5, "Scenarios complement task inventories (adding narrative context to task structures), feature personas (showing personas in action), and drive interaction models (detailed realizations of scenarios).")
    insert_answer(conn, term_id, 6, "Effective scenarios: based on research, include relevant context, show realistic work, feature personas, are specific enough to inform design, and tell engaging stories that help empathy.")
    insert_answer(conn, term_id, 7, "Scenarios are narratives (stories), task inventories are structures (hierarchies), interaction models are procedures (step-by-step). Scenarios provide context; task inventories provide organization; interaction models provide detail.")

    term_id = insert_term(conn, category_id, "Step-by-Step Task Interaction Model",
        "Detailed sequential description of user actions and system responses for specific tasks, showing the fine-grained interaction choreography.",
        parent_id=usm_term_id, hierarchy_level=2, order_num=4)
    insert_answer(conn, term_id, 1, "Step-by-step task interaction models detail the specific sequence of user actions and system responses for tasks - like interaction scripts showing exactly what users do and what systems do in response.")
    insert_answer(conn, term_id, 2, "They're important because they specify detailed interaction design - the precise choreography of user-system dialogue that makes or breaks usability.")
    insert_answer(conn, term_id, 3, "Interaction models are created during detailed design, implementing conceptual designs with specific interaction sequences. They guide prototyping and implementation of interaction behaviors.")
    insert_answer(conn, term_id, 4, "Examples: 'User clicks Search button → System displays search field with focus → User types query → System shows live results → User selects result → System navigates to detail view.'")
    insert_answer(conn, term_id, 5, "Interaction models provide detailed specifications implementing scenarios (high-level narratives) and task inventories (task structures). They bridge design and implementation.")
    insert_answer(conn, term_id, 6, "Effective interaction models: specify complete interaction sequences, show user actions and system responses, include error handling, consider edge cases, and provide implementable detail.")
    insert_answer(conn, term_id, 7, "Interaction models are detailed/procedural (step-by-step), scenarios are narrative (stories), task inventories are structural (hierarchies). Interaction models are most detailed, scenarios most contextual.")

    # Work Environment Models (sub-category of DIMs)
    wem_term_id = insert_term(conn, category_id, "Work Environment Models",
        "Design-informing models characterizing the physical and artifactual context where work occurs, including artifact models and physical models.",
        parent_id=dim_term_id, hierarchy_level=1, order_num=5)
    insert_answer(conn, wem_term_id, 1, "Work environment models characterize where and with what users work - the physical environment, artifacts they use, tools available, and contextual constraints. They include artifact and physical models.")
    insert_answer(conn, wem_term_id, 2, "Environment models are important because context affects system use - physical constraints, available artifacts, environmental factors all influence design requirements and feasibility.")
    insert_answer(conn, wem_term_id, 3, "Environment models are created from contextual inquiry observations of work settings, then used in design to ensure solutions fit actual work environments and contexts.")
    insert_answer(conn, wem_term_id, 4, "Examples: artifact models showing forms and tools used, physical models showing workspace layouts, models of mobile/standing/sitting work contexts, lighting and noise conditions.")
    insert_answer(conn, wem_term_id, 5, "Environment models complete the DIM picture: user models show who, usage models show what/how, environment models show where/with what - together providing complete design context.")
    insert_answer(conn, wem_term_id, 6, "Effective environment models: capture relevant contextual factors, identify constraints that designs must accommodate, show artifacts that systems must integrate with or replace.")
    insert_answer(conn, wem_term_id, 7, "Environment models describe context (where/with what), user models describe people (who), usage models describe activities (what/how). Environment provides the setting; user/usage provide the actors and actions.")

    # Work Environment Models sub-items
    term_id = insert_term(conn, category_id, "Artifact Model",
        "Representation of objects and artifacts users interact with during work - forms, documents, tools, devices - showing their role in work processes.",
        parent_id=wem_term_id, hierarchy_level=2, order_num=1)
    insert_answer(conn, term_id, 1, "Artifact models document the physical and digital artifacts users interact with - forms, documents, devices, tools - showing how they're used in work and what information they contain.")
    insert_answer(conn, term_id, 2, "Artifact models are important because artifacts reveal information needs, show current tools/processes that may need replacing or integrating, and demonstrate what formats/structures users are familiar with.")
    insert_answer(conn, term_id, 3, "Artifact models are created from artifacts collected during contextual inquiry, analyzed to understand their role, then used to inform information design and integration requirements.")
    insert_answer(conn, term_id, 4, "Examples: models of paper forms showing fields users complete, documents showing information structures, tools and devices users interact with, templates or checklists users reference.")
    insert_answer(conn, term_id, 5, "Artifact models inform information architecture (what information users work with), integration requirements (what tools must connect), and interaction design (familiar structures to build on).")
    insert_answer(conn, term_id, 6, "Effective artifact models: document relevant artifacts comprehensively, show artifact purpose and use in work, identify information they contain, note user modifications or annotations.")
    insert_answer(conn, term_id, 7, "Artifact models document objects (things), physical models document space (environment), usage models document activities (actions). Artifacts are tools/documents; physical models are spaces/layouts.")

    term_id = insert_term(conn, category_id, "Physical Model",
        "Representation of the physical work environment - workspace layout, equipment, environmental conditions - showing how physical context affects work.",
        parent_id=wem_term_id, hierarchy_level=2, order_num=2)
    insert_answer(conn, term_id, 1, "Physical models document the physical work environment: workspace layouts, equipment placement, mobility constraints, environmental conditions (lighting, noise), and how physical context affects work.")
    insert_answer(conn, term_id, 2, "Physical models matter because physical context creates constraints and opportunities - mobile vs. stationary work, noisy environments, lighting conditions, and space limitations all affect design requirements.")
    insert_answer(conn, term_id, 3, "Physical models are created from contextual inquiry observations of work environments, then used to inform design decisions about form factors, modalities, and physical constraints.")
    insert_answer(conn, term_id, 4, "Examples: models showing mobile work requiring portable devices, cramped spaces requiring compact interfaces, loud environments requiring visual feedback, outdoor work requiring bright displays.")
    insert_answer(conn, term_id, 5, "Physical models inform design decisions about device form factors, interaction modalities (touch, voice, etc.), environmental adaptations (brightness, volume), and physical ergonomics.")
    insert_answer(conn, term_id, 6, "Effective physical models: capture relevant environmental factors, identify constraints that designs must accommodate, note mobility and positioning requirements, consider environmental conditions.")
    insert_answer(conn, term_id, 7, "Physical models describe space/environment (where), artifact models describe objects (what with), usage models describe activities (what doing). Physical is environmental context; artifacts are work tools.")

    print(f"  Inserted Design-Informing Models section")

def main():
    """Main function to populate Analysis section"""
    print("Starting Analysis section population...")
    print("="*50)

    conn = create_connection()

    try:
        populate_analysis_section(conn)
        populate_design_informing_models(conn)

        # Get total count
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM terms")
        term_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM answers")
        answer_count = cursor.fetchone()[0]

        print("="*50)
        print(f"Analysis section completed!")
        print(f"Total terms in database: {term_count}")
        print(f"Total answers in database: {answer_count}")

    finally:
        conn.close()

if __name__ == "__main__":
    main()
