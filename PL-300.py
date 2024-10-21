import streamlit as st

# Total number of questions
total_questions = 47

# Function to display the question, options, and navigation
def display_question(question_number):
    # Questions and answers data
    questions = {
        1: {
            "question": """
                You need to import 45 Excel files to Power BI Desktop. All these files are in a unique desktop local folder and share the same structure. You want to import all these Excel files into a single table. Which of the following would help you in achieving the goal?
            """,
            "options": [
                "A. Adding the folder data source; using the Append Queries command",
                "B. Adding the folder data source; using the Combine Files Command",
                "C. Adding every single file to the model and then using Merge Query Command",
                "D. Adding the MS Excel Data Source; selecting all files of the folder",
                "E. Adding a folder data source and using the Merge Queries Command"
            ],
            "correct_answer": "B. Adding the folder data source; using the Combine Files Command",
            "explanation": """
                **Explanation:** The Combine Files Command is specifically designed to handle multiple files with the same structure, combining them into a single table.
            """,
            "reference": "https://support.microsoft.com/en-ie/office/combine-files-in-a-folder-with-combine-binaries-power-query-94b8023c-2e66-4f6b-8c78-6a00041c90e4"
        },
        2: {
            "question": """
                You have a 200 GB data warehouse that has data consolidated from several applications and runs on SQL Server 2017 Enterprise Edition. You notice that with your reports, there is a default limitation of eight daily refreshes. Your manager asks you to ensure that the reports are never more outdated than 1 hour. Which of the following can help you in achieving the same?
            """,
            "options": [
                "A. Building an application for monitoring the changes in the database and pushing them out utilizing the real-time streaming API",
                "B. Migrating the content to Power BI Premium",
                "C. Adding an SSAS tabular layer on top and enabling the Live connections",
                "D. Convert to DirectQuery to access the data warehouse"
            ],
            "correct_answer": "D. Convert to DirectQuery to access the data warehouse",
            "explanation": """
                **Explanation:** DirectQuery allows direct access to the data warehouse and provides up-to-date data without the need for refresh cycles.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-use-directquery"
        },
        3: {
            "question": """
                Suppose you have developed a query named consumers in Power BI Desktop to append the rows from 3 external tables with consumer data into a single table consumer. Now you want to ensure that each row in the consumer table has a unique ID value. Which of the following is the best way to add a new fabricated ID column to the consumer table?
            """,
            "options": [
                "A. Changing the data model by extending the consumers table with an Index column",
                "B. Changing the data model by extending the consumer table with a Counter column",
                "C. Modifying the consumers query by adding an Index column",
                "D. Modifying the consumers query by adding a Counter column"
            ],
            "correct_answer": "C. Modifying the consumers query by adding an Index column",
            "explanation": """
                **Explanation:** Query editor has an option 'Index Column' to add an indexed column starting from 1, 0, or any custom number.
            """,
            "reference": "https://powerbi.microsoft.com/fr-fr/blog/4-new-updates-in-power-query/"
        },
        4: {
            "question": """
                Why is it advised to avoid the NULL values in the numeric column?
            """,
            "options": [
                "A. DAX expression having SUM function on such data will provide incorrect results",
                "B. DAX expression having MAX function on such data will provide incorrect results",
                "C. DAX expression having an AVERAGE function on such data will provide incorrect results",
                "D. DAX Expressions can’t be applied if a numeric column has one or multiple NULL values",
                "E. All the above"
            ],
            "correct_answer": "C. DAX expression having an AVERAGE function on such data will provide incorrect results",
            "explanation": """
                **Explanation:** The AVERAGE function calculates the average by considering the total and dividing that by the number of non-null values.
            """,
            "reference": "https://docs.microsoft.com/en-us/learn/modules/clean-data-power-bi/2-shape-data"
        },
        5: {
            "question": """
                After you pivot the columns, the table appears as shown below with an error in the 3rd row. How would you fix this error? The solution needs to preserve all the data.
            """,
            "options": [
                "A. For the key column, use 'Duplicate Values'",
                "B. Rename column3",
                "C. Use 'Remove Errors' for Column3",
                "D. Modify the Data Type of the Value Column",
                "E. Change the Aggregate Value Function of the Pivot"
            ],
            "correct_answer": "E. Change the Aggregate Value Function of the Pivot",
            "explanation": """
                **Explanation:** While using the Pivot feature, the aggregate value functions should be correctly set to preserve all values.
            """,
            "reference": "https://databear.com/power-bi-pivot-and-unpivot-columns/"
        },
        6: {
            "question": """
                Which of the following DAX functions would return a date that is the last day of the month before or after a specified number of months?
            """,
            "options": [
                "A. DATESBETWEEN",
                "B. ENDOFMONTH",
                "C. CLOSINGBALANCEMONTH",
                "D. EOMONTH",
                "E. DATESYTD"
            ],
            "correct_answer": "D. EOMONTH",
            "explanation": """
                **Explanation:** The EOMONTH function returns the last day of the month that is the indicated number of months before or after the start date.
            """,
            "reference": "https://docs.microsoft.com/en-us/dax/eomonth-function-dax"
        },
        7: {
            "question": """
                You want to calculate the growth percentage between two years in Power BI. Which DAX function can help you achieve this?
            """,
            "options": [
                "A. PERCENTILE.EXC",
                "B. DIVIDE",
                "C. GROWTHPERCENT",
                "D. DATEDIFF",
                "E. CALCULATE"
            ],
            "correct_answer": "B. DIVIDE",
            "explanation": """
                **Explanation:** The DIVIDE function in DAX is useful for calculating ratios and percentages, as it handles division and returns the result as a percentage when necessary.
            """,
            "reference": "https://docs.microsoft.com/en-us/dax/divide-function-dax"
        },
        8: {
            "question": """
                What feature in Power BI allows you to view the relationships between different tables and manage their cardinality?
            """,
            "options": [
                "A. Relationship editor",
                "B. Data View",
                "C. Relationship Manager",
                "D. Model View",
                "E. Query Editor"
            ],
            "correct_answer": "D. Model View",
            "explanation": """
                **Explanation:** Model View in Power BI allows users to visually see relationships between tables and manage their cardinality (one-to-one, many-to-one, etc.).
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand"
        },
        9: {
            "question": """
                Which of the following features in Power BI enables you to group a set of visuals together so they can be easily moved or copied as a unit?
            """,
            "options": [
                "A. Visual Container",
                "B. Bookmark",
                "C. Grouping",
                "D. Report Pack",
                "E. Page Navigation"
            ],
            "correct_answer": "C. Grouping",
            "explanation": """
                **Explanation:** Grouping allows users to organize visuals on the report canvas by combining them into a group, so they can be managed together.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/create-reports/power-bi-visualization-groups"
        },
        10: {
            "question": """
                You want to build a custom visual in Power BI for your specific business case. What programming language would you use to achieve this?
            """,
            "options": [
                "A. Python",
                "B. R",
                "C. DAX",
                "D. JavaScript",
                "E. M"
            ],
            "correct_answer": "D. JavaScript",
            "explanation": """
                **Explanation:** Power BI custom visuals can be developed using JavaScript libraries like D3.js for advanced and interactive visualizations.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/developer/custom-visual-develop"
        },
    }

    # Get the current question data
    question_data = questions.get(question_number, {"question": "Question not found", "options": [], "correct_answer": ""})

    # Display question and options
    st.markdown(f"### Question {question_number} of {total_questions}")
    st.markdown(question_data["question"])
    selected_option = st.radio("Choose your answer:", question_data["options"])

    # Navigation buttons
    if st.button("Submit"):
        if selected_option == question_data["correct_answer"]:
            st.success("Correct answer!")
        else:
            st.error(f"Incorrect. The correct answer is: {question_data['correct_answer']}")
        st.markdown(question_data["explanation"])

    # Navigation buttons for previous and next questions
    col1, col2 = st.columns([1, 1])

    with col1:
        if question_number > 1:
            if st.button("Previous Question"):
                st.session_state["question_number"] = question_number - 1

    with col2:
        if question_number < total_questions:
            if st.button("Next Question"):
                st.session_state["question_number"] = question_number + 1

# Initialize question number in session state
if "question_number" not in st.session_state:
    st.session_state["question_number"] = 1

# Display the current question
display_question(st.session_state["question_number"])
