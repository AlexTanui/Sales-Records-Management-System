# Sales Records Management System

This project provides two main Python scripts for managing and analyzing sales records. The first script focuses on visualizing monthly sales performance from CSV data, while the second script provides functionalities for managing customer and sales records interactively.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Setup Instructions](#setup-instructions)
- [Running the Scripts](#running-the-scripts)
- [Author](#author)
- [License](#license)

## Overview

### Sales Data Visualization Script (`customsale.py`)
This script visualizes sales data stored in CSV files, allowing users to view overall monthly sales performance, monthly sales performance for a specific customer, and monthly sales performance for a specific postcode. The data is visualized using matplotlib.

### Customer and Sales Records Management Script (`customer_sales_record.py`)
This script provides an interactive menu for managing customer and sales records. Users can load data from CSV files, save records to CSV, add new customers and sales records, search for records, display sales for a specific customer, and delete records.

## Features

### Sales Data Visualization Script (`customsale.py`)
- **Overall Monthly Sales Performance**: Visualizes the overall monthly sales values and the number of sales.
- **Customer-Specific Sales Performance**: Displays monthly sales performance for a specified customer.
- **Postcode-Specific Sales Performance**: Shows monthly sales performance for a specified postcode.

### Customer and Sales Records Management Script (`customer_sales_record.py`)
- **Load Records**: Load customer and sales data from CSV files.
- **Save Records**: Save customer or sales records to CSV files.
- **Add Records**: Add new customers or sales records.
- **Search Records**: Search for customers or sales records.
- **Display Sales for Customer**: Display all sales records for a specific customer.
- **Delete Records**: Delete specific sales records or entire customer records.

## Usage

### For Sales Data Visualization:
1. Place the required CSV files (`customers.csv` and `sales.csv`) in the same directory as the script.
2. Run the script:
   ```sh
   python3 customsale.py
   ```
3. Follow the on-screen menu to select the desired visualization.
4. The script generates a plot saved as `monthly_sales_performance.png`.

### For Customer and Sales Records Management:
1. Run the script:
   ```sh
   python3 customer_sales_record.py
   ```
2. Follow the interactive menu to perform various operations such as loading, saving, adding, searching, displaying, and deleting records.

## Setup Instructions

1. Ensure you have Python 3.x installed.
2. Install the required Python libraries:
   ```sh
   pip install pandas matplotlib numpy
   ```
3. Prepare the required CSV files:
   - `customers.csv`: Should contain customer details (ID, name, postcode, phone).
   - `sales.csv`: Should contain sales details (date, transaction ID, customer ID, category, value).

## Running the Scripts

### For Sales Data Visualization:
1. Place `customers.csv` and `sales.csv` in the same directory as `customsale.py`.
2. Run `customsale.py`:
   ```sh
   python3 customsale.py
   ```
3. Follow the menu to visualize sales data.

### For Customer and Sales Records Management:
1. Run `customer_sales_record.py`:
   ```sh
   python3 customer_sales_record.py
   ```
2. Follow the interactive menu to manage records.

## Author

This project was developed by [NathanKimoi].

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.