from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Invoice App")
        bg_color="seagreen"
        title=Label(self.root,text="Invoice Generator Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",22,"bold"),pady=2).pack(fill=X)
        #==========variables==========
        #============Fruits========
        self.apple=IntVar()
        self.banana=IntVar()
        self.chickoo=IntVar()
        self.pear=IntVar()
        self.papaya=IntVar()
        self.water_melon=IntVar()
        #===========grocery================
        self.rice=IntVar()
        self.daal=IntVar()
        self.salt=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        self.cooking_oil=IntVar()
        #============Vegetables===============
        self.onion=IntVar()
        self.potato=IntVar()
        self.carrot=IntVar()
        self.brinjal=IntVar()
        self.capsicum=IntVar()
        self.cabbage=IntVar()

        #======Total Product Price & Tax Variables=====
        self.fruits_price=StringVar()
        self.grocery_price=StringVar()
        self.vegetables_price=StringVar()

        self.fruits_tax=StringVar()
        self.grocery_tax=StringVar()
        self.vegetables_tax=StringVar()

        #==============Customer========
        self.c_name=StringVar()
        self.c_phon=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()
        


        #========Customer Details frame
        F1=LabelFrame(self.root,bd=7,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=70,relwidth=1)

        cname_lbl=Label(F1,text="Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl=Label(F1,text="Phone no.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        cbill_lbl=Label(F1,text="Bill no.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_btn=Button(F1,text="Search" ,command=self.find_bill,width=10,bd=4,font="arial 12 bold").grid(row=0,column=6,padx=15,pady=10)

         #========Fruits frame
        F2=LabelFrame(self.root,bd=7,relief=GROOVE,text="Fruits",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=165,width=325,height=380)

        apple_lbl=Label(F2,text="Apple",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        apple_txt=Entry(F2,width=10,textvariable=self.apple,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Banana_lbl=Label(F2,text="Banana",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Banana_txt=Entry(F2,width=10,textvariable=self.banana,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        chickoo_lbl=Label(F2,text="Chickoo",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        chickoo_txt=Entry(F2,width=10,textvariable=self.chickoo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        pear_lbl=Label(F2,text="Pear",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        pear_txt=Entry(F2,width=10,textvariable=self.pear,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        papaya_lbl=Label(F2,text="Papaya",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        papaya_txt=Entry(F2,width=10,textvariable=self.papaya,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        watermelon_lbl=Label(F2,text="Watermelon",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        watermelon_txt=Entry(F2,width=10,textvariable=self.water_melon,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #========Grocery frame
        F3=LabelFrame(self.root,bd=7,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=165,width=325,height=380)

        rice_lbl=Label(F3,text="Rice",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        daal_lbl=Label(F3,text="Daal",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        daal_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        salt_lbl=Label(F3,text="Salt",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        salt_txt=Entry(F3,width=10,textvariable=self.salt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        tea_lbl=Label(F3,text="Tea",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        oil_lbl=Label(F3,text="Cooking Oil",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        oil_txt=Entry(F3,width=10,textvariable=self.cooking_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #========Vegetables frame
        F4=LabelFrame(self.root,bd=7,relief=GROOVE,text="Vegetables",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=165,width=325,height=380)

        onion_lbl=Label(F4,text="Onion",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        onion_txt=Entry(F4,width=10,textvariable=self.onion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        potato_lbl=Label(F4,text="Potato",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        potato_txt=Entry(F4,width=10,textvariable=self.potato,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        carrot_lbl=Label(F4,text="Carrot",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        carrot_txt=Entry(F4,width=10,textvariable=self.carrot,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        brinjal_lbl=Label(F4,text="Brinjal",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F4,width=10,textvariable=self.brinjal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        capsicum=Label(F4,text="Capsicum",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        capsicum_txt=Entry(F4,width=10,textvariable=self.capsicum,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        cabbage_lbl=Label(F4,text="Cabbage",font=("times new roman",15,"bold"),bg=bg_color,fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        cabbage_txt=Entry(F4,width=10,textvariable=self.cabbage,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===============Bill Area Frame
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=165,width=355,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=5,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL) 
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)  
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)  
        self.txtarea.pack(fill=BOTH,expand=1)

        #=========Button Frame
        F6=LabelFrame(self.root,bd=7,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=555,relwidth=1,height=145)

        #========Total Prices
        m1=Label(F6,text="Total Fruits Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.fruits_price,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F6,text="Total Vegetables Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.vegetables_price,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        #========Tax Price
        tax_m1=Label(F6,text="Fruits Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        tax_m1_txt=Entry(F6,width=18,textvariable=self.fruits_tax,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        tax_m2=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        tax_m2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        tax_m3=Label(F6,text="Vegetables Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        tax_m3_txt=Entry(F6,width=18,textvariable=self.vegetables_tax,font="arial 10 bold",bd=5,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_f=Frame(F6,bd=5,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)

        total_btn=Button(btn_f,command=self.total,text="Total",bg="gold",fg="black",bd=2,pady=15,width=11,font="arial 12 bold").grid(row=0,column=0,padx=5)

        Gbill_btn=Button(btn_f,text="Generate Bill",command=self.bill_area,bg="gold",fg="black",bd=2,pady=15,width=11,font="arial 12 bold").grid(row=0,column=1,padx=5)

        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="gold",fg="black",bd=2,pady=15,width=11,font="arial 12 bold").grid(row=0,column=2,padx=5)

        exit_btn=Button(btn_f,text="Exit",command=self.exit_app,bg="gold",fg="black",bd=2,pady=15,width=11,font="arial 12 bold").grid(row=0,column=3,padx=5)
        self.welcome_bill()

    
    def total(self):
        self.f_a_p=self.apple.get()*40
        self.f_b_p=self.banana.get()*3
        self.f_c_p=self.chickoo.get()*5
        self.f_pe_p=self.pear.get()*40
        self.f_pa_p=self.papaya.get()*40
        self.f_w_p=self.water_melon.get()*60

        self.total_fruits_price=float(
                                    self.f_a_p+
                                    self.f_b_p+
                                    self.f_c_p+
                                    self.f_pe_p+
                                    self.f_pa_p+
                                    self.f_w_p        
                                    )
        self.fruits_price.set("Rs.  "+str(self.total_fruits_price))
        self.f_tax=round((self.total_fruits_price*0.05),2)
        self.fruits_tax.set("Rs.  "+str(self.f_tax))

        self.g_r_p=self.rice.get()*70
        self.g_d_p=self.daal.get()*55
        self.g_sa_p=self.salt.get()*20
        self.g_su_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*120
        self.g_co_p=self.cooking_oil.get()*180

        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_d_p+
                                    self.g_sa_p+
                                    self.g_su_p+
                                    self.g_t_p+
                                    self.g_co_p        
                                    )
        self.grocery_price.set("Rs.  "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs.  "+str(self.g_tax))

        self.v_o_p=self.onion.get()*40
        self.v_po_p=self.potato.get()*20
        self.v_ca_p=self.carrot.get()*45
        self.v_br_p=self.brinjal.get()*40
        self.v_cm_p=self.capsicum.get()*60
        self.v_ce_p=self.cabbage.get()*55

        self.total_vegetables_price=float(
                                    self.v_o_p+
                                    self.v_po_p+
                                    self.v_ca_p+
                                    self.v_br_p+
                                    self.v_cm_p+
                                    self.v_ce_p       
                                    )
        self.vegetables_price.set("Rs.  "+str(self.total_vegetables_price))
        self.v_tax=round((self.total_vegetables_price*0.05),2)
        self.vegetables_tax.set("Rs.  "+str(self.v_tax))

        self.total_bill=float(self.total_fruits_price+
                              self.total_grocery_price+
                              self.total_vegetables_price+
                              self.f_tax+
                              self.g_tax+
                              self.v_tax
                              )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWELCOME\n")
        self.txtarea.insert(END,f"\n Bill no. :  {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone no. : {self.c_phon.get()}")
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n======================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are must")
        elif self.fruits_price.get()=="Rs.  0.0" and self.grocery_price.get()=="Rs.  0.0" and self.vegetables_price.get()=="Rs.  0.0":
            messagebox.showerror("Error","No Product Purchased")
        else:
            self.welcome_bill()
            #========fruits======
            if self.apple.get()!=0:
                self.txtarea.insert(END,f"\n Apple\t\t{self.apple.get()}\t\t{self.f_a_p}")
            if self.banana.get()!=0:
                self.txtarea.insert(END,f"\n Banana\t\t{self.banana.get()}\t\t{self.f_b_p}")
            if self.chickoo.get()!=0:
                self.txtarea.insert(END,f"\n Chickoo\t\t{self.chickoo.get()}\t\t{self.f_c_p}")
            if self.pear.get()!=0:
                self.txtarea.insert(END,f"\n Pear\t\t{self.pear.get()}\t\t{self.f_pe_p}")
            if self.papaya.get()!=0:
                self.txtarea.insert(END,f"\n Papaya\t\t{self.papaya.get()}\t\t{self.f_pa_p}")
            if self.water_melon.get()!=0:
                self.txtarea.insert(END,f"\n Water Melon\t\t{self.water_melon.get()}\t\t{self.f_w_p}")

            #========Grocery======
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.salt.get()!=0:
                self.txtarea.insert(END,f"\n Salt\t\t{self.salt.get()}\t\t{self.g_sa_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_su_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
            if self.cooking_oil.get()!=0:
                self.txtarea.insert(END,f"\n Cooking Oil\t\t{self.cooking_oil.get()}\t\t{self.g_co_p}")

            #========vegetables======
            if self.onion.get()!=0:
                self.txtarea.insert(END,f"\n Onion\t\t{self.onion.get()}\t\t{self.v_o_p}")
            if self.potato.get()!=0:
                self.txtarea.insert(END,f"\n Potato\t\t{self.potato.get()}\t\t{self.v_po_p}")
            if self.carrot.get()!=0:
                self.txtarea.insert(END,f"\n Carrot\t\t{self.carrot.get()}\t\t{self.v_ca_p}")
            if self.brinjal.get()!=0:
                self.txtarea.insert(END,f"\n Brinjal\t\t{self.brinjal.get()}\t\t{self.v_br_p}")
            if self.capsicum.get()!=0:
                self.txtarea.insert(END,f"\n Capsicum\t\t{self.Capsicum.get()}\t\t{self.v_cm_p}")
            if self.cabbage.get()!=0:
                self.txtarea.insert(END,f"\n Cabbage\t\t{self.cabbage.get()}\t\t{self.v_ce_p}")

            self.txtarea.insert(END,f"\n--------------------------------------")
            if self.fruits_tax.get()!="Rs.  0.0":
                self.txtarea.insert(END,f"\n Fruits Tax\t\t\t{self.fruits_tax.get()}")
            if self.grocery_tax.get()!="Rs.  0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.vegetables_tax.get()!="Rs.  0.0":
                self.txtarea.insert(END,f"\n Vegetables Tax\t\t\t{self.vegetables_tax.get()}")

            self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {self.total_bill}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            self.save_bill()


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} Saved Successfully")
        else:
            return


    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
            
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear ?")
        if op>0:

            #============Fruits========
            self.apple.set(0)
            self.banana.set(0)
            self.chickoo.set(0)
            self.pear.set(0)
            self.papaya.set(0)
            self.water_melon.set(0)
            #===========grocery================
            self.rice.set(0)
            self.daal.set(0)
            self.salt.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            self.cooking_oil.set(0)
            #============Vegetables===============
            self.onion.set(0)
            self.potato.set(0)
            self.carrot.set(0)
            self.brinjal.set(0)
            self.capsicum.set(0)
            self.cabbage.set(0)

            #======Total Product Price & Tax Variables=====
            self.fruits_price.set("")
            self.grocery_price.set("")
            self.vegetables_price.set("")

            self.fruits_tax.set("")
            self.grocery_tax.set("")
            self.vegetables_tax.set("")

            #==============Customer========
            self.c_name.set("")
            self.c_phon.set("")
            
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()


    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()



root=Tk()
obj=Bill_App(root)
root.mainloop()


        