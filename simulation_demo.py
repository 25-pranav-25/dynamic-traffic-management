import turtle
from time import sleep
import cv2
import glob
import random
from ultralytics import YOLO
import matplotlib.pyplot as plt
best_model = YOLO("yolov8n.pt")
all_images = ["all_images/cars1.jpg","all_images/cars2.jpg","all_images/cars3.jpg","all_images/cars4.jpg","all_images/cars5.jpg","all_images/cars6.jpg","all_images/cars7.jpg","all_images/cars8.jpg","all_images/cars9.jpg","all_images/cars10.jpg","all_images/cars11.jpg","all_images/cars12.jpg"]


# Cam Function
def camera():
    cam = cv2.VideoCapture(0)
    img_counter = 0

    while True:
        ret, image = cam.read()
        if (ret == False):
            print("failed to grab frame")
            break

        cv2.imshow('Imagetest',image)
        k = cv2.waitKey(1)
        if (k%256 == 32):
            img_name = "frame.png".format(img_counter)
            cv2.imwrite(img_name,image)
            print("screenshot")
            break

    cam.release()
    cv2.destroyAllWindows()

# Lane Functions
def Lane1():
    #camera()
    imagf = glob.glob(all_images[d])
    global cnt1
    for img_path in imagf:
        print("Img path", img_path)
        img = cv2.imread(img_path)
        results = best_model.predict(source=img_path, conf=0.6, imgsz=640, verbose=False)
        vehicle_boxes = results[0].boxes
        cnt1 = len(vehicle_boxes)
        print("Vehicle Count", cnt1)
        sample_image = results[0].plot(line_width=2)

        # Convert the color of the image from BGR to RGB for correct color representation in matplotlib
        sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)

        # Display annotated image
        plt.figure(figsize=(20,15))
        plt.imshow(sample_image)
        plt.title('Detected Objects in Sample Image by the Fine-tuned YOLOv8 Model', fontsize=20)
        plt.axis('off')
        plt.show()

def Lane2():
    imagf = glob.glob(all_images[a])
    global cnt2
    for img_path in imagf:
        print("Img path", img_path)
        img = cv2.imread(img_path)
        results = best_model.predict(source=img_path, conf=0.6, imgsz=640, verbose=False)
        vehicle_boxes = results[0].boxes
        cnt2 = len(vehicle_boxes)
        print("Vehicle Count", cnt2)
        sample_image = results[0].plot(line_width=2)

        # Convert the color of the image from BGR to RGB for correct color representation in matplotlib
        sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)

        # Display annotated image
        plt.figure(figsize=(20,15))
        plt.imshow(sample_image)
        plt.title('Detected Objects in Sample Image by the Fine-tuned YOLOv8 Model', fontsize=20)
        plt.axis('off')
        plt.show()


def Lane3():
    imagf = glob.glob(all_images[b])
    global cnt3
    for img_path in imagf:
        print("Img path", img_path)
        img = cv2.imread(img_path)
        results = best_model.predict(source=img_path, conf=0.6, imgsz=640, verbose=False)
        vehicle_boxes = results[0].boxes
        cnt3 = len(vehicle_boxes)
        print("Vehicle Count", cnt3)
        sample_image = results[0].plot(line_width=2)

        # Convert the color of the image from BGR to RGB for correct color representation in matplotlib
        sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)

        # Display annotated image
        plt.figure(figsize=(20,15))
        plt.imshow(sample_image)
        plt.title('Detected Objects in Sample Image by the Fine-tuned YOLOv8 Model', fontsize=20)
        plt.axis('off')
        plt.show()

def Lane4():
    imagf = glob.glob(all_images[c])
    global cnt4
    for img_path in imagf:
        print("Img path", img_path)
        img = cv2.imread(img_path)
        results = best_model.predict(source=img_path, conf=0.6, imgsz=640, verbose=False)
        vehicle_boxes = results[0].boxes
        cnt4 = len(vehicle_boxes)
        print("Vehicle Count", cnt4)
        sample_image = results[0].plot(line_width=2)

        # Convert the color of the image from BGR to RGB for correct color representation in matplotlib
        sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)

        # Display annotated image
        plt.figure(figsize=(20,15))
        plt.imshow(sample_image)
        plt.title('Detected Objects in Sample Image by the Fine-tuned YOLOv8 Model', fontsize=20)
        plt.axis('off')
        plt.show()

wn = turtle.Screen()
wn.title("Traffic Lights")
wn.bgcolor("black")
# turtle.speed(speed=20)
turtle.speed(0)
pen = turtle.Turtle()

# Writing Texts Lane1
pen.penup()
pen.goto(0, 170)
pen.color("white")
pen.write('Lane1', align="center", font=("Serif", 18))

# Draw box around the stoplight Lane1
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 320)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

# Red light
red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0, 300)

# Yellow light
yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0, 260)

# Green light
green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0, 220)

