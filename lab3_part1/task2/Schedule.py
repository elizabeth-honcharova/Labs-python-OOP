class Schedule:

    __schedule = {"Monday": None, "Tuesday": None, "Wednesday": None, "Thursday": None,
                  "Friday": None, "Saturday": None, "Sunday": None}

    @staticmethod
    def update_schedule(day_of_week, dish):
        if day_of_week not in Schedule.__schedule.keys():
            raise ValueError
        Schedule.__schedule[day_of_week] = dish

    @staticmethod
    def get_dish(title):
        if title in Schedule.__schedule.keys():
            return Schedule.__schedule[title]
        else:
            raise ValueError


