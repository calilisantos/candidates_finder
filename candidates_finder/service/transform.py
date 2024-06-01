from candidates_finder.configs import transform as transform_confs
from pyspark.sql import DataFrame, functions as F, SparkSession


class Transform:
    def __init__(self, spark: SparkSession, followers_list: list) -> None:
        self._spark = spark
        self._source = followers_list
        self._dataframe = DataFrame

    def _read_followers_list(self) -> None:
        self._dataframe = self._spark.createDataFrame(self._source, transform_confs.SCHEMA)

    def _transform_date_column(self) -> None:
        self._dataframe = self._dataframe.withColumn(
            transform_confs.DATE_COLUMN,
            F.date_format(
                F.col(transform_confs.DATE_COLUMN),
                transform_confs.DATE_FORMAT
            )
        )

    def _transform_company_column(self) -> None:
        self._dataframe = self._dataframe.withColumn(
            "company",
            F.regexp_replace(
                F.col("company"),
                transform_confs.COMPANY_PATTERN_TO_REMOVE,
                ""
            )
        )

    def _save_to_csv(self) -> None:
        self._dataframe.toPandas().to_csv(transform_confs.CSV_FILE, index=False)

    def run(self) -> None:
        self._read_followers_list()
        self._transform_date_column()
        self._transform_company_column()
        self._save_to_csv()