# Writing Texts Lane2
pen.penup()
pen.goto(-220, -10)
pen.color("white")
pen.write('Lane2', align="center", font=("Serif", 18))

# Draw box around the stoplight Lane2
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-320, -60)
pen.pendown()
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)

# Red light
red_light1 = turtle.Turtle()
red_light1.shape("circle")
red_light1.color("grey")
red_light1.penup()
red_light1.goto(-290, 40)

# Yellow light
yellow_light1 = turtle.Turtle()
yellow_light1.shape("circle")
yellow_light1.color("grey")
yellow_light1.penup()
yellow_light1.goto(-290, 0)

# Green light
green_light1 = turtle.Turtle()
green_light1.shape("circle")
green_light1.color("grey")
green_light1.penup()
green_light1.goto(-290, -40)

# Writing Texts Lane3
pen.penup()
pen.goto(220, -10)
pen.color("white")
pen.write('Lane3', align="center", font=("Serif", 18))

# Draw box around the stoplight Lane3
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(320, -60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

# Red light
red_light2 = turtle.Turtle()
red_light2.shape("circle")
red_light2.color("grey")
red_light2.penup()
red_light2.goto(290, 40)

# Yellow light
yellow_light2 = turtle.Turtle()
yellow_light2.shape("circle")
yellow_light2.color("grey")
yellow_light2.penup()
yellow_light2.goto(290, 0)

# Green light
green_light2 = turtle.Turtle()
green_light2.shape("circle")
green_light2.color("grey")
green_light2.penup()
green_light2.goto(290, -40)

# Writing Texts Lane4
pen.penup()
pen.goto(0, -180)
pen.color("white")
pen.write('Lane4', align="center", font=("Serif", 18))

# Draw box around the stoplight Lane4
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(30, -310)
pen.pendown()
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

# Red light
red_light3 = turtle.Turtle()
red_light3.shape("circle")
red_light3.color("grey")
red_light3.penup()
red_light3.goto(0, -210)

# Yellow light
yellow_light3 = turtle.Turtle()
yellow_light3.shape("circle")
yellow_light3.color("grey")
yellow_light3.penup()
yellow_light3.goto(0, -250)

# Green light
green_light3 = turtle.Turtle()
green_light3.shape("circle")
green_light3.color("grey")
green_light3.penup()
green_light3.goto(0, -290)


while True:

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    k = 1
    a = random.randint(0, 11)
    b = random.randint(0, 11)
    c = random.randint(0, 11)
    d = random.randint(0, 11)
# Lane1
    Lane1()
    green_light.color("green")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("grey")
    red_light1.color("red")
    red_light2.color("red")
    red_light3.color("red")

    yellow_light.color("grey")
    yellow_light1.color("grey")
    yellow_light2.color("grey")
    yellow_light3.color("grey")
    sleep(k*cnt1)

# Delay 1
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("grey")
    red_light1.color("grey")
    red_light2.color("red")
    red_light3.color("red")

    yellow_light.color("yellow")
    yellow_light1.color("yellow")
    yellow_light2.color("grey")
    yellow_light3.color("grey")
    sleep(1)

# Lane2
    Lane2()
    green_light.color("grey")
    green_light1.color("green")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("red")
    red_light1.color("grey")
    red_light2.color("red")
    red_light3.color("red")

    yellow_light.color("grey")
    yellow_light1.color("grey")
    yellow_light2.color("grey")
    yellow_light3.color("grey")
    sleep(k*cnt2)

# Delay 2
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("red")
    red_light1.color("grey")
    red_light2.color("grey")
    red_light3.color("red")

    yellow_light.color("grey")
    yellow_light1.color("yellow")
    yellow_light2.color("yellow")
    yellow_light3.color("grey")
    sleep(1)

# Lane3
    Lane3()
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("green")
    green_light3.color("grey")

    red_light.color("red")
    red_light1.color("red")
    red_light2.color("grey")
    red_light3.color("red")

    yellow_light.color("grey")
    yellow_light1.color("grey")
    yellow_light2.color("grey")
    yellow_light3.color("grey")
    sleep(k*cnt3)

# Delay 3
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("red")
    red_light1.color("red")
    red_light2.color("grey")
    red_light3.color("grey")

    yellow_light.color("grey")
    yellow_light1.color("grey")
    yellow_light2.color("yellow")
    yellow_light3.color("yellow")
    sleep(1)

# Lane4
    Lane4()
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("green")

    red_light.color("red")
    red_light1.color("red")
    red_light2.color("red")
    red_light3.color("grey")

    yellow_light.color("grey")
    yellow_light1.color("grey")
    yellow_light2.color("grey")
    yellow_light3.color("grey")
    sleep(k*cnt4)

# Delay 4
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("grey")
    red_light1.color("red")
    red_light2.color("red")
    red_light3.color("grey")

    yellow_light.color("yellow")
    yellow_light1.color("grey")
    yellow_light2.color("grey")
    yellow_light3.color("yellow")
    sleep(1)

wn.mainloop()
