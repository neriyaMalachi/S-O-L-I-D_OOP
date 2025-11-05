
class ReportSaver:
    def save(self, text):
        with open("./S_single_responsibility/report.txt", "w") as f:
            f.write(text)
        print("Report saved!")

