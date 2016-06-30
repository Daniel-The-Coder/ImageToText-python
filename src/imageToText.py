from PIL import Image


def display(fileName):
    img = Image.open(fileName)

    imgWidth, imgHeight = img.size
    if imgWidth > imgHeight:
        imgNew = img.resize((int(100*imgWidth/imgHeight) ,50))
    else:
        imgNew = img.resize((100, int(50*imgHeight/imgWidth)))

    imgNew.save("jd_resized.jpeg")

    imgWidth, imgHeight = imgNew.size
    #L=[]
    for i in range(imgHeight):
        st = ""
        #lst = []
        for j in range(imgWidth):
            pixel = imgNew.getpixel((j,i))
            if isinstance(pixel, int):
                if pixel < 255/4:#[0]+pixel[1]+pixel[2] < 255*3/2:
                    st += " "
                    #lst+=[" "]
                elif pixel <255/2:
                    st += "."
                    #lst+=["."]
                elif pixel < (3*255/4):
                    st += "/"
                    #lst+=["/"]
                else:
                    st+= "X"
                    #lst+=["X"]
            else:
                if pixel[0]+pixel[1]+pixel[2] < 255*3/4:
                    st += " "
                elif pixel[0]+pixel[1]+pixel[2] < 255*3/2:
                    st += "."
                elif pixel[0]+pixel[1]+pixel[2] < 255*9/4:
                    st += "/"
                else:
                    st += "X"
        #L+=[lst]
        print(st)
    #print(L)

while True:
    fileName = input("Enter file name: ")
    display(fileName)
    print()
