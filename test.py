import cv2
path1 = "E:/MẠNH_12725/MANH_12725/2022-10-13/CAMERA 03_C3-20-ABUAA-H/test/2022-10-13_04-00-55-4742.jfz/Input1_Camera0.jpg"
path = "C:/Check1/2022-10-17_11-02-04-437184.jpg"
path = r"E:\MẠNH_12725\MANH_12725\2022-10-13\CAMERA 02_C2-20-ABUAA-H\NG\2022-10-13_04-14-39-4821.jfz\Input1_Camera0.jpg"
path = r"E:\1.jpg"
img = cv2.imread(path)
cv2.imshow('a',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 