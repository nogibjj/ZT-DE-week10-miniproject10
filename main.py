from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('YourAppName').getOrCreate()

# Loading dataset
file_path = 'dataset.csv'

# Load the CSV file into a DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Show the first few rows of the DataFrame
# df.show()

# Prints the schema of the DataFrame, which gives the data types and column names
# df.printSchema()

# df.describe().show()
