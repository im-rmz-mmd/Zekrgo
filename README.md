🎯 When a Joke Turned into a Program!

One night, we were joking around in a group chat, having fun as usual. But then, in a perfectly coordinated operation, we pranked one of our friends a little too hard. The result? He got upset and left the group! 😂

I felt kinda bad and thought, "I need to make it up to him somehow." 🥰
Then, out of nowhere, an idea struck me—one that no one saw coming:
A program that shows daily Islamic supplications! 😂

🤖 What Did I Build? 

A simple yet unique program!

Using Tkinter, I created an app that:

🔸 Has 7 buttons, each labeled with a day of the week.

text = "Day of the Week" 

🔹 Clicking a button opens a messagebox displaying the supplication for that day.

messagebox.showinfo("Supplication of the Day", "Supplication Text") 

🔸 There's also a red exit button to close the app, because obviously, we need a way out!

command = x.destroy 

🔹 At the bottom, I added a signature label—my GitHub link—so anyone using it knows who the genius behind this is! 🥰

Label(text="GitHub: my_link_here") 🛠 How Does It Work? 

✨ Main Components of the Code:

🔹 Creating the main window & basic settings:

x = Tk() x.title("Supplications of the Week") x.geometry("400x210") x.resizable(False, False) 

🔹 Displaying a message when a button is clicked:

def fb1(): messagebox.showinfo("Monday Supplication", "Supplication Text") b1 = Button(text="Monday", command=fb1) 

🔸 Exit button:

b8 = Button(text="Exit", command=x.destroy) 

🔹 Adding the signature label:

Label(x, text="Programmed by Me! GitHub: my_link_here") 

🔸 Running the application:

x.mainloop() ✅ A Simple Yet Fun Program! 

At first, I made it just to cheer up my friend. But once it was done, I actually liked it myself! 😂

💡 What did I do next? 

✅ Created an EXE file so it runs without needing Python installed—now it's a real standalone app!
✅ Sent it to my friend to show him what I made for him. His reaction? Priceless! 😂

🚀 Final Outcome? 

A prank that started with someone leaving a group chat ended up inspiring a cool little project! 😃

Not only did I learn how to work with Tkinter, but I also made a fun memory that I’ll always remember! 🥰
