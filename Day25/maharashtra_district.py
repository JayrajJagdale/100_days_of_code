import turtle
import pandas

screen = turtle.Screen()
screen.title("Maharashtra District")
image = "D:/100_Days_Code/Day25/m_map.gif"
screen.addshape(image)
turtle.shape(image)

total_guess = []
data = pandas.read_csv("D:/100_Days_Code/Day25/36_district.csv")

district_list = data.district.to_list()

while len(total_guess) < 36:
    user_input = screen.textinput(f"{len(total_guess)}/36", "Guess the District:").title()

    if user_input == "Exit":
        missing_district = []
        for states in district_list:
            if states not in total_guess:
                 missing_district.append(states)
        new_data = pandas.DataFrame(missing_district)
        new_data.to_csv("D:/100_Days_Code/Day25/not_guessesd_district.csv")
        
        break

    if user_input in district_list: 
        total_guess.append(user_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        dis = data[data.district == user_input]
        t.goto(dis.x.item(), dis.y.item())
        t.write(user_input)
       

    print(total_guess)










