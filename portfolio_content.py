"""
Portfolio Content Configuration
================================
Update this file to change all text, metrics, links, and case studies.
No need to touch app.py or components.py for content changes.

Strategic north star:
"An operations transformation leader who uses analytics and technology
to help people work better and leaders make better decisions."
"""

# ---------- PERSONAL INFO ----------
NAME = "Macy Ziegler"
TAGLINE = "OPERATIONS • ANALYTICS • TRANSFORMATION"
HEADLINE = "Industrial engineering taught me to see the system. Technology gave me the tools to change it."
SUBHEADLINE = (
    "As an analytics professional, I look for pain points, root causes, and opportunities "
    "to improve. My technology experience allows me to choose the right solution, "
    "whether that means answering a question through analysis, automating a process, or "
    "developing a product."
)

# ---------- PROFESSIONAL SNAPSHOT ----------
SNAPSHOT = {
    "current": "Sr. Analyst, Solutions & Automation at The Walt Disney Company",
    "education": "Industrial Engineering & Engineering Management, South Dakota Mines",
    "location": "Orlando, Florida",
}

# ---------- HEADSHOT ----------
HEADSHOT_PATH = "assets/headshot.jpg"
HEADSHOT_ALT = "Professional headshot of Macy Ziegler"

# ---------- LINKS ----------
EMAIL = "macyzig5@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/macy-ziegler/"
GITHUB = "https://github.com/yourusername"  # TODO: Replace if desired
RESUME_FILE = "app/static/resume.pdf"  # Served via Streamlit static file serving

# ---------- NAVIGATION ----------
NAV_BRAND = "MACY ZIEGLER"
NAV_ITEMS = ["Work", "Experience", "About", "LinkedIn", "Download Resume"]

# ---------- PROFESSIONAL SUPERPOWERS ----------
SUPERPOWERS_LABEL = "WHAT SETS ME APART"
SUPERPOWERS_HEADING = "My Professional Superpowers"
SUPERPOWERS_SUBTITLE = "The skills that help me turn ambiguous problems into solutions people understand, trust, and use."

SUPERPOWERS = [
    {
        "title": "Asking the Right Questions",
        "description": "I look beyond the initial request to uncover the real problem, constraints, and decisions that matter.",
        "icon": "search",
    },
    {
        "title": "Seeing the Whole System",
        "description": "I connect people, processes, data, and technology to identify opportunities others may miss.",
        "icon": "network",
    },
    {
        "title": "Storytelling",
        "description": "I turn complex analysis into a clear narrative that helps people understand what matters and act with confidence.",
        "icon": "presentation",
    },
    {
        "title": "Building Relationships",
        "description": "I build trust across operational, technical, and leadership teams so solutions reflect how work actually happens.",
        "icon": "handshake",
    },
]

# ---------- IN THE ROOM SECTION ----------
IN_THE_ROOM_LABEL = "IN THE ROOM, I'M THE PERSON WHO…"

IN_THE_ROOM_FEATURED = {
    "headline": "ASKS THE QUESTIONS OTHERS MIGHT MISS.",
    "highlight": "",
    "description": (
        "The first request rarely tells the whole story. I ask questions to understand "
        "what changed, where the work breaks down, who feels the impact, what the data "
        "might be missing, and what decision we actually need to make."
    ),
}

IN_THE_ROOM_SUPPORTING = [
    {
        "title": "Sees the Whole System",
        "description": "I connect what is happening across people, processes, data, and technology.",
        "icon": "system",
    },
    {
        "title": "Tells the Story People Need",
        "description": "I translate complex analysis into a clear narrative that helps people understand what matters and what to do next.",
        "icon": "story",
    },
    {
        "title": "Builds Relationships That Move Work Forward",
        "description": "I create trust, involve the right voices, and turn cross-functional conversations into solutions people believe in and adopt.",
        "icon": "relationships",
    },
]

# ---------- HOW I WORK WITH AI ----------
AI_SECTION_LABEL = "HOW I WORK WITH AI"
AI_SECTION_HEADLINE = "A Jetpack, Not an Autopilot."
AI_SECTION_COPY = (
    "AI has become a jetpack for how I work. I use it to explore ideas, move faster "
    "from ambiguity to structure, accelerate development, and pressure-test what I've built. "
    "It doesn't replace judgment, context, or accountability.\n\n"
    "I still own the questions, the decisions, and the quality of the outcome. For me, "
    "AI creates more room for the work that matters most: thinking critically, solving "
    "the right problem, and building something people can trust."
)

