def add_border(func):
    def wrapper(*args):
        print("==============================")
        func(*args)
        print("==============================")
    return wrapper
class Report:
    def __init__(self, title):
        self.title = title
        self.data = []
    def add(self, text):
        self.data.append(text)
    @add_border
    def show(self):
        print(f"REPORT: {self.title}")
        for item in self.data:
            print("-", item)
    @classmethod
    def create_template(cls, title):
        r = cls(title)
        r.add("Note: Official Document")
        return r
    def __len__(self):
        return len(self.data)
    def __add__(self, other):
        new_report = Report(self.title + " & " + other.title)
        new_report.data = self.data + other.data
        return new_report
if __name__ == "__main__":
    r1 = Report.create_template("Marksheet")
    r1.add("Maths: 90")
    r1.add("Science: 85")
    r1.show()
    print("Total items in r1:", len(r1))
    r2 = Report("Attendance")
    r2.add("Present: 95%")
    merged = r1 + r2
    merged.show()
