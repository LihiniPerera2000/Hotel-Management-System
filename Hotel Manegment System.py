from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import time


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1528x792+0+0")
        self.root.config(bg="black")
        self.root.resizable(False, False)

# Main Frame window===================================================================================================
        self.login_frame = Frame(self.root, bg="White", bd=13, relief=RIDGE)
        self.login_frame.place(x=480, y=180, width=500, height=400)
        self.label = Label(self.root, text="..WELCOME TO HOTEL SUNSET LODGE..", font=("Monaco", 36, "bold"), bg="black", fg="white")
        self.label.place(x=280, y=12)

# Title & subtitle
        self.title = Label(self.login_frame, text="Login Here", font=("Goudy old style", 24, "bold"), bg="white")
        self.title.place(x=150, y=20)
        self.title = Label(self.login_frame, text="Hotel Sunset lodge staff only.", font=("Goudy old style", 14, "bold"), bg="white")
        self.title.place(x=50, y=65)
# User name
        self.username = Label(self.login_frame, text="User Name", font=("Goudy old style", 16, "bold"), bg="white")
        self.username.place(x=50, y=100)
        self.username_entry = Entry(self.login_frame, font=("Times new roman", 14), bg="light grey")
        self.username_entry.place(x=50, y=140, width=350, height=35)
# Password
        self.password = Label(self.login_frame, text="Password", font=("Goudy old style", 16, "bold"), bg="white")
        self.password.place(x=50, y=190)
        self.password_entry = Entry(self.login_frame, font=("Times new roman", 14), bg="light grey")
        self.password_entry.place(x=50, y=230, width=350, height=35)

# Login Button
        self.button = Button(self.login_frame, text="LOGIN", font=("Goudy old style", 16, "bold"), bd=6, fg="Black", bg="Red", command=self.chek)
        self.button.place(x=180, y=300, width=140, height=40)

    def chek(self):
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error!", "Filling all data before login.", parent=self.root)
        elif self.username_entry.get() != "user_sunset" or self.password_entry.get() != "sunset@123":
            messagebox.showerror("Error!", "Your Username or Password is Invalid.", parent=self.root)
        else:
            messagebox.showinfo("Welcome to our services.", f"welcome {self.username_entry.get()}") and self.login_frame.destroy()


# selection window=====================================================================================================
            self.login_frame2 = Frame(self.root, bg="White", bd=13, relief=RIDGE)
            self.login_frame2.place(x=480, y=180, width=500, height=400)
# Title
            self.title = Label(self.login_frame2, text="WELCOME", font=("Times new roman", 24, "bold"), bg="white", fg="dark blue")
            self.title.place(x=160, y=25)
# subtitle
            self.title = Label(self.login_frame2, text="EXCLUSIVE ACCESS", font=("Monaco", 24, "bold"), bg="white", fg="black")
            self.title.place(x=90, y=100)
            self.title = Label(self.login_frame2, text="TO", font=("Monaco", 24, "bold"), bg="white", fg="black")
            self.title.place(x=210, y=140)
            self.title = Label(self.login_frame2, text="UNIQUE EXPERIENCES.", font=("Monaco", 24, "bold"), bg="white", fg="black")
            self.title.place(x=70, y=180)
# Booking Button
            self.button1 = Button(self.login_frame2, text="BOOKING", font=("Times new roman", 18, "bold"), fg="black", bg="red", bd=6, command=self.openbooking)
            self.button1.place(x=40, y=280, width=160, height=50)
# Dining Button
            self.button2 = Button(self.login_frame2, text="DETAILS", font=("Times new roman", 18, "bold"), fg="white", bg="dark blue", bd=6, command=self.opendetails)
            self.button2.place(x=290, y=280, width=160, height=50)


# Booking Window=======================================================================================================
    def openbooking(self):
        self.login_frame2.destroy()
        self.booking_frame3 = Frame(self.root, bg="White", bd=13, relief=RIDGE)
        self.booking_frame3.place(x=220, y=80, width=1100, height=650)
# Title & subtitles
        self.title = Label(self.booking_frame3, text="BOOKING", font=("Goudy old style", 24, "bold", "underline"), bg="white")
        self.title.place(x=450, y=30)
        self.subtitle = Label(self.booking_frame3, text="We have different types of packages to suit your needs.", font=("Goudy old style", 16, "bold"), bg="white")
        self.subtitle.place(x=70, y=85)
# Luxury Suite
        self.luxury = Label(self.booking_frame3, text="A. Luxury Suite ============================================", font=("Goudy old style", 20, "bold"), bg="white")
        self.luxury.place(x=70, y=130)

        self.luxury = Label(self.booking_frame3, text="   Breakfast, lunch & dinner included.", font=("Goudy old style", 13, "bold"), bg="white")
        self.luxury.place(x=130, y=160)
        self.luxury = Label(self.booking_frame3, text="   Single/Double/Family ", font=("Goudy old style", 13, "bold"), bg="white")
        self.luxury.place(x=130, y=180)
        self.luxury = Label(self.booking_frame3, text="   Price For 1 night :", font=("Goudy old style", 13, "bold"), bg="white")
        self.luxury.place(x=130, y=200)
        self.luxury = Label(self.booking_frame3, text="   LKR 23,000 - 29,000", font=("Goudy old style", 13, "bold"), fg="red", bg="white")
        self.luxury.place(x=130, y=220)
        self.luxury = Label(self.booking_frame3, text="   +LKR 15% taxes & charges. ", font=("Goudy old style", 13, "bold"), bg="white")
        self.luxury.place(x=130, y=240)
# Button
        self.luxury = Button(self.booking_frame3, text="Reserve", font=("Times new roman", 18, "bold"), fg="white", bg="dark blue", bd=4, command=self.opendetail_lux)
        self.luxury.place(x=870, y=160, width=110, height=38)

# Delux Suite
        self.delux = Label(self.booking_frame3, text="B. Delux Suite =============================================", font=("Goudy old style", 20, "bold"), bg="white")
        self.delux.place(x=70, y=270)

        self.delux = Label(self.booking_frame3, text="   Breakfast, lunch & dinner included", font=("Goudy old style", 13, "bold"), bg="white")
        self.delux.place(x=130, y=300)
        self.delux = Label(self.booking_frame3, text="   Single/Double/Family", font=("Goudy old style", 13, "bold"), bg="white")
        self.delux.place(x=130, y=320)
        self.delux = Label(self.booking_frame3, text="   Price For 1 night: ", font=("Goudy old style", 13, "bold"), bg="white")
        self.delux.place(x=130, y=340)
        self.delux = Label(self.booking_frame3, text="   LKR 16,000 - 21,000 ", font=("Goudy old style", 13, "bold"), fg="red", bg="white")
        self.delux.place(x=130, y=360)
        self.delux = Label(self.booking_frame3, text="   +LKR 10% taxes & charges. ", font=("Goudy old style", 13, "bold"), bg="white")
        self.delux.place(x=130, y=380)
# Button
        self.delux = Button(self.booking_frame3, text="Reserve", font=("Times new roman", 18, "bold"), fg="white", bg="dark blue", bd=4, command=self.opendetail_delux)
        self.delux.place(x=870, y=300, width=110, height=38)

# Premier suite
        self.premier = Label(self.booking_frame3, text="C. Premier Suite ===========================================", font=("Goudy old style", 20, "bold"), bg="white")
        self.premier.place(x=70, y=410)
        self.luxury = Label(self.booking_frame3, text="   Breakfast, lunch & dinner included", font=("Goudy old style", 13, "bold"), bg="white")
        self.luxury.place(x=130, y=440)
        self.luxury = Label(self.booking_frame3, text="   Single/Double/Family", font=("Goudy old style", 13, "bold"), bg="white")
        self.luxury.place(x=130, y=460)
        self.luxury = Label(self.booking_frame3, text="   Price For 1 night: ", font=("Goudy old style", 13, "bold"), bg="white")
        self.luxury.place(x=130, y=480)
        self.luxury = Label(self.booking_frame3, text="   LKR 8,000 - 14,000 ", font=("Goudy old style", 13, "bold"), fg="red", bg="white")
        self.luxury.place(x=130, y=500)
        self.luxury = Label(self.booking_frame3, text="   +LKR 5% taxes & charges. ", font=("Goudy old style", 13, "bold"), bg="white")
        self.luxury.place(x=130, y=520)
# Button
        self.premier = Button(self.booking_frame3, text="Reserve", font=("Times new roman", 18, "bold"), fg="white", bg="dark blue", bd=4, command=self.opendetail_premier)
        self.premier.place(x=870, y=440, width=110, height=38)

# Back Button
        self.back = Button(self.booking_frame3, text="DETAILS", font=("Times new roman", 16, "bold"), fg="black", bg="red", bd=4, command=self.opendetails)
        self.back.place(x=70, y=560, width=120, height=40)

# Exit Button
        self.back = Button(self.booking_frame3, text="EXIT", font=("Times new roman", 16, "bold"), fg="white", bg="black", bd=4, command=self.exit_programme)
        self.back.place(x=870, y=560, width=120, height=40)


