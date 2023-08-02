from tkinter import *
from tkinter import ttk
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


window = Tk()
window.geometry("500x500")
window.title("API")
window.resizable(False, False)


def scrape(url):
    driver = webdriver.Chrome()
    driver.get(url)

    elements = ["a", "h1", "h2", "h3", "h4", "h5", "h6", "img"]
    json = dict()

    for elem in elements:
        elements = driver.find_elements(by=By.TAG_NAME, value=elem)
        elems = []
        for i in elements:
            try:
                elems.append(i.get_attribute())
            except Exception:
                try:
                    if elem == "a":
                        elems.append(i.get_attribute("href"))
                    elif elem == "img":
                        elems.append(i.get_attribute("src"))
                except Exception:
                    continue
        json.update({elem: elems})

    driver.close()
    return json


def post(json_url, scrape_url):
    request = requests.post(url=json_url, json=scrape(scrape_url))
    print(request.text)
    try:
        return request.json()
    except Exception:
        return request.text


def main_function():
    print(entry.get(), entry2.get())
    try:
        post(
            json_url=str(entry.get()),
            scrape_url=str(entry2.get())
        )
        label = Label(text="JSON posted successfully!")
        label.config(bg="green")
        label.grid(row=1, column=4)
    except Exception:
        label = Label(text="Unexpected error occured! Try again by typing urls correctly")
        label.config(bg="red")
        label.grid(row=1, column=4)


frame = Frame(window)
frame.place(x=50, y=100)
lab1 = Label(frame, text="Website url to be scraped: ")
lab1.grid(row=1, column=1)
entry = ttk.Entry(frame)
entry.grid(row=2, column=2)
lab2 = Label(frame, text="URL that json to be posted to: ")
lab2.grid(row=2, column=1)
entry2 = ttk.Entry(frame)
entry2.grid(row=1, column=2)
button = ttk.Button(frame, text="POST", command=main_function)
button.grid(row=3, column=2)
window.mainloop()
