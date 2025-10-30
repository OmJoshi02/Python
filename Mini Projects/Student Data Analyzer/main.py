import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# ----------------------------
# Constants and Mappings
# ----------------------------
PROGRAM_SHORTNAMES = {
    "B.Tech - Computer Science & Engineering": "CSE",
    "B.Tech - Computer Science & Engineering (Data Science)": "CSE (DS)",
    "B.Tech - Electronics & Tele.communication Engineering": "E&TC",
    "B.Tech - Chemical Engineering": "Chem",
    "B.Tech - Mechanical Engineering": "Mech",
    "B.Tech - Civil Engineering": "Civil"
}

# ----------------------------
# Helper Functions
# ----------------------------
def load_data(file_path="data.csv"):
    """Load CSV file into a DataFrame and prepare short names."""
    df = pd.read_csv(file_path)
    df['Program Short Name'] = df['Program Name'].apply(
        lambda x: PROGRAM_SHORTNAMES.get(x.strip(), x.strip())
    )
    df['Program Short'] = df['Program Short Name']
    print(f"Data successfully loaded from {file_path}. Total records: {len(df)}")
    return df

def clean_name(name):
    """Convert program name to a safe filename."""
    return re.sub(r'[()\s&/]+', '_', name).strip('_')

# ----------------------------
# Core Functions
# ----------------------------
def save_students_by_program(df):
    """Sort students by program and save each program as a CSV."""
    df_sorted = df.sort_values(by="Program Name")
    output_dir = "program_wise_students"
    os.makedirs(output_dir, exist_ok=True)

    for program, group in df_sorted.groupby("Program Name"):
        filename = f"{clean_name(program)}_students.csv"
        filepath = os.path.join(output_dir, filename)
        group.to_csv(filepath, index=False)
        print(f"Saved {len(group)} students for '{program}' → {filepath}")
    print("\nAll program-wise student files created successfully!")

def plot_number_of_students(df):
    """Plot the number of students in each program."""
    program_counts = df['Program Short'].value_counts().sort_values(ascending=True)

    print("\nStudent count per program:")
    print(program_counts.to_markdown(numalign="left", stralign="left"), "\n")

    plt.figure(figsize=(12, 7))
    bars = plt.barh(program_counts.index, program_counts.values, color='#3498db', edgecolor='black')

    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{int(width)}',
                 ha='left', va='center', fontsize=12, fontweight='bold')

    plt.title("Number of Students by Program", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Number of Students", fontsize=14)
    plt.ylabel("Program", fontsize=14)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.xlim(right=program_counts.max() * 1.1)
    plt.tight_layout()
    plt.show()

def plot_average_cgpa():
    """Plot the average CGPA of each program based on saved CSVs."""
    output_dir = "program_wise_students"
    avg_cgpa_data = {}

    if not os.path.exists(output_dir):
        print("No program-wise CSV files found. Please run 'save_students_by_program' first.")
        return

    # Map filenames to short program names
    short_name_map = {clean_name(full): short for full, short in PROGRAM_SHORTNAMES.items()}

    for filename in os.listdir(output_dir):
        if filename.endswith("_students.csv"):
            filepath = os.path.join(output_dir, filename)
            df_program = pd.read_csv(filepath)
            program_key = filename.replace('_students.csv', '')
            chart_label = short_name_map.get(program_key, program_key.replace('_', ' '))
            avg_cgpa_data[chart_label] = df_program["CGPA"].mean()

    avg_cgpa_series = pd.Series(avg_cgpa_data).sort_values(ascending=False)
    programs = avg_cgpa_series.index.tolist()
    averages = avg_cgpa_series.values.tolist()

    plt.figure(figsize=(10, 8))
    bars = plt.bar(programs, averages, color='#e74c3c', edgecolor='black')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.05, f'{height:.2f}',
                 ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.title("Average CGPA by Academic Program", fontsize=20, fontweight='bold', pad=20)
    plt.xlabel("Academic Program", fontsize=14)
    plt.ylabel("Average CGPA", fontsize=14)
    plt.ylim(bottom=avg_cgpa_series.min() * 0.9, top=avg_cgpa_series.max() * 1.1)
    plt.xticks(rotation=15, ha='right', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# ----------------------------
# Menu System
# ----------------------------
def run_menu(df):
    while True:
        print("\n==============================================")
        print("  Student Data Analyzer Menu")
        print("==============================================")
        print("1. Sort and Save Students by Program (Creates CSV files)")
        print("2. Plot Number of Students by Program")
        print("3. Plot Average CGPA by Academic Program (Requires files from Option 1)")
        print("4. Exit")
        print("==============================================")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            save_students_by_program(df)
        elif choice == '2':
            plot_number_of_students(df)
        elif choice == '3':
            plot_average_cgpa()
        elif choice == '4':
            print("Exiting Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# ----------------------------
# Main Execution
# ----------------------------
if __name__ == "__main__":
    df = load_data("data.csv")
    run_menu(df)
