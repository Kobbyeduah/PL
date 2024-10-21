import streamlit as st
import html

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
    
        11: {
            "question": """
                You have a table named 'Sales' with columns 'ProductID', 'Date', and 'SalesAmount'. You want to create a new column in Power BI to show the cumulative total of 'SalesAmount'. Which DAX function would be most appropriate for this task?
            """,
            "options": [
                "A. TOTALYTD",
                "B. CALCULATE",
                "C. SUMX",
                "D. SUMMARIZE",
                "E. CUMULATIVE"
            ],
            "correct_answer": "A. TOTALYTD",
            "explanation": """
                **Explanation:** TOTALYTD calculates the year-to-date value of the specified expression, which is ideal for cumulative totals.
            """,
            "reference": "https://docs.microsoft.com/en-us/dax/totalytd-function-dax"
        },
        12: {
            "question": """
                You have a table named 'Sales' with columns 'ProductID', 'Date', and 'SalesAmount'. You want to create a measure to calculate year-over-year growth. What is the most appropriate function to use?
            """,
            "options": [
                "A. SAMEPERIODLASTYEAR",
                "B. DATESYTD",
                "C. DATEDIFF",
                "D. TOTALMTD",
                "E. PREVIOUSYEAR"
            ],
            "correct_answer": "A. SAMEPERIODLASTYEAR",
            "explanation": """
                **Explanation:** SAMEPERIODLASTYEAR returns a table that is shifted one year back in time, ideal for calculating year-over-year growth.
            """,
            "reference": "https://docs.microsoft.com/en-us/dax/sameperiodlastyear-function-dax"
        },
        13: {
            "question": """
                Which of the following reserved parameters respectively configure the start and end of where Incremental refresh should happen?
            """,
            "options": [
                "A. Start and End parameters",
                "B. StartRange and EndRange parameters",
                "C. RangeStart and RangeEnd parameters",
                "D. RefreshStart and RefreshEnd parameters",
                "E. StartRefresh and EndRefresh parameters"
            ],
            "correct_answer": "C. RangeStart and RangeEnd parameters",
            "explanation": """
                **Explanation:** RangeStart and RangeEnd parameters are used in Incremental Refresh to configure the start and end of where Incremental refresh should happen.
            """,
            "reference": "https://docs.microsoft.com/en-us/learn/modules/manage-datasets-power-bi/6-incremental-refresh"
        },
        14: {
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
        15: {
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
        16: {
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
        17: {
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
        18: {
            "question": """
                You need to create a data model that includes multiple tables. Which tool should you use?
            """,
            "options": [
                "A. Power BI",
                "B. Power Automate",
                "C. Power Apps",
                "D. Power Query"
            ],
            "correct_answer": "A. Power BI",
            "explanation": """
                **Explanation:** Power BI allows you to connect, transform, and model data across multiple tables and is the best tool for creating data models.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-modeling"
        },
        19: {
            "question": """
                Which DAX function would you use to ignore filters on a column or table?
            """,
            "options": [
                "A. ALL",
                "B. FILTER",
                "C. CALCULATE",
                "D. SELECTCOLUMNS"
            ],
            "correct_answer": "A. ALL",
            "explanation": """
                **Explanation:** The ALL function returns all rows in a table or values in a column, ignoring any filters that might have been applied.
            """,
            "reference": "https://docs.microsoft.com/en-us/dax/all-function-dax"
        },
        20: {
            "question": """
                Which of the following types of visualizations are supported by Power BI for displaying the relationship between two numerical values?
            """,
            "options": [
                "A. Line chart",
                "B. Scatter chart",
                "C. Pie chart",
                "D. Donut chart"
            ],
            "correct_answer": "B. Scatter chart",
            "explanation": """
                **Explanation:** Scatter charts in Power BI are used to display the relationship between two numerical values by plotting them on an x and y-axis.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-scatter"
        },
    
        21: {
            "question": """
                Your company is planning to utilize the Power BI Service to get multiple visualizations from data stored in a custom application.
                The developers ask to push the data into the Power BI Service from the custom app.
                How would you ensure this task?
            """,
            "options": [
                "A. Go to Office 365 Admin portal and register a web application",
                "B. Go to app.powerbi.com and build an empty report",
                "C. Go to tenant settings from the Power BI admin portal and set the API permissions",
                "D. Go to dev.powerbi.com/apps and register an application"
            ],
            "correct_answer": "D. Go to dev.powerbi.com/apps and register an application",
            "explanation": """
                **Explanation:** You need to register the application at dev.powerbi.com/apps to integrate Power BI APIs and push data from your custom app.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/developer/embedded/register-app"
        },
        22: {
            "question": """
                Which of the following can’t be seen from the data lineage view in Power BI?
            """,
            "options": [
                "A. Where the dataflows are being utilized as a data source for datasets",
                "B. The data sources that are being utilized by the dashboards/reports/datasets in a workspace",
                "C. The credentials utilized to connect to datasets",
                "D. Where gateways are being utilized as a data source for datasets"
            ],
            "correct_answer": "C. The credentials utilized to connect to datasets",
            "explanation": """
                **Explanation:** The data lineage view does not display the credentials used to connect to datasets, it shows where dataflows, data sources, and gateways are utilized.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-data-lineage"
        },
        23: {
            "question": """
                You need to configure a Gauge chart. Where would you set the goal for this?
            """,
            "options": [
                "A. Format Settings",
                "B. Power Query",
                "C. Calculated Column",
                "D. DAX Expression"
            ],
            "correct_answer": "A. Format Settings",
            "explanation": """
                **Explanation:** In Power BI's Format pane, you can set the Maximum, Minimum, and Target values for the Gauge chart.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-radial-gauge-charts"
        },
        24: {
            "question": """
                You want to calculate/return the last day of the month in the BS data to make sure that the BS data can be related to the Date table. Which of the following type of calculations would you use?
            """,
            "options": [
                "A. A DAX calculated column",
                "B. A DAX calculated measure",
                "C. An M custom column",
                "D. None of the above"
            ],
            "correct_answer": "A. A DAX calculated column",
            "explanation": """
                **Explanation:** A DAX calculated column is ideal to compute the last day of the month for each row and make it possible to relate the BS data with the Date table.
            """,
            "reference": "https://docs.microsoft.com/en-us/dax/lastdate-function-dax"
        },
        25: {
            "question": """
                As per the case study, you are supposed to create the Top Customers report. Which of the following type of filters would you use at the visual level to meet the goal?
            """,
            "options": [
                "A. Basic",
                "B. Advanced",
                "C. TOP N",
                "D. UPPER N"
            ],
            "correct_answer": "C. TOP N",
            "explanation": """
                **Explanation:** TOP N filter helps you display the top customers based on highest sales amounts in the given filters.
            """,
            "reference": "https://docs.microsoft.com/en-us/dax/topn-function-dax"
        },
        26: {
            "question": """
                You need to create a report that demonstrates the percentage of late orders in Power BI. Which of the following type of visualization would you use?
            """,
            "options": [
                "A. Scatterplot",
                "B. Pie chart",
                "C. Funnel Chart",
                "D. Bar chart"
            ],
            "correct_answer": "D. Bar chart",
            "explanation": """
                **Explanation:** Bar and column charts are best suited for showing metrics such as the percentage of late orders by different dimensions like country or region.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-bar-and-column-charts"
        },
        27: {
            "question": """
                Is it possible to create a relationship between the ProductID column of the Order Details table and the ProductName column of the Products table?
            """,
            "options": [
                "A. Yes",
                "B. No"
            ],
            "correct_answer": "B. No",
            "explanation": """
                **Explanation:** It is not possible to create a relationship between columns of different data types. ProductID is of type int, whereas ProductName is of type NVARCHAR.
            """,
            "reference": "https://docs.microsoft.com/en-us/learn/modules/optimize-model-power-bi/2-performance"
        },
        28: {
            "question": """
                You are working on a model training task using the K sliding window method. What is the minimum number of data points required for inference?
            """,
            "options": [
                "A. K+1 points",
                "B. K-1 points",
                "C. K*K points",
                "D. K points"
            ],
            "correct_answer": "D. K points",
            "explanation": """
                **Explanation:** To ensure valid results during inference in the k-sliding window method, at least k data points are required.
            """,
            "reference": "https://docs.microsoft.com/en-us/azure/cognitive-services/anomaly-detector/tutorials/learn-multivariate-anomaly-detection"
        },
        29: {
            "question": """
                There are several methods that can be used to fill/handle the missing values (known as nan) in the merged table. Which of the following fillNAMethod would you use to fill the nan with the padding value?
            """,
            "options": [
                "A. Linear",
                "B. Previous",
                "C. Padding",
                "D. Subsequent",
                "E. Zero",
                "F. Fixed"
            ],
            "correct_answer": "F. Fixed",
            "explanation": """
                **Explanation:** The Fixed option is used to fill missing values (nan) with the padding value.
            """,
            "reference": "https://docs.microsoft.com/en-us/azure/cognitive-services/anomaly-detector/tutorials/learn-multivariate-anomaly-detection"
        },
        30: {
            "question": """
                While attempting to enable the security labels in Power BI, you receive an error message and are not able to enable the security labels. Which of the following might be the possible reason?
            """,
            "options": [
                "A. You don’t have an Azure Information Protection license",
                "B. Sensitivity labels haven’t been migrated to the MS Information Protection version that Power BI supports",
                "C. No MS Information Protection sensitivity labels are defined/specified in the organization",
                "D. Any of the above"
            ],
            "correct_answer": "D. Any of the above",
            "explanation": """
                **Explanation:** All the mentioned reasons could be the cause of the error when enabling security labels in Power BI.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/admin/service-security-enable-data-sensitivity-labels"
        },
    
        31: {
            "question": """
                Microsoft Information Protection sensitivity labels allow the users to classify the sensitive/critical content in Power BI without affecting the productivity or the collaborating ability. These Sensitivity labels can be applied to which of the following items in Power BI Service?
            """,
            "options": [
                "A. Only datasets",
                "B. Only reports",
                "C. Only dashboards",
                "D. Only dataflows",
                "E. Only datasets and reports",
                "F. All including reports, datasets, dataflows, and dashboards"
            ],
            "correct_answer": "F. All including reports, datasets, dataflows, and dashboards",
            "explanation": """
                **Explanation:** Sensitivity labels in Power BI Service can be applied to reports, datasets, dataflows, and dashboards.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/admin/service-security-sensitivity-label-overview"
        },
        32: {
            "question": """
                As only a limited number of summaries can be created, Smart Narratives considers only the most interesting stuff to summarize for the visual. Smart Narratives can create up to _______ summaries per visual and up to ______ summaries per page.
            """,
            "options": [
                "A. 1, 2",
                "B. 1, 4",
                "C. 4, 1",
                "D. 4, 16",
                "E. 2, 8"
            ],
            "correct_answer": "D. 4, 16",
            "explanation": """
                **Explanation:** Smart Narratives can generate up to 4 summaries per visual and up to 16 summaries per page.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-smart-narrative"
        },
        33: {
            "question": """
                While creating visuals for your Power BI dashboards, there is an opportunity to break down your visuals into slices called small multiples. Which of the following options cover the full list of visuals supporting small multiples?
            """,
            "options": [
                "A. Bar, column and line",
                "B. Doughnut, bar, area and line",
                "C. Bar, column, area and line",
                "D. Pie, doughnut, bar, line"
            ],
            "correct_answer": "C. Bar, column, area and line",
            "explanation": """
                **Explanation:** Small multiples in Power BI are supported by bar, column, area, and line charts.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-small-multiples"
        },
        34: {
            "question": """
                For your Power BI dashboard, you have just created a pie chart visualizing the actual sales figures by region for the last year. In order to give decision makers a deeper insight, you want to extend the visual with a breakdown by countries. You decide to use the small multiples feature as a comfortable way of exploding visuals by a given dimension. Is it a feasible solution?
            """,
            "options": [
                "A. Yes",
                "B. No"
            ],
            "correct_answer": "B. No",
            "explanation": """
                **Explanation:** Small multiples are not supported for pie charts in Power BI.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-small-multiples"
        },
        35: {
            "question": """
                You have just created a bar chart visualizing the actual sales figures by region for the past years. In order to give decision makers a deeper insight, you want to extend the visual with a breakdown by countries using the small multiples feature, and you also want to enhance it by showing the trend lines. Is it a feasible way of solving the problem?
            """,
            "options": [
                "A. Yes, because all the formatting options available for visuals also work for small multiples",
                "B. No, because adding trend lines to small multiples charts is currently not available",
                "C. Yes, because while many formatting options don’t work for small multiples, trend lines can be applied with no limitation",
                "D. No, because bar charts cannot be broken down into small multiples"
            ],
            "correct_answer": "B. No, because adding trend lines to small multiples charts is currently not available",
            "explanation": """
                **Explanation:** Trend lines are not currently supported in small multiples charts in Power BI.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-small-multiples#formatting-options"
        },
        36: {
            "question": """
                You are creating a dashboard by using the Power BI service. You have an existing report page that contains three charts. You need to add the charts to the dashboard while maintaining the interactivity between the charts. What should you do?
            """,
            "options": [
                "A. Edit interactions in the report and set all interactions to Filter.",
                "B. Pin each chart as a tile.",
                "C. Edit the dashboard theme and pin each chart as a tile.",
                "D. Pin the report page as a live tile."
            ],
            "correct_answer": "D. Pin the report page as a live tile.",
            "explanation": """
                **Explanation:** Pinning the entire report page as a live tile ensures that the interactivity between charts is maintained.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/create-reports/power-bi-dashboards"
        },
        37: {
            "question": """
                You need to create a data model that includes multiple tables. Which tool should you use?
            """,
            "options": [
                "A. Power BI",
                "B. Power Automate",
                "C. Power Apps",
                "D. Power Query"
            ],
            "correct_answer": "A. Power BI",
            "explanation": """
                **Explanation:** Power BI allows users to connect, transform, and model data across multiple tables and is the best tool for creating data models.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-modeling"
        },
        38: {
            "question": """
                You want to show the relationship between two variables in a dataset. Which chart type would be best to use?
            """,
            "options": [
                "A. Scatter chart",
                "B. Bar chart",
                "C. Line chart",
                "D. Pie chart"
            ],
            "correct_answer": "A. Scatter chart",
            "explanation": """
                **Explanation:** Scatter charts in Power BI are ideal for showing relationships between two numerical values.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-scatter"
        },
        39: {
            "question": """
                How can you ensure that datasets are up-to-date in Power BI?
            """,
            "options": [
                "A. Manually refresh each dataset",
                "B. Use a scheduled refresh",
                "C. Use a live connection to the data source",
                "D. Use a direct query to the data source"
            ],
            "correct_answer": "B. Use a scheduled refresh",
            "explanation": """
                **Explanation:** Scheduled refresh ensures automatic updates to your datasets without manual intervention.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/connect-data/refresh-data"
        },
        40: {
            "question": """
                You are building a Power BI report. Users will view the report by using their mobile device. You need to configure the report to display data based on each user’s location. Which two actions should you perform? Each correct answer presents part of the solution. NOTE: Each correct selection is worth one point.
            """,
            "options": [
                "A. From Power Query Editor, detect the data types of the relevant columns.",
                "B. In Data Category, set the geographic data category for the relevant columns.",
                "C. Create a hierarchy for columns of the geography data type.",
                "D. Use the columns of the geography data type in all visuals.",
                "E. For the relevant columns, set synonyms to match common geographical terms."
            ],
            "correct_answer": "B. In Data Category, set the geographic data category for the relevant columns.; D. Use the columns of the geography data type in all visuals.",
            "explanation": """
                **Explanation:** Set the geographic data category for the relevant columns and use these columns in all visuals to display data based on users' locations.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-data-categorization"
        },
    
        41: {
            "question": """
                What is the difference between a shared and a personal workspace in Power BI?
            """,
            "options": [
                "A. Shared workspaces can be accessed by multiple users",
                "B. Personal workspaces can only be accessed by the owner",
                "C. Shared workspaces can be edited by multiple users",
                "D. Personal workspaces can be shared with other users"
            ],
            "correct_answer": "A. Shared workspaces can be accessed by multiple users; B. Personal workspaces can only be accessed by the owner; C. Shared workspaces can be edited by multiple users",
            "explanation": """
                **Explanation:** Shared workspaces can be accessed and edited by multiple users, while personal workspaces are private and can only be accessed by the owner.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-workspaces"
        },
        42: {
            "question": """
                How can you ensure that only authorized users have access to a dataset in Power BI?
            """,
            "options": [
                "A. Use row-level security",
                "B. Use column-level security",
                "C. Use object-level security",
                "D. Use workspace-level security"
            ],
            "correct_answer": "A. Use row-level security",
            "explanation": """
                **Explanation:** Row-level security (RLS) is used to restrict data access for certain users, ensuring only authorized users can view specific rows in a dataset.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/admin/service-admin-rls"
        },
        43: {
            "question": """
                How can you manage permissions for a workspace in Power BI?
            """,
            "options": [
                "A. Add or remove members",
                "B. Assign roles to members",
                "C. Set permissions for specific reports",
                "D. Delete a workspace"
            ],
            "correct_answer": "B. Assign roles to members",
            "explanation": """
                **Explanation:** Assigning roles to members (Admin, Member, Contributor) is the most efficient way to manage workspace permissions in Power BI.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-create-the-new-workspaces"
        },
        44: {
            "question": """
                What is the purpose of the Power BI Gateway?
            """,
            "options": [
                "A. To allow users to connect to on-premises data sources",
                "B. To allow users to create custom visuals",
                "C. To allow users to share reports with others",
                "D. To allow users to create dashboards"
            ],
            "correct_answer": "A. To allow users to connect to on-premises data sources",
            "explanation": """
                **Explanation:** The Power BI Gateway is used to connect on-premises data sources with cloud-based Power BI services.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/connect-data/service-gateway-onprem"
        },
        45: {
            "question": """
                What is the purpose of the Power BI data model?
            """,
            "options": [
                "A. To provide a visual representation of data",
                "B. To store data in a centralized location",
                "C. To create reports and dashboards",
                "D. To analyze data using DAX formulas"
            ],
            "correct_answer": "B. To store data in a centralized location",
            "explanation": """
                **Explanation:** The Power BI data model stores data in a centralized location and serves as the foundation for creating reports, dashboards, and analyzing data with DAX.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-modeling"
        },
        46: {
            "question": """
                You have a project management app that is fully hosted in Microsoft Teams. The app was developed by using Microsoft Power Apps. You need to create a Power BI report that connects to the project management app. Which connector should you select?
            """,
            "options": [
                "A. Microsoft Teams Personal Analytics",
                "B. SQL Server database",
                "C. Dataverse",
                "D. Dataflows"
            ],
            "correct_answer": "C. Dataverse",
            "explanation": """
                **Explanation:** Since the project management app is built using Microsoft Power Apps, it likely uses Dataverse as the data source.
            """,
            "reference": "https://docs.microsoft.com/en-us/powerapps/maker/common-data-service/data-platform-intro"
        },
        47: {
            "question": """
                You have four sales regions. Each region has multiple sales managers. You implement row-level security (RLS) in a data model. You assign the relevant mail-enabled security group to each role. A sales manager changes to a different region. You need to ensure that the sales manager can see the correct sales data. What should you do?
            """,
            "options": [
                "A. Change the Microsoft Power BI license type of the sales manager.",
                "B. From Microsoft Power BI Desktop, edit the Row-Level Security setting for the reports.",
                "C. Manage the permissions of the underlying dataset.",
                "D. Request that the sales manager be added to the correct Azure Active Directory group."
            ],
            "correct_answer": "D. Request that the sales manager be added to the correct Azure Active Directory group.",
            "explanation": """
                **Explanation:** The most efficient way to update access for the sales manager is by adding them to the correct Azure Active Directory group.
            """,
            "reference": "https://docs.microsoft.com/en-us/power-bi/admin/service-security-rls"
        }
    }

    # Get the current question data
    question_data = questions.get(question_number, {"question": "Question not found", "options": [], "correct_answer": "", "explanation": ""})

    # Display progress bar
    st.progress(question_number / total_questions)

    st.markdown(
    """
    <style>
    /* Background color for the entire page */
    body {
        background-color: #f4f4f2;
    }
    
    /* Container that holds all content, including questions */
    .reportview-container .main .block-container{
        max-width: 1000px;
        padding-top: 5rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 5rem;
    }
    
    /* Ensure that content does not overflow horizontally */
    .question-container {
        border: 3px solid #4CAF50;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        max-width: 800px;  /* Set a max width to prevent horizontal scrolling */
        width: 100%;  /* Ensure the container takes the full available width */
        box-sizing: border-box;  /* Include padding and border in the width calculation */
        overflow-wrap: break-word;  /* Ensure long text will wrap and not overflow */
        word-wrap: break-word;  /* Older browsers support */
        text-align: left;  /* Align text to the left */
        background-color: #ffffff;  /* White background for question box */
    }
    
    .stRadio > label {
        display: block;
        color: #4CAF50;
        margin: 10px 0;
    }
    
    .css-1y0tads {
        max-width: 100%;
    }
    </style>
    """, 
    unsafe_allow_html=True
    )

    # Display question with border and background
        # Escape HTML special characters in the question text to avoid unexpected HTML rendering
    escaped_question = html.escape(question_data['question'])

    # Display question with border and background
    st.markdown(f"""<div class="question-container">
                    <h3>Question {question_number} of {total_questions}</h3>
                    {escaped_question} 
                    </div>""", 
                    unsafe_allow_html=True)


    # Display options for answers
    selected_option = st.radio("Choose your answer:", question_data["options"], key=f"option_{question_number}")

    # Submit button to check answer
    if st.button("Submit"):
        if selected_option == question_data["correct_answer"]:
            st.success("Correct answer!")
            st.markdown(question_data["explanation"])
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