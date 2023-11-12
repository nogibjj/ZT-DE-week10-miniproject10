from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('YourAppName').getOrCreate()

# Loading dataset
file_path = 'birds.csv'

# Load the CSV file into a DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)

#########################################################################################
# List all column names
# column_names = df.columns
# print(column_names)

# Data Exploration
# df.show()
# df.describe().show()
#########################################################################################

# DATA TRANSFORMATION AND ANALYSIS

# Filtering to get records where the label is "ZEBRA DOVE"
filtered_df = df.filter(df['labels'] == 'ZEBRA DOVE')

# Display the filtered DataFrame
# filtered_df.show()

from pyspark.sql import functions as F

# Grouping by 'labels' and calculating the average 'class id'
aggregated_df = df.groupBy('labels').agg(F.mean('class id').alias('average_class_id'))

# Display the aggregated DataFrame
aggregated_df.show()


# Convert Spark DataFrame to Pandas DataFrame
pandas_df = aggregated_df.toPandas()

# Create Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='labels', y='average_class_id', data=pandas_df)

# Rotate the x labels if they are too cramped
plt.xticks(rotation=45)

# Add title and labels
plt.title('Average Class ID for Each Label')
plt.xlabel('Labels')
plt.ylabel('Average Class ID')

# Show the plot
plt.show()

# Save the plot to a file
plt.savefig('plot.png')

# Register DataFrame as a temporary view
df.createOrReplaceTempView("birds")

# Spark SQL query
result = spark.sql("SELECT labels, COUNT(*) as count FROM birds GROUP BY labels")
result.show()
