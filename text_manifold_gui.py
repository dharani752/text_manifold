#Main packages

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
from tkinter import font

# Other pkgs
import time
timestr= time.strftime("%Y%m%d-%H%M%S")

#Required packages
from text_summarizer import nltk_summarizer
from extract_keyword import ex_keywords
from lang_detection import langProb, langdetection
from lang_translation import translation
from abstract_summarizer_abs import abstract_summarizer

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen


 # Structure and Layout
window = Tk()
window.title("TEXT MANIFOLD")
window.geometry("700x400")

window.config(background='black')

style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn',)

tab_control = ttk.Notebook(window,style='lefttab.TNotebook')

my_font1 = font.Font(family='Calibri', size=18)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)
tab7 = ttk.Frame(tab_control)
tab8 = ttk.Frame(tab_control)
tab9 = ttk.Frame(tab_control)
tab15 = ttk.Frame(tab_control)
# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Home":^60s}')
#tab_control.add(tab15, text=f'{"  ":^60s}')
tab_control.add(tab2, text=f'{"File":^60s}')
tab_control.add(tab3, text=f'{"URL":^20s}')
tab_control.add(tab4, text=f'{"Language Detection ":^20s}')
tab_control.add(tab5, text=f'{"Language Translation ":^20s}')
tab_control.add(tab6, text=f'{"Text Summarizer ":^20s}')
tab_control.add(tab7, text=f'{"Keyword extraction ":^20s}')
tab_control.add(tab8, text=f'{"Abstract summarizer ":^20s}')
tab_control.add(tab9, text=f'{"ABOUT ":^20s}')
#tab_control.add(tab1, text=f'<h1>{"Home":^60s}</h1>')

label1 = Label(tab1, text= 'TEXT MANIFOLD',padx=5, pady=5,font=50)
label1.grid(column=0, row=0)
 
label2 = Label(tab2, text= 'Summarization of uploaded files',padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text= 'Summarization of text from url',padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab4, text= 'Language Detection',padx=5, pady=5)
label4.grid(column=0, row=0)

label5 = Label(tab5, text= 'Language Translation',padx=5, pady=5)
label5.grid(column=0, row=0)

label6 = Label(tab6, text= 'Text Summarizer',padx=5, pady=5)
label6.grid(column=0, row=0)

label7 = Label(tab7, text= 'Extraction of top 10 keywords',padx=5, pady=5)
label7.grid(column=0, row=0)

label8 = Label(tab8, text= 'Abstract Summarizer',padx=5, pady=5)
label8.grid(column=0, row=0)

label9 = Label(tab9, text= 'About',padx=5, pady=5)
label9.grid(column=0, row=0)


tab_control.pack(expand=1, fill='both')

# Functions---------------------------------------------------------------------------------------------------
def get_summary():
	raw_text = str(entry.get('1.0',tk.END))
	final_text = nltk_summarizer(raw_text)
	print(final_text)
	result = '\nSummary:{}'.format(final_text)
	tab6_display.insert(tk.END,result)

def save_summary():
    raw_text = entry.get('1.0',tk.END)
    final_text = nltk_summarizer(raw_text)
    file_name = 'yoursummary'+ timestr + '.txt'
    with open(file_name,'w') as f:
        f.write(final_text)
    result ='\nName of File: {}, \nSummary: {}'.format(file_name,final_text)
    tab6_display.insert(tk.END,result)


# Clear entry widget
def clear_text():
	entry.delete('1.0',END)

def clear_display_result():
	tab6_display.delete('1.0',END)


# Clear Text  with position 1.0
def clear_text_file():
	displayed_file.delete('1.0',END)

# Clear Result of Functions
def clear_text_result():
	tab2_display_text.delete('1.0',END)

# Clear For URL-----------------------------------------------------------------------
def clear_url_entry():
	url_entry.delete(0,END)

def clear_url_display():
	tab3_display_text.delete('1.0',END)


# Clear entry widget
#def clear_compare_text():
	#entry1.delete('1.0',END)

#def clear_compare_display_result():
	#tab6_display.delete('1.0',END)

