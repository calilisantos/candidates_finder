from candidates_finder.service.report import Report


class Main:
    def __init__(self) -> None:
        self._report = Report()

    def run(self) -> None:
        self._report.run()


if __name__ == '__main__':
    Main().run()
