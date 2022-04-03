import datetime
import sys


class Passenger:
    def passenger_detail(self, passenger_name, passenger_age, passenger_gender, passenger_phone_number):
        self.passenger_name = passenger_name
        self.passenger_age = passenger_age
        self.passenger_gender = passenger_gender
        self.passenger_phone_number = passenger_phone_number

    def bill_detail(self):
        self.file_handle = open("data.txt", "a+")
        print("Passenger name ~ Passenger age ~ Passenger mail ~ package name ~ place name ~ place detail name")
        self.file_handle.write(str(self.passenger_name)+"<-->"+str(self.passenger_age)+"<-->"+str(self.passenger_gender)+"<-->"+str(self.passenger_phone_number)+"<-->"+Tourpackage_obj.package_name+"<-->"+Tourpackage_obj.place_name+"<-->"+Tourpackage_obj.place_description+"\n")
        self.file_handle.flush()

    def addpassengerinfo(self):
        self.file_handle = open("data.txt")
        self.s = ' '
        self.file_handle.seek(0)
        while self.s:
            self.s = self.file_handle.readline()
            print(self.s)
        self.file_handle.close()

    def display_details(self):
        print("Passenger name : ", self.passenger_name)
        print("passenger age : ", self.passenger_age)
        print("Passenger gender : ", self.passenger_gender)
        print("Passenger phone number : ", self.passenger_phone_number)
        print("Passenger tour Package : ", Tourpackage_obj.package_name)
        print(" Tour type and location : ", Tourpackage_obj.place_name, "\n", Tourpackage_obj.place_description)
        print(datetime.datetime.now())


class Tourpackage(Passenger):
    def tourpackage(self, package_name):
        self.package_name = package_name

    def tour_details(self, place_name, place_description):
        self.place_name = place_name
        self.place_description = place_description

if __name__ == '__main__':

    Tourpackage_obj = Tourpackage()

    while True:
        print("*** Tourist management system***")
        print("1. Add Passenger")
        print("2. Choose a tour package")
        print("3. Choose a Place")
        print("4. Display details of an passenger")
        print("5. Update employee information in File")
        print("6. Display details of an employee")
        print("7. exit")

        user_input = input()
        if user_input not in ['1', '2', '3', '4', '5', '6', '7']:
            print("choose a valid option : ")
            continue

        user_input = int(user_input)

        if user_input == 1:
            print("Welcome to Tourism management")
            passenger_name = str(input("passenger name : "))
            passenger_age = int(input("age of passenger : "))
            passenger_gender = str(input("Passenger gender : "))
            passenger_phone_number = int(input("Passenger phone number : "))
            Tourpackage_obj.passenger_detail(passenger_name, passenger_age, passenger_gender, passenger_phone_number)

        elif user_input == 2:
            print("Tourism package detail : ")
            print("1.International \n 2.India \n 3.Karnataka \n 4.Mysore")
            passenger_choice = int(input())
            if passenger_choice == 1:
                package_name = " International "
                Tourpackage_obj.tourpackage(package_name)
            elif passenger_choice == 2:
                package_name = " India "
                Tourpackage_obj.tourpackage(package_name)
            elif passenger_choice == 3:
                package_name = " Karnataka "
                Tourpackage_obj.tourpackage(package_name)
            elif passenger_choice == 4:
                package_name = " Mysore "
                Tourpackage_obj.tourpackage(package_name)
            else:
                print("choose any above package ")

        elif user_input == 3:
            print("choose a place : ")
            if passenger_choice == 1:
                print("1.Maldives\n 2.Germany")
                place_choose = int(input())
                if place_choose == 1:
                    place_name = "Maldives"
                    place_description = "4days 3 Nights  =  28000 "
                    Tourpackage_obj.tour_details(place_name, place_description)
                elif place_choose == 2:
                    place_name = "Germany"
                    place_description = "6 days 5 nights = 38000 "
                    Tourpackage_obj.tour_details(place_name, place_description)
                else:
                    print("choose a valid role")

            elif passenger_choice == 2:
                print("1.Delhi\n2.Jaipur")
                place_choose = int(input())
                if place_choose == 1:
                    place_name = " Delhi"
                    place_description = "3days 2 nights = 20000"
                    Tourpackage_obj.tour_details(place_name, place_description)
                elif place_choose == 2:
                    place_name = "jaipur"
                    place_description = "2 days 1 nights = 18000"
                    Tourpackage_obj.tour_details(place_name, place_description)

                else:
                    print("invalid choice")

            elif passenger_choice == 3:
                print("1.Madikere\n 2.Chickmagalur")
                place_choose = int(input())
                if place_choose == 1:
                    place_name = " Madikeri "
                    place_description = " 2 days 1 night= 4000"
                    Tourpackage_obj.tour_details(place_name, place_description)

                elif place_choose == 2:
                    place_name = " chickmagalur "
                    place_description = " 3 days 2 night= 6000"
                    Tourpackage_obj.tour_details(place_name, place_description)

                else:
                    print("invalid choice")

            elif passenger_choice == 4:
                print("1.Mysorelocal\n 2.Mandyalocal")
                place_choose = int(input())
                if place_choose == 1:
                    place_name = " mysore Local"
                    place_description = "1day 1 night =2000"
                    Tourpackage_obj.tour_details(place_name, place_description)

                elif place_choose == 2:
                    place_name = " mandya Local"
                    place_description = "1day 1 night =1000"
                    Tourpackage_obj.tour_details(place_name, place_description)

        elif user_input == 4:
            print("this is called!!")
            Tourpackage_obj.display_details()

        elif user_input == 5:
            print("details")
            Tourpackage_obj.bill_detail()

        elif user_input == 6:
            print("Passenger Ticket Bill")
            Tourpackage_obj.addpassengerinfo()

        elif user_input == 7:
            sys.exit()
            break
