class Task:
    def __init__(self,title, subject, priority, status):
        self.title = title
        self.subject = subject
        self.priority = priority
        self.status = status

    def display(self):
        print(
            f"Title: {self.title}\n",
            f"Subject: {self.subject}\n",
            f"Priority: {self.priority}\n",
            f"Status: {self.status}"
        )

    def is_high_priority(self):
        return self.priority.lower() == "high"

    def mark_completed(self):
        self.status = "Completed"

myTask = Task("Complete Project", "Programming", "High", "Pending")
print(myTask.is_high_priority())
myTask.mark_completed()
print(myTask.status)