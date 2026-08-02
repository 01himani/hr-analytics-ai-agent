import pandas as pd

# Read Excel file
def load_data(file):

    df = pd.read_excel(file)

    return df


# Calculate HR KPIs
def calculate_kpis(df):

    total_employees = len(df)

    attrition_count = len(df[df["Attrition"] == "Yes"])

    active_employees = total_employees - attrition_count

    attrition_rate = round((attrition_count / total_employees) * 100, 2)

    average_age = round(df["Age"].mean(), 2)

    average_salary = round(df["MonthlyIncome"].mean(), 2)

    return {
        "Total Employees": total_employees,
        "Active Employees": active_employees,
        "Attrition Count": attrition_count,
        "Attrition Rate": f"{attrition_rate}%",
        "Average Age": average_age,
        "Average Salary": f"INR {average_salary:,.2f}"
    }