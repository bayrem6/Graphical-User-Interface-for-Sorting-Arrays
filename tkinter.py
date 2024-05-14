def trirap(L):
    """trirapide(L): tri rapide (quicksort) de la liste L"""
    def trirap(L, g, d):
        pivot = L[(g+d)//2]
        i = g
        j = d
        while True:
            while L[i]<pivot:
                i+=1
            while L[j]>pivot:
                j-=1
            if i>j:
                break
            if i<j:
                L[i], L[j] = L[j], L[i]
            i+=1
            j-=1
        if g<j:
            trirap(L,g,j)
        if i<d:
            trirap(L,i,d)
 
    g=0
    d=len(L)-1
    trirap(L,g,d)
    return L


List=[]

l=[]
def trirapide(l):
    L=l[:]
    for child in Output.winfo_children():
        child.destroy()
    try:
        if int(valu.get()) !=0:
            trirap(L)
        else:
            L=trirap(L)
            L=L[::-1]
            return(L)
    except:
                info2.config(text="remplir tous le tableau'",fg="red")
    return(L)





from tkinter.messagebox import *
from tkinter import *
fn=Tk()
#supprimer title bar
#fn.overrideredirect(1)
#fn.wm_geometry("+800+0")
res=False





def guider():
    info3.config(text="couleur vert pour valide'",fg="green")
    info4.config(text="couleur rouge pour error d'entree (donner un character au lieux d'un nombre)",fg="red")
    info5.config(text="case vide",fg="blue")
    
    return


def Advanced():
    pass
def Setting():
    pass
def hek():
    pass
def remove(widget1):
    widget1.grid_remove()
def create():
    global res
    res=False
    global Entries
    number.pack_forget()
    for i in Entries:
        i.grid_forget()
    nbele=int(entry.get())
    Entries=[]
    enter= Entry(number, width=5 , bg="red", font=('Arial',16, 'bold'),justify=CENTER)
    for i in range (nbele):
        number.pack()
        enter= Entry(number, width=5 , bg="red", font=('Arial',16, 'bold'),justify=CENTER)
        enter.grid(column=(i%6), row=int(i//6)*2, padx=15, pady=15 )

        reg = fn.register(callback)
        enter.config(validate ="key", validatecommand =(reg, '%P'))
        Entries.append(enter)
    Entries[0].focus_set()



def creat(event):
    create()
def callback2(P):
	
		if len(P) ==0 :
			entry.config(bg="blue")
			return True

		try :
				int(P)
				entry.config(bg="green")
				info.config(text="validate",fg="green")

				return True 
		except:
                    
			entry.config(bg="red")
			info.config(text="give number : your pressed the key '"+P+"' ",fg="red")
			return False

def callback(P):
            enter=fn.focus_get()
            if len(P) ==0 :
                enter.config(bg="blue")
                return True
            elif len(P)==1 and P[0]=="-":
                enter.config(bg="green")
                return True
            try :
                float(P)
                enter.config(bg="green")
                print(l)

                return True
            except:
                enter.config(bg="red")
                return False

def affichage():
    global mini
    global maxi
    global l
    l=[]
    for i in Entries:
 
            try:
                l.append(float(i.get()))
                info2.config(text="tableau trie'",fg="green")
            except:
                info2.config(text="remplir tous le tableau'",fg="red")

        
    
    m=trirapide(l)
    maxi=max(l)
    mini=min(l)
    global sortie

    for j in sortie:
        j.destroy()
    sortie=[]
    Outputnumber=Frame(Output,padx=5,pady=5)

    for i in range(len(m)):
        Outputnumber.pack()
        enter2= Label(Outputnumber,text=m[i], width=5 , font=('Arial',16, 'bold'))
        enter2.grid(column=(i%6), row=int(i//6)*2, padx=15, pady=15 )
        sortie.append(enter2)
        print(l)
def maxim():
    global maxi
    print(l)
    info4.config(text="Le max est  "+str(maxi),fg="red")
    return
def mini():
    info5.config(text="le min est  "+str(min(l)),fg="blue")
    return
def sup(event):
    somm=0
    s=entry2.get()
    for i in l:
        if str(i)>=s:
            somm+=1
    info6.config(text="le nombre du numero superieur et egale a "+str(s)+" est :  "+str(somm),fg="blue")
    return


OPTIONS = [
"guide",
"Advanced",
"Setting"]


Entries=[]
sortie=[]
app_width = 750
app_height = 800
fn.resizable(False, False) 
def restart():
    fn.destroy()
    os.startfile("main.py")
    
screen_width = fn.winfo_screenwidth()
screen_height = fn.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)

fn.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

fn.title("programme de tri d'un tableau")



#######
option1 = Frame(fn, width=20,height=50,padx=10,pady=10)
option1.pack(side=TOP,fill=Y)
#-------------
Input = Frame(fn, width=20,height=50,padx=10,pady=10)
#Input.pack(side=TOP,fill=Y)

#-------------

verif = Frame(fn, width=20,height=50,padx=10,pady=10)
verif.pack(side=TOP,fill=Y)
label = Label(verif, text="donner le taille du tableau",fg="Blue")
label.pack()
info=Label(fn)
info.pack()
#-------------
option2 = Frame(fn, width=300,height=100)
option2.pack(side=TOP, fill=Y)
"""variable = StringVar(fn)
variable.set("sort type") # default value
w = OptionMenu(option2, variable, *OPTIONS)
w.pack()"""

def ok():
    print ("value is:" + variable.get())

button = Button(option2, text="trier", command=affichage)
button.pack()




valu = IntVar() 
bouton1 = Radiobutton(option2, text="croissant", variable=valu, value=True)
bouton2 = Radiobutton(option2, text="decroissant", variable=valu, value=False)
bouton1.pack(side = LEFT, padx = 2, pady = 2)
bouton2.pack(side = LEFT, padx = 2, pady = 2)

#-------------
table = Frame(fn, width=400,height=100)
table.pack(side=TOP, fill=Y)
number=Frame(table,padx=5,pady=5)
info2=Label(fn)
info2.pack()
#-------------
Output = Frame(fn, width=400,height=100)
Output.pack(side=TOP, fill=Y)
Outputnumber=Frame(Output,padx=5,pady=5)

#-------------
guid = Frame(fn, width=400,height=100)
guid.pack(side=TOP, fill=Y)
#-------------
supp = Frame(fn, width=400,height=100)
supp.pack(side=TOP, fill=Y)
entry2= Entry(supp,bd = 5,font=('Century 20'),width=5,justify="center")
entry2.bind('<Return>',sup)
labeli = Label(supp, text="Supperieur",fg="Blue")
labeli.pack()

entry2.pack()
info6=Label(supp)
info6.pack()

################## les boutons

bouton1 = Button(option1, text="guide", command=guider)
bouton1.pack(side = LEFT, padx = 2, pady = 2)
info3=Label(guid)
info3.pack()
info4=Label(guid)
info4.pack()
info5=Label(guid)
info5.pack()

#----------------
bouton2 = Button(option1, text=" min", command=mini)
bouton2.pack(side = LEFT, padx = 2, pady = 2)
bouton5 = Button(option1, text=" max", command=maxim)
bouton5.pack(side = LEFT, padx = 2, pady = 2)
#----------------
bouton3 = Button(option1, text="exist", command=restart)
bouton3.pack(side = LEFT, padx = 2, pady = 2)

#----------------
#########################Inputs
Input1 = Entry(Input,width = 20)
Input1.pack(side = LEFT, padx = 1, pady = 1) 
################## message



entry= Entry(verif,bd = 5,font=('Century 20'),width=5,justify="center")
entry.focus_set()

fun= fn.register(callback2)
entry.config(validate='key', validatecommand=(fun,'%P'))

test=fn.bind('<Return>',creat)
print(test)
entry.pack()

################## les labels


######################
"""mbtn = Menubutton(fn, text="Type du sort", relief=RAISED)
mbtn.grid()
mbtn.menu = Menu(mbtn, tearoff = 0)
mbtn["menu"] = mbtn.menu

pythonVar = IntVar()
javaVar = IntVar()
phpVar = IntVar()

mbtn.menu.button(label="insertion", variable=pythonVar)
mbtn.menu.button(label="quick", variable=javaVar)
mbtn.menu.button(label="PHP", variable=phpVar)

mbtn.pack()"""


##"optmenu.bind('<Button-1>', onactivate)

value = IntVar() 
"""
# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("700x350")

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
   if file:
      content = file.read()
      file.close()
      print("%d characters in this file" % len(content))

# Add a Label widget
label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button
ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

win.mainloop()



"""
