import base64

with open("/home/junu/Downloads/test2.jpeg", "rb") as image_file:
    base64_image_string = base64.b64encode(image_file.read()).decode('utf-8')
    print(base64_image_string)


print("hello word")