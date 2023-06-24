import customtkinter
from PIL import Image
from plyer import notification
import os
from connection import *
from user import User
from product import Product
import cart

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

user_main = User(0, None, None, None, None)

class App(customtkinter.CTk):
    width = 1000
    height = 600

    def __init__(self):
        super().__init__()
        self.title("AleDev Shop - By AleDev")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/img/background.png"), size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="AleDev Shop\nLogin Page", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.login_username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="Username")
        self.login_username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.login_password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="Password")
        self.login_password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 10))
        self.register_button = customtkinter.CTkButton(self.login_frame, text="Register", command=self.show_register, width=200)
        self.register_button.grid(row=4, column=0, padx=30, pady=(10, 10))

        # create register frame
        self.register_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.register_frame.grid(row=0, column=0, sticky="ns")
        self.register_label = customtkinter.CTkLabel(self.register_frame, text="AleDev Shop\nRegister Page", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.register_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.register_username_entry = customtkinter.CTkEntry(self.register_frame, width=200, placeholder_text="Username")
        self.register_username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.register_email_entry = customtkinter.CTkEntry(self.register_frame, width=200, placeholder_text="Email")
        self.register_email_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.register_password_entry = customtkinter.CTkEntry(self.register_frame, width=200, show="*", placeholder_text="Password")
        self.register_password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.register_confirm_password_entry = customtkinter.CTkEntry(self.register_frame, width=200, show="*", placeholder_text="Confirm password")
        self.register_confirm_password_entry.grid(row=4, column=0, padx=30, pady=(0, 15))
        self.register_button = customtkinter.CTkButton(self.register_frame, text="Register", command=self.register_event, width=200)
        self.register_button.grid(row=5, column=0, padx=30, pady=(15, 10))
        self.register_back_button = customtkinter.CTkButton(self.register_frame, text="Back", command=self.show_login, width=200)
        self.register_back_button.grid(row=6, column=0, padx=30, pady=(10, 10))

        # create main frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="ns")
        self.sidebar_frame.grid_columnconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="AleDev Shop", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 100))
        self.products_button = customtkinter.CTkButton(self.sidebar_frame, text="Products", command=self.list_products, width=200)
        self.products_button.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.cart_button = customtkinter.CTkButton(self.sidebar_frame, text="Cart", command=self.list_cart, width=200)
        self.cart_button.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.invoices_button = customtkinter.CTkButton(self.sidebar_frame, text="Invoices history", command=self.show_Invoices, width=200)
        self.invoices_button.grid(row=5, column=0, padx=20, pady=(10, 10))
        self.profile_button = customtkinter.CTkButton(self.sidebar_frame, text="Profile", command=self.show_profile, width=200)
        self.profile_button.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.logout_button = customtkinter.CTkButton(self.sidebar_frame, text="Logout", fg_color="red", command=self.logout_event, width=200)
        self.logout_button.grid(row=7, column=0, padx=20, pady=(10, 10))

        # Create frame content
        self.content_frame = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")
        self.content_frame.grid(row=0, rowspan=3, column=1, columnspan=2, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)
        # add title label to content frame
        self.title_label = customtkinter.CTkLabel(self.content_frame, text="AleDev Shop", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=30, pady=(30, 30))

        self.show_login()

    def list_products(self):
        # create products frame
        self.products_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0, fg_color="transparent")
        self.products_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        # create title frame
        self.products_title_frame = customtkinter.CTkFrame(self.products_frame, corner_radius=0, fg_color="transparent")
        self.products_title_frame.grid(row=0, column=0, sticky="nsew")
        self.products_title_frame.grid_columnconfigure(0, weight=1)
        self.products_title_frame.grid_rowconfigure(0, weight=1)
        self.products_title_label = customtkinter.CTkLabel(self.products_title_frame, text="Products", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.products_title_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")

        # create CTkScrollableFrame for products
        self.products_scrollable_frame = customtkinter.CTkScrollableFrame(self.products_frame, corner_radius=0, width=700, height=550)
        self.products_scrollable_frame.grid(row=1, rowspan=2, column=0, columnspan=2, sticky="nsew")
        self.products_scrollable_frame.grid_columnconfigure(0, weight=1)
        self.products_scrollable_frame.grid_rowconfigure(0, weight=1)

        __list_products = Get_products()

        # create list of products
        self.list_products = []

        for product in __list_products:
            self.product_frame = customtkinter.CTkFrame(self.products_scrollable_frame, border_color="gray", border_width=1)
            self.product_frame.grid(row=len(self.list_products), column=0, padx=20, pady=(0, 5), sticky="nsew")
            self.product_frame.grid_columnconfigure(0, weight=1)
            self.product_frame.grid_rowconfigure(0, weight=1)
            self.product_name_label = customtkinter.CTkLabel(self.product_frame, text=product[1], font=customtkinter.CTkFont(size=15, weight="bold"))
            self.product_name_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
            self.product_description_label = customtkinter.CTkLabel(self.product_frame, text=product[2], font=customtkinter.CTkFont(size=10))
            self.product_description_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
            self.product_price_label = customtkinter.CTkLabel(self.product_frame, text=str(product[3]) + "€", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.product_price_label.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="e")
            self.product_category_label = customtkinter.CTkLabel(self.product_frame, text=product[4], font=customtkinter.CTkFont(size=10))
            self.product_category_label.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="e")
            self.product_button = customtkinter.CTkButton(self.product_frame, text="Add to cart", command=lambda item=product: cart.add_item(item), width=200)
            self.product_button.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
            self.list_products.append(self.product_frame)

    def list_cart(self):
        # create cart frame
        self.cart_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0, fg_color="transparent")
        self.cart_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        # create title frame
        self.cart_title_frame = customtkinter.CTkFrame(self.cart_frame, corner_radius=0, fg_color="transparent")
        self.cart_title_frame.grid(row=0, column=0, sticky="nsew")
        self.cart_title_frame.grid_columnconfigure(0, weight=1)
        self.cart_title_frame.grid_rowconfigure(0, weight=1)
        self.cart_title_label = customtkinter.CTkLabel(self.cart_title_frame, text="Cart total: "+str(cart.get_total_price())+"€", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.cart_title_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")
        self.cart_button_clear = customtkinter.CTkButton(self.cart_title_frame, text="Clear cart", command=self.refresh_cart, width=100, fg_color="red")
        self.cart_button_clear.grid(row=0, column=1, padx=20, pady=(5, 5), sticky="e")
        self.cart_button_checkout = customtkinter.CTkButton(self.cart_title_frame, text="Pay", command=lambda: self.checkout(), width=100, fg_color="green")
        self.cart_button_checkout.grid(row=0, column=2, padx=20, pady=(5, 5), sticky="e")

        # create CTkScrollableFrame for cart
        self.cart_scrollable_frame = customtkinter.CTkScrollableFrame(self.cart_frame, corner_radius=0, width=700, height=550)
        self.cart_scrollable_frame.grid(row=1, rowspan=2, column=0, columnspan=2, sticky="nsew")
        self.cart_scrollable_frame.grid_columnconfigure(0, weight=1)
        self.cart_scrollable_frame.grid_rowconfigure(0, weight=1)

        # create list of products
        self.list_cart = []

        __items = cart.get_items()

        if len(__items) == 0:
            self.cart_empty_label = customtkinter.CTkLabel(self.cart_scrollable_frame, text="Your cart is empty", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.cart_empty_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
            self.list_cart.append(self.cart_empty_label)
            return

        for item in __items:
            self.cart_item_frame = customtkinter.CTkFrame(self.cart_scrollable_frame, border_color="gray", border_width=1)
            self.cart_item_frame.grid(row=len(self.list_cart), column=0, padx=20, pady=(0, 5), sticky="nsew")
            self.cart_item_frame.grid_columnconfigure(0, weight=1)
            self.cart_item_frame.grid_rowconfigure(0, weight=1)
            self.cart_item_name_label = customtkinter.CTkLabel(self.cart_item_frame, text=item[1], font=customtkinter.CTkFont(size=15, weight="bold"))
            self.cart_item_name_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
            self.cart_item_ammount_label = customtkinter.CTkLabel(self.cart_item_frame, text="Ammount: " + str(item[5]), font=customtkinter.CTkFont(size=10, weight="bold"))
            self.cart_item_ammount_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
            self.cart_item_price_label = customtkinter.CTkLabel(self.cart_item_frame, text="Total: "+str(item[6]) + "€", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.cart_item_price_label.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="e")
            self.cart_item_total_ammount_label = customtkinter.CTkLabel(self.cart_item_frame, text="Unit: "+str(item[3])+"€", font=customtkinter.CTkFont(size=10))
            self.cart_item_total_ammount_label.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="e")
            self.list_cart.append(self.cart_item_frame)

    def checkout(self):
        if len(cart.get_items()) == 0:
            log("err", "Your cart is empty")
            notification.notify(
                title="Error",
                message="Your cart is empty",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            return

        self.checkout_window = customtkinter.CTk()
        self.checkout_window.title("Checkout")
        self.checkout_window.geometry(f"{350}x{240}")
        self.checkout_window.resizable(False, False)

        self.checkout_frame = customtkinter.CTkFrame(self.checkout_window, width=350, height=500)
        self.checkout_frame.pack(pady=10, padx=10, fill="x")

        self.checkout_title = customtkinter.CTkLabel(self.checkout_frame, text="Checkout", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.checkout_title.pack(pady=10, padx=10, fill="x")

        self.checkout_description = customtkinter.CTkLabel(self.checkout_frame, text="Are you sure you want to buy all the products", font=customtkinter.CTkFont(size=15))
        self.checkout_description.pack(pady=10, padx=10, fill="x")

        self.checkout_total = customtkinter.CTkLabel(self.checkout_frame, text="Total: "+str(cart.get_total_price())+"€", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.checkout_total.pack(pady=10, padx=10, fill="x")

        self.checkout_button_frame = customtkinter.CTkFrame(self.checkout_frame, width=350, height=50)
        self.checkout_button_frame.pack(pady=10, padx=10, fill="x")

        self.checkout_button_cancel = customtkinter.CTkButton(self.checkout_button_frame, text="Cancel", fg_color="red", command=self.checkout_window.destroy)
        self.checkout_button_cancel.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        self.checkout_button_confirm = customtkinter.CTkButton(self.checkout_button_frame, text="Confirm", fg_color="green", command=self.checkout_confirm)
        self.checkout_button_confirm.pack(side="right", padx=10, pady=10, fill="x", expand=True)

        self.checkout_window.mainloop()

    def checkout_confirm(self):
        if len(cart.get_items()) == 0:
            log("err", "Your cart is empty")
            notification.notify(
                title="Error",
                message="Your cart is empty",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            return

        Create_invoice(user_main.id, cart.get_items())
        self.checkout_window.destroy()
        self.refresh_cart()

    def refresh_cart(self):
        self.cart_scrollable_frame.destroy()
        cart.clear_items()

        # create list of products
        self.list_cart = []

        __items = cart.get_items()

        if len(__items) == 0:
            self.cart_empty_label = customtkinter.CTkLabel(self.cart_scrollable_frame, text="Your cart is empty",
                                                           font=customtkinter.CTkFont(size=15, weight="bold"))
            self.cart_empty_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
            self.list_cart.append(self.cart_empty_label)
            return

        for item in __items:
            self.cart_item_frame = customtkinter.CTkFrame(self.cart_scrollable_frame, border_color="gray",
                                                          border_width=1)
            self.cart_item_frame.grid(row=len(self.list_cart), column=0, padx=20, pady=(0, 5), sticky="nsew")
            self.cart_item_frame.grid_columnconfigure(0, weight=1)
            self.cart_item_frame.grid_rowconfigure(0, weight=1)
            self.cart_item_name_label = customtkinter.CTkLabel(self.cart_item_frame, text=item[1],
                                                               font=customtkinter.CTkFont(size=15, weight="bold"))
            self.cart_item_name_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
            self.cart_item_ammount_label = customtkinter.CTkLabel(self.cart_item_frame, text="Ammount: " + str(item[5]),
                                                                  font=customtkinter.CTkFont(size=10, weight="bold"))
            self.cart_item_ammount_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
            self.cart_item_price_label = customtkinter.CTkLabel(self.cart_item_frame,
                                                                text="Total: " + str(item[6]) + "€",
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
            self.cart_item_price_label.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="e")
            self.cart_item_total_ammount_label = customtkinter.CTkLabel(self.cart_item_frame,
                                                                        text="Unit: " + str(item[3]) + "€",
                                                                        font=customtkinter.CTkFont(size=10))
            self.cart_item_total_ammount_label.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="e")
            self.list_cart.append(self.cart_item_frame)

    def show_Invoices(self):
        # create products frame
        self.invoices_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0, fg_color="transparent")
        self.invoices_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # create title frame
        self.invoices_title_frame = customtkinter.CTkFrame(self.invoices_frame, corner_radius=0, fg_color="transparent")
        self.invoices_title_frame.grid(row=0, column=0, sticky="nsew")
        self.invoices_title_frame.grid_columnconfigure(0, weight=1)
        self.invoices_title_frame.grid_rowconfigure(0, weight=1)
        self.invoices_title_label = customtkinter.CTkLabel(self.invoices_title_frame, text="Invoices history", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.invoices_title_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")

        # create CTkScrollableFrame for products
        self.invoices_scrollable_frame = customtkinter.CTkScrollableFrame(self.invoices_frame, corner_radius=0, width=700, height=550)
        self.invoices_scrollable_frame.grid(row=1, rowspan=2, column=0, columnspan=2, sticky="nsew")
        self.invoices_scrollable_frame.grid_columnconfigure(0, weight=1)
        self.invoices_scrollable_frame.grid_rowconfigure(0, weight=1)

        __list_invoices = Get_invoices_by_user(user_main.id)

        # create list of products
        self.list_invoices = []

        for profile in __list_invoices:
            self.invoices_frame = customtkinter.CTkFrame(self.invoices_scrollable_frame, border_color="gray",
                                                        border_width=1)
            self.invoices_frame.grid(row=len(self.list_invoices), column=0, padx=20, pady=(0, 5), sticky="nsew")
            self.invoices_frame.grid_columnconfigure(0, weight=1)
            self.invoices_frame.grid_rowconfigure(0, weight=1)
            self.invoices_id_label = customtkinter.CTkLabel(self.invoices_frame, text="Id invoice: "+str(profile[0]), font=customtkinter.CTkFont(size=15, weight="bold"))
            self.invoices_id_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
            self.invoices_time_label = customtkinter.CTkLabel(self.invoices_frame, text=str(profile[1]),
                                                              font=customtkinter.CTkFont(size=15, weight="bold"))
            self.invoices_time_label.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="e")
            self.invoices_button = customtkinter.CTkButton(self.invoices_frame, text="View invoice",
                                                          command=lambda id=profile[0]: self.show_invoice(id), width=200)
            self.invoices_button.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
            self.list_invoices.append(self.invoices_frame)

    def show_invoice(self, id):
        # create products frame
        self.invoice_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0, fg_color="transparent")
        self.invoice_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        # create title frame
        self.invoice_title_frame = customtkinter.CTkFrame(self.invoice_frame, corner_radius=0, fg_color="transparent")
        self.invoice_title_frame.grid(row=0, column=0, sticky="nsew")
        self.invoice_title_frame.grid_columnconfigure(0, weight=1)
        self.invoice_title_frame.grid_rowconfigure(0, weight=1)
        self.invoice_title_label = customtkinter.CTkLabel(self.invoice_title_frame, text="Invoice id "+str(id)+" detail",
                                                           font=customtkinter.CTkFont(size=20, weight="bold"))
        self.invoice_title_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")
        self.invoice_button = customtkinter.CTkButton(self.invoice_title_frame, text="Back to invoices", width=200, command=self.show_profile)
        self.invoice_button.grid(row=0, column=1, padx=20, pady=(5, 5), sticky="e")
        # create textbox
        self.invoice_textbox = customtkinter.CTkTextbox(self.invoice_frame, corner_radius=0, width=700, height=550)
        self.invoice_textbox.grid(row=1, rowspan=2, column=0, columnspan=2, padx=20, pady=(5, 5), sticky="nsew")

        __list_invoice = Get_invoice_by_id(id)

        # create list of products
        self.total_price = 0
        self.invoice_textbox.insert("end", "Invoice id: "+str(__list_invoice[0][0])+" Date: "+str(__list_invoice[0][1])+"\n")
        self.invoice_textbox.insert("end", "\nUser: "+str(__list_invoice[0][4])+"\n")
        self.invoice_textbox.insert("end", "\nList products: \n")
        self.invoice_textbox.insert("end", "\n-------------------------------------------------------------------\n")
        for invoice in __list_invoice:
            if invoice[3] > 1: self.total_price += invoice[7] * invoice[3]
            else: self.total_price += invoice[7]
            self.invoice_textbox.insert("end", "\nProduct name: "+str(invoice[6])+" Quantity: "+str(invoice[3])+" Units Price: "+str(invoice[7])+"€\n")
        self.invoice_textbox.insert("end", "\n-------------------------------------------------------------------\n")
        self.invoice_textbox.insert("end", "\nTotal price: "+str(self.total_price)+"€\n")

        self.invoice_textbox.configure(state="disabled")

    def show_profile(self):
        # create profile frame
        self.profile_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0, fg_color="transparent")
        self.profile_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # create title frame
        self.profile_title_frame = customtkinter.CTkFrame(self.profile_frame, corner_radius=0, fg_color="transparent")
        self.profile_title_frame.grid(row=0, column=0, sticky="nsew")
        self.profile_title_frame.grid_columnconfigure(0, weight=1)
        self.profile_title_frame.grid_rowconfigure(0, weight=1)
        self.profile_title_label = customtkinter.CTkLabel(self.profile_title_frame, text="Profile",
                                                              font=customtkinter.CTkFont(size=20, weight="bold"))
        self.profile_title_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")

        # create from to display user info
        self.profile_form_frame = customtkinter.CTkFrame(self.profile_frame, corner_radius=0, fg_color="transparent")
        self.profile_form_frame.grid(row=1, column=0, sticky="nsew")
        self.profile_form_frame.grid_columnconfigure(0, weight=1)
        self.profile_form_frame.grid_rowconfigure(0, weight=1)

        # create username label
        self.profile_username_label = customtkinter.CTkLabel(self.profile_form_frame, text="Username: "+user_main.username,
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.profile_username_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")

        # create email label
        self.profile_email_label = customtkinter.CTkLabel(self.profile_form_frame, text="Email: "+user_main.email,
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.profile_email_label.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="w")

        # create button frame
        self.profile_button_frame = customtkinter.CTkFrame(self.profile_frame, corner_radius=0, fg_color="transparent")
        self.profile_button_frame.grid(row=2, column=0, sticky="nsew")
        self.profile_button_frame.grid_columnconfigure(0, weight=1)
        self.profile_button_frame.grid_rowconfigure(0, weight=1)

        # create edit button
        self.profile_edit_button = customtkinter.CTkButton(self.profile_button_frame, text="Edit profile", width=200, command=self.show_edit_profile)
        self.profile_edit_button.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")

        # create change password button
        self.profile_change_password_button = customtkinter.CTkButton(self.profile_button_frame, text="Change password", width=200, command=self.show_change_password)
        self.profile_change_password_button.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="w")

    def show_edit_profile(self):
        self.edit_window = customtkinter.CTk()
        self.edit_window.title("Edit profile")
        self.edit_window.geometry(f"400x300+{int(self.edit_window.winfo_screenwidth()/2 - 400/2)}+{int(self.edit_window.winfo_screenheight()/2 - 300/2)}")
        self.edit_window.resizable(False, False)

        # create edit profile frame
        self.edit_profile_frame = customtkinter.CTkFrame(self.edit_window, corner_radius=0, fg_color="transparent")
        self.edit_profile_frame.grid(row=0, column=0, sticky="nsew")
        self.edit_profile_frame.grid_columnconfigure(0, weight=1)
        self.edit_profile_frame.grid_rowconfigure(0, weight=1)

        # create username label
        self.edit_username_label = customtkinter.CTkLabel(self.edit_profile_frame, text="Username: "+user_main.username,
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.edit_username_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")

        # create email label
        self.edit_email_label = customtkinter.CTkLabel(self.edit_profile_frame, text="Email: "+user_main.email,
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.edit_email_label.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="w")

        # create new username label
        self.edit_new_username_label = customtkinter.CTkLabel(self.edit_profile_frame, text="New username:",
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.edit_new_username_label.grid(row=2, column=0, padx=20, pady=(5, 5), sticky="w")

        # create new username entry
        self.edit_new_username_entry = customtkinter.CTkEntry(self.edit_profile_frame, width=300)
        self.edit_new_username_entry.grid(row=3, column=0, padx=20, pady=(5, 5), sticky="w")

        # create new email label
        self.edit_new_email_label = customtkinter.CTkLabel(self.edit_profile_frame, text="New email:",
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.edit_new_email_label.grid(row=4, column=0, padx=20, pady=(5, 5), sticky="w")

        # create new email entry
        self.edit_new_email_entry = customtkinter.CTkEntry(self.edit_profile_frame, width=300)
        self.edit_new_email_entry.grid(row=5, column=0, padx=20, pady=(5, 5), sticky="w")

        # create button frame
        self.edit_button_frame = customtkinter.CTkFrame(self.edit_profile_frame, corner_radius=0, fg_color="transparent")
        self.edit_button_frame.grid(row=6, column=0, sticky="nsew")
        self.edit_button_frame.grid_columnconfigure(0, weight=1)
        self.edit_button_frame.grid_rowconfigure(0, weight=1)

        # create save button
        self.edit_save_button = customtkinter.CTkButton(self.edit_button_frame, text="Save", width=150, fg_color='green', command=lambda: self.save_edit_profile(self.edit_new_username_entry.get(), self.edit_new_email_entry.get()))
        self.edit_save_button.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")

        # create cancel button
        self.edit_cancel_button = customtkinter.CTkButton(self.edit_button_frame, text="Cancel", width=150, fg_color='red', command=lambda: self.edit_window.destroy())
        self.edit_cancel_button.grid(row=0, column=1, padx=20, pady=(5, 5), sticky="e")

        self.edit_window.mainloop()

    def save_edit_profile(self, new_username, new_email):
        if len(new_username) > 0:
            user_main.username = new_username
            notification.notify(
                title="Success",
                message="Username changed successfully",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
        if len(new_email) > 0:
            user_main.email = new_email
            notification.notify(
                title="Success",
                message="Email changed successfully",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
        Update_user(user_main)
        self.edit_username_label.configure(text="Username: "+user_main.username)
        self.edit_email_label.configure(text="Email: "+user_main.email)
        self.edit_window.destroy()

    def show_change_password(self):
        # create change password window
        self.change_password_window = customtkinter.CTk()
        self.change_password_window.title("Change password")
        self.change_password_window.geometry(f"400x300+{int(self.change_password_window.winfo_screenwidth() / 2 - 400 / 2)}+{int(self.change_password_window.winfo_screenheight() / 2 - 300 / 2)}")
        self.change_password_window.resizable(False, False)

        # create change password frame
        self.change_password_frame = customtkinter.CTkFrame(self.change_password_window, corner_radius=0, fg_color="transparent")
        self.change_password_frame.grid(row=0, column=0, sticky="nsew")
        self.change_password_frame.grid_columnconfigure(0, weight=1)
        self.change_password_frame.grid_rowconfigure(0, weight=1)

        # create old password label
        self.change_password_old_password_label = customtkinter.CTkLabel(self.change_password_frame, text="Old password:",
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.change_password_old_password_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")

        # create old password entry
        self.change_password_old_password_entry = customtkinter.CTkEntry(self.change_password_frame, width=300, show="*")
        self.change_password_old_password_entry.grid(row=1, column=0, padx=20, pady=(5, 5), sticky="w")

        # create new password label
        self.change_password_new_password_label = customtkinter.CTkLabel(self.change_password_frame, text="New password:",
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.change_password_new_password_label.grid(row=2, column=0, padx=20, pady=(5, 5), sticky="w")

        # create new password entry
        self.change_password_new_password_entry = customtkinter.CTkEntry(self.change_password_frame, width=300, show="*")
        self.change_password_new_password_entry.grid(row=3, column=0, padx=20, pady=(5, 5), sticky="w")

        # create confirm new password label
        self.change_password_confirm_new_password_label = customtkinter.CTkLabel(self.change_password_frame, text="Confirm new password:",
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.change_password_confirm_new_password_label.grid(row=4, column=0, padx=20, pady=(5, 5), sticky="w")

        # create confirm new password entry
        self.change_password_confirm_new_password_entry = customtkinter.CTkEntry(self.change_password_frame, width=300, show="*")
        self.change_password_confirm_new_password_entry.grid(row=5, column=0, padx=20, pady=(5, 5), sticky="w")

        # create button frame
        self.change_password_button_frame = customtkinter.CTkFrame(self.change_password_frame, corner_radius=0, fg_color="transparent")
        self.change_password_button_frame.grid(row=6, column=0, sticky="nsew")
        self.change_password_button_frame.grid_columnconfigure(0, weight=1)
        self.change_password_button_frame.grid_rowconfigure(0, weight=1)

        # create save button
        self.change_password_save_button = customtkinter.CTkButton(self.change_password_button_frame, text="Save", width=150, fg_color='green', command=lambda: self.save_change_password(self.change_password_old_password_entry.get(), self.change_password_new_password_entry.get(), self.change_password_confirm_new_password_entry.get()))
        self.change_password_save_button.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")

        # create cancel button
        self.change_password_cancel_button = customtkinter.CTkButton(self.change_password_button_frame, text="Cancel", width=150, fg_color='red', command=lambda: self.change_password_window.destroy())
        self.change_password_cancel_button.grid(row=0, column=1, padx=20, pady=(5, 5), sticky="e")

        self.change_password_window.mainloop()

    def save_change_password(self, old_password, new_password, confirm_new_password):
        if new_password != confirm_new_password:
            notification.notify(
                title="Error",
                message="Passwords do not match",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            return

        if old_password == user_main.password:
            user_main.password = new_password
            Change_password(user_main)
            notification.notify(
                title="Success",
                message="Password changed successfully",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            self.change_password_window.destroy()
        else:
            notification.notify(
                title="Error",
                message="Old password incorrect",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )

    def admin_acctions(self):
        # create admin frame
        self.admin_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0, fg_color="transparent")
        self.admin_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # create title frame
        self.admin_title_frame = customtkinter.CTkFrame(self.admin_frame, corner_radius=0, fg_color="transparent")
        self.admin_title_frame.grid(row=0, column=0, sticky="nsew")
        self.admin_title_frame.grid_columnconfigure(0, weight=1)
        self.admin_title_frame.grid_rowconfigure(0, weight=1)
        self.admin_title_label = customtkinter.CTkLabel(self.admin_title_frame, text="Product management",
                                                           font=customtkinter.CTkFont(size=20, weight="bold"))
        self.admin_title_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")

        # create add product button
        self.admin_add_product_button = customtkinter.CTkButton(self.admin_title_frame, text="Add product", width=150, fg_color='green', command=self.show_add_product)
        self.admin_add_product_button.grid(row=0, column=1, padx=20, pady=(5, 5), sticky="e")

        # create CTkScrollableFrame for products
        self.admin_scrollable_frame = customtkinter.CTkScrollableFrame(self.admin_frame, corner_radius=0,
                                                                          width=700, height=550)
        self.admin_scrollable_frame.grid(row=1, rowspan=2, column=0, columnspan=2, sticky="nsew")
        self.admin_scrollable_frame.grid_columnconfigure(0, weight=1)
        self.admin_scrollable_frame.grid_rowconfigure(0, weight=1)

        __list_admin = Get_products()

        # create list of products
        self.list_admin = []

        for product in __list_admin:
            self.product_frame = customtkinter.CTkFrame(self.admin_scrollable_frame, border_color="gray",
                                                        border_width=1)
            self.product_frame.grid(row=len(self.list_admin), column=0, padx=20, pady=(0, 5), sticky="nsew")
            self.product_frame.grid_columnconfigure(0, weight=1)
            self.product_frame.grid_rowconfigure(0, weight=1)
            self.product_name_label = customtkinter.CTkLabel(self.product_frame, text=product[1],
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
            self.product_name_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
            self.product_description_label = customtkinter.CTkLabel(self.product_frame, text=product[2],
                                                                    font=customtkinter.CTkFont(size=10))
            self.product_description_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
            self.product_price_label = customtkinter.CTkLabel(self.product_frame, text=str(product[3]) + "€",
                                                              font=customtkinter.CTkFont(size=15, weight="bold"))
            self.product_price_label.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="e")
            self.product_category_label = customtkinter.CTkLabel(self.product_frame, text=product[4],
                                                                 font=customtkinter.CTkFont(size=10))
            self.product_category_label.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="e")
            # ponemos 2 botones en el frame eliminar y editar
            self.product_button_frame = customtkinter.CTkFrame(self.product_frame, corner_radius=0, fg_color="transparent")
            self.product_button_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
            self.product_button_frame.grid_columnconfigure(0, weight=1)
            self.product_button_frame.grid_rowconfigure(0, weight=1)
            self.button_edit = customtkinter.CTkButton(self.product_button_frame, text="Edit", fg_color="green",
                                                       command=lambda product_id=product[0]: self.eddit_product(product_id))
            self.button_edit.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")
            self.button_delete = customtkinter.CTkButton(self.product_button_frame, text="Delete", fg_color="red",
                                                         command=lambda product_id=product[0]: self.delete_product(product[0]))
            self.button_delete.grid(row=0, column=1, padx=(10, 0), pady=5, sticky="e")
            self.list_admin.append(self.product_frame)

    def show_add_product(self):
        _list_categories = Get_catalog()

        self.list_categories = []
        self.list_categories.append("Select category")
        for category in _list_categories:
            self.list_categories.append(category[1])

        _value_categoty = None
        def set_value_category(value):
            nonlocal _value_categoty
            _value_categoty = value

        # create add product frame
        self.add_product_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0, fg_color="transparent")
        self.add_product_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.add_product_frame.grid_columnconfigure(0, weight=1)
        self.add_product_frame.grid_rowconfigure(0, weight=1)
        self.add_product_title_label = customtkinter.CTkLabel(self.add_product_frame, text="Add product",
                                                              font=customtkinter.CTkFont(size=20, weight="bold"))
        self.add_product_title_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")
        # create product name label and entry
        self.add_product_name_label = customtkinter.CTkLabel(self.add_product_frame, text="Product name",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.add_product_name_label.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="w")
        self.add_product_name_entry = customtkinter.CTkEntry(self.add_product_frame, width=400)
        self.add_product_name_entry.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
        # create product description label and entry
        self.add_product_description_label = customtkinter.CTkLabel(self.add_product_frame, text="Product description",
                                                                    font=customtkinter.CTkFont(size=15, weight="bold"))
        self.add_product_description_label.grid(row=3, column=0, padx=20, pady=(20, 0), sticky="w")
        self.add_product_description_entry = customtkinter.CTkEntry(self.add_product_frame, width=400)
        self.add_product_description_entry.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="w")
        # create product price label and entry
        self.add_product_price_label = customtkinter.CTkLabel(self.add_product_frame, text="Product price",
                                                              font=customtkinter.CTkFont(size=15, weight="bold"))
        self.add_product_price_label.grid(row=5, column=0, padx=20, pady=(20, 0), sticky="w")
        self.add_product_price_entry = customtkinter.CTkEntry(self.add_product_frame, width=400)
        self.add_product_price_entry.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="w")
        # create product category label and dropdown
        self.add_product_category_label = customtkinter.CTkLabel(self.add_product_frame, text="Product category",
                                                                    font=customtkinter.CTkFont(size=15, weight="bold"))
        self.add_product_category_label.grid(row=7, column=0, padx=20, pady=(20, 0), sticky="w")
        self.add_product_category_entry = customtkinter.CTkOptionMenu(self.add_product_frame, values=self.list_categories, command=set_value_category)
        self.add_product_category_entry.grid(row=8, column=0, padx=20, pady=(0, 20), sticky="w")
        # create add product button
        self.add_product_button = customtkinter.CTkButton(self.add_product_frame, text="Add product", fg_color="green",
                                                            command=lambda: self.add_product(self.add_product_name_entry.get(),
                                                                                             self.add_product_description_entry.get(),
                                                                                             self.add_product_price_entry.get(), _value_categoty))
        self.add_product_button.grid(row=9, column=0, padx=20, pady=(0, 20), sticky="w")

        # Create back button
        self.back_button = customtkinter.CTkButton(self.add_product_frame, text="Back", fg_color="red",
                                                   command=lambda: self.refres_admin_frame())
        self.back_button.grid(row=9, column=0, padx=20, pady=(0, 20), sticky="e")
        self.list_admin.append(self.add_product_frame)

    def add_product(self, product_name, product_description, product_price, product_category):

        if product_name == "" or product_description == "" or product_price == "" or product_category == None:
            notification.notify(
                title="Error",
                message="All fields are required",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            return

        produc = Product(None, None, None, None, None, None)
        produc.name = product_name
        produc.description = product_description
        produc.price = product_price

        _id_categories = Get_catalog()

        for category in _id_categories:
            if category[1] == product_category:
                produc.category = category[0]
                break

        Insert_product(produc)
        notification.notify(
            title="Success",
            message="Product added",
            app_icon="img/LogoNegro.ico",
            timeout=5,
        )
        # refresh admin frame
        self.add_product_frame.destroy()
        self.refres_admin_frame()


    def eddit_product(self, product_id):
        # get product
        product = Get_product(product_id)

        # get categories
        _list_categories = Get_catalog()

        self.list_categories = []
        self.list_categories.append("Select category")
        for category in _list_categories:
            self.list_categories.append(category[1])

        _value_categoty = None

        def set_value_category(value):
            nonlocal _value_categoty
            _value_categoty = value

        # create add product frame
        self.edit_product_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0, fg_color="transparent")
        self.edit_product_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.edit_product_frame.grid_columnconfigure(0, weight=1)
        self.edit_product_frame.grid_rowconfigure(0, weight=1)
        self.edit_product_title_label = customtkinter.CTkLabel(self.edit_product_frame, text="Add product",
                                                              font=customtkinter.CTkFont(size=20, weight="bold"))
        self.edit_product_title_label.grid(row=0, column=0, padx=20, pady=(5, 5), sticky="w")
        # create product name label and entry
        self.edit_product_name_label = customtkinter.CTkLabel(self.edit_product_frame, text="Product name",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.edit_product_name_label.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="w")
        self.edit_product_name_entry = customtkinter.CTkEntry(self.edit_product_frame, width=400)
        self.edit_product_name_entry.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
        # create product description label and entry
        self.edit_product_description_label = customtkinter.CTkLabel(self.edit_product_frame, text="Product description",
                                                                    font=customtkinter.CTkFont(size=15, weight="bold"))
        self.edit_product_description_label.grid(row=3, column=0, padx=20, pady=(20, 0), sticky="w")
        self.edit_product_description_entry = customtkinter.CTkEntry(self.edit_product_frame, width=400)
        self.edit_product_description_entry.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="w")
        # create product price label and entry
        self.edit_product_price_label = customtkinter.CTkLabel(self.edit_product_frame, text="Product price",
                                                              font=customtkinter.CTkFont(size=15, weight="bold"))
        self.edit_product_price_label.grid(row=5, column=0, padx=20, pady=(20, 0), sticky="w")
        self.edit_product_price_entry = customtkinter.CTkEntry(self.edit_product_frame, width=400)
        self.edit_product_price_entry.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="w")
        # create product category label and dropdown
        self.edit_product_category_label = customtkinter.CTkLabel(self.edit_product_frame, text="Product category",
                                                                 font=customtkinter.CTkFont(size=15, weight="bold"))
        self.edit_product_category_label.grid(row=7, column=0, padx=20, pady=(20, 0), sticky="w")
        self.edit_product_category_entry = customtkinter.CTkOptionMenu(self.edit_product_frame,
                                                                      values=self.list_categories,
                                                                      command=set_value_category)
        self.edit_product_category_entry.grid(row=8, column=0, padx=20, pady=(0, 20), sticky="w")
        # create add product button
        self.edit_product_button = customtkinter.CTkButton(self.edit_product_frame, text="Save", fg_color="green",
                                                          command=lambda: self.update_product(product[0], self.edit_product_name_entry.get(),
                                                                                        self.edit_product_description_entry.get(),
                                                                                        self.edit_product_price_entry.get(),
                                                                                        _value_categoty))
        self.edit_product_button.grid(row=9, column=0, padx=20, pady=(0, 20), sticky="w")

        # Create back button
        self.edit_back_button = customtkinter.CTkButton(self.edit_product_frame, text="Back", fg_color="red",
                                                   command=lambda: self.refres_admin_frame())
        self.edit_back_button.grid(row=9, column=0, padx=20, pady=(0, 20), sticky="e")
        self.list_admin.append(self.edit_product_frame)

        # set values
        self.edit_product_name_entry.insert(0, product[1])
        self.edit_product_description_entry.insert(0, product[2])
        self.edit_product_price_entry.insert(0, product[3])
        self.edit_product_category_entry.set(product[4])

    def update_product(self, product_id, product_name, product_description, product_price, product_category):
        if product_name == "" or product_description == "" or product_price == "" or product_category == "":
            notification.notify(
                title="Error",
                message="All fields are required",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
        else:
            produc = Product(None, None, None, None, None, None)
            produc.id = product_id
            produc.name = product_name
            produc.description = product_description
            produc.price = product_price

            _id_categories = Get_catalog()

            for category in _id_categories:
                if category[1] == product_category:
                    produc.category = category[0]
                    break

            Update_product(produc)
            notification.notify(
                title="Success",
                message="Product updated",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            # refresh admin frame
            self.edit_product_frame.destroy()
            self.refres_admin_frame()

    def delete_product(self, product_id):
        Delete_product(product_id)
        notification.notify(
            title="Success",
            message="Product deleted",
            app_icon="img/LogoNegro.ico",
            timeout=5,
        )
        # refresh admin frame
        self.add_product_frame.destroy()
        self.refres_admin_frame()

    def refres_admin_frame(self):
        self.admin_scrollable_frame.destroy()

        __list_admin = Get_products()

        # create list of products
        self.list_admin = []

        for product in __list_admin:
            self.product_frame = customtkinter.CTkFrame(self.admin_scrollable_frame, border_color="gray",
                                                        border_width=1)
            self.product_frame.grid(row=len(self.list_admin), column=0, padx=20, pady=(0, 5), sticky="nsew")
            self.product_frame.grid_columnconfigure(0, weight=1)
            self.product_frame.grid_rowconfigure(0, weight=1)
            self.product_name_label = customtkinter.CTkLabel(self.product_frame, text=product[1],
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
            self.product_name_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
            self.product_description_label = customtkinter.CTkLabel(self.product_frame, text=product[2],
                                                                    font=customtkinter.CTkFont(size=10))
            self.product_description_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
            self.product_price_label = customtkinter.CTkLabel(self.product_frame, text=str(product[3]) + "€",
                                                              font=customtkinter.CTkFont(size=15, weight="bold"))
            self.product_price_label.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="e")
            self.product_category_label = customtkinter.CTkLabel(self.product_frame, text=product[4],
                                                                 font=customtkinter.CTkFont(size=10))
            self.product_category_label.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="e")
            # ponemos 2 botones en el frame eliminar y editar
            self.product_button_frame = customtkinter.CTkFrame(self.product_frame, corner_radius=0,
                                                               fg_color="transparent")
            self.product_button_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
            self.product_button_frame.grid_columnconfigure(0, weight=1)
            self.product_button_frame.grid_rowconfigure(0, weight=1)
            self.button_edit = customtkinter.CTkButton(self.product_button_frame, text="Edit", fg_color="green",
                                                       command=lambda product_id=product[0]: self.eddit_product(product_id))
            self.button_edit.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="w")
            self.button_delete = customtkinter.CTkButton(self.product_button_frame, text="Delete", fg_color="red",
                                                         command=lambda product_id=product[0]: self.delete_product(product_id))
            self.button_delete.grid(row=0, column=1, padx=(10, 0), pady=5, sticky="e")
            self.list_admin.append(self.product_frame)

    def admin_invoices(self):
        # create admin invoices frame
        self.admin_invoices_frame = customtkinter.CTkFrame(self.content_frame, corner_radius=0, fg_color="transparent")
        self.admin_invoices_frame.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="nsew")
        self.admin_invoices_frame.grid_columnconfigure(0, weight=1)
        self.admin_invoices_frame.grid_rowconfigure(0, weight=1)
        self.admin_invoices_frame.grid_rowconfigure(1, weight=1)

        # create text to total facturation
        self.total_facturation_label = customtkinter.CTkLabel(self.admin_invoices_frame, text="Total facturation: " + str(Get_total_facturation()) + "€",
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.total_facturation_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

        # create text to total facturation to product
        self.total_facturation_product_label = customtkinter.CTkLabel(self.admin_invoices_frame, text="Total facturation to product: ",
                                                                font=customtkinter.CTkFont(size=15, weight="bold"))
        self.total_facturation_product_label.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="w")

        # create CTkOptionMenu to select product
        self.product_list = Get_products()

        self.product_list_name = []
        self.product_list_name.append("Select product")

        for product in self.product_list:
            self.product_list_name.append(product[1])

        def set_value_category(value):
            for product in self.product_list:
                if value == product[1]:
                    self.total_facturation_product_label.configure(text="Total facturation to product: " + str(Get_total_facturation_by_product(product[0])) + "€")

        self.option_menu_product = customtkinter.CTkOptionMenu(self.admin_invoices_frame, values=self.product_list_name, command=set_value_category)
        self.option_menu_product.grid(row=1, column=1, padx=20, pady=(20, 0), sticky="w")

    def show_login(self):
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.register_frame.grid_forget()
        self.main_frame.grid_forget()

    def show_register(self):
        self.register_frame.grid(row=0, column=0, sticky="ns")
        self.login_frame.grid_forget()
        self.main_frame.grid_forget()

    def login_event(self):
        user_main.username = self.login_username_entry.get()
        user_main.password = self.login_password_entry.get()

        if not self.login_username_entry.get() or not self.login_password_entry.get():
            log("err", "Username or password empty")
            notification.notify(
                title="Error",
                message="Username or password empty",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            return

        if Login(user_main)[0]:
            notification.notify(
                title="Success",
                message="Login successful",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            info = Login(user_main)[1]
            user_main.id = info[0]
            user_main.username = info[1]
            user_main.email = info[2]
            user_main.password = info[3]
            user_main.role = info[4]

            if user_main.role == 1:
                self.admin_button = customtkinter.CTkButton(self.sidebar_frame, text="Product management", command=self.admin_acctions, width=200)
                self.admin_button.grid(row=1, column=0, padx=20, pady=(10, 10))
                self.admin_invoinces_button = customtkinter.CTkButton(self.sidebar_frame, text="Invoices management", command=self.admin_invoices, width=200)
                self.admin_invoinces_button.grid(row=2, column=0, padx=20, pady=(10, 10))

            self.login_frame.grid_forget()
            self.register_frame.grid_forget()
            self.main_frame.grid(row=0, column=0, sticky="nsew")

            self.login_username_entry.delete(0, "end")
            self.login_password_entry.delete(0, "end")
        else:
            log("err", "Username or password incorrect")
            notification.notify(
                title="Error",
                message="Username or password incorrect",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            return


    def register_event(self):
        user_main.username = self.register_username_entry.get()
        user_main.email = self.register_email_entry.get()
        user_main.password = self.register_password_entry.get()
        user_main.role = "client"

        if not self.register_username_entry.get() or not self.register_email_entry.get():
            log("err", "Username or email empty")
            notification.notify(
                title="Error",
                message="Username or email empty",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            return

        if not self.register_email_entry.get().endswith("@gmail.com"):
            self.register_email_entry.delete(0, "end")
            log("err", "Email invalid")
            notification.notify(
                title="Error",
                message="Email invalid",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            return

        if self.register_password_entry.get() != self.register_confirm_password_entry.get() or self.register_password_entry.get() == "" or self.register_confirm_password_entry.get() == "":
            self.register_password_entry.delete(0, "end")
            self.register_confirm_password_entry.delete(0, "end")
            log("err", "Passwords don't match")
            notification.notify(
                title="Error",
                message="Passwords don't match",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            return

        if Register(user_main):
            notification.notify(
                title="Success",
                message="User registered",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            self.show_login()
        else:
            log("err", "User not registered")
            notification.notify(
                title="Error",
                message="User not registered",
                app_icon="img/LogoNegro.ico",
                timeout=5,
            )
            self.register_username_entry.delete(0, "end")
            self.register_email_entry.delete(0, "end")
            self.register_password_entry.delete(0, "end")
            self.register_confirm_password_entry.delete(0, "end")

    def logout_event(self):
        user_main.id = None
        user_main.username = None
        user_main.email = None
        user_main.password = None
        user_main.role = None
        self.show_login()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    connect()