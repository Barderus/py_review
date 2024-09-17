import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 1. Line plot
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# 2. Bar Chart
products = ["Product A", "Product B", "Product C", "Product D"]
sales = [25, 40, 15, 30]

plt.bar(products, sales, color="green")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# 3. Histogram
# Generate random data
data = np.random.randn(1000)

# Create histogram
plt.hist(data, bins=30, alpha=0.7, color='blue')

# Add titles and labels
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot
x = [x for x in np.random.randint(100, size = 25)]
y = [i for i in np.random.randint(100, size = 25)]

plt.scatter(x, y, color="orange")
plt.scatter(x,y, color="green")
plt.show()

# 5. Pie Chart
responses = ["Agree", "Disagree", "Neutral"]
counts = [50, 30, 20]

plt.pie(counts, autopct='%1.1f%%')
plt.show()

# 6. Line plot from Pandas DataFrame
data = {"Month":["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales":[100, 120, 115, 140, 129, 139]}
df = pd.DataFrame(data)
x = df["Month"].values
y = df["Sales"].values
print(x)
print(y)
plt.plot(x, y, color="red", label="Sales")
plt.legend()
plt.show()

# 7. Histogram from a Pandas Series
ages = pd.Series([23, 25, 31, 35, 29, 42, 38, 30, 27, 24, 32])
plt.hist(ages, bins=5, alpha=0.7, color='blue')
plt.show()
