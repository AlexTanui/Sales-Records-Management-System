import matplotlib
matplotlib.use('agg')  # Use the 'agg' backend

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV files into DataFrames
customers_df = pd.read_csv('customers.csv')
sales_df = pd.read_csv('sales.csv')

# Remove leading spaces from column names
sales_df.columns = sales_df.columns.str.strip()

# Function to get monthly sales data
# Function to get monthly sales data
def get_monthly_data(df, filter_func=None):
    df = df.copy()  # Create a copy of the DataFrame
    if filter_func:
        df = df[df.apply(filter_func, axis=1)]
    df['date'] = pd.to_datetime(df['date'])
    df['year_month'] = df['date'].dt.to_period('M')
    grouped = df.groupby('year_month').agg({'value': 'sum', 'trans_id': 'count'}).reset_index()
    grouped['year_month'] = grouped['year_month'].astype(str)
    return grouped['year_month'], grouped['value'], grouped['trans_id']

# Function to plot monthly sales values and number of sales
def plot_monthly_sales(dates, values, counts, title):
    fig, ax1 = plt.subplots()

    # Plot sales values
    ax1.plot(dates, values, color='tab:blue', label='Sales Value')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Sales Value', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Create a second y-axis for number of sales
    ax2 = ax1.twinx()
    ax2.plot(dates, counts, color='tab:orange', label='Number of Sales')
    ax2.set_ylabel('Number of Sales', color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange')

    # Set title and legend
    plt.title(title)
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Save the plot instead of showing it
    plt.savefig('monthly_sales_performance.png')

# Function to display the monthly sales performance
def display_overall_sales_performance():
    dates, values, counts = get_monthly_data(sales_df)
    plot_monthly_sales(dates, values, counts, 'Overall Monthly Sales Performance')

# Function to display monthly sales performance for a given customer
def display_sales_for_customer(customer_id):
    customer_sales_df = sales_df[sales_df['customer_id'] == customer_id]
    dates, values, counts = get_monthly_data(customer_sales_df)
    plot_monthly_sales(dates, values, counts, f'Monthly Sales Performance for Customer {customer_id}')

# Function to display monthly sales performance for a given postcode
def display_sales_for_postcode(postcode):
    postcode_customers = customers_df[customers_df['postcode'] == postcode]['customer_id']
    postcode_sales_df = sales_df[sales_df['customer_id'].isin(postcode_customers)]
    dates, values, counts = get_monthly_data(postcode_sales_df)
    plot_monthly_sales(dates, values, counts, f'Monthly Sales Performance for Postcode {postcode}')

# Main menu function
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Display overall monthly sales performance")
        print("2. Display monthly sales performance for a given customer")
        print("3. Display monthly sales performance for a given postcode")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_overall_sales_performance()
        elif choice == '2':
            customer_id = int(input("Enter customer ID: "))
            display_sales_for_customer(customer_id)
        elif choice == '3':
            postcode = input("Enter postcode: ")
            display_sales_for_postcode(postcode)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
