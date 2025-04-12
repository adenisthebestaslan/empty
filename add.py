import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import SUCCESS
from bs4 import BeautifulSoup, Comment
from tkinter import filedialog

def addcontent(div_ids, soup, dropdown):
    addcontent = tk.Tk()
    addcontent.title("Add Content")
    addcontent.geometry("400x300")
        
    overalltext = ["Headings","Paragraphs","Fonts"]
    textcolours = ["red","blue","green","purple","black","white"]
    overallvisuals =["Backgrounds","Images"]
    Headngs = ["h1","h2","h3","h4","h5","h6"]
    Paragraph = ["p","a","ul","b","i","u","comments"]
    Backgrounds = ["background-color","background-image",]
    Images = ["img"]
    padding = ["padding,"]
    HTMLstuff= ["HTML insert","buttons","image buttons","lists","Styled buttons"]
    audiostuff = ["audio"]

    dropdowncontent = ttk.Combobox(addcontent, values=overalltext, width=25)
    dropdowncontent.set("text.")  # Default text
    dropdowncontent.pack(pady=20)

    dropdowncontent1 = ttk.Combobox(addcontent, values=overallvisuals, width=25)
    dropdowncontent1.set("images.")  # Default text
    dropdowncontent1.pack(pady=20)

    dropdowncontent2 = ttk.Combobox(addcontent, values=padding, width=25)
    dropdowncontent2.set("padding.")  # Default text
    dropdowncontent2.pack(pady=20)

    dropdowncontent3 = ttk.Combobox(addcontent, values=HTMLstuff, width=25)
    dropdowncontent3.set("HTML Insert.")  # Default text
    dropdowncontent3.pack(pady=20)

    dropdowncontent4 = ttk.Combobox(addcontent, values=audiostuff, width=25)
    dropdowncontent4.set("Audio.")  # Default text
    dropdowncontent4.pack(pady=20)

    
    

    def nextbutton():
        whereback = ["div","body"]
        nonlocal textcolours
        OPTION = dropdowncontent.get()
        if OPTION == "text.":
            OPTION = dropdowncontent1.get()
            if OPTION == "images.":
                OPTION = dropdowncontent2.get()
                if OPTION == "padding.":
                    OPTION = dropdowncontent3.get()
                    if OPTION == "HTML Insert.":
                        OPTION = dropdowncontent4.get()


                                                

            
        #100 lines :D
        addcontent1 = tk.Tk()
        addcontent1.title("Continue")
        addcontent1.geometry("400x300")
        #It seems to not be reading the options from here
        print("OPTION", OPTION)
        if OPTION == "Headings":
            print("hEADINGS")
            dropdownheading = ttk.Combobox(addcontent1, values=Headngs, width=25)
            dropdownheading.set("Select a heading :)")  # Default text
            dropdownheading.pack(pady=20)
            textboxContentheading = ttk.Entry(addcontent1)
            textboxContentheading.pack(pady=20)
        if OPTION == "Paragraphs":
            print("Paragraphs")
            dropdownparagraphs = ttk.Combobox(addcontent1, values=Paragraph, width=40)
            dropdownparagraphs.set("Select a paragraph, then insert the text it will show")  # Default text
            dropdownparagraphs.pack(pady=20)
            textboxContentparagraph = ttk.Entry(addcontent1)
            textboxContentparagraph.pack(pady=20)
        if OPTION == "Fonts":
            print("FONTS")
            print(OPTION) 
            fontfamily = ttk.Entry(addcontent1)
            fontfamily.insert(0, "Font Family")
            fontfamily.pack(pady=20)
            colourselect = ttk.Combobox(addcontent1, values=textcolours, width=25)
            colourselect.set("select a colour")  # Default text
            colourselect.pack(pady=20)      
            Fontname = ttk.Entry(addcontent1)
            Fontname.insert(0, "Font Name")
            Fontname.pack(pady=20)
        if OPTION == "Images":
            print("skibdi simga")
            file_path = filedialog.askopenfilename(title="Select a file")  # Prints the selected file path
            print(file_path)
            with1 = ttk.Entry(addcontent1)
            with1.insert(0, "with of image")
            with1.pack(pady=20)
            altxt = ttk.Entry(addcontent1)
            altxt.insert(0, "alt text")
            altxt.pack(pady=20)
            print("done")
        if OPTION == "Backgrounds":
            print("Backgrounds")
            dropdownbackground = ttk.Combobox(addcontent1, values=Backgrounds, width=25)
            dropdownbackground.set("Background")  # Default text
            dropdownbackground.pack(pady=20)

        if OPTION == "padding,":
            

            print("Padding")


            label = ttk.Label(addcontent1, text="the default mesurmeants are for centering the div. you can change them to your liking. the first one is top, the second bottom, the third left, fourth right.")
            print("making labe'")
            label.pack(pady=20)
            print("made")

            paddingy = ttk.Entry(addcontent1)
            paddingy.insert(0, "50")
            paddingy.pack(pady=20)

            paddingy1 = ttk.Entry(addcontent1)
            paddingy1.insert(0, "850")
            paddingy1.pack(pady=20)
            
            paddingx = ttk.Entry(addcontent1)
            paddingx.insert(0, "50")
            paddingx.pack(pady=20)

            paddingx1 = ttk.Entry(addcontent1)
            paddingx1.insert(0, "850")
            paddingx1.pack(pady=20)
                
            wherepad = ttk.Combobox(addcontent1, values=whereback, width=25)
            wherepad.set('div or body')
            wherepad.pack(pady=20)
            dividpad= ttk.Combobox(addcontent1, values=div_ids, width=25)
            dividpad.set('div ids')
            dividpad.pack(pady=20)
            ttk.Button(addcontent1, text="Padding", style=SUCCESS)


        if OPTION == "HTML insert":
            print("HTML")
            textbox = ttk.ScrolledText(addcontent1,  font=("Arial", 12), height=10, width=40)
            textbox.pack(padx=10, pady=10)

        if OPTION == "buttons":
            print("HTML")
            buttoncontent = ttk.Entry(addcontent1)
            buttoncontent.pack(pady=20)
            buttonsize = ttk.Entry(addcontent1)
            buttonsize.pack(pady=20)
            buttonlink = ttk.Entry(addcontent1)
            buttonlink.pack(pady=20)
        
        if OPTION == "image buttons":
            file_path = filedialog.askopenfilename(title="Select a file")  # Prints the selected file path
            print(file_path)
            buttoncontent = ttk.Entry(addcontent1)
            buttoncontent.pack(pady=20)
            buttonsize = ttk.Entry(addcontent1)
            buttonsize.pack(pady=20)
            buttonlink = ttk.Entry(addcontent1)
            buttonlink.pack(pady=20)                


        if OPTION == "lists":
            listtype = ["ol","ul"]
            # seperate your list items by comma. example: hi,i,am,a,list
            listitems = ttk.Entry(addcontent1)
            listitems.pack(pady=20)
            listypedrop = ttk.Combobox(addcontent1, values=listtype, width=25)
            listypedrop.set("Select a list type")  # Default text
            listypedrop.pack(pady=20)

        if OPTION == "audio":
            print("audio")
            file_path = filedialog.askopenfilename(title="Select a file")
            print(file_path)
            autotrue = ["Autoplay","no autoplay"]
            soundsettings1 = ttk.Combobox(addcontent1, values=autotrue, width=25)
            soundsettings1.set("set autoplay")  # Default text
            soundsettings1.pack(pady=20)
    

            




            
            
        def submitbutton(soup=soup):
            selectedid = dropdown.get()
            print("DIV IDS inside submit button:", div_ids)
            if OPTION == "Headings":
                divtag = soup.find("div", id=selectedid)
                h_tag = soup.new_tag(dropdownheading.get())
                h_tag.string = (textboxContentheading.get())
                divtag.append(h_tag)
            
                with open("output1.html", "w", encoding="utf-8") as file:
                    file.write(soup.prettify())

            if OPTION == "Paragraphs":
                what = dropdownparagraphs.get()
                if what != "a" and what != "comments":
                    divtag = soup.find("div", id=selectedid)
                    p_tag = soup.new_tag(dropdownparagraphs.get())
                    p_tag.string = (textboxContentparagraph.get())
                    divtag.append(p_tag)
                    with open("output1.html", "w", encoding="utf-8") as file:
                        file.write(soup.prettify())
                if what == "a":
                    addcontent2 = tk.Tk()
                    addcontent2.title("Add Content")
                    addcontent2.geometry("400x300")
                    textboxContentheadin1 = ttk.Entry(addcontent2)
                    textboxContentheadin1.pack(pady=20)
                    def addlink():
                        new_link = soup.new_tag("a", href=textboxContentheadin1.get())
                        print("Made link")
                        new_link.string = textboxContentparagraph.get()
                        print("Got hyperlink text")
                        div = soup.find('div', id=selectedid)
                        print("Found div")
                        div.append(new_link)
                        with open("output1.html", "w", encoding="utf-8") as file:
                            file.write(soup.prettify())
                            print("Written to file")
                    button = ttk.Button(addcontent2, text="add content1", bootstyle=SUCCESS, command=addlink)
                    button.pack(pady=20)
                if what == "comments":
                    div = soup.find("div", id=selectedid)
                    commentinst = Comment(textboxContentparagraph.get())
                    div.append(commentinst)
                    with open("output1.html", "w", encoding="utf-8") as file:
                        file.write(soup.prettify())     



            if OPTION == "Fonts":
                print("fonts")
                nonlocal colourselect
                nonlocal fontfamily
                nonlocal Fontname

                with open("output1.html", "r", encoding="utf-8") as file:
                    soup = BeautifulSoup(file, "html.parser")


                textcolour = colourselect.get()
                fontfam = fontfamily.get()
                flnoidl = Fontname.get() #flnoidl = font legal name on its driver liscense
                div = soup.find("div", id=selectedid)
                existingstyle1 = div.get('style', '')

                div['style'] = f"{existingstyle1}color: {textcolour}; font-family: '{fontfam}','{flnoidl}';"
                
                colournotes = Comment(f"color: {textcolour}; font-family: '{fontfam}','{flnoidl}';")
                div.append(colournotes)                      

                with open("output1.html", "w", encoding="utf-8") as file:
                    file.write(str(soup))

            
            if OPTION == "Images":
                nonlocal with1
                nonlocal altxt
                altxt = altxt.get()
                with1 = with1.get()
                div = soup.find("div", id=selectedid)
                imgtag = soup.new_tag("img", src=file_path, alt=altxt, width=with1)
                div.append(imgtag)
                
                with open("output1.html", "w", encoding="utf-8") as file:
                    file.write(soup.prettify())
            
            if OPTION == "Backgrounds":
                nonlocal textcolours
                nonlocal whereback
                backtype = dropdownbackground.get()
                with open("output1.html", "r", encoding="utf-8") as file:
                    soup = BeautifulSoup(file, "html.parser")

                
                if backtype == "background-color":
                    backgroundcolour = tk.Tk()
                    backgroundcolour.title("Continue")
                    backgroundcolour.geometry("400x300")

                    backcolourselect = ttk.Combobox(backgroundcolour, values=textcolours, width=25)
                    backcolourselect.set("select a colour")  # Default text
                    backcolourselect.pack(pady=20)
                    backwhereselcet = ttk.Combobox(backgroundcolour, values=whereback, width=25)
                    backwhereselcet.set("Div or Body")  # Default text
                    backwhereselcet.pack(pady=20)

                    
                else:
                    backgroundimgsel = tk.Tk()
                    backgroundimgsel.title("Continue")
                    backgroundimgsel.geometry("400x300")
                    
                    filepathbackground = filedialog.askopenfilename(title="Select a file")  # Prints the selected file path
                    print(filepathbackground)

                    backwhereselcetimg = ttk.Combobox(backgroundimgsel, values=whereback, width=25)
                    backwhereselcetimg.set("Div or Body")  # Default text
                    backwhereselcetimg.pack(pady=20)
                nonlocal dividpad
                def submitbackgrounds():
                    nonlocal backtype
                    nonlocal filepathbackground
                    nonlocal backwhereselcet
                    nonlocal backgroundimgsel
                    nonlocal backcolourselect
                    nonlocal backwhereselcetimg
                    nonlocal dividpad
                    print("test")
                    
                    if backtype == "background-color":
                        backcolour = backcolourselect.get()
                        backwhere = backwhereselcet.get()
                        # div= soup.find(id=dividpad.get())
                        # existingstyle1 = backwhereselcet.get("style", "")
                        print(backwhere)
                        existingstyle1 = soup.find(backwhere, id=selectedid).get('style', '')

                        soup.find(backwhere, id=selectedid)['style'] = f"{existingstyle1}background-color: {backcolour};"
                        
                        # print(existingstyle)


                        notes = Comment(f"background-color: {backcolour};")

                    else:
                        backwhere = backwhereselcetimg.get()
                        print(backwhere)
                        soup.find(backwhere, id=selectedid)['style'] = f'background-image: url({filepathbackground})'
                        notes = Comment(f"background-image: {filepathbackground};")

                    with open("output1.html", "w", encoding="utf-8") as file:
                        file.write(str(soup))
                    div_tag = soup.new_tag("div")
                    div_tag["class"] = "bodinfo"
                    print("added class")
                    div_tag["id"] = "bodinfo"
                    div_tag.append(notes)
                    soup.body.append(div_tag)



                    with open("output1.html", "w", encoding="utf-8") as file:
                        print("opening file")
                        file.write(str(soup))
                        print("writing file")

                if backtype == "background-color":
                    button = ttk.Button(backgroundcolour, text="submit", bootstyle=SUCCESS, command=submitbackgrounds)
                    button.pack(pady=20)
                else:
                    button = ttk.Button(backgroundimgsel, text="submit", bootstyle=SUCCESS, command=submitbackgrounds)
                    button.pack(pady=20)

            if OPTION == "buttons":
                nonlocal  buttoncontent
                nonlocal  buttonsize
                nonlocal  buttonlink

                div = soup.find("div", id=selectedid)

                linkbutton = soup.new_tag('a')
                linkbutton['href'] = buttonlink.get()
                buttontag = soup.new_tag('button')
                buttontag.string = buttoncontent.get()
                buttontag['type'] = 'submit'
                buttontag['style'] = f'font-size: {buttonsize.get()}px;'
                linkbutton.append(buttontag)
                div.append(linkbutton)
                with open('output1.html', 'w',encoding='utf-8') as file:
                    file.write(soup.prettify())



            
            if OPTION == "padding,":
            
                p_up = paddingy.get()
                p_ri = paddingx1.get()
                p_bm = paddingy1.get()
                p_lf = paddingx.get()
                padding = f"padding: {p_up}px {p_ri}px {p_lf}px {p_bm}px;"
                div= soup.find(id=dividpad.get())
                existingstyle = div.get("style", "")
                if existingstyle:
                    div["style"] = f"{existingstyle}; {padding}".strip()
                else:
                    div["style"] = f"{padding}".strip()
                with open("output1.html", "w", encoding="utf-8") as file:
                    file.write(soup.prettify())
                

            if OPTION == "HTML insert":
                # import html
                nonlocal textbox
                print("...")
                divtag = soup.find("div", id=selectedid)
                htmlcode = textbox.get("1.0", ttk.constants.END).strip()
                print(htmlcode)
                # htmlcode = html.unescape(htmlcode)
                # htmlcode = BeautifulSoup(htmlcode, 'html.parser').text
                divtag.append(htmlcode)
                print(htmlcode)
                with open("output1.html", "w", encoding="utf-8") as file:    
                    print(htmlcode)
                    file.write((soup.prettify(formatter=None)))

            if OPTION == "image buttons":
                ibc = listitems.get()
                ibs = buttonsize.get()
                ibl = buttonlink.get()
                
                div = soup.find("div", id=selectedid)

                linkbutton = soup.new_tag('a')
                linkbutton['href'] = ibl
                imgtag = soup.new_tag('img')
                imgtag['src'] = file_path
                imgtag['alt'] = ibc
                imgtag['width'] = ibs
                linkbutton.append(imgtag)
                div.append(linkbutton)
                with open('output1.html', 'w',encoding='utf-8') as file:
                    file.write(soup.prettify())

            if OPTION == "lists":
                listitems1 = listitems.get()
                listcont = listitems1.split(',')
                print(listcont)
                listtype = listypedrop.get()
                div = soup.find("div", id=selectedid)
                listtag = soup.new_tag(listtype)
                for item in listcont:
                    itemtag = soup.new_tag('li')
                    itemtag.string = item
                    listtag.append(itemtag)

                div.append(listtag)
                with open('output1.html', 'w',encoding='utf-8') as file:
                    file.write(soup.prettify())
                print("done")
            if OPTION == "audio":
                autotrue = soundsettings1.get()
                # div = soup.find("body")
                audiotag = soup.new_tag("audio", autoplay=autotrue if autotrue == "Autoplay" else False, controls=True)
                sourcetag = soup.new_tag("source")
                sourcetag['src'] = file_path
                sourcetag['type'] = 'audio/mpeg'
                audiotag.append(sourcetag)
                
                soup.body.append(audiotag)
                with open('output1.html', 'w',encoding='utf-8') as file:
                    file.write(soup.prettify())

#  0000000000 an army of zeros.


        button = ttk.Button(addcontent1, text="submit", bootstyle=SUCCESS, command=submitbutton)
        button.pack(pady=20)

    button = ttk.Button(addcontent, text="continue", bootstyle=SUCCESS, command=nextbutton)
    button.pack(pady=20)

