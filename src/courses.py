import datetime
import webbrowser
import yagmail


class Course:
    def __init__(self, course_info, course_name):
        self.course_name = course_name
        self.day = course_info["day"]
        self.time_starts = course_info["time"]["time_starts"]
        self.time_ends = course_info["time"]["time_ends"]
        self.course_type = course_info["course_type"]
        self.building = course_info["building"]
        self.zoom_link = course_info["zoom_link"]

    def is_near(self):
        today_info = datetime.datetime.now()
        hour = float(today_info.time().hour)
        today = today_info.strftime("%A")
        if today == self.day:
            # check one hour before class starts
            if hour == float(self.time_starts[:2]) - 1:
                return True

    def send_email(self, sender, recipient, password):
        message = f"""
                <p>Course: {self.course_name} {self.course_type}</p>
                <p>Starts at: {self.time_starts}.00</p>
                <p>Ends at: {self.time_ends}</p>
                <p><a href="{self.zoom_link}">zoom link</a></p>        
                """
        with yagmail.SMTP(sender, password) as yag:
            yag.send(to=recipient, subject="schedule", contents=message)

    def open_zoom(self):
        if self.zoom_link:
            webbrowser.open(self.zoom_link)

    # to be refactored
    def change_course(self, courses):
        add_or_change = input("add or change?: ").lower()
        if add_or_change == "c":
            old_course = input("Old course: ")
            courses.pop(old_course)
        course_name = input("course name: ")
        course_type = input("course type: ")
        day = input("day: ")
        building = input("building: ")
        zoom_link = input("zoom link: ")
        time_starts = input("time starts: ")
        time_ends = input("time ends: ")
        courses[course_name] = [
            {
                "day": day,
                "time": {"time_starts": time_starts, "time_ends": time_ends},
                "course_type": course_type,
                "building": building,
                "zoom_link": zoom_link,
            }
        ]
        return courses
