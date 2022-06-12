# importing relevant packages
import csv

'''

>>> This is a text-based application to search a location in Keele University Campus.
>>> I have used Tree datastructure to implement this application.
>>> I took some syntax references of Tree DS from the YT video of code-basics 'https://www.youtube.com/c/codebasics'.

'''


class UniversityMap:

    def __init__(self, location):
        self.location = location
        self.subPlaces = []  # list of child nodes
        self.places = None  # parent node indicator
        self.reference = []  # empty list for csv file values

    @property
    def fetch_list(self):  # converts and return the data into a list of dictionary from the csv file
        try:
            with open("Appendix-A.csv", newline="", ) as f:
                d_reader = csv.DictReader(f)
                for item in d_reader:
                    self.reference.append(item)
            return self.reference
        except IndexError:
            print("No values exists!!")

    # function to add a child to their parent node
    def adding_sub_place(self, place):
        place.places = self
        if place not in self.subPlaces:
            self.subPlaces.append(place)

    # function to search into the tree
    def search_in_tree_leaf(self, prompt):
        lst = []
        for value in self.subPlaces:
            for v in value.location:
                if prompt.lower() in v.lower():
                    x = f'{value.location[0]} -> {value.location[1]} -> {value.location[2]}'
                    lst.append(x)
                    continue
        lst = set(lst)

        if len(lst) == 1:
            for v in lst:
                print(f'You are at {v} in Keele University.\n')
        else:
            for v in lst:
                print(v)
            if len(lst) < 1:
                print(f'{len(lst)} result exists!!\n')
            else:
                print(f'{len(lst)} results exists!!\n')
        request = input("Would you like to visit somewhere else? yes/no :- ")
        print("\n")
        while True:
            if request.lower() in {'yes', 'no'}:
                break
            else:
                print("Type the input correctly\n")
            request = input("Would you like to visit somewhere else? yes/no :- ")
            print("\n")
        if request.lower() == "yes":
            map.look_into_building()
        elif request.lower() == "no":
            print("\nVisit Again Soon!!")
            exit()

    # building a hierarchy to find the location
    def look_into_building(self):
        request = input(f"Do you want to enter into the {self.location[0]}? yes/no :- ")  # first level search
        print("\n")
        if request.lower() == "no":
            print("Visit Again Soon!!")
            exit()
        elif request.lower() == "yes":
            if self.subPlaces:
                for area in self.subPlaces:
                    print(f'{area.location[0]}')
                    print(f'{len(area.location[0]) * "-"}')
                print("\n")
                colony = input(f'Which building do you want to enter in {self.location[0]}? ')
                print("\n")
                if colony == "":
                    print("Sorry haven't typing anything!!!\n")
                    self.look_into_building()
                for area in self.subPlaces:  # second level search
                    if colony.lower() in area.location[0].lower() or colony.lower() in area.subPlaces[0].location[0]:
                        permit = input(f'Do you want to enter into {area.location[0]}? yes/no :- ')
                        print("\n")
                        if permit.lower() == "yes":
                            print(f"Your are in {area.location[0]}.\n")
                            if area.subPlaces:
                                for build in area.subPlaces:
                                    print(f'Name:- {build.location[0]} and Reference '
                                          f'Number:- {build.location[1]}')
                                    print(
                                        f'       {len(build.location[0]) * "-"}                        '
                                        f'{len(build.location[1]) * "-"}')
                                choice = input(f'Enter the name/number of the hall in {area.location[0]} :- ')
                                print("\n")
                                area.search_in_tree_leaf(choice)
                                exit()
                        elif permit.lower() == "no":
                            ques = input(f'Do you want to get back to {self.location[0]}? yes/no :- ')
                            print("\n")
                            if ques.lower() == "yes":
                                self.look_into_building()
                            elif ques.lower() == "no":
                                print("Visit Again Soon!!")
                                exit()
                            else:
                                print("Incorrect Response!!\n")
                                exit()
                        else:
                            self.look_into_building()
                else:
                    print("Incorrect input!!\n")
                    self.look_into_building()
        else:
            print("Type options correctly!!\n")
            self.look_into_building()

# connecting the child to their parent nodes


def building_a_map():
    root = UniversityMap(["Keele University Campus"])  # Initializing a root to the tree
    classifiers = []
    reference = root.fetch_list
    for refer in range(len(reference)):
        for j in reference[refer].keys():
            if j == "Classification":
                classifiers.append(reference[refer]["Classification"])
    classifiers = set(classifiers)
    final_classifiers = []
    mapped_classifiers = []

    for ele in classifiers:
        final_classifiers.append(ele)
        mapped_classifiers.append(UniversityMap([ele]))

    for refer in range(len(reference)):  # making a list for the leaf node

        for j in reference[refer].keys():
            for k in range(len(final_classifiers)):
                if final_classifiers[k] == reference[refer]["Classification"] and j == "Name":
                    mapped_classifiers[k].adding_sub_place(
                        UniversityMap([reference[refer]["Name"], reference[refer]["Reference"],
                                       reference[refer]["Classification"]]))

    for classify in mapped_classifiers:
        root.adding_sub_place(classify)

    return root


if __name__ == '__main__':
    map = building_a_map()
    print("Welcome to the Keele university!!!\n")
    map.look_into_building()  # calling the program here