# Open File to Read and Process
def openfiles():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)


def get_file_summary():
	raw_text = displayed_file.get('1.0',tk.END)
	final_text = nltk_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)

# Fetch Text From Url
def get_text():
	raw_text = str(url_entry.get())
	page = urlopen(raw_text)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	url_display.insert(tk.END,fetched_text)

def get_url_summary():
	raw_text = url_display.get('1.0',tk.END)
	final_text = nltk_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab3_display_text.insert(tk.END,result)	

#functions for detection------------------------------------------------------

def detect_lang():
    raw_text = str(entry1.get('1.0',tk.END))
    final_text = langdetection(raw_text)
    result = '\nLanguage of given text:{}'.format(final_text)
    tab4_display.insert(tk.END,final_text)


def detect_lang_prob():
    raw_text = str(entry1.get('1.0',tk.END))
    final_text = langProb(raw_text)
    ll=langdetection(raw_text)
    print(final_text)
    result = '\nLanguage:{}\nProbability:{}'.format(ll,final_text)
    tab4_display.insert(tk.END,result)
    
def clear_display_result_ld():
	tab4_display.delete('1.0',END)

def clear_text_ld():
    entry1.delete('1.0',END)

# functions for keyword extraction---------------------------------------

def clear_text_ke():
    entry2.delete('1.0',END)

def clear_display_result_ke():
    tab7_display.delete('1.0',END)

def getKeys():
	raw_text = str(entry2.get('1.0',tk.END))
	final_keys = ex_keywords(raw_text)
    #keys = ' '.join(final_keys)
	result = '\nThe top 10 keywords from given text are :{}'.format(final_keys)
	tab7_display.insert(tk.END,result)


# functions for abstract summarizer-----------------------------------------
def get_summary_abs():
	raw_text = str(entry3.get('1.0',tk.END))
	final_text = abstract_summarizer(raw_text)
	print(final_text)
	result = '\nSummary:{}'.format(final_text)
	tab8_display.insert(tk.END,result)

def save_summary_abs():
    raw_text = entry3.get('1.0',tk.END)
    final_text = abstract_summarizer(raw_text)
    file_name = 'your_abstract_summary'+ timestr + '.txt'
    with open(file_name,'w') as f:
        f.write(final_text)
    result ='\nName of File: {}, \nSummary: {}'.format(file_name,final_text)
    tab8_display.insert(tk.END,result)

def clear_text_abs():
    entry3.delete('1.0',END)

def clear_display_result_abs():
    tab8_display.delete('1.0',END)

# functions for translation---------------------------------------------------

def clear_text_lt():
    entry4.delete('1.0',END)

def translate():
    raw_text = str(entry4.get('1.0',tk.END))
    ln=str(entry4_0.get('1.0',tk.END))

    final_text = translation(raw_text,ln)
    print(final_text)
    result = '\nTranslation:{}'.format(final_text)
    tab5_display.insert(tk.END,result)

def clear_display_result_lt():
    tab5_display.delete('1.0',END)

def save_translation():
    raw_text = entry4.get('1.0',tk.END)
    final_text = abstract_summarizer(raw_text)
    file_name = 'your_translation_text'+ timestr + '.txt'
    with open(file_name,'w') as f:
        f.write(final_text)
    result ='\nName of File: {}, \nTranslation: {}'.format(file_name,final_text)
    tab5_display.insert(tk.END,result)








# Home TAB





my_font = font.Font(family='Calibri', size=20)


l11=Label(tab1,text="A complete toolkit for various text tasks.",font=my_font)
l11.grid(row=1,column=0)


# FILE TAB-----------------------------------------------------------------------------------------------------------------------------------
l21=Label(tab2,text="Open File To Summarize")
l21.grid(row=1,column=1)

displayed_file = ScrolledText(tab2,height=7)# Initial was Text(tab2)
displayed_file.grid(row=2,column=0, columnspan=3,padx=5,pady=3)

# BUTTONS FOR FILE READING TAB
b20=Button(tab2,text="Open File", width=12,command=openfiles,bg='#c5cae9')
b20.grid(row=3,column=0,padx=10,pady=10)

