[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QKp42A0s)
# 121CAT

1.Follow all of the steps on the [Book](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/93f2c351e3c34598b8b71bf2ebc40abe)

2. Complete the addigional features:
   ![image](https://github.com/user-attachments/assets/f99d7777-6fea-47e5-bf9a-fc452f835952)

3. Create a video of the app working with all of the additional features. Make the video small enough to render here or upload to a video service witha aviawable link.

https://github.com/user-attachments/assets/72e6678f-31ba-4cc7-9def-92ca9ee00867

4. Choose two snapshots of code that demonstrate the algorithm(s) used to implement the additional features. Explain the code in the screenshots.

![Screenshot 2024-10-24 at 10 33 05 PM](https://github.com/user-attachments/assets/55fd68d8-c48d-4efe-9380-8ca316ccec3a)

First, this function moves the time turtle to the right. Then, it writes the time on the turtle screen using the in-built .write() function. It then follows an algorithm: if there is more than 0 seconds left, the time will reduce 1 second every 1000 milliseconds and it will display it next to the written message. However, once the time reaches 0, it sets the game_active variable to be false, clears the previous message, and writes that the time is up. It also makes it so that you are unable to click anything on the screen, making users unable to keep on playing after the time has run out.

![Screenshot 2024-10-24 at 10 36 15 PM](https://github.com/user-attachments/assets/feeaf198-f8ac-4fea-a71c-8b5a530182a0)

In this section of the code, the different colors of the turtles and the shapes of the turtles are written within a list. These are used with the random.randint() function to randomize the colors and the shapes of the turtle after the user presses it. The same is done with the shape size. For the turtle_move() function, if the game is active, the turtle will teleport to random coordinates, fitting within the screen. It then calls the randomize function to give the turtle that teleported attributes such as color, shape, and shapesize
