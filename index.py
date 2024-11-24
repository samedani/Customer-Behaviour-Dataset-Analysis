import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('customers.csv')
#Created Dataframe
df = pd.DataFrame(data)
print(df.describe())


avg_spent_by_job = df.groupby('job')['spent'].mean()
avg_orders_by_job = df.groupby('job')['orders'].mean()
avg_spent_by_gender = df.groupby('gender')['spent'].mean()
avg_orders_by_gender = df.groupby('gender')['orders'].mean()
avg_orders_by_marital_status = df.groupby('is_married')['orders'].mean()
avg_spent_by_marital_status =  df.groupby('is_married')['spent'].mean()
avg_orders_by_hobby = df.groupby('hobbies')['orders'].mean()
avg_spent_by_hobby = df.groupby('hobbies')['spent'].mean()

print(avg_spent_by_hobby)
print(avg_spent_by_job)
print(avg_orders_by_job)
print(avg_spent_by_gender)
print(avg_orders_by_gender)
print(avg_spent_by_marital_status)
print(avg_orders_by_marital_status)

# Visualizing Spending by Gender
avg_spent_by_gender.plot(kind='bar', title="Average Spending by Gender")
plt.ylabel("Average Spending")
plt.show()

# Visualizing Orders by Gender
avg_orders_by_gender.plot(kind='bar', title="Average Orders by Gender")
plt.ylabel("Average Orders")
plt.show()

# Visualizing Orders by Job
avg_orders_by_job.plot(kind='bar', title="Average Orders by Job")
plt.ylabel("Average Orders")
plt.show()

# Visualizing Spending by job
avg_spent_by_job.plot(kind='bar', title="Average Spending by Job")
plt.ylabel("Average Spending")
plt.show()

# Visualizing Spending by Marital Status
avg_spent_by_marital_status.plot(kind='bar', title="Average Spending by Marital Status")
plt.ylabel("Average Spending")
plt.show()


# Visualizing Orders by Marital Status
avg_orders_by_marital_status.plot(kind='bar', title="Average Orders by Marital Status")
plt.ylabel("Average Orders")
plt.show()


# Scatter plot for Age vs. Spending
df.plot(kind='scatter', x='age', y='spent', title="Age vs. Spending")
plt.show()


#Box plot for Gender vs Spent
sns.boxplot(data = df, x ='gender', y = 'spent')
plt.title("Spending by Gender")
plt.show()


#Scatter plot for Spending vs. Orders
sns.scatterplot(data=df, x='orders', y='spent', hue='gender')
plt.title('Spending vs. Orders (Colored by Gender)')
plt.show()


# Correlation between Age and Spending
age_spending_correlation = df['age'].corr(df['spent'])
print(f"Correlation between Age and Spending: {age_spending_correlation}")



# Grouped 'job' and 'hobbies' to show average spending
avg_spent_by_job = df.groupby('job')['spent'].mean()




#

# Save the cleaned DataFrame to a CSV file for future analysis
df.to_csv('cleaned_data.csv', index=False)




















"""

"""
avg_age = df['age'].mean()
print("Average Age:", avg_age)
avg_orders = df['orders'].mean()
print("Average Orders:", avg_orders)
avg_spent = df['spent'].mean()
print("Average Spent:", avg_spent)

avg_orders_by_gender = df.groupby('gender')['orders'].mean()
print("Average Orders by Gender:", avg_orders_by_gender)

avg_age_by_gender = df.groupby('gender')['age'].mean()
print("Average Age by Gender:", avg_age_by_gender)

avg_spent_by_job = df.groupby('job')['spent'].mean()
print("Average Spending by Job:", avg_spent_by_job)

avg_orders_by_marital_status = df.groupby('is_married')['orders'].mean()
print("Average Orders by Marital Status:", avg_orders_by_marital_status)

avg_age_by_job = df.groupby('job')['age'].mean()
print("Average Age by Job:", avg_age_by_job)

avg_spent_by_hobby = df.groupby('hobbies')['spent'].mean()
print("Average Spending by Hobby:", avg_spent_by_hobby)

recent_registrations = df[df['registered'] > '1/1/2023']
avg_recent_orders = recent_registrations['orders'].mean()
avg_recent_spent = recent_registrations['spent'].mean()
print("Average Orders for Recent Registrations:", avg_recent_orders)
print("Average Spending for Recent Registrations:", avg_recent_spent)
bins = [20, 30, 40, 50, 60, 70, 80]
labels = ['20-30', '30-40', '40-50', '50-60', '60-70', '70-80']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)


total_spent = df['spent'].sum()
total_orders = df['orders'].sum()
print("Total Spending:", total_spent)
print("Total Orders:", total_orders)




high_spenders = df[df['spent'] > df['spent'].mean()]
low_spenders = df[df['spent'] <= df['spent'].mean()]
print("High Spenders:", high_spenders)
print("Low Spenders:", low_spenders)









