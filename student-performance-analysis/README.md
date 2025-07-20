# Data Analysis and Visualization Project

This project demonstrates data analysis and visualization techniques using Python, focusing on student study habits and their impact on academic performance.

## Current Implementation

The project uses a Kaggle dataset on student study habits to analyze:

1. **Data Loading and Exploration**
   - Dataset from Kaggle (prekshad2166/student-study-habits)
   - Basic dataset information
   - Summary statistics

2. **Statistical Analysis**
   - Impact of study hours on final grades
   - Effect of sleep patterns on academic performance
   - Correlation between attendance and grades
   - Influence of part-time jobs and extracurricular activities

3. **Visualizations**
   - Study hours vs final grade scatter plot
   - Sleep hours vs final grade scatter plot
   - Attendance vs final grade scatter plot
   - Correlation heatmap of academic factors
   - Distribution of final grades

## Requirements

The project requires the following Python packages:
- pandas >= 2.0.0
- matplotlib >= 3.0.0
- seaborn >= 0.12.0
- kagglehub

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

Run the analysis script:
```bash
python data_analysis.py
```

The script will generate several PNG files containing visualizations:
- study_grade.png
- sleep_grade.png
- attendance_grade.png
- correlation_heatmap.png
- grade_distribution.png

## Future Improvements

1. **Analysis Enhancement**
   - Add more advanced statistical tests
   - Implement predictive modeling for grade prediction
   - Include multivariate analysis
   - Add confidence intervals and hypothesis testing

2. **Code Structure**
   - Create modular functions for reusability
   - Add error handling and input validation
   - Implement logging for better debugging
   - Add configuration file for parameters

3. **Visualization Enhancement**
   - Add interactive plots using Plotly
   - Create a dashboard using Streamlit
   - Include more advanced visualizations
   - Add customizable plot themes

4. **Documentation**
   - Add detailed code comments
   - Include function docstrings
   - Add example outputs and interpretation
   - Include data dictionary