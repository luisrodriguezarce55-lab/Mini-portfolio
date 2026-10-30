🚀  **Automated Data Quality Pipeline & Executive Reporting Engine**

👥 **Target Audience**

For HR / Recruiters: Demonstrates the ability to transform programming code into real business solutions, automating repetitive tasks and delivering executive-ready outputs.

For Technical Leads / Data Leads: Evidences solid data engineering skills using pandas, statistical anomaly handling, schema validation, and automated formal documentation generation (python-docx).

📦 **What Do You Get at the End?**

When running this pipeline, the system automatically outputs two professional deliverables:

A Clean Database (.csv): A fully audited, deduplicated, and enriched dataset ready for advanced analytics and machine learning.

An Executive Audit Report (.docx): A professionally formatted Word document detailing every error found, metrics corrected, and new variable created.

🎯 **The Business Problem**

In data analytics, raw data is frequently contaminated with duplicates, garbage entries, typing errors, and extreme values. Analyzing uncleaned data leads to flawed financial metrics and poor strategic decisions.

This script fully automates Data Quality Assurance, ensuring a reliable dataset and generating a technical audit report in seconds.

**Map of the project/**

├── code/

│   └── Data_cleaning_code                 # All the code of the project in python

│   

├── Data base/

│   └── Raw      

│       └── Data-Online_retail             # Raw data base

├── Project solution/

│   ├── online_retail_cleaned        # Data base clean, update and ready to use

│   └── Data_Cleaning_Report.docs    # document of documentation of the changes, adds and cleaning of the data base 

└── README.md                        # Explanation of the project

🧱 **Architecture & Code Blocks**

The script is designed under a modular approach, clearly separating the user interface, logical processing, and presentation layers:

1. Graphical User Interface (Tkinter)
What it does: Opens a native file selection window (filedialog) so the user can interactively choose their dataset (.csv or .xlsx), avoiding hardcoded file paths.

2. Data Cleaning & Transformation Pipeline (Pandas & NumPy)
The analytical core processes the information through 11 key steps:

Deduplication: Removes identical rows to prevent artificial sales inflation.

Text Normalization: Standardizes formats, strips redundant whitespace, applies uppercase to codes and Title Case to descriptions.

Garbage Data Cleanup: Detects and isolates empty cells or corrupt symbols (?, ??, NaN), standardizing them as UNKNOWN.

Data Typing & Corrections: Safely casts data types, correcting negative quantities (typing errors) using absolute values (.abs()).

Outlier Filtering (IQR): Utilizes the Interquartile Range (IQR) method to detect and filter statistically extreme values in prices and quantities, protecting the analysis from severe skews.

🧠 **Feature Engineering: Boosting Business Logic & Future Analysis**

Beyond just cleaning errors, the pipeline introduces strategic data enrichment. By creating targeted new columns, it unlocks deeper business insights and prepares the data for advanced forecasting or dashboarding:

IsProduct: Separates physical inventory sales from administrative fees (like shipping, postage, or bank charges), ensuring financial metrics and unit-sales calculations aren't skewed.

Temporal Breakdown (YearMonth, Month, DayOfWeek, Hour): Extracts calendar details from timestamps, enabling behavioral analytics to discover peak sales seasons, profitable weekdays, or purchasing hours.

TotalAmount: Computes the exact monetary value per transaction (Quantity * UnitPrice), serving as the primary baseline revenue metric for future analytics.

3. Automated Reporting Engine (Python-Docx)
What it does: Uses a dictionary of metrics collected in real-time during execution to build a corporate Word document (.docx). It features standard 1-inch margins, formal typography (Times New Roman), and dynamic tables detailing:

The detailed log of errors found versus the corrective actions applied.

The dictionary of newly created variables and their business purpose.

⭐ **Technical Best Practices Implemented**

Dynamic Traceability: The generated report is not static; it feeds directly from the processed data of that specific execution, guaranteeing absolute accuracy.

Clean Code & Modularity: Clean functions with single responsibilities (generate_error_report, set_run_font), facilitating maintenance and scalability.

Exception Handling: A robust try-except structure to catch runtime errors and prevent unexpected program crashes.

⚙️ **Installation and Usage Instructions**

Install the required dependencies:

Bash
pip install pandas numpy python-docx
Run the main script in your Python environment:

Bash
python your_script_name.py
Select your dataset file in the popup window that appears. The system will handle the rest and hand you both your clean database and your Word documentation report!
