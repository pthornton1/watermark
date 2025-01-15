from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageGrab


class Watermarker():
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Watermarker")
        self.window.config(padx=50,pady=50, height=1000,width=1000)
        self.ui_setup()
    
    
    
    def open_background_img(self):
        # Get user to select file with dialog
        filename = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("gif files", "*.gif*"), ("png files", "*.png")))
        
        #  open image with pillow and resize to fit canvas
        image = Image.open(filename)    
        image.thumbnail((800,800), Image.Resampling.LANCZOS)
        my_image = ImageTk.PhotoImage(image)

        # need to create reference to the image so it doesn't get garbage collected
        self.canvas.reference = my_image
        
        # update background on canvas
        self.canvas.itemconfig(self.canvas_bg_img, image=my_image)

        
        
        
    def open_watermark_img(self):
        # Get user to select file with dialog
        filename = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(("jpeg files", "*.jpg"), ("gif files", "*.gif*"), ("png files", "*.png")))
        
        #  open image with pillow and resize to fit canvas
        image = Image.open(filename)    
        image.thumbnail((100,100), Image.Resampling.LANCZOS)
        my_image = ImageTk.PhotoImage(image)

        # need to create reference to the image so it doesn't get garbage collected
        self.canvas.reference_2 = my_image
        
        # show image on canvas
        self.canvas.itemconfig(self.canvas_fg_img, image=my_image)


        
    def add_watermark_text(self):
        # Get user entered text
        text = self.watermark_text.get() 
        # Update text on canvas
        self.canvas.itemconfig(self.canvas_text, text=text)
        
        
    def save_img(self):
        # save postscipt image 
        fileName = self.save_path.get()
        self.canvas.postscript(file = fileName + '.eps') 
        # use PIL to convert to PNG 
        img = Image.open(fileName + '.eps') 
        img.save(fileName + '.png', 'png') 



    def ui_setup(self):
        """
        Creates tkinter window and renders GUI
        """
        # Program Title
        title_label = Label(text="Watermarker", font=("Times New Roman",35,"bold"))
        title_label.grid(column=0,row=0,columnspan=2)
        
        # Image Canvas
        self.canvas = Canvas(width=800,height=700)
        self.canvas.grid(column=0,row=1, columnspan=2)
        
        # Canvas background image to be updated
        self.canvas_bg_img = self.canvas.create_image(400,400)
        self.canvas_fg_img = self.canvas.create_image(400,400)
        #  canvas text to be updated
        self.canvas_text = self.canvas.create_text(400,400,text="", fill="white", font=("Times New Roman",20,"bold"), angle=45)
        
        
        # Background Image label
        background_img_label = Label(text="Background Image:")
        background_img_label.grid(column=0,row=2)

        # Search Background Image button
        search_background_button = Button(text="Select Image",command=self.open_background_img, width=13)
        search_background_button.grid(column=1,row=2)
        
        # Watermark Image label
        watermark_img_label = Label(text="Watermark Image:")
        watermark_img_label.grid(column=0,row=3)

        # Search Watermark Image button
        search_watermark_button = Button(text="Select Image",command=self.open_watermark_img, width=13)
        search_watermark_button.grid(column=1,row=3)
        
        # Watermark Text label
        self.watermark_text = Entry()
        self.watermark_text.insert(0, 'Watermark Text')
        self.watermark_text.grid(column=0,row=4)
        

        # Add Watermark text button
        search_watermark_button = Button(text="Add Text",command=self.add_watermark_text, width=13)
        search_watermark_button.grid(column=1,row=4)
        
         # Add Watermark text button
        self.save_path = Entry()
        self.save_path.insert(0, 'Save File Name')
        self.save_path.grid(column=0,row=5)
        
        # Save button
        save_button = Button(text="Save Image",command=self.save_img, width=13)
        save_button.grid(column=1,row=5)
        
    
        self.window.mainloop()