# Exit function=====================================================================================================
    def exit_programme(self):
        Exit = messagebox.askyesno("Hotel Management System", "Confirm if you want to exit.")
        if Exit > 0:
            self.root.destroy()
        return


# Total cost luxury suite==============================================================================================


    def Total_Date_lux(self):
        self.indate = self.in_date_entry.get()
        self.outdate = self.out_date_entry.get()
        self.indate = datetime.strptime(self.indate, "%d/%m/%y")
        self.outdate = datetime.strptime(self.outdate, "%d/%m/%y")
        self.Total_days.set(abs((self.outdate-self.indate).days))


        if (self.combo2.get()=="Single"):
            price1 = float(21000)
            days = float(self.Total_days.get())
            total =float(price1 * days)
            tax = "Rs" + str("%.2f" % ((total)*15/100))
            sub_tol = "Rs" + str("%.2f" % (total))
            Tol_cost = "Rs" + str("%.2f" % (total + ((total)*15/100)))
            self.paid_tax.set(tax)
            self.sub_total .set(sub_tol)
            self.total_cost.set(Tol_cost)

        elif (self.combo2.get()=="Double"):
            price1 = float(23000)
            days = float(self.Total_days.get())
            total = float(price1 * days)
            tax = "Rs" + str("%.2f" % ((total) * 15/100))
            sub_tol = "Rs" + str("%.2f" % (total))
            Tol_cost = "Rs" + str("%.2f" % (total + ((total) * 15/100)))
            self.paid_tax.set(tax)
            self.sub_total.set(sub_tol)
            self.total_cost.set(Tol_cost)

        elif (self.combo2.get()=="Family"):
            price1 = float(25000)
            days = float(self.Total_days.get())
            total = float(price1 * days)
            tax = "Rs" + str("%.2f" % ((total) * 15/100))
            sub_tol = "Rs" + str("%.2f" % (total))
            Tol_cost = "Rs" + str("%.2f" % (total + ((total) * 15/100)))
            self.paid_tax.set(tax)
            self.sub_total.set(sub_tol)
            self.total_cost.set(Tol_cost)


# Save customers details to the text file===========================================================================
    def save_info_Luxury(self):
        number_info = self.number_entry.get()
        name_info = self.name_entry.get()
        address_info = self.address_entry.get()
        tel_no_info = self.tel_no_entry.get()
        id_type_info = self.combo.get()
        id_no_info = self.id_no_entry.get()
        check_in_info = self.in_date_entry.get()
        chek_out_info = self.out_date_entry.get()
        room_type_info = self.combo2.get()
        room_floor_info = self.floor_combo.get()
        adults_info = self.combo3.get()
        child_info = self.combo4.get()

        room_no_info = self.comboRN.get()
        no_of_days_info = self.noof_days_entry.get()
        paid_tax_info = self.paid_tax.get()
        sub_tol_info = self.sub_tol_entry.get()
        tol_cost_info = self.tol_cost_entry.get()

        print(number_info, name_info, address_info, tel_no_info, id_type_info, id_no_info, check_in_info, chek_out_info, room_type_info, room_floor_info,
              adults_info, child_info, room_no_info, no_of_days_info, paid_tax_info, sub_tol_info, tol_cost_info)

        customer_details = open("Luxury Customers details.txt", "a")
        customer_details.write("Ref Number: " + number_info)
        customer_details.write("\n""Name: " + name_info)
        customer_details.write("\n""Address: " + address_info)
        customer_details.write("\n""Contact No: " + str(tel_no_info))
        customer_details.write("\n""Type of ID: " + id_type_info)
        customer_details.write("\n""Id Number: " + id_no_info)
        customer_details.write("\n""Chek In Date: " + check_in_info)
        customer_details.write("\n""Check Out Date: " + chek_out_info)
        customer_details.write("\n""Room type: " + room_type_info)
        customer_details.write("\n""Room Floor: " + room_floor_info)
        customer_details.write("\n""Adults: " + str(adults_info))
        customer_details.write("\n""Children: " + str(child_info))
        customer_details.write("\n""Room No: " + str(room_no_info))
        customer_details.write("\n""No Of Days: " + no_of_days_info)
        customer_details.write("\n""***")

        customer_details.write("\n""Paid Tax: " + str(paid_tax_info))
        customer_details.write("\n""Sub Total: " + str(sub_tol_info))
        customer_details.write("\n""Total Cost: " + str(tol_cost_info))
        customer_details.write("\n")
        customer_details.write("\n")

        customer_details.close()


# luxury customer Details window...............................................................................................

    def opendetail_lux(self):
        self.booking_frame3.destroy()
        self.detail_frame5 = Frame(self.root, bg="White", bd=13, relief=RIDGE)
        self.detail_frame5.place(x=220, y=80, width=1100, height=650)

# Receipt==================================================================================

        self.receipt_lux = Frame(self.detail_frame5, bg="light grey", bd=10, relief=RIDGE)
        self.receipt_lux.place(x=340, y=200, width=300, height=340)
# Receipt title
        self.title = Label(self.receipt_lux, text="TOTAL COST", font=("Times new roman", 16, "bold", "underline"), fg="black", bg="light grey")
        self.title.place(x=70, y=8)
# Room Number
        self.room_no = Label(self.receipt_lux, text="Room no", font=("Goudy old style", 12, "bold"), bg="light grey")
        self.room_no.place(x=140, y=45)
        self.comboRN = IntVar
        self.comboRN = ttk.Combobox(self.receipt_lux, textvariable=self.comboRN, font=("Times new roman", 12), width=4, height=30)
        self.comboRN.place(x=210, y=45)
        self.comboRN['values'] = ("*Single*", 101, 102, 103, "*Double*", 115, 116, 117, "*Family*", 120, 121, 122)