AI_APPLICATIONS = [
    {
        "number": "01",
        "title": "Brainstorm",
        "subtitle": "Expand my thinking",
        "description": "I use AI to get beyond the blank page by organizing messy ideas, exploring different approaches, and surfacing questions I may not have considered.",
    },
    {
        "number": "02",
        "title": "Build",
        "subtitle": "Move ideas into action",
        "description": "I use it to turn direction into something tangible faster by drafting code, prototyping workflows, and iterating as I build.",
    },
    {
        "number": "03",
        "title": "Pressure-Test",
        "subtitle": "Make the work stronger",
        "description": "I use it as a second set of eyes to challenge my logic, uncover edge cases, and identify where an idea or solution needs more work.",
    },
]

AI_HUMAN_LABEL = "WHAT STAYS HUMAN"
AI_HUMAN_VALUE = "Judgment · Context · Accountability"

# ---------- SELECTED IMPACT METRICS ----------
METRICS = [
    {
        "value": "$2.5M+",
        "label": "Annual Labor Savings",
        "description": "Led a cross-functional root-cause analysis of rising floor-replenishment labor, modeled expected pick demand, and redesigned Smart Stock processes and training.",
        "behind_metric": "The labor problem was actually a system-and-process problem.",
        "case_study_index": 2,
    },
    {
        "value": "37%",
        "label": "Shrink Reduction",
        "description": "Built a daily inventory shrink dashboard that enabled earlier mitigation and contributed to a 37% reduction in the year following implementation.",
        "behind_metric": "The data existed. The operation just couldn't see it in time to act.",
        "case_study_index": 1,
    },
    {
        "value": "1,000+",
        "label": "Leaders Using Mobile Analytics",
        "description": "Developed Walt Disney World's first mobile Merchandise reporting application and trained leaders across the operation.",
        "behind_metric": "The product had to work for a leader with a phone in one hand and a walkie-talkie in the other.",
        "case_study_index": 0,
    },
    {
        "value": "35 Hours",
        "label": "Saved Per Enhancement Cycle",
        "description": "Built an automated LLM evaluation framework that measured response accuracy and replaced manual testing.",
        "behind_metric": "Testing the AI needed to scale as quickly as the product did.",
        "case_study_index": 3,
    },
]

