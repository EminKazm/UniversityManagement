from bus import Bus
from Equipment.classroom import Classroom
from department import Department
from Equipment.lab import Lab
from yard import Yard
from Hostel.boyshostel import BoysHostel
from Hostel.girlshostel import GirlsHostel
from Student.masters import MasterStudent
from Student.bachelor import Bachelor
from noticeboard import NewsBoard
from auditorium import Auditorium
from parking import Park
from university import UniversityManagement
from Staff.library import Library
from Staff.teacher import Teacher
from Equipment.labequipments import LabEquipments
from Equipment.classequipments import ClassEquipments
from Staff.canteen import Canteen
from Staff.seller import Seller
from Staff.librarian import Librarian
from Staff.doorkeeper import DoorKeeper

print("---------------------------------------University------------------------------------------")
print(UniversityManagement.__doc__)
khazar = UniversityManagement("Khazar", "NEFTCHILER", 12, 1000, True, "literature", 15, 1320, 414, 4, 30, False)
print(khazar.uniDetails())
khazar.isOpen()
ada_uni = UniversityManagement("ADA", "GENCLIK", 55, 1000, False, "IT department", 16, 1200, 202, 2, 30, False)

print(ada_uni.uniDetails())
ada_uni.isOpen()
print("---------------------------------------Bus------------------------------------------")
bus136 = Bus(136, "Ilqar", 25, False)
print(Bus.__doc__)
print(bus136.busDetails())
bus136.seatsavailability()
print("---------------------------------------Classroom------------------------------------------")
print(Classroom.__doc__)
n = Classroom("402N", 4, 30, True)
print(f"class id:{n.class_id},class is in floor{n.floor}num of students:{n.count_student}")
n.isFull()
print("---------------------------------------Department------------------------------------------")
it_depart = Department("IT department", 30, 300)
print(Department.__doc__)
it_depart.depart_Details()
print("---------------------------------------lAB------------------------------------------")
print(Lab.__doc__)

computer_lab = Lab("10", "Computer Lab", 30, True, 30, "15", "computer", 30, "3000", False)
print(computer_lab.infoLab())
print(computer_lab.lab_equips.repair())
computer_lab.fullLab()
print("---------------------------------------Yard------------------------------------------")
print(Yard.__doc__)
khazar_yard = Yard(150, 150)
leng = khazar_yard.getlength()
w = khazar_yard.getweight()
print(f"weight of area:{w} metr")
print(f"length of area :{leng} metr")
print(f"area of yard:{khazar_yard.area()} metr")
print("---------------------------------------Hostel------------------------------------------")
print(BoysHostel.__doc__)
tural = BoysHostel("Tural", 102, 23)
tural.max_students_capacity()
print(tural.infoStudents())
print(GirlsHostel.__doc__)
sara = GirlsHostel("Sara", 100, 21)
sara.max_student_capacity()
print(sara.infoStudents())
print("---------------------------------------Student------------------------------------------")
print(MasterStudent.__doc__)
m = MasterStudent("Ali", "Male", 22)
m.infoStudent()
m.ageofstudents()
print(Bachelor.__doc__)
b = Bachelor("Tural", "Male", 18)
b.infoStudent()
b.ageofstudents()
print("---------------------------------------NewsBoard------------------------------------------")
print(NewsBoard.__doc__)
print("Latest news:")
news = NewsBoard()
news.addnews("-Khazar University will Host Eurasian Nanotechnology Conference ")
news.addnews("-Zoom Webinar will be held")
news.addnews("-Full Scholarship for Postgraduate Female Students")

print(news.display())
print("---------------------------------------Auditorium------------------------------------------")
print(Auditorium.__doc__)
main_auidorium = Auditorium("Mermer Hall", 60)
main_auidorium.addEvents("There will be meeting with new students in the  \"Mermer Hall")
print(main_auidorium.infoAuditorium())
print("Latest events:")
print(main_auidorium.booksEvents())
print("---------------------------------------Parking-------------------------------------------")
print(Park.__doc__)
bmw = Park("BMW", "Ali", 23)
print(bmw.detailsVehicle())
print("---------------------------------------Library-------------------------------------------")
print(Library.__doc__)
khz_lib = Library("01", ["1984", "Animal Farm", "The Great Gatsby"])
print(khz_lib.infoLibrary())
khz_lib.searchbooks()
khz_lib.lendbooks("1984")
khz_lib.returnbook("Frankenstein")
khz_lib.searchbooks()
print("---------------------------------------Staff-------------------------------------------")
print(Teacher.__doc__)
t1 = Teacher('Elvin', 25, 12000, 200)
print(t1.staffDetails(), "Total salary of teacher:", t1.total_salary())
print(Seller.__doc__)
Nargiz = Seller("101", "Nargiz", 42, 6000, 100)
print("Seller id:", Nargiz.get_id(), Nargiz.staffDetails(), "Total salary of Seller:", Nargiz.total_salary())
print(Librarian.__doc__)
Ilgar = Librarian("03", "Ilgar", 43, 6000, 100)
print("Librarian id:", Ilgar.get_id(), Ilgar.staffDetails(), "Total salary of Librarian:", Ilgar.total_salary())
print(DoorKeeper.__doc__)
Akif = DoorKeeper("Akif", 45, 6000, 100)
print(Akif.staffDetails(), "Total salary of Doorkeeper:", Ilgar.total_salary())
print("---------------------------------------Canteen-------------------------------------------")
print(Canteen.__doc__)
kzr_canteen = Canteen(["pizza", "cofe", "cola 0.5ml", "burger"], ["40", "40", "20", "24"],
                      ["1 azn", "0.3 azn", "1 azn", "1.2 azn"])

print(kzr_canteen.display())
print(kzr_canteen.available_items())

print("---------------------------------------Equipments-------------------------------------------")
print(LabEquipments.__doc__)

print(ClassEquipments.__doc__)
class1 = ClassEquipments("2", 12, False, 30, 60, 4)
print(class1.infoEquipment(), "table count", class1.table, "chair count:", class1.chair, "board count:", class1.board)
class1.repair()