b21=Button(tab2,text="Reset ", width=12,command=clear_text_file,bg="#b9f6ca")
b21.grid(row=3,column=1,padx=10,pady=10)

b22=Button(tab2,text="Summarize", width=12,command=get_file_summary,bg='blue',fg='#fff')
b22.grid(row=3,column=2,padx=10,pady=10)

b23=Button(tab2,text="Clear Result", width=12,command=clear_text_result)
b23.grid(row=5,column=1,padx=10,pady=10)

b24=Button(tab2,text="Close", width=12,command=window.destroy)
b24.grid(row=5,column=2,padx=10,pady=10)

# Display Screen
tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2,height=10)
tab2_display_text.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)


# URL TAB----------------------------------------------------------------------------------------------------------------------------------------------
l31=Label(tab3,text="Enter URL To Summarize")
l31.grid(row=1,column=0)

raw_entry=StringVar()
url_entry=Entry(tab3,textvariable=raw_entry,width=50)
url_entry.grid(row=1,column=1)

# BUTTONS
button31=Button(tab3,text="Reset url",command=clear_url_entry, width=12,bg='#03A9F4',fg='#fff')
button31.grid(row=4,column=0,padx=10,pady=10)

button32=Button(tab3,text="Get Text",command=get_text, width=12,bg='#03A9F4',fg='#fff')
button32.grid(row=4,column=1,padx=10,pady=10)

button33=Button(tab3,text="Clear Result", command=clear_url_display,width=12,bg='#03A9F4',fg='#fff')
button33.grid(row=5,column=0,padx=10,pady=10)

button34=Button(tab3,text="Summarize",command=get_url_summary, width=12,bg='#03A9F4',fg='#fff')
button34.grid(row=5,column=1,padx=10,pady=10)

button35=Button(tab3,text="Clear Text", command=clear_url_display,width=12,bg='#03A9F4',fg='#fff')
button35.grid(row=5,column=0,padx=10,pady=10)

button36=Button(tab3,text="Summarize",command=get_url_summary, width=12,bg='#03A9F4',fg='#fff')
button36.grid(row=5,column=1,padx=10,pady=10)

# Display Screen For Result
url_display = ScrolledText(tab3,height=10)
url_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


tab3_display_text = ScrolledText(tab3,height=10)
tab3_display_text.grid(row=10,column=0, columnspan=3,padx=5,pady=5)

# language detection tab--------------------------------------------------------------------------------------------------------------------------------
l41=Label(tab4,text="Enter Text To Detect Language")
l41.grid(row=1,column=0)

entry1=ScrolledText(tab4,height=10)#Text(tab4,height=10)
entry1.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

# BUTTONS
button41=Button(tab4,text="Reset",command=clear_text_ld, width=12,bg='#25D366',fg='#fff')
button41.grid(row=4,column=0,padx=10,pady=10)

button42=Button(tab4,text="Detect Language",command=detect_lang, width=12,bg='#03A9F4',fg='#fff')
button42.grid(row=4,column=1,padx=10,pady=10)

button43=Button(tab4,text="Clear Result", command=clear_display_result_ld,width=12,bg='#03A9F4',fg='#fff')
button43.grid(row=5,column=0,padx=10,pady=10)

button44=Button(tab4,text="Detect Probability", command=detect_lang_prob, width=12,bg='#cd201f',fg='#fff')
button44.grid(row=5,column=1,padx=10,pady=10)

tab4_display = ScrolledText(tab4,height=10)
tab4_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# language translation------------------------------------------------------------------------------------
l51=Label(tab5,text="Enter Text To Translste")
l51.grid(row=2,column=0)

entry4=ScrolledText(tab5,height=10)#Text(tab6,height=10)
entry4.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

l52=Label(tab5,text="Enter the language to be translated to")
l52.grid(row=1,column=0)

entry4_0=Text(tab5,height=5)
entry4_0.grid(row=1,column=1,columnspan=2,padx=5,pady=5)



