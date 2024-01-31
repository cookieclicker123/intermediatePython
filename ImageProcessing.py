from PIL import Image, ImageOps
import matplotlib.pyplot as plt

imagePath = '/Users/seb/Documents/raceCar.png'

image = Image.open(imagePath)

#rotated_image = image.rotate(45)  # Rotate image 45 degrees
#rotated_image.show()

#from PIL import ImageFilter

#blurred_image = image.filter(ImageFilter.BLUR)  # Apply blur filter
#blurred_image.show()

#from PIL import ImageDraw

#draw = ImageDraw.Draw(image)
#draw.rectangle(((50, 50), (500, 500)), outline="red")  # Draw a red rectangle
#draw.text((100, 100), 'Hello', fill='blue')  # Draw blue text
#image.show()

print(image.format)  # Print image format
print(image.size)  # Print image size
print(image.mode)  # Print image mode

grayImage = ImageOps.grayscale(image)

new_size = (600,600)  
resized_image = grayImage.resize(new_size)

crop_area = (25, 200, 500, 400)
cropped_image = resized_image.crop(crop_area)

plt.imshow(cropped_image,cmap='gray')
plt.axis('off')
plt.show()


processed_image_path = '/Users/seb/Documents/ProcessedRaceCar.png'  # Replace with your save path
cropped_image.save(processed_image_path)


print(cropped_image.format)  #`` Print image format
print(cropped_image.size)  # Print image size
print(cropped_image.mode)  # Print image mode
