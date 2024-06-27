from tkinter import *
import requests
import json
df=Tk()
df.title("Whether App")

v=StringVar()
def action():
    city = v.get()
    url ="https://api.weatherapi.com/v1/current.json?key=638ba7c08aa4460794393515231104&q="
    url = url + city
    data = requests.get(url)
    data = json.loads(data.content)
    df4.config(text="Region="+data["location"]["region"])
    df5.config(text="Temperature in celcious="+str(data["current"]["temp_c"]))



df1= Label(df ,text="Whether Forecasting App", fg ="white" ,bg = "black")
df1.place(x=570,y=250)


img=PhotoImage(file="D:\Downloads\wheather.png")
df2=Label(df,image=img)
df2.pack()

df2 = Entry(df , font=("Arial",20),textvariable=v)
df2.place(x=500,y=300)

df3 = Button(df, text="Get The Result",fg="white",bg="black",command=action)
df3.place(x=570,y=350)

df4= Label(df ,text="Whether Forecasting App", fg ="white" ,bg = "black")
df4.place(x=570,y=400)

df5= Label(df ,text="Temperature in celsiu", fg ="white" ,bg = "black")
df5.place(x=570,y=450)

df.mainloop()