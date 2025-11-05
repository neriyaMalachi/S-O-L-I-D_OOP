class StudentReport:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def create_report(self):
        return f"{self.name} got {self.grade}"

    def save_to_file(self):  # אחריות שנייה
        with open("./S_single_responsibility/report.txt", "w") as f:
            f.write(self.create_report())
        print("Report saved!")


