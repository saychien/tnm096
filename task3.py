# import random
#
#
# class Schedule:
#     def __init__(self):
#         self.classes = {
#             'MT101': None, 'MT102': None, 'MT103': None, 'MT104': None, 'MT105': None,
#             'MT106': None, 'MT107': None, 'MT201': None, 'MT202': None, 'MT203': None,
#             'MT204': None, 'MT205': None, 'MT206': None, 'MT301': None, 'MT302': None,
#             'MT303': None, 'MT304': None, 'MT401': None, 'MT402': None, 'MT403': None,
#             'MT501': None, 'MT502': None
#         }
#         self.classrooms = ['TP51', 'SP34', 'K3']
#         self.times = ['9', '10', '11', '12', '1', '2', '3', '4']
#
#     def is_valid(self, class_name, classroom, time):
#         # check if there is a clash in 1 classroom for 2 classes
#         for c in self.classes:
#             if self.classes[c] == (classroom, time) and c != class_name:
#                 return False
#
#         # check if there are classes sharing the same first digit be scheduled at the same time
#         first_digit = class_name[2]
#         for c in self.classes:
#             if c != class_name and c[2] == first_digit and self.classes[c] is not None and self.classes[c][1] == time:
#                 return False
#         if first_digit == '5' and class_name != 'MT502' and self.classes['MT501'] is not None and self.classes['MT501'][
#             1] == time:
#             return False
#         if first_digit == '5' and class_name != 'MT501' and self.classes['MT502'] is not None and self.classes['MT502'][
#             1] == time:
#             return False
#
#         return True
#
#     def min_conflicts(self, iterations=100):
#         # Generate a complete assignment for all variables (probably with conflicts)
#         assigned_classes = set()
#         for class_name in self.classes:
#             while True:
#                 classroom = random.choice(self.classrooms)
#                 time = random.choice(self.times)
#                 if self.is_valid(class_name, classroom, time) and (classroom, time) not in assigned_classes:
#                     self.classes[class_name] = (classroom, time)
#                     assigned_classes.add((classroom, time))
#                     break
#
#         # minimizing conflicts in iteration
#         for i in range(iterations):
#             most_conflicts = 0
#             most_conflicts_class = None
#             for class_name in self.classes:
#                 conflicts = 0
#                 for classroom in self.classrooms:
#                     for time in self.times:
#                         if not self.is_valid(class_name, classroom, time):
#                             conflicts += 1
#                 if conflicts > most_conflicts:
#                     most_conflicts = conflicts
#                     most_conflicts_class = class_name
#
#             # if there is no conflicts, stop iterating
#             if most_conflicts == 0:
#                 break
#
#             possible_assignments = []
#             for classroom in self.classrooms:
#                 for time in self.times:
#                     if self.is_valid(most_conflicts_class, classroom, time):
#                         possible_assignments.append((classroom, time))
#
#             if possible_assignments:
#                 new_assignment = random.choice(possible_assignments)
#                 self.classes[most_conflicts_class] = new_assignment
#
#     def display(self):
#         print("Time   TP51         SP34         K3")
#         print("---    ---          ---          ---")
#         for time in self.times:
#             print(f"{time:<4}", end="")
#             for classroom in self.classrooms:
#                 for class_name in self.classes:
#                     if self.classes[class_name] == (classroom, time):
#                         print(f" {'':<2}{class_name:<9}", end="")
#                         break
#                 else:
#                     print(f" {'':<11}", end="")
#             print()
#
#
# schedule = Schedule()
# schedule.min_conflicts()
#
# schedule.display()


import random

class Schedule:
    def __init__(self):
        self.classes = {
            'MT101': None, 'MT102': None, 'MT103': None, 'MT104': None, 'MT105': None,
            'MT106': None, 'MT107': None, 'MT201': None, 'MT202': None, 'MT203': None,
            'MT204': None, 'MT205': None, 'MT206': None, 'MT301': None, 'MT302': None,
            'MT303': None, 'MT304': None, 'MT401': None, 'MT402': None, 'MT403': None,
            'MT501': None, 'MT502': None
        }
        self.classrooms = ['TP51', 'SP34', 'K3']
        self.times = ['9', '10', '11', '12', '1', '2', '3', '4']

    def is_valid(self, class_name, classroom, time):
        # check if there is a clash in classroom assignment
        for c in self.classes:
            if self.classes[c] == (classroom, time) and c != class_name:
                return False

        # check if there are classes sharing the same first digit be scheduled at the same time
        first_digit = class_name[2]
        for c in self.classes:
            if c != class_name and c[2] == first_digit and self.classes[c] is not None and self.classes[c][1] == time:
                return False
        if first_digit == '5' and class_name != 'MT502' and self.classes['MT501'] is not None and self.classes['MT501'][
            1] == time:
            return False
        if first_digit == '5' and class_name != 'MT501' and self.classes['MT502'] is not None and self.classes['MT502'][
            1] == time:
            return False

        return True

    def calculate_conflicts(self):
        conflicts = 0
        for class_name1 in self.classes:
            for class_name2 in self.classes:
                if class_name1 != class_name2 and self.classes[class_name1] is not None and self.classes[class_name2] is not None:
                    if self.classes[class_name1] == self.classes[class_name2]:
                        conflicts += 1
                    elif class_name1[2] == class_name2[2] and self.classes[class_name1][1] == self.classes[class_name2][1]:
                        conflicts += 1
        return conflicts

    def min_conflicts(self, iterations=100):
        # Generate an assignment for all variables (probably with conflicts)
        for class_name in self.classes:
            while True:
                classroom = random.choice(self.classrooms)
                time = random.choice(self.times)
                if self.is_valid(class_name, classroom, time):
                    self.classes[class_name] = (classroom, time)
                    break

        # minimizing conflicts in iteration
        best_schedule = self.classes.copy()
        min_conflicts = self.calculate_conflicts()
        for i in range(iterations):
            for class_name in self.classes:
                # Randomly change the assignment of the class
                original_assignment = self.classes[class_name]
                self.classes[class_name] = None  # Temporarily remove the assignment

                possible_assignments = []
                for classroom in self.classrooms:
                    for time in self.times:
                        if self.is_valid(class_name, classroom, time):
                            possible_assignments.append((classroom, time))

                if possible_assignments:
                    new_assignment = random.choice(possible_assignments)
                    self.classes[class_name] = new_assignment

                    # calculate conflicts for the new assignment
                    current_conflicts = self.calculate_conflicts()

                    # if the new assignment has fewer conflicts, update the best schedule
                    if current_conflicts < min_conflicts:
                        min_conflicts = current_conflicts
                        best_schedule = self.classes.copy()

                    # If the new assignment has more or equal conflicts, revert to the original assignment
                    else:
                        self.classes[class_name] = original_assignment

        # Restore the best schedule found
        self.classes = best_schedule

    def display(self):
        print("Time   TP51         SP34         K3")
        print("---    ---          ---          ---")
        for time in self.times:
            print(f"{time:<4}", end="")
            for classroom in self.classrooms:
                for class_name in self.classes:
                    if self.classes[class_name] == (classroom, time):
                        print(f" {'':<2}{class_name:<9}", end="")
                        break
                else:
                    print(f" {'':<11}", end="")
            print()


schedule = Schedule()
schedule.min_conflicts()

schedule.display()