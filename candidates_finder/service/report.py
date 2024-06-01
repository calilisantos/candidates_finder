from candidates_finder.configs import logs as logs_confs
from candidates_finder.model.read import Read
from candidates_finder.service.transform import Transform
import logging
from pyspark.sql import SparkSession


class Report:
    def __init__(self) -> None:
        self._logger = logging.getLogger(__name__)
        self._spark = (
            SparkSession.builder
                .appName('candidates_finder')
                    .master('local[*]')
                        .getOrCreate()
        )

    def _configure_logger(self) -> None:
        logging.basicConfig(
            level=logging.INFO,
            format=logs_confs.LOG_FORMAT,
            datefmt=logs_confs.LOG_DATE_FORMAT,
            style=logs_confs.LOG_STYLE
        )

    def run(self) -> None:
        self._configure_logger()
        self._logger.info('Starting the process')
        read = Read()
        self._logger.info('Getting the potential candidates')
        followers = read.get_followers_request()
        self._logger.info('Getting the potential candidates github pages')
        followers_url = read.get_followers_info_list(followers)
        self._logger.info('Getting the potential candidates info')
        followers_info = list(map(read.get_followers_info_request, followers_url))
        self._logger.info('Creating the candidantes report')
        transform = Transform(self._spark, followers_info)
        try:
            transform.run()
            self._logger.info('Report created with success.')
        except Exception as e:
            self._logger.error(f'An error occurred: {e}')
