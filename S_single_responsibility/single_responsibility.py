from S_single_responsibility.bad.StudentReport import StudentReport
from S_single_responsibility.good.ReportCreator import ReportCreator
from S_single_responsibility.good.ReportSaver import  ReportSaver


def bad_Function_S():
    report = StudentReport("Avi", 95)
    report.save_to_file()


def  good_Function_S():
    creator = ReportCreator()
    text = creator.create("Avi", 95)
    ReportSaver().save(text)