# ---------- SELECTED WORK (Case Study Cards) ----------
CASE_STUDIES = [
    {
        "title": "Mobile Operational Reporting Platform",
        "category": "Analytics Product • Power BI • Operational Decision Support",
        "summary": (
            "Designed, developed, and launched Walt Disney World Merchandise's first "
            "mobile reporting application, providing more than 1,000 leaders with "
            "hourly performance insights and dynamically generated KPI targets."
        ),
        "skills": ["Power BI", "Forecasting", "Product Development", "Operational Analytics", "User Training"],
        "detail_type": "mobile_reporting",
        "detail": {
            "skills": ["Power BI", "Forecasting", "Product Development", "Operational Analytics", "User Training"],
            "headline": (
                "Putting hourly performance insights in the hands of more than "
                "1,000 operational leaders."
            ),
            "at_a_glance": {
                "Platform": "Microsoft Power BI",
                "Scale": "1,000+ operational leaders",
                "Duration": "Approximately 12 months",
                "Cadence": "Refreshed and used hourly",
            },
            "challenge": (
                "Walt Disney World Merchandise leaders were making decisions in "
                "real time, but the reporting they relied on was tied to desktop "
                "tools, Excel files, and manual processes. Getting an answer often "
                "meant leaving the sales floor.\n\n"
                "I designed the product around a simple principle: a leader holding "
                "a phone in one hand and a walkie-talkie in the other should be able "
                "to understand performance in about 30 seconds."
            ),
            "solution": (
                "I designed, coded, and launched Walt Disney World Merchandise's "
                "first mobile reporting application in Power BI. The product gave "
                "leaders hourly performance visibility and made actual-versus-target "
                "results easy to interpret on a mobile device.\n\n"
                "I also developed a multidimensional forecasting model that generated "
                "KPI targets using hour-of-day patterns, day-of-week effects, and "
                "fiscal-week trends. This gave leaders a relevant benchmark at each "
                "point in the operating day instead of relying on a single static "
                "target."
            ),
            "delivery": [
                "Gathered requirements through roundtables and ongoing feedback with operational leaders.",
                "Built the complete Power BI product, including the reporting logic, mobile experience, and forecasting model.",
                "Piloted and refined the product through user testing before the broader launch.",
                "Personally trained more than 1,000 leaders and supported adoption across Walt Disney World.",
            ],
            "outcome": (
                "Delivered Walt Disney World Merchandise's first mobile reporting "
                "application, trained more than 1,000 leaders, and enabled hourly "
                "performance decisions across the operation."
            ),
        },
    },
    {
        "title": "Inventory Shrink Visibility & Reporting Automation",
        "category": "Data Engineering • Tableau • Snowflake",
        "summary": (
            "Created daily inventory visibility that contributed to a 37% reduction "
            "in shrink in the year following implementation."
        ),
        "skills": ["Tableau", "Snowflake", "Data Engineering", "Process Automation", "Analytics"],
        "detail_type": "shrink_reporting",
        "detail": {
            "skills": ["Tableau", "Snowflake", "Data Engineering", "Process Automation", "Analytics"],
            "headline": (
                "Creating daily inventory visibility that contributed to a 37% "
                "reduction in shrink in the year following implementation."
            ),
            "at_a_glance": {
                "Platform": "Tableau and Snowflake",
                "Scale": "~200+ inventory leaders",
                "Duration": "9 months",
                "Cadence": "Daily",
            },
            "challenge": (
                "Merchandise locations could only see inventory shrink after their "
                "annual physical inventory. Throughout the year, there was no "
                "consolidated way to detect where losses were emerging, compare "
                "trends across locations, or understand which product categories "
                "were driving the results.\n\n"
                "Producing the annual inventory results also required approximately "
                "three months of dedicated manual reporting work."
            ),
            "solution": (
                "I created two connected capabilities: a daily shrink visibility "
                "dashboard and an automated annual inventory reporting workflow.\n\n"
                "The dashboard allowed teams to monitor inventory loss by individual "
                "store, across the property, and within specific product categories. "
                "The automated workflow delivered each location's annual inventory "
                "results within 24 hours."
            ),
            "delivery": [
                "Located the source system containing cycle-count records.",
                "Modeled the data in Snowflake to support store-level, property-wide, and product-category analysis.",
                "Built a Tableau dashboard that translated inventory records into daily, actionable shrink insights.",
                "Connected directly to annual inventory data and coded the workflow that generated each location's results.",
            ],
            "delivery_labels": ["Source", "Structure", "Visualize", "Automate"],
            "outcome": (
                "In the year following implementation, inventory shrink decreased by "
                "37%. Teams gained daily visibility to identify emerging risks and "
                "focus mitigation strategies by location or product category.\n\n"
                "The automated workflow also reduced the turnaround for annual "
                "inventory results from approximately three months to 24 hours."
            ),
        },
    },
    {
        "title": "Floor-Replenishment Labor Optimization",
        "category": "Operations Analytics • Industrial Engineering • Labor Strategy",
        "summary": (
            "Uncovered the system behavior behind rising labor and created a "
            "demand-based labor model that delivered $2.5M in realized annual savings."
        ),
        "skills": ["Root-Cause Analysis", "Scenario Modeling", "Industrial Engineering", "Cross-Functional Partnership"],
        "detail_type": "labor_optimization",
        "detail": {
            "skills": ["Root-Cause Analysis", "Scenario Modeling", "Industrial Engineering", "Cross-Functional Partnership"],
            "headline": (
                "Uncovering the system behavior behind rising labor and creating a "
                "demand-based labor model that delivered $2.5M in realized annual savings."
            ),
            "at_a_glance": {
                "Role": "Lead Analyst",
                "Duration": "Approximately six months",
                "Partners": "Industrial Engineering, Operations, Labor Relations, Workforce Management",
                "Impact": "$2.5M in realized annual labor savings",
            },
            "challenge": (
                "Floor-replenishment labor continued to increase, yet teams were "
                "still unable to keep pace with pick demand. Adding labor addressed "
                "the immediate workload but did not resolve the underlying problem, "
                "causing labor requirements to continue growing."
            ),
            "solution": (
                "I led the root-cause analysis and found that Smart Stock workflows "
                "were not being used as intended. This unintentionally created excess "
                "pick demand, making it difficult for teams to complete the work and "
                "driving progressively higher labor allocations.\n\n"
                "What appeared to be a staffing problem was ultimately a "
                "system-and-process problem."
            ),
            "delivery": [
                "Investigated the relationship between Smart Stock usage, pick demand, operational execution, and labor allocation to isolate the source of the continued labor growth.",
                "Partnered with Industrial Engineering, Operations, Labor Relations, and Workforce Management to evaluate alternative system-use scenarios.",
                "Developed scenario models that forecasted expected pick demand when Smart Stock was used as intended.",
                "Used the demand forecasts to establish new labor requirements and support standardized operating processes across the operation.",
            ],
            "delivery_labels": ["Diagnose", "Test", "Model", "Implement"],
            "outcome": (
                "The new standards corrected the behaviors creating unnecessary "
                "demand, while the forecasting model aligned labor allocation with "
                "the workload the system should generate under intended use.\n\n"
                "The project replaced compounding labor growth with a sustainable, "
                "demand-based approach and delivered $2.5 million in realized annual "
                "labor savings."
            ),
        },
    },
    {
        "title": "Automated LLM Evaluation Framework",
        "category": "AI • Python • Snowflake • Quality Assurance",
        "summary": (
            "Transformed manual AI validation into a repeatable 300-question testing "
            "framework, saving an estimated 35 hours per enhancement cycle."
        ),
        "skills": ["Python", "Snowflake", "Cortex Analyst", "Test Automation", "AI Evaluation"],
        "detail_type": "llm_evaluation",
        "detail": {
            "skills": ["Python", "Snowflake", "Cortex Analyst", "Test Automation", "AI Evaluation"],
            "headline": (
                "Transforming manual AI validation into a repeatable 300-question "
                "testing framework and saving an estimated 35 hours per enhancement cycle."
            ),
            "at_a_glance": {
                "Platform": "Snowflake Cortex Analyst & Agent",
                "Build Time": "Approximately one week",
                "Scale": "300 questions per evaluation cycle",
                "Ownership": "Independently designed and developed",
            },
            "challenge": (
                "Each enhancement to the Workforce Data Assistant introduced the "
                "possibility of changing how the AI interpreted questions, applied "
                "filters, selected time periods, generated SQL, or enforced privacy "
                "requirements.\n\n"
                "Validating these behaviors manually required analysts to submit "
                "questions individually, review the generated results, and compare "
                "each response with an expected answer. Repeating that process after "
                "every enhancement was time-intensive and difficult to scale."
            ),
            "solution": (
                "I independently developed an automated evaluation framework using "
                "Python, Snowflake, and Snowflake Cortex Analyst and Agent.\n\n"
                "The framework submitted 300 test questions, captured the generated "
                "responses and SQL, stored the results in Snowflake, and evaluated "
                "them against expected outcomes. The test suite covered SQL accuracy, "
                "filter interpretation, time-period logic, data suppression, and "
                "privacy requirements."
            ),
            "delivery": [
                "Organized 300 test questions and their expected outcomes across key analytical and governance scenarios.",
                "Built the Python workflow that automatically submitted each question to Snowflake Cortex Analyst and Agent.",
                "Developed the logic used to compare generated SQL and results with expected answers.",
                "Stored evaluation results in Snowflake so discrepancies could be reviewed and testing could be repeated after future enhancements.",
            ],
            "delivery_labels": ["Structure", "Execute", "Evaluate", "Monitor"],
            "outcome": (
                "The framework converted a largely manual validation process into a "
                "repeatable evaluation cycle capable of testing 300 questions "
                "consistently.\n\n"
                "Built independently in approximately one week, it saved an estimated "
                "35 hours of manual testing per enhancement cycle while improving test "
                "coverage and confidence in the assistant's analytical accuracy, "
                "suppression logic, and privacy protections."
            ),
        },
    },
]

