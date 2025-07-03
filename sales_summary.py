import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('sales_data.db')

# SQL query
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

# Read query result into DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Print summary
print("Sales Summary:\n")
print(df)

# Plot revenue per product
df.plot(kind='bar', x='product', y='revenue', color='orange', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Save the plot
plt.show()  # Show the plot
