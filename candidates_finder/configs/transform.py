from pyspark.sql import types as T

COMPANY_PATTERN_TO_REMOVE: str = "@"
CSV_FILE: str = "candidates_report.csv"
DATE_COLUMN: str = "created_at"
DATE_FORMAT: str = "dd/MM/yyyy"
SCHEMA = T.StructType([
    T.StructField("name", T.StringType(), True),
    T.StructField("company", T.StringType(), True),
    T.StructField("blog", T.StringType(), True),
    T.StructField("email", T.StringType(), True),
    T.StructField("bio", T.StringType(), True),
    T.StructField("public_repos", T.IntegerType(), True),
    T.StructField("followers", T.IntegerType(), True),
    T.StructField("following", T.IntegerType(), True),
    T.StructField("created_at", T.StringType(), True)
])