# BUTTONS
button51=Button(tab5,text="Reset",command=clear_text_lt, width=12,bg='#25D366',fg='#fff')
button51.grid(row=4,column=0,padx=10,pady=10)

button52=Button(tab5,text="Translate",command=translate, width=12,bg='#03A9F4',fg='#fff')
button52.grid(row=4,column=1,padx=10,pady=10)

button53=Button(tab5,text="Clear Result", command=clear_display_result_lt,width=12,bg='#03A9F4',fg='#fff')
button53.grid(row=5,column=0,padx=10,pady=10)

button54=Button(tab5,text="Save", command= save_translation, width=12,bg='#cd201f',fg='#fff')
button54.grid(row=5,column=1,padx=10,pady=10)

# Display Screen For Result
tab5_display = Text(tab5)
tab5_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# text summarizer------------------------------------------------------------------------------------------
l61=Label(tab6,text="Enter Text To Summarize")
l61.grid(row=1,column=0)

entry=ScrolledText(tab6,height=10)#Text(tab6,height=10)
entry.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

# BUTTONS
button61=Button(tab6,text="Reset",command=clear_text, width=12,bg='#25D366',fg='#fff')
button61.grid(row=4,column=0,padx=10,pady=10)

button62=Button(tab6,text="Summarize",command=get_summary, width=12,bg='#03A9F4',fg='#fff')
button62.grid(row=4,column=1,padx=10,pady=10)

button63=Button(tab6,text="Clear Result", command=clear_display_result,width=12,bg='#03A9F4',fg='#fff')
button63.grid(row=5,column=0,padx=10,pady=10)

button64=Button(tab6,text="Save", command= save_summary, width=12,bg='#cd201f',fg='#fff')
button64.grid(row=5,column=1,padx=10,pady=10)

# Display Screen For Result
tab6_display = Text(tab6)
tab6_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# Keyword extractor---------------------------------------------------------------------------------------
l71=Label(tab7,text="Enter Text To Get Top 10 Keywords")
l71.grid(row=1,column=0)

entry2=ScrolledText(tab7,height=10)#Text(tab7,height=10)
entry2.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

# BUTTONS
button71=Button(tab7,text="Reset",command=clear_text_ke, width=12,bg='#25D366',fg='#fff')
button71.grid(row=4,column=0,padx=10,pady=10)

button72=Button(tab7,text="Get Keywords",command=getKeys, width=12,bg='#03A9F4',fg='#fff')
button72.grid(row=4,column=1,padx=10,pady=10)

button73=Button(tab7,text="Clear Result", command=clear_display_result_ke,width=12,bg='#03A9F4',fg='#fff')
button73.grid(row=5,column=0,padx=10,pady=10)

tab7_display = ScrolledText(tab7,height=10)
tab7_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


# Abstract summarizer------------------------------------------------------------------------------------
l81=Label(tab8,text="Enter Text To Summarize")
l81.grid(row=1,column=0)

entry3=ScrolledText(tab8,height=10)#Text(tab8,height=10)
entry3.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

# BUTTONS
button81=Button(tab8,text="Reset",command=clear_text_abs, width=12,bg='#25D366',fg='#fff')
button81.grid(row=4,column=0,padx=10,pady=10)

button82=Button(tab8,text="Summarize",command=get_summary_abs, width=12,bg='#03A9F4',fg='#fff')
button82.grid(row=4,column=1,padx=10,pady=10)

button83=Button(tab8,text="Clear Result", command=clear_display_result_abs,width=12,bg='#03A9F4',fg='#fff')
button83.grid(row=5,column=0,padx=10,pady=10)

button84=Button(tab8,text="Save", command= save_summary_abs, width=12,bg='#cd201f',fg='#fff')
button84.grid(row=5,column=1,padx=10,pady=10)

# Display Screen For Result
tab8_display = Text(tab8)
tab8_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)






# About TAB
about_label = Label(tab9,text="TEXT MANIFOLD GUI FOR VARIOUS TEXT PROCESSING TASKS\n\n By BHAGYA SREE SUHRUTHA & DHARANI",pady=5,padx=5)
about_label.grid(column=1,row=1)



window.mainloop()