# ---------- HOW I APPROACH TRANSFORMATION (Process Steps) ----------
PROCESS_SECTION_TITLE = "How I Approach Transformation"
PROCESS_SECTION_SUBTITLE = (
    "A structured method for turning ambiguous operational challenges into "
    "lasting, scalable improvements."
)

PROCESS_STEPS = [
    {
        "step": "01",
        "title": "Understand the Operation",
        "description": (
            "Learn how the work actually happens—stakeholders, constraints, "
            "volume, and current processes."
        ),
    },
    {
        "step": "02",
        "title": "Challenge the Assumptions",
        "description": (
            "Question the original request and determine whether it addresses "
            "the true problem."
        ),
    },
    {
        "step": "03",
        "title": "Define the Decision",
        "description": (
            "Clarify what someone needs to understand, choose, or do differently."
        ),
    },
    {
        "step": "04",
        "title": "Prioritize the Opportunity",
        "description": (
            "Focus effort on the work with the greatest potential value "
            "and feasibility."
        ),
    },
    {
        "step": "05",
        "title": "Build & Validate",
        "description": (
            "Translate the need into a practical solution and test it against "
            "real operational requirements."
        ),
    },
    {
        "step": "06",
        "title": "Enable Adoption & Measure Impact",
        "description": (
            "Make the solution usable, establish trust, and evaluate whether "
            "it improves the intended outcome."
        ),
    },
]