# Number of days
        self.noof_days = Label(self.receipt_lux, text="No Of Days : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.noof_days.place(x=10, y=90)
        self.noof_days_entry = StringVar
        self.Total_days = StringVar()
        self.noof_days_entry = Entry(self.receipt_lux, textvariable=self.Total_days, font=("Times new roman", 12), bg="dark grey", bd=2)
        self.noof_days_entry.place(x=110, y=90, width=150, height=30)
# paid Tax
        self.tax = Label(self.receipt_lux, text="Paid Tax : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.tax.place(x=10, y=130)
        self.tax_entry = IntVar
        self.paid_tax = StringVar()
        self.tax_entry = Entry(self.receipt_lux, textvariable=self.paid_tax, font=("Times new roman", 12), bg="dark grey", bd=2)
        self.tax_entry.place(x=110, y=130, width=150, height=30)
# sub total
        self.sub_tol = Label(self.receipt_lux, text="Sub Total : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.sub_tol.place(x=10, y=170)
        self.sub_tol_entry = IntVar
        self.sub_total = StringVar()
        self.sub_tol_entry = Entry(self.receipt_lux, textvariable=self.sub_total , font=("Times new roman", 12), bg="dark grey", bd=2)
        self.sub_tol_entry.place(x=110, y=170, width=150, height=30)
# Total Cost
        self.tol_cost = Label(self.receipt_lux, text="Total Cost : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.tol_cost.place(x=10, y=210)
        self.tol_cost_entry = IntVar
        self.total_cost = StringVar()
        self.tol_cost_entry = Entry(self.receipt_lux, textvariable=self.total_cost, font=("Times new roman", 12), bg="dark grey", bd=2)
        self.tol_cost_entry.place(x=110, y=210, width=150, height=30)

# Total button
        self.total_but = Button(self.receipt_lux, text="TOTAL", font=("Times new roman", 14, "bold"), fg="black", bg="dark grey", bd=4, command=self.Total_Date_lux)
        self.total_but.place(x=20, y=270, width=100, height=30)

# Receipt button
        self.total_but = Button(self.receipt_lux, text="RECEIPT", font=("Times new roman", 14, "bold"), fg="black", bg="dark grey", bd=4, command=self.Receipt)
        self.total_but.place(x=160, y=270, width=100, height=30)


# Title & Subtitle=====================================================================================================
        self.title = Label(self.detail_frame5, text="Luxury Suite", font=("monaco", 24, "bold"), fg="black", bg="white")
        self.title.place(x=50, y=20)
        self.subtitle = Label(self.detail_frame5, text="Enter customer details here.", font=("Goudy old style", 14, "bold"), bg="white")
        self.subtitle.place(x=50, y=75)
# Date
        self.Date1 = StringVar()
        self.Date1.set(time.strftime("%d/%m/%y"))
        self.lbl_Date = Label(self.detail_frame5, textvariable=self.Date1, font=("monaco", 12, "bold"), pady=9, bg="white", fg="black")
        self.lbl_Date.place(x=560, y=15)
# Customer Number
        self.number = Label(self.detail_frame5, text="Customer Ref : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.number.place(x=375, y=70)
        self.number_entry = StringVar
        self.number_entry = Entry(self.detail_frame5, textvariable=self.number_entry, font=("Times new roman", 14), bg="white", bd=1)
        self.number_entry.place(x=500, y=70, width=100, height=30)
# Customer Name
        self.name = Label(self.detail_frame5, text="Name : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.name.place(x=50, y=120)
        self.name_entry = StringVar
        self.name_entry = Entry(self.detail_frame5, textvariable=self.name_entry, font=("Times new roman", 14), bg="white", bd=1)
        self.name_entry.place(x=200, y=120, width=400, height=30)
# customer Address
        self.address = Label(self.detail_frame5, text="Address : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.address.place(x=50, y=160)
        self.address_entry = StringVar
        self.address_entry = Entry(self.detail_frame5, textvariable=self.address_entry, font=("Times new roman", 14), bg="white", bd=1)
        self.address_entry.place(x=200, y=160, width=400, height=30)
# customer Contact Number
        self.tel_no = Label(self.detail_frame5, text="Contact No : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.tel_no.place(x=50, y=200)
        self.tel_no_entry = IntVar
        self.tel_no_entry = Entry(self.detail_frame5, textvariable=self.tel_no_entry, font=("Times new roman", 14), bg="white", bd=1)
        self.tel_no_entry.place(x=200, y=200, width=130, height=30)
# Nationality
        self.Nationality = Label(self.detail_frame5, text="Type of ID : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.Nationality.place(x=50, y=240)
        self.combo = StringVar
        self.combo= ttk.Combobox(self.detail_frame5, textvariable=self.combo, font=("Times new roman", 14), width=12, height=30)
        self.combo.place(x=200, y=240,)
        self.combo['values'] = ("National ID", "Driving Licence", "Passport")
# customer Id Number
        self.id_no = Label(self.detail_frame5, text="Id No : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.id_no.place(x=50, y=280)
        self.id_no_entry = StringVar
        self.id_no_entry = Entry(self.detail_frame5, textvariable=self.id_no_entry, font=("Times new roman", 14), bg="white", bd=1)
        self.id_no_entry.place(x=200, y=280, width=130, height=30)
# chek in date
        self.in_date = Label(self.detail_frame5, text="Chek in date : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.in_date.place(x=50, y=320)
        self.in_date_entry = StringVar()
        self.in_date_entry= Entry(self.detail_frame5, textvariable=self.Date1, font=("Times new roman", 14), bg="white", bd=1)
        self.in_date_entry.place(x=200, y=320, width=130, height=30)
# chek out date
        self.out_date = Label(self.detail_frame5, text="Chek out date : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.out_date.place(x=50, y=360)
        self.out_date_entry = StringVar()
        self.out_date_entry = Entry(self.detail_frame5, textvariable=self.out_date_entry, font=("Times new roman", 14), bg="white", bd=1)
        self.out_date_entry.place(x=200, y=360, width=130, height=30)
# Room Type
        self.room_type = Label(self.detail_frame5, text="Room Type : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.room_type.place(x=50, y=400)
        self.combo2 = StringVar()
        self.combo2 = ttk.Combobox(self.detail_frame5, textvariable=self.combo2, font=("Times new roman", 14), width=12, height=30)
        self.combo2.place(x=200, y=400, )
        self.combo2['values'] = ("Single", "Double", "Family")
# Room Floor
        self.no_of_days = Label(self.detail_frame5, text="Room Floor : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.no_of_days.place(x=50, y=440)
        self.floor_combo = StringVar
        self.floor_combo = ttk.Combobox(self.detail_frame5, textvariable=self.floor_combo, font=("Times new roman", 14), width=12, height=30)
        self.floor_combo.place(x=200, y=440)
        self.floor_combo["values"] = ("","1st Floor", "2nd Floor", "3rd Floor")
# How many Adults
        self.adults = Label(self.detail_frame5, text="Adults : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.adults.place(x=70, y=480)
        self.combo3 = IntVar
        self.combo3 = ttk.Combobox(self.detail_frame5, textvariable=self.combo3, font=("Times new roman", 11), width=3, height=30)
        self.combo3.place(x=70, y=510, )
        self.combo3['values'] = (0, 1, 2, 3, 4, 5, "(max)")
# How many children
        self.child = Label(self.detail_frame5, text="Children : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.child.place(x=160, y=480)
        self.combo4 = IntVar
        self.combo4 = ttk.Combobox(self.detail_frame5, textvariable=self.combo4, font=("Times new roman", 11), width=3, height=30)
        self.combo4.place(x=175, y=510, )
        self.combo4['values'] = (0, 1, 2, 3, 4, 5, "(max)")


# Back button (back to open booking frame)
        self.back = Button(self.detail_frame5, text="BACK", font=("Times new roman", 16, "bold"), fg="black", bg="red", bd=4, command=self.openbooking)
        self.back.place(x=50, y=560, width=100, height=40)

# Save Button Save in text File
        self.save = Button(self.detail_frame5, text="SAVE", font=("Times new roman", 16, "bold"), fg="black", bg="green", bd=4, command=self.save_info_Luxury)
        self.save.place(x=300, y=560, width=100, height=40)

# Exit Button
        self.exit = Button(self.detail_frame5, text="EXIT", font=("Times new roman", 16, "bold"), fg="white", bg="black", bd=4, command=self.exit_programme)
        self.exit.place(x=550, y=560, width=100, height=40)

# Receipt==========================================================================================================
    def Receipt(self):
        self.txtreceiptlux = Text(self.detail_frame5, font=("monaco", 12))
        self.txtreceiptlux.place(x=680, y=0, width=400, height=625)
        self.txtreceiptlux.insert(END, "\n""  Date " + self.Date1.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t      SUNSET LODGE" "\n")
        self.txtreceiptlux.insert(END, "       No21, De Cross Road, Negombo." "\n")
        self.txtreceiptlux.insert(END, "\t     TP : +942229456" "\n""\n")
        self.txtreceiptlux.insert(END, "\t     ****************" "\n")
        self.txtreceiptlux.insert(END, "  Cashier : User" "\n""\n")
        self.txtreceiptlux.insert(END, "  Name         : " + self.name_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "  Contact No   : " + self.tel_no_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "  Chek in Date : " + self.in_date_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "  Chek out Date: " + self.out_date_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t    *****************" "\n""\n")
        self.txtreceiptlux.insert(END, "\t      Paid tax   : " + self.tax_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t      Sub Total  : " + self.sub_total.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t      Total Cost : " + self.tol_cost_entry.get() + "\n""\n""\n")
        self.txtreceiptlux.insert(END, "     We hope you are satisfied with  " "\n")
        self.txtreceiptlux.insert(END, "\t    our services.." "\n""\n")
        self.txtreceiptlux.insert(END, "\t  THANK YOU COME AGAIN..!" "\n""\n")



# Total cost Delux suite ==============================================================================================

    def Total_Date_delux(self):
            self.indate = self.in_date_entry.get()
            self.outdate = self.out_date_entry.get()
            self.indate = datetime.strptime(self.indate, "%d/%m/%y")
            self.outdate = datetime.strptime(self.outdate, "%d/%m/%y")
            self.Total_days.set(abs((self.outdate - self.indate).days))

            if (self.combo2.get() == "Single"):
                price1 = float(15000)
                days = float(self.Total_days.get())
                total = float(price1 * days)
                tax = "Rs" + str("%.2f" % ((total) * 10 / 100))
                sub_tol = "Rs" + str("%.2f" % (total))
                Tol_cost = "Rs" + str("%.2f" % (total + ((total) * 10 / 100)))
                self.paid_tax.set(tax)
                self.sub_total.set(sub_tol)
                self.total_cost.set(Tol_cost)

            elif (self.combo2.get() == "Double"):
                price1 = float(17000)
                days = float(self.Total_days.get())
                total = float(price1 * days)
                tax = "Rs" + str("%.2f" % ((total) * 10 / 100))
                sub_tol = "Rs" + str("%.2f" % (total))
                Tol_cost = "Rs" + str("%.2f" % (total + ((total) * 10 / 100)))
                self.paid_tax.set(tax)
                self.sub_total.set(sub_tol)
                self.total_cost.set(Tol_cost)

            elif (self.combo2.get() == "Family"):
                price1 = float(19000)
                days = float(self.Total_days.get())
                total = float(price1 * days)
                tax = "Rs" + str("%.2f" % ((total) * 10 / 100))
                sub_tol = "Rs" + str("%.2f" % (total))
                Tol_cost = "Rs" + str("%.2f" % (total + ((total) * 10 / 100)))
                self.paid_tax.set(tax)
                self.sub_total.set(sub_tol)
                self.total_cost.set(Tol_cost)

    # Save customers details to the text file.
    def save_info_Delux(self):
        number_info = self.number_entry.get()
        name_info = self.name_entry.get()
        address_info = self.address_entry.get()
        tel_no_info = self.tel_no_entry.get()
        id_type_info = self.combo.get()
        id_no_info = self.id_no_entry.get()
        check_in_info = self.in_date_entry.get()
        chek_out_info = self.out_date_entry.get()
        room_type_info = self.combo2.get()
        room_floor_info = self.combo_floor.get()
        adults_info = self.combo3.get()
        child_info = self.combo4.get()

        room_no_info = self.comboRN.get()
        no_of_days_info = self.noof_days_entry.get()
        paid_tax_info = self.tax_entry.get()
        sub_tol_info = self.sub_tol_entry.get()
        tol_cost_info = self.tol_cost_entry.get()

        print(number_info, name_info, address_info, tel_no_info,  id_type_info, id_no_info, check_in_info, chek_out_info, room_type_info, room_floor_info,
              adults_info, child_info, room_no_info, no_of_days_info, paid_tax_info, sub_tol_info, tol_cost_info)

        customer_details = open("Delux Customers details.txt", "a")
        customer_details.write("Ref Number: " + number_info)
        customer_details.write("\n""Name: " + name_info)
        customer_details.write("\n""Address: " + address_info)
        customer_details.write("\n""Contact No: " + str(tel_no_info))
        customer_details.write("\n""Type of ID: " + id_type_info)
        customer_details.write("\n""Id Number: " + id_no_info)
        customer_details.write("\n""Chek In Date: " + check_in_info)
        customer_details.write("\n""Check Out Date: " + chek_out_info)
        customer_details.write("\n""Room Type: " + room_type_info)
        customer_details.write("\n""Room Floor: " + room_floor_info)
        customer_details.write("\n""Adults: " + str(adults_info))
        customer_details.write("\n""Children: " + str(child_info))
        customer_details.write("\n""Room No: " + str(room_no_info))
        customer_details.write("\n""No Of Days: " + str(no_of_days_info))
        customer_details.write("\n""*** ")

        customer_details.write("\n""Paid Tax: " + str(paid_tax_info))
        customer_details.write("\n""Sub Total: " + str(sub_tol_info))
        customer_details.write("\n""Total Cost: " + str(tol_cost_info))
        customer_details.write("\n")
        customer_details.write("\n")

        customer_details.close()

# Delux customer detail window..........................................................................................
    def opendetail_delux(self):
        self.login_frame2.destroy()
        self.delux_detail_frame6 = Frame(self.root, bg="White", bd=13, relief=RIDGE)
        self.delux_detail_frame6.place(x=220, y=80, width=1100, height=650)

# Receipt=============================================================================================================
        self.receipt_delux = Frame(self.delux_detail_frame6, bg="light grey", bd=10, relief=RIDGE)
        self.receipt_delux.place(x=340, y=200, width=300, height=340)
# Receipt title
        self.title = Label(self.receipt_delux, text="TOTAL COST", font=("Times new roman", 16, "bold", "underline"), fg="black", bg="light grey")
        self.title.place(x=70, y=8)
# Room Number
        self.room_no = Label(self.receipt_delux, text="Room no", font=("Goudy old style", 12, "bold"), bg="light grey")
        self.room_no.place(x=140, y=45)
        self.comboRN = IntVar
        self.comboRN = ttk.Combobox(self.receipt_delux, textvariable=self.comboRN, font=("Times new roman", 12), width=4, height=30)
        self.comboRN.place(x=210, y=45)
        self.comboRN['values'] = ("*Single*", 201, 202, 203, "*Double*", 215, 216, 217, "*Family*", 220, 221, 222)
# Number of days
        self.noof_days = Label(self.receipt_delux, text="No Of Days : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.noof_days.place(x=10, y=90)
        self.noof_days_entry = StringVar
        self.Total_days = StringVar()
        self.noof_days_entry = Entry(self.receipt_delux, textvariable=self.Total_days, font=("Times new roman", 12), bg="dark grey", bd=2)
        self.noof_days_entry.place(x=110, y=90, width=150, height=30)
# paid Tax
        self.tax = Label(self.receipt_delux, text="Paid Tax : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.tax.place(x=10, y=130)
        self.tax_entry = IntVar
        self.paid_tax = StringVar()
        self.tax_entry = Entry(self.receipt_delux, textvariable=self.paid_tax, font=("Times new roman", 12), bg="dark grey", bd=2)
        self.tax_entry.place(x=110, y=130, width=150, height=30)
# sub total
        self.sub_tol = Label(self.receipt_delux, text="Sub Total : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.sub_tol.place(x=10, y=170)
        self.sub_tol_entry = IntVar
        self.sub_total = StringVar()
        self.sub_tol_entry = Entry(self.receipt_delux, textvariable=self.sub_total, font=("Times new roman", 12), bg="dark grey", bd=2)
        self.sub_tol_entry.place(x=110, y=170, width=150, height=30)
# Total Cost
        self.tol_cost = Label(self.receipt_delux, text="Total Cost : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.tol_cost.place(x=10, y=210)
        self.tol_cost_entry = IntVar
        self.total_cost = StringVar()
        self.tol_cost_entry = Entry(self.receipt_delux, textvariable=self.total_cost, font=("Times new roman", 12), bg="dark grey", bd=2)
        self.tol_cost_entry.place(x=110, y=210, width=150, height=30)

# Total button
        self.total_but = Button(self.receipt_delux, text="TOTAL", font=("Times new roman", 14, "bold"), fg="black", bg="dark grey", bd=4, command=self.Total_Date_delux)
        self.total_but.place(x=20, y=270, width=100, height=30)

# Receipt button
        self.Receipt_but = Button(self.receipt_delux, text="RECEIPT", font=("Times new roman", 14, "bold"), fg="black", bg="dark grey", bd=4, command=self.Receipt_delux)
        self.Receipt_but.place(x=160, y=270, width=100, height=30)


# Title & Subtitle====================================================================================================
        self.title = Label(self.delux_detail_frame6, text="Delux Suite", font=("monaco", 24, "bold"), fg="black", bg="white")
        self.title.place(x=50, y=20)
        self.subtitle = Label(self.delux_detail_frame6, text="Enter customer details here.", font=("Goudy old style", 14, "bold"), bg="white")
        self.subtitle.place(x=50, y=70)
# Date
        self.Date1 = StringVar()
        self.Date1.set(time.strftime("%d/%m/%y"))
        self.lbl_Date = Label(self.delux_detail_frame6, textvariable=self.Date1, font=("monaco", 12, "bold"), pady=9, bg="white", fg="black")
        self.lbl_Date.place(x=560, y=15)
# Customer Number
        self.number = Label(self.delux_detail_frame6, text="Customer Ref : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.number.place(x=375, y=70)
        self.number_entry = StringVar
        self.number_entry = Entry(self.delux_detail_frame6, textvariable=self.number_entry, font=("Times new roman", 14), bg="white", bd=1)
        self.number_entry.place(x=500, y=70, width=100, height=30)
# Customer Name
        self.name = Label(self.delux_detail_frame6, text="Name : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.name.place(x=50, y=120)
        self.name_entry = StringVar
        self.name_entry = Entry(self.delux_detail_frame6, font=("Times new roman", 14), bg="white", bd=1)
        self.name_entry.place(x=200, y=120, width=400, height=30)
# customer Address
        self.address = Label(self.delux_detail_frame6, text="Address : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.address.place(x=50, y=160)
        self.address_entry = StringVar
        self.address_entry = Entry(self.delux_detail_frame6, font=("Times new roman", 14), bg="white", bd=1)
        self.address_entry.place(x=200, y=160, width=400, height=30)
# customer Contact Number
        self.tel_no = Label(self.delux_detail_frame6, text="Contact No : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.tel_no.place(x=50, y=200)
        self.tel_no_entry = IntVar
        self.tel_no_entry = Entry(self.delux_detail_frame6, font=("Times new roman", 14), bg="white", bd=1)
        self.tel_no_entry.place(x=200, y=200, width=130, height=30)
# Type of ID
        self.Nationality = Label(self.delux_detail_frame6, text="Type Of ID : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.Nationality.place(x=50, y=240)
        self.combo = StringVar
        self.combo = ttk.Combobox(self.delux_detail_frame6, font=("Times new roman", 14), width=12, height=30)
        self.combo.place(x=200, y=240, )
        self.combo['values'] = ("National ID", "Driving license", "Passport")
# customer Id Number
        self.id_no = Label(self.delux_detail_frame6, text="Id No : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.id_no.place(x=50, y=280)
        self.id_no_entry = StringVar
        self.id_no_entry = Entry(self.delux_detail_frame6, font=("Times new roman", 14), bg="white", bd=1)
        self.id_no_entry.place(x=200, y=280, width=130, height=30)
# chek in date
        self.in_date = Label(self.delux_detail_frame6, text="Chek in date : ", font=("Goudy old style", 14, "bold"),bg="white")
        self.in_date.place(x=50, y=320)
        self.in_date_entry =StringVar()
        self.in_date_entry = Entry(self.delux_detail_frame6, textvariable=self.Date1, font=("Times new roman", 14),bg="white", bd=1)
        self.in_date_entry.place(x=200, y=320, width=130, height=30)
# chek out date
        self.out_date = Label(self.delux_detail_frame6, text="Chek out date : ", font=("Goudy old style", 14, "bold"),bg="white")
        self.out_date.place(x=50, y=360)
        self.out_date_entry = StringVar()
        self.out_date_entry = Entry(self.delux_detail_frame6,textvariable=self.out_date_entry, font=("Times new roman", 14),bg="white", bd=1)
        self.out_date_entry.place(x=200, y=360, width=130, height=30)
# Room Type
        self.room_type = Label(self.delux_detail_frame6, text="Room Type : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.room_type.place(x=50, y=400)
        self.combo2 = StringVar
        self.combo2 = ttk.Combobox(self.delux_detail_frame6, textvariable=self.combo2, font=("Times new roman", 14), width=12, height=30)
        self.combo2.place(x=200, y=400, )
        self.combo2['values'] = ("Single", "Double", "Family")
# Room Floor
        self.room_floor = Label(self.delux_detail_frame6, text="Room Floor : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.room_floor.place(x=50, y=440)
        self.combo_floor = StringVar
        self.combo_floor = ttk.Combobox(self.delux_detail_frame6, textvariable=self.combo_floor, font=("Times new roman", 14), width=12, height=30)
        self.combo_floor.place(x=200, y=440)
        self.combo_floor['values'] = ("", "1st Floor", "2nd Floor", "3rd Floor")
# How many Adults
        self.adults = Label(self.delux_detail_frame6, text="Adults : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.adults.place(x=70, y=480)
        self.combo3 = IntVar
        self.combo3 = ttk.Combobox(self.delux_detail_frame6, textvariable=self.combo3, font=("Times new roman", 14), width=3, height=30)
        self.combo3.place(x=70, y=510, )
        self.combo3['values'] = (0, 1, 2, 3, 4, 5, "(max)")
# How many children
        self.child = Label(self.delux_detail_frame6, text="Children : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.child.place(x=160, y=480)
        self.combo4 = IntVar
        self.combo4 = ttk.Combobox(self.delux_detail_frame6, textvariable=self.combo4, font=("Times new roman", 14), width=3, height=30)
        self.combo4.place(x=175, y=510, )
        self.combo4['values'] = (0, 1, 2, 3, 4, 5, "(max)")


# Back button (back to open booking frame)
        self.back = Button(self.delux_detail_frame6, text="BACK", font=("Times new roman", 16, "bold"), fg="black", bg="red", bd=4, command=self.openbooking)
        self.back.place(x=50, y=560, width=100, height=40)

# Save Button (Save to file)
        self.save = Button(self.delux_detail_frame6, text="SAVE", font=("Times new roman", 16, "bold"), fg="black", bg="green", bd=4, command=self.save_info_Delux)
        self.save.place(x=300, y=560, width=100, height=40)

# Exit Button
        self.back = Button(self.delux_detail_frame6, text="EXIT", font=("Times new roman", 16, "bold"), fg="white", bg="black", bd=4, command=self.exit_programme)
        self.back.place(x=550, y=560, width=100, height=40)

# Receipt==========================================================================================================
    def Receipt_delux(self):
        self.txtreceiptlux = Text(self.delux_detail_frame6, font=("monaco", 12))
        self.txtreceiptlux.place(x=680, y=0, width=400, height=625)
        self.txtreceiptlux.insert(END, "\n""  Date " + self.Date1.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t      SUNSET LODGE" "\n")
        self.txtreceiptlux.insert(END, "       No21, De Cross Road, Negombo." "\n")
        self.txtreceiptlux.insert(END, "\t     TP : +942229456" "\n""\n")
        self.txtreceiptlux.insert(END, "\t     ****************" "\n")
        self.txtreceiptlux.insert(END, "  Cashier : User" "\n""\n")
        self.txtreceiptlux.insert(END, "  Name         : " + self.name_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "  Contact No   : " + self.tel_no_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "  Chek in Date : " + self.in_date_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "  Chek out Date: " + self.out_date_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t    *****************" "\n""\n")
        self.txtreceiptlux.insert(END, "\t      Paid tax   : " + self.tax_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t      Sub Total  : " + self.sub_total.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t      Total Cost : " + self.tol_cost_entry.get() + "\n""\n""\n")
        self.txtreceiptlux.insert(END, "     We hope you are satisfied with  " "\n")
        self.txtreceiptlux.insert(END, "\t    our services.." "\n""\n")
        self.txtreceiptlux.insert(END, "\t  THANK YOU COME AGAIN..!" "\n""\n")


# Total cost premier suite ============================================================================================
#======================================================================================================================

    def Total_Date_premier(self):
            self.indate = self.in_date_entry.get()
            self.outdate = self.out_date_entry.get()
            self.indate = datetime.strptime(self.indate, "%d/%m/%y")
            self.outdate = datetime.strptime(self.outdate, "%d/%m/%y")
            self.Total_days.set(abs((self.outdate - self.indate).days))

            if (self.combo2.get() == "Single"):
                price1 = float(9000)
                days = float(self.Total_days.get())
                total = float(price1 * days)
                tax = "Rs" + str("%.2f" % ((total) * 5/ 100))
                sub_tol = "Rs" + str("%.2f" % (total))
                Tol_cost = "Rs" + str("%.2f" % (total + ((total) * 5 / 100)))
                self.paid_tax.set(tax)
                self.sub_total.set(sub_tol)
                self.total_cost.set(Tol_cost)

            elif (self.combo2.get() == "Double"):
                price1 = float(11000)
                days = float(self.Total_days.get())
                total = float(price1 * days)
                tax = "Rs" + str("%.2f" % ((total) * 5 / 100))
                sub_tol = "Rs" + str("%.2f" % (total))
                Tol_cost = "Rs" + str("%.2f" % (total + ((total) * 5 / 100)))
                self.paid_tax.set(tax)
                self.sub_total.set(sub_tol)
                self.total_cost.set(Tol_cost)

            elif (self.combo2.get() == "Family"):
                price1 = float(13000)
                days = float(self.Total_days.get())
                total = float(price1 * days)
                tax = "Rs" + str("%.2f" % ((total) * 5 / 100))
                sub_tol = "Rs" + str("%.2f" % (total))
                Tol_cost = "Rs" + str("%.2f" % (total + ((total) * 5 / 100)))
                self.paid_tax.set(tax)
                self.sub_total.set(sub_tol)
                self.total_cost.set(Tol_cost)


# Save customers details to the text file.==============================================================================
    def save_info_Premier(self):
        number_info = self.number_entry.get()
        name_info = self.name_entry.get()
        address_info = self.address_entry.get()
        tel_no_info = self.tel_no_entry.get()
        id_type_info = self.combo.get()
        id_no_info = self.id_no_entry.get()
        check_in_info = self.in_date_entry.get()
        chek_out_info = self.out_date_entry.get()
        room_type_info = self.combo2.get()
        room_floor_info = self.combo_floor.get()
        adults_info = self.combo3.get()
        child_info = self.combo4.get()

        room_no_info = self.comboRN.get()
        no_of_days_info = self.noof_days_entry.get()
        paid_tax_info = self.tax_entry.get()
        sub_tol_info = self.sub_tol_entry.get()
        tol_cost_info = self.tol_cost_entry.get()

        print(number_info, name_info, address_info, tel_no_info, id_type_info, id_no_info, check_in_info, chek_out_info, room_type_info, room_floor_info,
              adults_info, child_info, room_no_info, no_of_days_info, paid_tax_info, sub_tol_info, tol_cost_info)

        customer_details = open("Premier Customers details.txt", "a")
        customer_details.write("Ref Number: " + number_info)
        customer_details.write("\n""Name: " + name_info)
        customer_details.write("\n""Address: " + address_info)
        customer_details.write("\n""Contact No: " + str(tel_no_info))
        customer_details.write("\n""Type of ID: " + id_type_info)
        customer_details.write("\n""Id Number: " + id_no_info)
        customer_details.write("\n""Chek In Date: " + check_in_info)
        customer_details.write("\n""Check Out Date: " + chek_out_info)
        customer_details.write("\n""Room Type: " + room_type_info)
        customer_details.write("\n""Room Floor: " + room_floor_info)
        customer_details.write("\n""Adults: " + str(adults_info))
        customer_details.write("\n""Children: " + str(child_info))
        customer_details.write("\n""Room No: " + str(room_no_info))
        customer_details.write("\n""No Of Days: " + str(no_of_days_info))
        customer_details.write("\n""*** ")

        customer_details.write("\n""Paid Tax: " + str(paid_tax_info))
        customer_details.write("\n""Sub Total: " + str(sub_tol_info))
        customer_details.write("\n""Total Cost: " + str(tol_cost_info))
        customer_details.write("\n")
        customer_details.write("\n")

        customer_details.close()


# Premier customer detail window..........................................................................................
    def opendetail_premier(self):
        self.login_frame2.destroy()
        self.premier_detail_frame7 = Frame(self.root, bg="White", bd=13, relief=RIDGE)
        self.premier_detail_frame7.place(x=220, y=80, width=1100, height=650)

# Receipt==================================================================================
        self.receipt_premier = Frame(self.premier_detail_frame7, bg="light grey", bd=10, relief=RIDGE)
        self.receipt_premier.place(x=340, y=200, width=300, height=340)
# Receipt title
        self.title = Label(self.receipt_premier, text="RECEIPT", font=("Times new roman", 16, "bold", "underline"), fg="black", bg="light grey")
        self.title.place(x=70, y=8)
# Room Number
        self.room_no = Label(self.receipt_premier, text="Room no", font=("Goudy old style", 12, "bold"), bg="light grey")
        self.room_no.place(x=140, y=45)
        self.comboRN = IntVar
        self.comboRN = ttk.Combobox(self.receipt_premier, textvariable=self.comboRN, font=("Times new roman", 12), width=4, height=30)
        self.comboRN.place(x=210, y=45)
        self.comboRN['values'] = ("*Single*", 301, 302, 303, "*Double*", 315, 316, 317, "*Family*", 320, 321, 322)
# Number of days
        self.noof_days = Label(self.receipt_premier, text="No Of Days : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.noof_days.place(x=10, y=90)
        self.noof_days_entry = StringVar
        self.Total_days = StringVar()
        self.noof_days_entry = Entry(self.receipt_premier, textvariable=self.Total_days, font=("Times new roman", 12), bg="dark grey", bd=2)
        self.noof_days_entry.place(x=110, y=90, width=150, height=30)
# paid Tax
        self.tax = Label(self.receipt_premier, text="Paid Tax : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.tax.place(x=10, y=130)
        self.tax_entry = IntVar
        self.paid_tax = StringVar()
        self.tax_entry = Entry(self.receipt_premier, textvariable=self.paid_tax, font=("Times new roman", 12), bg="dark grey", bd=2)
        self.tax_entry.place(x=110, y=130, width=150, height=30)
# sub total
        self.sub_tol = Label(self.receipt_premier, text="Sub Total : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.sub_tol.place(x=10, y=170)
        self.sub_tol_entry = IntVar
        self.sub_total = StringVar()
        self.sub_tol_entry = Entry(self.receipt_premier, textvariable=self.sub_total, font=("Times new roman", 12), bg="dark grey", bd=2)
        self.sub_tol_entry.place(x=110, y=170, width=150, height=30)
# Total Cost
        self.tol_cost = Label(self.receipt_premier, text="Total Cost : ", font=("Times new roman", 12, "bold"), bg="light grey")
        self.tol_cost.place(x=10, y=210)
        self.tol_cost_entry = IntVar
        self.total_cost = StringVar()
        self.tol_cost_entry = Entry(self.receipt_premier, textvariable=self.total_cost, font=("Times new roman", 12),  bg="dark grey", bd=2)
        self.tol_cost_entry.place(x=110, y=210, width=150, height=30)

# Total button
        self.total_but = Button(self.receipt_premier, text="TOTAL", font=("Times new roman", 14, "bold"), fg="black", bg="dark grey", bd=4, command=self.Total_Date_premier)
        self.total_but.place(x=20, y=270, width=100, height=30)

# Receipt button
        self.receipt_but = Button(self.receipt_premier, text="RECEIPT", font=("Times new roman", 14, "bold"), fg="black", bg="dark grey", bd=4, command=self.Receipt_premier)
        self.receipt_but.place(x=160, y=270, width=100, height=30)


# Title & Subtitle====================================================================================================
        self.title = Label(self.premier_detail_frame7, text="Premier Suite", font=("monaco", 24, "bold"), fg="black", bg="white")
        self.title.place(x=50, y=20)
        self.subtitle = Label(self.premier_detail_frame7, text="Enter customer details here.", font=("Goudy old style", 14, "bold"), bg="white")
        self.subtitle.place(x=50, y=70)
# Date
        self.Date1 = StringVar()
        self.Date1.set(time.strftime("%d/%m/%y"))
        self.lbl_Date = Label(self.premier_detail_frame7, textvariable=self.Date1, font=("monaco", 12, "bold"), pady=9, bg="white", fg="black")
        self.lbl_Date.place(x=560, y=15)
# Customer Number
        self.number = Label(self.premier_detail_frame7, text="Customer Ref : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.number.place(x=375, y=70)
        self.number_entry = StringVar
        self.number_entry = Entry(self.premier_detail_frame7, textvariable=self.number_entry, font=("Times new roman", 14), bg="white", bd=1)
        self.number_entry.place(x=500, y=70, width=100, height=30)
# Customer Name
        self.name = Label(self.premier_detail_frame7, text="Name : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.name.place(x=50, y=120)
        self.name_entry = StringVar
        self.name_entry = Entry(self.premier_detail_frame7, font=("Times new roman", 14), bg="white", bd=1)
        self.name_entry.place(x=200, y=120, width=400, height=30)
# customer Address
        self.address = Label(self.premier_detail_frame7, text="Address : ", font=("Goudy old style", 14, "bold"),bg="white")
        self.address.place(x=50, y=160)
        self.address_entry = StringVar
        self.address_entry = Entry(self.premier_detail_frame7, font=("Times new roman", 14), bg="white", bd=1)
        self.address_entry.place(x=200, y=160, width=400, height=30)
# customer Contact Number
        self.tel_no = Label(self.premier_detail_frame7, text="Contact No : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.tel_no.place(x=50, y=200)
        self.tel_no_entry = IntVar
        self.tel_no_entry = Entry(self.premier_detail_frame7, font=("Times new roman", 14), bg="white", bd=1)
        self.tel_no_entry.place(x=200, y=200, width=130, height=30)
# Type of ID
        self.Nationality = Label(self.premier_detail_frame7, text="Type of ID : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.Nationality.place(x=50, y=240)
        self.combo = StringVar
        self.combo = ttk.Combobox(self.premier_detail_frame7, font=("Times new roman", 14), width=12, height=30)
        self.combo.place(x=200, y=240, )
        self.combo['values'] = ("National ID", "Driving License", "Passport")
# customer Id Number
        self.id_no = Label(self.premier_detail_frame7, text="Id No : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.id_no.place(x=50, y=280)
        self.id_no_entry = StringVar
        self.id_no_entry = Entry(self.premier_detail_frame7, font=("Times new roman", 14), bg="white", bd=1)
        self.id_no_entry.place(x=200, y=280, width=130, height=30)
# chek in date
        self.in_date = Label(self.premier_detail_frame7, text="Chek in date : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.in_date.place(x=50, y=320)
        self.in_date_entry = StringVar()
        self.in_date_entry = Entry(self.premier_detail_frame7, textvariable=self.Date1, font=("Times new roman", 14), bg="white", bd=1)
        self.in_date_entry.place(x=200, y=320, width=130, height=30)
# chek out date
        self.out_date = Label(self.premier_detail_frame7, text="Chek out date : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.out_date.place(x=50, y=360)
        self.out_date_entry = StringVar()
        self.out_date_entry = Entry(self.premier_detail_frame7, textvariable=self.out_date_entry, font=("Times new roman", 14), bg="white", bd=1)
        self.out_date_entry.place(x=200, y=360, width=130, height=30)
# Room Type
        self.room_type = Label(self.premier_detail_frame7, text="Room Type : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.room_type.place(x=50, y=400)
        self.combo2 = StringVar
        self.combo2 = ttk.Combobox(self.premier_detail_frame7, textvariable=self.combo2, font=("Times new roman", 14), width=12, height=30)
        self.combo2.place(x=200, y=400, )
        self.combo2['values'] = ("Single", "Double", "Family")
# Room Floor
        self.room_floor = Label(self.premier_detail_frame7, text="Room Floor : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.room_floor.place(x=50, y=440)
        self.combo_floor = StringVar
        self.combo_floor = ttk.Combobox(self.premier_detail_frame7, textvariable=self.combo_floor, font=("Times new roman", 14), width=12, height=30)
        self.combo_floor.place(x=200, y=440)
        self.combo_floor["values"] = ("", "1st Floor", "2nd Floor", "3rd Floor")
# How many Adults
        self.adults = Label(self.premier_detail_frame7, text="Adults : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.adults.place(x=70, y=480)
        self.combo3 = IntVar
        self.combo3 = ttk.Combobox(self.premier_detail_frame7, textvariable=self.combo3, font=("Times new roman", 14), width=3, height=30)
        self.combo3.place(x=70, y=510, )
        self.combo3['values'] = (0, 1, 2, 3, 4, 5, "(max)")
# How many children
        self.child = Label(self.premier_detail_frame7, text="Children : ", font=("Goudy old style", 14, "bold"), bg="white")
        self.child.place(x=160, y=480)
        self.combo4 = IntVar
        self.combo4 = ttk.Combobox(self.premier_detail_frame7, textvariable=self.combo4, font=("Times new roman", 14), width=3, height=30)
        self.combo4.place(x=175, y=510, )
        self.combo4['values'] = (0, 1, 2, 3, 4, 5, "(max)")

# Back button (back to open booking frame)
        self.back = Button(self.premier_detail_frame7, text="BACK", font=("Times new roman", 16, "bold"), fg="black", bg="red", bd=4, command=self.openbooking)
        self.back.place(x=50, y=560, width=100, height=40)

# Save Button (Save to file)
        self.save = Button(self.premier_detail_frame7, text="SAVE", font=("Times new roman", 16, "bold"), fg="black", bg="green", bd=4, command=self.save_info_Premier)
        self.save.place(x=300, y=560, width=100, height=40)

# Exit Button
        self.back = Button(self.premier_detail_frame7, text="EXIT", font=("Times new roman", 16, "bold"), fg="white", bg="black", bd=4, command=self.exit_programme)
        self.back.place(x=550, y=560, width=100, height=40)

# Receipt==========================================================================================================
    def Receipt_premier(self):
        self.txtreceiptlux = Text(self.premier_detail_frame7, font=("monaco", 12))
        self.txtreceiptlux.place(x=680, y=0, width=400, height=625)
        self.txtreceiptlux.insert(END, "\n""  Date " + self.Date1.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t      SUNSET LODGE" "\n")
        self.txtreceiptlux.insert(END, "       No21, De Cross Road, Negombo." "\n")
        self.txtreceiptlux.insert(END, "\t     TP : +942229456" "\n""\n")
        self.txtreceiptlux.insert(END, "\t     ****************" "\n")
        self.txtreceiptlux.insert(END, "  Cashier : User" "\n""\n")
        self.txtreceiptlux.insert(END, "  Name         : " + self.name_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "  Contact No   : " + self.tel_no_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "  Chek in Date : " + self.in_date_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "  Chek out Date: " + self.out_date_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t    *****************" "\n""\n")
        self.txtreceiptlux.insert(END, "\t      Paid tax   : " + self.tax_entry.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t      Sub Total  : " + self.sub_total.get() + "\n""\n")
        self.txtreceiptlux.insert(END, "\t      Total Cost : " + self.tol_cost_entry.get() + "\n""\n""\n")
        self.txtreceiptlux.insert(END, "     We hope you are satisfied with  " "\n")
        self.txtreceiptlux.insert(END, "\t    our services.." "\n""\n")
        self.txtreceiptlux.insert(END, "\t  THANK YOU COME AGAIN..!" "\n""\n")

# Detail Window=======================================================================================================
    def opendetails(self):
        self.login_frame2.destroy()
        self.details_frame4= Frame(self.root, bg="White", bd=13, relief=RIDGE)
        self.details_frame4.place(x=220, y=80, width=1100, height=650)
# Title & subtitles
        self.title = Label(self.details_frame4, text="DETAILS", font=("Goudy old style", 28, "bold", "underline"), bg="white")
        self.title.place(x=430, y=30)
        self.title = Label(self.details_frame4, text="You can get more details about our hotel by clicking Read More button.", font=("Goudy old style", 16, "bold"), bg="white")
        self.title.place(x=100, y=90)

# Property Description
        self.title = Label(self.details_frame4, text="Property Description", font=("Goudy old style", 24, "bold"), bg="white")
        self.title.place(x=100, y=150)
# Short description
        self.title = Label(self.details_frame4, text="Here you can find information about our hotel properties.", font=("Goudy old style", 14, "bold"), bg="white", fg="dark blue")
        self.title.place(x=150, y=185)
# Read more Button
        self.read_more1 = Button(self.details_frame4, text="Read more", font=("Goudy old style", 16, "bold", "underline"), fg="red", bg="white", bd=0, command=self.Property_description)
        self.read_more1.place(x=800, y=180, width=120, height=40)

# Health and Safety
        self.title = Label(self.details_frame4, text="Health and Safety", font=("Goudy old style", 24, "bold"), bg="white")
        self.title.place(x=100, y=240)
# Short description
        self.title = Label(self.details_frame4, text="Here you can find out about the health care policies followed bu our hotel. ", font=("Goudy old style", 14, "bold"), bg="white", fg="dark blue")
        self.title.place(x=150, y=275)
# Read more Button
        self.read_more2 = Button(self.details_frame4, text="Read more", font=("Goudy old style", 16, "bold", "underline"),  fg="red", bg="white", bd=0, command=self.Health_Safty)
        self.read_more2.place(x=800, y=270, width=120, height=40)

# Facilities
        self.title = Label(self.details_frame4, text="Facilities", font=("Goudy old style", 24, "bold"), bg="white")
        self.title.place(x=100, y=330)
# Short description
        self.title = Label(self.details_frame4, text="Here you can find information about the facilities provided by our hotel.", font=("Goudy old style", 14, "bold"), bg="white", fg="dark blue")
        self.title.place(x=150, y=365)
# Read more Button
        self.read_more3 = Button(self.details_frame4, text="Read more", font=("Goudy old style", 16, "bold", "underline"), fg="red", bg="white", bd=0, command=self.Facilities)
        self.read_more3.place(x=800, y=360, width=120, height=40)

# Property Surrounding
        self.title = Label(self.details_frame4, text="Property Surrounding", font=("Goudy old style", 24, "bold"), bg="white")
        self.title.place(x=100, y=420)
# Short description
        self.title = Label(self.details_frame4, text="This will give you information about the locations and properties around our hotel.", font=("Goudy old style", 14, "bold"), bg="white", fg="dark blue")
        self.title.place(x=150, y=455)
# Read more Button
        self.read_more4 = Button(self.details_frame4, text="Read more", font=("Goudy old style", 16, "bold", "underline"), fg="red", bg="white", bd=0, command=self.pro_surrouding)
        self.read_more4.place(x=800, y=450, width=120, height=40)

# Back button(back to open booking frame)
        self.back = Button(self.details_frame4, text="BACK", font=("Times new roman", 16, "bold"), fg="black", bg="red", bd=4, command=self.openbooking)
        self.back.place(x=100, y=540, width=100, height=40)

# Exit Button
        self.back = Button(self.details_frame4, text="EXIT", font=("Times new roman", 16, "bold"), fg="white", bg="black", bd=4, command=self.exit_programme)
        self.back.place(x=850, y=540, width=100, height=40)


# about property description==========================================================================================
    def Property_description(self):
        self.details_frame4.destroy()
        self.details_frame_property= Frame(self.root, bg="White", bd=13, relief=RIDGE)
        self.details_frame_property.place(x=220, y=80, width=1100, height=650)
# Title
        self.title = Label(self.details_frame_property, text="Property Description", font=("Goudy old style", 22, "bold", "underline"), bg="white")
        self.title.place(x=120, y=50)
# about
        self.title = Label(self.details_frame_property, text="-Featuring free WiFi and an outdoor pool,Sunset Lodge offers accomadation in Negombo.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=120)
        self.title = Label(self.details_frame_property, text="-Free privet park is available on site.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=160)
        self.title = Label(self.details_frame_property, text="-All rooms include a flat-screen TV with satellite channels.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=200)
        self.title = Label(self.details_frame_property, text="-Certain rooms feature a seating area to relax in after a busy day.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=240)
        self.title = Label(self.details_frame_property, text="-Each room is equipped with a privet bathroom fitted with a hot tub.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=280)
        self.title = Label(self.details_frame_property, text="-Extras include slippers, free toiletries & a hair dryer.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=320)
        self.title = Label(self.details_frame_property, text="-Comman area include a sun terrace & shared kitchen.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=360)
        self.title = Label(self.details_frame_property, text="-Guest can enjoy a meal at the on-site restaurant.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=400)
        self.title = Label(self.details_frame_property, text="-The property also offers room service & special diet menus .", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=440)
        self.title = Label(self.details_frame_property, text="-Bike hire is available at this hotel & thr area is popular for fishing .", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=440)

# Back to Main Detail window
        self.back = Button(self.details_frame_property, text="BACK", font=("Times new roman", 16, "bold"), fg="Black", bg="Red", bd=4, command=self.opendetails)
        self.back.place(x=150, y=540, width=100, height=40)

# Exit button
        self.back = Button(self.details_frame_property, text="EXIT", font=("Times new roman", 16, "bold"), fg="white", bg="black", bd=4, command=self.exit_programme)
        self.back.place(x=850, y=540, width=100, height=40)


# about Health & Safety==============================================================================================
    def Health_Safty(self):
        self.details_frame4.destroy()
        self.details_frame_health = Frame(self.root, bg="White", bd=13, relief=RIDGE)
        self.details_frame_health.place(x=220, y=80, width=1100, height=650)
# Title
        self.title = Label(self.details_frame_health, text="Health & Safety", font=("Goudy old style", 22, "bold", "underline"), bg="white")
        self.title.place(x=120, y=50)
# about
        self.title = Label(self.details_frame_health, text="-Staff follow all safety protocols as directed by local authorities.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=120)
        self.title = Label(self.details_frame_health, text="-Hand sanitizer in guest accommodation and key areas.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=160)
        self.title = Label(self.details_frame_health, text="-Process in place to check health of guests.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=200)
        self.title = Label(self.details_frame_health, text="-First aid kit available & access to healthcare professionals.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=240)
        self.title = Label(self.details_frame_health, text="-Physical distancing rules followed.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=280)
        self.title = Label(self.details_frame_health, text="-Screens or physical barriers placed between staff & guest in appropriate areas.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=320)
        self.title = Label(self.details_frame_health, text="-Linens,towels and laundry washed in accordance with local authority guidlines.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=360)
        self.title = Label(self.details_frame_health, text="-Guest accommodation sealed after cleaning.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=400)
        self.title = Label(self.details_frame_health, text="-Physical distancing in dining areas.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=440)
        self.title = Label(self.details_frame_health, text="-All plates,cutlery,glasses & other tableware have been senitized.",font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=440)
        self.title = Label(self.details_frame_health, text="-Delivered food is securely covered.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=480)

# Back to Main Detail window
        self.back = Button(self.details_frame_health, text="BACK", font=("Times new roman", 16, "bold"), fg="Black", bg="Red", bd=4, command=self.opendetails)
        self.back.place(x=150, y=540, width=100, height=40)

# Exit button
        self.back = Button(self.details_frame_health, text="EXIT", font=("Times new roman", 16, "bold"), fg="white", bg="black", bd=4, command=self.exit_programme)
        self.back.place(x=850, y=540, width=100, height=40)


# about Facilities====================================================================================================
    def Facilities(self):
        self.details_frame4.destroy()
        self.details_frame_facilities = Frame(self.root, bg="White", bd=13, relief=RIDGE)
        self.details_frame_facilities.place(x=220, y=80, width=1100, height=650)
# Title
        self.title = Label(self.details_frame_facilities, text="Facilities", font=("Goudy old style", 22, "bold", "underline"), bg="white")
        self.title.place(x=120, y=50)
# about
        self.title = Label(self.details_frame_facilities, text="-Outdoor pool (all pools are free of charge & all ages welcome) with towels", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=120)
        self.title = Label(self.details_frame_facilities, text="-Free privet park is possible on site (reservation isn't needed).", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=160)
        self.title = Label(self.details_frame_facilities, text="-WiFi is available in all areas & is free of charge.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=200)
        self.title = Label(self.details_frame_facilities, text="-Pets are not allowed.", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=240)
        self.title = Label(self.details_frame_facilities, text="-Entertainment & family services( children television, networks).", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=280)
        self.title = Label(self.details_frame_facilities, text="-Bottle of water/Special diet menus", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=320)
        self.title = Label(self.details_frame_facilities, text="-Wine/Champagne/Bar/Restauarent available/Sun terrace/BBQ facilities", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=360)
        self.title = Label(self.details_frame_facilities, text="-Grocery deliveries/Mini market/Gift shop/Bridal suits/VIP facilities", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=400)
        self.title = Label(self.details_frame_facilities, text="-Daily house keeping/Shoeshine/Ironing service/Dry clening/Laundry", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=440)
        self.title = Label(self.details_frame_facilities, text="-Fax/Photocopying", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=440)
        self.title = Label(self.details_frame_facilities, text="-Meeting/Banquet", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=480)


# Back to Main Detail window
        self.back = Button(self.details_frame_facilities, text="BACK", font=("Times new roman", 16, "bold"), fg="Black", bg="Red", bd=4, command=self.opendetails)
        self.back.place(x=150, y=540, width=100, height=40)

# Exit button
        self.back = Button(self.details_frame_facilities, text="EXIT", font=("Times new roman", 16, "bold"), fg="white", bg="black", bd=4, command=self.exit_programme)
        self.back.place(x=850, y=540, width=100, height=40)


# about property surrounding==========================================================================================
    def pro_surrouding(self):
        self.details_frame4.destroy()
        self.details_frame_pro_surround = Frame(self.root, bg="White", bd=13, relief=RIDGE)
        self.details_frame_pro_surround.place(x=220, y=80, width=1100, height=650)
# Title
        self.title = Label(self.details_frame_pro_surround, text="Property Surroundings", font=("Goudy old style", 22, "bold", "underline"), bg="white")
        self.title.place(x=120, y=50)
# about
        self.title = Label(self.details_frame_pro_surround, text="Attractions...", font=("Goudy old style", 16, "bold"), bg="white")
        self.title.place(x=150, y=120)
        self.title = Label(self.details_frame_pro_surround, text="Top attractions.", font=("Goudy old style", 15, "bold"), fg="red", bg="white")
        self.title.place(x=150, y=160)
        self.title = Label(self.details_frame_pro_surround, text="---Khan Clock Tower", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=200)
        self.title = Label(self.details_frame_pro_surround, text="---Ceylon Tea Museum", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=240)
        self.title = Label(self.details_frame_pro_surround, text="---Kandy Museum", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=280)
        self.title = Label(self.details_frame_pro_surround, text="Whats nearby.", font=("Goudy old style", 15, "bold"),fg="red", bg="white")
        self.title.place(x=150, y=320)
        self.title = Label(self.details_frame_pro_surround, text="---The beach Park", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=360)
        self.title = Label(self.details_frame_pro_surround, text="---Village in Resort", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=400)
        self.title = Label(self.details_frame_pro_surround, text="---Dino Park", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=440)
        self.title = Label(self.details_frame_pro_surround, text="Closet Beaches.", font=("Goudy old style", 15, "bold"), fg="red", bg="white")
        self.title.place(x=150, y=440)
        self.title = Label(self.details_frame_pro_surround, text="---Negombo Beach park", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=150, y=480)


        self.title = Label(self.details_frame_pro_surround, text="Eat & Drink...", font=("Goudy old style", 16, "bold"), bg="white")
        self.title.place(x=400, y=120)
        self.title = Label(self.details_frame_pro_surround, text="Restaurants.", font=("Goudy old style", 15, "bold"), fg="red", bg="white")
        self.title.place(x=400, y=160)
        self.title = Label(self.details_frame_pro_surround, text="---Olanro Hotel", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=400, y=200)
        self.title = Label(self.details_frame_pro_surround, text="---Dine Breakfast shop", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=400, y=240)
        self.title = Label(self.details_frame_pro_surround, text="---Sea joy Restaurant", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=400, y=280)
        self.title = Label(self.details_frame_pro_surround, text="Cafe & Bars.", font=("Goudy old style", 15, "bold"), fg="red", bg="white")
        self.title.place(x=400, y=320)
        self.title = Label(self.details_frame_pro_surround, text="---Peacock Sea food", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=400, y=360)
        self.title = Label(self.details_frame_pro_surround, text="---Spazio Pub", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=400, y=400)
        self.title = Label(self.details_frame_pro_surround, text="---Cafe Zen", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=400, y=440)
        self.title = Label(self.details_frame_pro_surround, text="Supermarkets.", font=("Goudy old style", 15, "bold"), fg="red", bg="white")
        self.title.place(x=400, y=440)
        self.title = Label(self.details_frame_pro_surround, text="---Food City", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=400, y=480)
        self.title = Label(self.details_frame_pro_surround, text="---Keels Super", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=400, y=520)

        self.title = Label(self.details_frame_pro_surround, text="Transports...", font=("Goudy old style", 16, "bold"), bg="white")
        self.title.place(x=650, y=120)
        self.title = Label(self.details_frame_pro_surround, text="Public Transports.", font=("Goudy old style", 15, "bold"), fg="red", bg="white")
        self.title.place(x=650, y=160)
        self.title = Label(self.details_frame_pro_surround, text="---Railway Station", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=650, y=200)
        self.title = Label(self.details_frame_pro_surround, text="    (Negombo) 2.2km", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=650, y=240)
        self.title = Label(self.details_frame_pro_surround, text="---Bus Station", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=650, y=280)
        self.title = Label(self.details_frame_pro_surround, text="    (Negombo) 1.6km", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=650, y=320)
        self.title = Label(self.details_frame_pro_surround, text="Closet airport.", font=("Goudy old style", 15, "bold"),fg="red", bg="white")
        self.title.place(x=650, y=360)
        self.title = Label(self.details_frame_pro_surround, text="---Bandaranayake", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=650, y=400)
        self.title = Label(self.details_frame_pro_surround, text="   International Airport 6km", font=("Goudy old style", 13, "bold"), bg="white")
        self.title.place(x=650, y=430)

# Back to Main Detail window
        self.back = Button(self.details_frame_pro_surround, text="BACK", font=("Times new roman", 16, "bold"), fg="Black", bg="Red", bd=4, command=self.opendetails)
        self.back.place(x=150, y=540, width=100, height=40)

# Exit button
        self.back = Button(self.details_frame_pro_surround, text="EXIT", font=("Times new roman", 16, "bold"), fg="white", bg="black", bd=4, command=self.exit_programme)
        self.back.place(x=850, y=540, width=100, height=40)



root = Tk()
login = Login(root)
root.mainloop()