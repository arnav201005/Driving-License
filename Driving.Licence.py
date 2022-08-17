from tkinter import*
root=Tk()
root.title("DRIVING LICENSE")
root.geometry("300x400")
root.configure(bg="white")
canvas = Canvas(root, width=300, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="Driving Licence")
label_Id_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="Id :")
label_name_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="Name :")
label_pin_tag = canvas.create_text(40, 205, font=('Times', '16', 'bold'), text="Pin :")
label_Address = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Address :")
label_vehicle_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="Authorisation to drive the following vehicles:")
label_dob_tag = canvas.create_text(40, 180, font=('Times', '16', 'bold'), text="DOB :")

label_Id = Label(root)
#add label for ID
label_name = Label(root)
#add label for name
label_dob = Label(root)
#add label for Date-of-birth
label_pin = Label(root)
#add label for Pin
label_Address = Label(root)
#add label for Address
label_vehicle = Label(root)
#add label for Authorisation to drive the following vehicles


#add function
def myCardDetails():
Id_value = "33106789"
print(type(Id_value))
name = "Arnav Thakur"
print(type(name))
dob ="10/may/2010"
print(type(dob))
pin  = "110018"
print(type(Pin-NO))
Address - "S2/121 OLD MAHAVIR NAGAR,TILAK NAGAR NEW DELHI"
print(type(Address))
vehicle - "Two Four"
print (type(vehicle))

label_Id['text'] = Id_value
label_no['text'] = name
label_dob["text"]=  dob
label_adress['text'] = Address
label_vehicle['text'] = vehicle
   
   
  #add buttonbutton1= Button(root, text ="show my Driving License", command = myCardDetails)
button1 = Button(root, text = "Show My Driving License", command = myCardDetails() )
button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(120, 165, anchor=CENTER, window=label_Id)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_pin_window = canvas.create_window(90, 205, anchor=CENTER, window=label_Pinno)
label_Adress_window = canvas.create_window(155, 252, anchor=CENTER, window=label_Address)
label_address_window = canvas.create_window(80, 52, anchor=CENTER, window=label_Authorisationtodrivethefollowingvehicles)
label_vehicle_window = canvas.create_window(40, 165, anchor=CENTER, window=label_vehicle )
label_dob_window = canvas.create_window(40, 180, anchor=CENTER, window=label_dob )
 
canvas.pack()
   
root.mainloop()  
