from tkinter import*
import math
import random, os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        
        self.root.title("Billing Software")
        bg_color="#074463"
        #bg_color="#aa0c75"
        title=Label(self.root, text="Billing Desk",bd=12, relief=GROOVE,bg= bg_color,fg="white",font=("times new roman", 30,"bold"),pady=2).pack(fill=X)
        #===========Cosmetics=========
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.shampoo = IntVar()
        self.gel = IntVar()
        self.body_wash = IntVar()

        #========grocery======
        self.oil = IntVar()
        self.sugar = IntVar()
        self.rice = IntVar()
        self.noodles = IntVar()
        self.tea = IntVar()
        self.kitkat = IntVar()

        #=========cold drinks====
        self.pepsi = IntVar()
        self.maza = IntVar()
        self.deo = IntVar()
        self.thumbs_up = IntVar()
        self.frooti = IntVar()
        self.limca = IntVar()

        #=== total product price and tax variable======

        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()


        #=====Customere====

        self.c_name = StringVar()
        self.c_phon = StringVar()
        
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


        F1= LabelFrame(self.root,bd=10,relief=GROOVE, text="Customer Details",font=("times new roman", 15,"bold"), fg="gold", bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1, text="Customer name",bg=bg_color, fg="white", font=("times new roman", 15,"bold")).grid(row=0,column=0,padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable= self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Mobile No.",bg=bg_color, fg="white", font=("times new roman", 15,"bold")).grid(row=0,column=2,padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable= self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number",bg=bg_color, fg="white", font=("times new roman", 15,"bold")).grid(row=0,column=4,padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable= self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1, text="Search",command= self.find_bill, textvariable= self.find_bill, width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10, pady=10)

        F2= LabelFrame(self.root,bd=10,relief=GROOVE, text="Cosmetics",font=("times new roman", 15,"bold"), fg="gold", bg=bg_color)
        F2.place(x=5,y=180,width=325, height=380)

        bath_lbl1= Label(F2, text="Bath Soap", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0,padx=10, pady=10,sticky="w")
        bath_lbl1_txt = Entry(F2, width=10,textvariable= self.soap, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        face_cream_lbl1= Label(F2, text="Face Cream", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0,padx=10, pady=10,sticky="w")
        face_cream_lbl1_txt = Entry(F2, width=10,textvariable= self.face_cream ,font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        face_w_lbl1= Label(F2, text="Face Wash", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0,padx=10, pady=10,sticky="w")
        face_w_lbl1_txt = Entry(F2, width=10, textvariable= self.face_wash, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        hair_s_lbl1= Label(F2, text="Hair Shampoo", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0,padx=10, pady=10,sticky="w")
        hair_s_lbl1_txt = Entry(F2, width=10, textvariable= self.shampoo, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        hair_g_lbl1= Label(F2, text="Hair gel", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4, column=0,padx=10, pady=10,sticky="w")
        hair_g_lbl1_txt = Entry(F2, width=10,textvariable= self.gel, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        body_lbl1= Label(F2, text="Body Wash", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5, column=0,padx=10, pady=10,sticky="w")
        body_lbl1_txt = Entry(F2, width=10,textvariable= self.body_wash, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)





        F3= LabelFrame(self.root,bd=10,relief=GROOVE, text="Grocery",font=("times new roman", 15,"bold"), fg="gold", bg=bg_color)
        F3.place(x=340,y=180,width=325, height=380)

        oil_lbl1= Label(F3, text="Oil", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0,padx=10, pady=10,sticky="w")
        oil_lbl1_txt = Entry(F3, width=10,textvariable= self.oil, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        sugar_lbl1= Label(F3, text="Sugar", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0,padx=10, pady=10,sticky="w")
        sugar_lbl1_txt = Entry(F3, width=10,textvariable= self.sugar, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        rice_lbl1= Label(F3, text="Rice", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0,padx=10, pady=10,sticky="w")
        rice_lbl1_txt = Entry(F3, width=10,textvariable= self.rice, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        noodles_lbl1= Label(F3, text="Noodles", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0,padx=10, pady=10,sticky="w")
        noodles_lbl1_txt = Entry(F3, width=10,textvariable= self.noodles, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        tea_lbl1= Label(F3, text="Tea", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4, column=0,padx=10, pady=10,sticky="w")
        tea_lbl1_txt = Entry(F3, width=10,textvariable= self.tea, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        kitkat_lbl1= Label(F3, text="Kitkat", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5, column=0,padx=10, pady=10,sticky="w")
        kitkat_lbl1_txt = Entry(F3, width=10,textvariable= self.kitkat, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)


        F4= LabelFrame(self.root,bd=10,relief=GROOVE, text="Cold Drink",font=("times new roman", 15,"bold"), fg="gold", bg=bg_color)
        F4.place(x=670,y=180,width=325, height=380)

        pepsi_lbl1= Label(F4, text="pepsi", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0, column=0,padx=10, pady=10,sticky="w")
        pepsi_lbl1_txt = Entry(F4, width=10,textvariable= self.pepsi, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        maza_lbl1= Label(F4, text="Maza", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1, column=0,padx=10, pady=10,sticky="w")
        maza_lbl1_txt = Entry(F4, width=10,textvariable= self.maza, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        deo_lbl1= Label(F4, text="Deo", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2, column=0,padx=10, pady=10,sticky="w")
        deo_lbl1_txt = Entry(F4, width=10,textvariable= self.deo, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        thumbs_lbl1= Label(F4, text="Thumbs up", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3, column=0,padx=10, pady=10,sticky="w")
        thumbs_lbl1_txt = Entry(F4, width=10,textvariable= self.thumbs_up, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        frooti_lbl1= Label(F4, text="Frooti", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4, column=0,padx=10, pady=10,sticky="w")
        frooti_lbl1_txt = Entry(F4, width=10,textvariable= self.frooti, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        limca_lbl1= Label(F4, text="Limca", font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5, column=0,padx=10, pady=10,sticky="w")
        limca_lbl1_txt = Entry(F4, width=10,textvariable= self.limca, font=("times new roman", 16,"bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

        F5= Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350, height=380)
        bill_title=Label(F5,text="Bill Area", bd=7, relief=GROOVE, font="arial 16 bold").pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5, yscrollcommand=scrol_y)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)



        F6= LabelFrame(self.root,bd=10,relief=GROOVE, text="Bill Menu",font=("times new roman", 15,"bold"), fg="gold", bg=bg_color)
        F6.place(x=0,y=560,relwidth=1, height=140)

        m1_lbl=Label(F6, text="Total Cosmetic Price",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=0,padx=20, pady=1, sticky="w")
        m1_txt=Entry(F6, width=18,textvariable= self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=1, padx=10, pady=1)

        m2_lbl=Label(F6, text="Total Grocery Price",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=1, column=0,padx=20, pady=1, sticky="w")
        m2_txt=Entry(F6, width=18,textvariable= self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,column=1, padx=10, pady=1)

        m3_lbl=Label(F6, text="Total Cold Drinks Price",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=2, column=0,padx=20, pady=1, sticky="w")
        m3_txt=Entry(F6, width=18,textvariable= self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2,column=1, padx=10, pady=1)

        c1_lbl=Label(F6, text="Cosmetic Tax",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=2,padx=20, pady=1, sticky="w")
        c1_txt=Entry(F6, width=18,textvariable= self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=3, padx=10, pady=1)

        c2_lbl=Label(F6, text="Grocery Tax",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=1, column=2,padx=20, pady=1, sticky="w")
        c2_txt=Entry(F6, width=18,textvariable= self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,column=3, padx=10, pady=1)

        c3_lbl=Label(F6, text="Cold Drinks Tax",bg=bg_color,fg="white", font=("times new roman", 14, "bold")).grid(row=2, column=2,padx=20, pady=1, sticky="w")
        c3_txt=Entry(F6, width=18,textvariable= self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2,column=3, padx=10, pady=1)

        btn_F=Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)

        total_btn=Button(btn_F,command= self.total, text="Total", bg="cadetblue", fg="white",bd=2,pady=15, width=10, font="arial 14 bold").grid(row=0, column=0, padx=5, pady=5)
        GBill_btn=Button(btn_F,command = self.bill_area, text="Generate Bill", bg="cadetblue", fg="white",bd=2,pady=15, width=10, font="arial 14 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn=Button(btn_F,command= self.clear_data, text="Clear", bg="cadetblue", fg="white",bd=2,pady=15, width=10, font="arial 14 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn=Button(btn_F, command= self.Exit_app, text="Exit", bg="cadetblue", fg="white",bd=2,pady=15, width=10, font="arial 14 bold").grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()


    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*100
        self.c_hs_p=self.shampoo.get()*400
        self.c_g_p=self.gel.get()*140
        self.c_bw_p=self.body_wash.get()*240
        
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_g_p+
                                    self.c_bw_p

                                    )

        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        self.g_o_p=self.oil.get()*450
        self.g_s_p=self.sugar.get()*160
        self.g_r_p=self.rice.get()*150
        self.g_n_p=self.noodles.get()*40
        self.g_t_p=self.tea.get()*2
        self.g_k_p=self.kitkat.get()*10

        self.total_grocery_price=float(
                                    self.g_o_p+
                                    self.g_s_p+
                                    self.g_r_p+
                                    self.g_n_p+
                                    self.g_t_p+
                                    self.g_k_p

                                    )

        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.03),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))


        self.cd_p_p=self.pepsi.get()*40
        self.cd_m_p=self.maza.get()*120
        self.cd_d_p=self.deo.get()*100
        self.cd_t_p=self.thumbs_up.get()*400
        self.cd_f_p=self.frooti.get()*140
        self.cd_l_p=self.limca.get()*240

        self.total_cold_drink_price=float(
                                    self.cd_p_p+
                                    self.cd_m_p+
                                    self.cd_d_p+
                                    self.cd_t_p+
                                    self.cd_f_p+
                                    self.cd_l_p

                                    )

        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.d_tax=round((self.total_cold_drink_price*0.02),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))


        self.Total_bill= float( 
                                self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_cold_drink_price+
                                self.c_tax+
                                self.g_tax+
                                self.d_tax

                            )

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END , "\tWelcome GDL Retail\n")
        self.txtarea.insert(END , f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END , f"\n Customer Number : {self.c_name.get()}")
        self.txtarea.insert(END , f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END , f"\n=====================================")
        self.txtarea.insert(END , f"\n Products\t\tQTY\tPrice")
        self.txtarea.insert(END , f"\n====================================")

    def bill_area(self):
        if self.c_name.get()=='' or self.c_phon.get()=='':
            messagebox.showerror("Error", "Customers details are must")

        elif self.cosmetic_price.get()=='Rs. 0.0' and self.grocery_price.get()=='Rs. 0.0' and self.cold_drink_price.get()=='Rs. 0.0':
            messagebox.showerror("Error", "No Product purchased")
        else:
            self.welcome_bill()



            #=======costmetics========
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.shampoo.get()!=0:
                self.txtarea.insert(END,f"\n Shampoo\t\t{self.shampoo.get()}\t\t{self.c_hs_p}")
            if self.gel.get()!=0:
                self.txtarea.insert(END,f"\n Gel\t\t{self.gel.get()}\t\t{self.c_g_p}")
            if self.body_wash.get()!=0:
                self.txtarea.insert(END,f"\n Body Wash\t\t{self.body_wash.get()}\t\t{self.c_bw_p}")



                #======grocery========
            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\n oil\t\t{self.oil.get()}\t\t{self.g_o_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.noodles.get()!=0:
                self.txtarea.insert(END,f"\n Noodles\t\t{self.noodles.get()}\t\t{self.g_n_p}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
            if self.kitkat.get()!=0:
                self.txtarea.insert(END,f"\n Kitkat\t\t{self.kitkat.get()}\t\t{self.g_k_p}")




                #=========cold_drinks=============

            if self.pepsi.get()!=0:
                self.txtarea.insert(END,f"\n pepsi\t\t{self.pepsi.get()}\t\t{self.cd_p_p}")
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.cd_m_p}")
            if self.deo.get()!=0:
                self.txtarea.insert(END,f"\n Deo\t\t{self.deo.get()}\t\t{self.cd_d_p}")
            if self.thumbs_up.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs up\t\t{self.thumbs_up.get()}\t\t{self.cd_t_p}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.cd_f_p}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.cd_l_p}")

            self.txtarea.insert(END , f"\n-----------------------------------")
            if  self.cosmetic_tax.get!="Rs. 0.0":
                self.txtarea.insert(END , f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            if  self.grocery_tax.get!="Rs. 0.0":
                self.txtarea.insert(END , f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if  self.cold_drink_tax.get!="Rs. 0.0":
                self.txtarea.insert(END , f"\n Drinks Tax\t\t\t{self.cold_drink_tax.get()}")
            
            self.txtarea.insert(END , f"\n------------------------------------")
            self.txtarea.insert(END , f"\n Total Bill: \t\t\t Rs. {self.Total_bill}")
            self.txtarea.insert(END , f"\n------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op>0:

            self.bill_data=self.txtarea.get('1.0', END)
            f1=open("bills/" +str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. :{self.bill_no.get()} saved Successfully")

        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:

                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"

        if present == "no":
            messagebox.showerror("Error", "Invalid bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear", "Do you really want to clear")

        if op>0:
            
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.shampoo.set(0)
            self.gel.set(0)
            self.body_wash.set(0)

            #========grocery======
            self.oil.set(0)
            self.sugar.set(0)
            self.rice.set(0)
            self.noodles.set(0)
            self.tea.set(0)
            self.kitkat.set(0)

            #=========cold drinks====
            self.pepsi.set(0)
            self.maza.set(0)
            self.deo.set(0)
            self.thumbs_up.set(0)
            self.frooti.set(0)
            self.limca.set(0)

            #=== total product price and tax variable======

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")


            #=====Customere====

            self.c_name.set("")
            self.c_phon.set("")
            
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit", "Do you really want to exit")

        if op>0:
            self.root.destroy()







root = Tk()
obj = Bill_App(root)
root.mainloop()