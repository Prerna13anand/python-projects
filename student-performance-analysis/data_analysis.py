import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
from typing import Tuple, Dict

def load_data() -> pd.DataFrame:
    """Load the student study habits dataset from Kaggle.
    
    Returns:
        pd.DataFrame: The loaded dataset
    """
    path = kagglehub.dataset_download('prekshad2166/student-study-habits')
    return pd.read_csv(f'{path}/student_study_habits.csv')

def display_basic_info(df: pd.DataFrame) -> None:
    """Display basic information about the dataset.
    
    Args:
        df (pd.DataFrame): The dataset to analyze
    """
    print('\nDataset Info:')
    print(df.info())
    
    print('\nFirst few rows:')
    print(df.head())
    
    print('\nSummary statistics:')
    print(df.describe())

def create_performance_plots(df: pd.DataFrame) -> None:
    """Create scatter plots showing relationships with final grade.
    
    Args:
        df (pd.DataFrame): The dataset to visualize
    """
    # Study Hours vs Final Grade
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='study_hours_per_week', y='final_grade')
    plt.title('Study Hours per Week vs Final Grade')
    plt.tight_layout()
    plt.savefig('study_grade.png')
    plt.close()
    
    # Sleep Hours vs Final Grade
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='sleep_hours_per_day', y='final_grade')
    plt.title('Sleep Hours per Day vs Final Grade')
    plt.xlabel('Sleep Hours per Day')
    plt.ylabel('Final Grade')
    plt.tight_layout()
    plt.savefig('sleep_grade.png')
    plt.close()
    
    # Attendance vs Final Grade
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='attendance_percentage', y='final_grade')
    plt.title('Attendance Percentage vs Final Grade')
    plt.xlabel('Attendance Percentage')
    plt.ylabel('Final Grade')
    plt.tight_layout()
    plt.savefig('attendance_grade.png')
    plt.close()

def create_correlation_heatmap(df: pd.DataFrame) -> None:
    """Create a correlation heatmap for numeric features.
    
    Args:
        df (pd.DataFrame): The dataset to analyze
    """
    numeric_columns = ['study_hours_per_week', 'sleep_hours_per_day', 
                      'attendance_percentage', 'assignments_completed', 'final_grade']
    correlation_matrix = df[numeric_columns].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix of Academic Factors')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png')
    plt.close()

def create_grade_distribution(df: pd.DataFrame) -> None:
    """Create a histogram showing the distribution of final grades.
    
    Args:
        df (pd.DataFrame): The dataset to visualize
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='final_grade', bins=20)
    plt.title('Distribution of Final Grades')
    plt.xlabel('Final Grade')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('grade_distribution.png')
    plt.close()

def analyze_activity_impact(df: pd.DataFrame) -> Dict[str, pd.Series]:
    """Analyze the impact of activities on final grades.
    
    Args:
        df (pd.DataFrame): The dataset to analyze
        
    Returns:
        Dict[str, pd.Series]: Dictionary containing analysis results
    """
    results = {
        'part_time_job': df.groupby('part_time_job_Yes')['final_grade'].mean(),
        'extracurricular': df.groupby('extracurricular_Yes')['final_grade'].mean()
    }
    
    print('\nAverage Final Grade by Part-time Job Status:')
    print(results['part_time_job'])
    
    print('\nAverage Final Grade by Extracurricular Activities:')
    print(results['extracurricular'])
    
    return results

def main():
    """Main function to run the analysis."""
    # Load data
    df = load_data()
    
    # Display basic information
    display_basic_info(df)
    
    # Create visualizations
    create_performance_plots(df)
    create_correlation_heatmap(df)
    create_grade_distribution(df)
    
    # Analyze impact of activities
    analyze_activity_impact(df)
    
    print('\nAnalysis complete! Check the generated PNG files for visualizations.')

if __name__ == '__main__':
    main()