# ---------- EXPERIENCE TIMELINE ----------
EXPERIENCE = [
    {
        "title": "Sr. Analyst, Solutions & Automation",
        "organization": "The Walt Disney Company",
        "dates": "March 2026 – Present",
        "description": (
            "Own development of AI-powered HR analytics solutions using Snowflake "
            "Cortex, translating complex workforce data and business requirements "
            "into trusted data products."
        ),
        "achievements": [
            "Design semantic models and data architecture in Snowflake, defining business logic, metrics, and relationships for workforce analytics",
            "Built automated AI evaluation framework reducing testing time by ~35 hours per enhancement cycle",
            "Lead product planning, prioritization, and stakeholder communication for senior leadership",
        ],
        "capabilities": ["Snowflake Cortex", "Python", "AI Evaluation", "Product Ownership"],
    },
    {
        "title": "Senior F&B/Merchandise Analyst",
        "organization": "The Walt Disney Company",
        "dates": "August 2023 – March 2026",
        "description": (
            "Led analytics initiatives across merchandise operations, delivering "
            "enterprise reporting products, operational redesigns, and forecasting "
            "models that drove measurable business impact."
        ),
        "achievements": [
            "Led stockroom analytics and operating-model redesign, delivering $2.5M+ in annualized savings",
            "Owned end-to-end delivery of Disney's first Merchandise mobile reporting product for 1,000+ leaders",
            "Designed and launched enterprise-wide shrink analytics solution, reducing reporting latency from 3 months to 24 hours",
        ],
        "capabilities": ["Power BI", "Tableau", "Python", "Forecasting"],
    },
    {
        "title": "Labor Transformation Analyst",
        "organization": "The Walt Disney Company",
        "dates": "November 2021 – August 2023",
        "description": (
            "Developed workforce planning models and analytics dashboards to "
            "translate operational demand into resource requirements across "
            "complex operations."
        ),
        "achievements": [
            "Developed workforce planning and staffing models supporting labor planning and scheduling decisions",
            "Built Tableau workforce analytics dashboards providing real-time staffing visibility",
            "Built attrition and hiring forecasting models using historical trends and seasonality",
        ],
        "capabilities": ["Tableau", "Workforce Planning", "Forecasting", "SQL"],
    },
    {
        "title": "BS Industrial Engineering & Engineering Management",
        "organization": "South Dakota School of Mines & Technology",
        "dates": "May 2021",
        "description": "3.8 GPA, Magna Cum Laude",
        "achievements": [],
        "capabilities": [],
    },
]

# ---------- BEYOND THE WORK ----------
BEYOND_LABEL = "BEYOND THE WORK"
BEYOND_HEADLINE = "The person behind the portfolio."

BEYOND_YOGA_LABEL = "ON THE MAT"
BEYOND_YOGA_COPY = (
    "Outside of analytics, I teach yoga, where I practice a different kind of "
    "leadership by reading the room, communicating clearly, and helping people "
    "build confidence through challenge."
)
BEYOND_YOGA_IMAGE = "assets/yoga.jpg"
BEYOND_YOGA_ALT = "Macy teaching or practicing yoga"

BEYOND_HOME_LABEL = "AT HOME"
BEYOND_HOME_COPY = (
    "At home, I am a proud dog mom to Miles and Barkley. I am happiest when I "
    "have time to move, create, learn something new, and spend time with the "
    "people and animals I love."
)
BEYOND_HOME_IMAGE = "assets/miles_barkley.jpg"
BEYOND_HOME_ALT = "Macy's dogs, Miles and Barkley"

# ---------- CONTACT ----------
CONTACT_HEADLINE = "Let's connect."
CONTACT_TEXT = (
    "I enjoy connecting with people who are solving complex problems across analytics, "
    "operations, and technology. If my experience feels relevant to what your team is "
    "building, I'd love to start a conversation and learn more."
)
