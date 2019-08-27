import csv
#importing csv file as its roles and colums
places_file = open('places.csv', 'r')
places_list_n = places_file.readlines()
places_list = [i.replace("\n", '') for i in places_list_n]
places_file.close()
#creating a list to put the places
individual_places_list = []
for i in range(len(places_list)):
    individual_places_list.append(places_list[i].split(','))


def main():
    print("Travel Tracker")
    main_menu()
    exit("User quit program")

#asking user inputs
def main_menu():
    print("Menu: ")
    print("L - List places")
    print("A - Add places")
    print("M - Mark new place as visited")
    print("Q - Quit")
    print("")
    menu_choice_l = input(">>>")
    print("")
    choices = ["l", "a", "m", "q"]
    menu_choice = menu_choice_l.lower()
#checking input errors
    while menu_choice not in choices:
        print("Invalid menu choice.")
        print("")
        menu_choice_l = input(">>>")
        print("")
        menu_choice = menu_choice_l.lower()
#calling functions as the user inputs
    while menu_choice != "q":
        if menu_choice == "l":
            print_places()
            main_menu()
        if menu_choice == "a":
            add_menu()
            main_menu()
        if menu_choice == "m":
            mark_menu()
            main_menu()
#add the places into csv file
    write_file = open('places.csv', 'w')
    for j in range(len(individual_places_list)):
        for i in range(4):
            write_file.write(str(individual_places_list[j][i]) + ",")

        write_file.write("\n")
    write_file.close()
    print("{} places saved to {}".format(len(individual_places_list), 'places.csv'))
    exit("")

#listing out the places visited
def print_places():
    to_visit_count = 0
    for i in range(len(individual_places_list)):
        if individual_places_list[i][3] == "n":
            to_visit_count += 1
            print("*{}. {:<8} in {:<11} priority {}.".format(i + 1, individual_places_list[i][0],
                                                             individual_places_list[i][1],
                                                             individual_places_list[i][2]))
        else:
            print(" {}. {:<8} in {:<11} priority {}.".format(i + 1, individual_places_list[i][0],
                                                             individual_places_list[i][1],
                                                             individual_places_list[i][2]))
    print("")
    if to_visit_count > 0:
        print(" {} places. You still want to visit {} places.".format(len(individual_places_list), to_visit_count))
    else:
        print(" {} places. No places left to visit. Why not add some more?".format(len(individual_places_list)))
    print("")

#function to add new places
def add_menu():
    new_name = input("Name: ")
    while new_name == "":
        print("Input cannot be blank.")
        new_name = input("Name: ")
    new_country = input("Country: ")
    while new_country == "":
        print("Input cannot be blank.")
        new_country = input("Country: ")
    new_priority = ask_priority("Please input a priority: ")
    print("{} in {} (priority {}) added to Travel Tracker".format(new_name, new_country, new_priority))
    print("")
    new_place = [new_name, new_country, new_priority, "n"]
    individual_places_list.append(new_place)

#function for asking priority and catching invalid inputs
def ask_priority(message):
    valid = False
    while not valid:
        try:
            number = int(input(message))
            while number <= 0:
                print("Number must be more than 0.")
                number = int(input(message))
                valid = True
            valid = True
        except ValueError:
            print("Invalid input, please enter a valid number.")
    return number

#function to mark the places as visited
def mark_menu():
    print_places()
    non_visited_count = 0
    for i in range(len(individual_places_list)):
        if individual_places_list[i][3] == "n":
            non_visited_count += 1
    if non_visited_count == 0:
        print("No unvisited places.")
        print("")
        main_menu()
    print("Enter the number of the place to mark as visited.")
    ask_number = ask_priority(">>>")
    mark_number = ask_number - 1
    while mark_number > len(individual_places_list):
        print("There aren't that many places.")
        print("Enter the number of the place to mark as visited.")
        ask_number = ask_priority(">>>")
        mark_number = ask_number - 1
    while individual_places_list[mark_number][3] == "v":
        print("You have already visited that place.")
        print("Enter the number of the place to mark as visited.")
        ask_number = ask_priority(">>>")
        mark_number = ask_number - 1
    else:
        individual_places_list[mark_number][3] = "v"
        print(
            "{} in {} visited.".format(individual_places_list[mark_number][0], individual_places_list[mark_number][1]))
        print("")


if __name__ == '__main__':
    main()