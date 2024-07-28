import sys
from PIL import Image, ImageOps

def main():
  if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
  if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

  input_path = sys.argv[1]
  output_path = sys.argv[2]

  # Extract extensions and convert to lowercase
  input_extension = input_path.split('.')[-1].lower()
  output_extension = output_path.split('.')[-1].lower()

  # Validate extensions
  valid_extensions = ["jpg", "jpeg", "png"]
  if input_extension not in valid_extensions or output_extension not in valid_extensions:
    sys.exit("Invalid input: Only .jpg, .jpeg, or .png files are allowed")

  # Validate extension matching
  if input_extension != output_extension:
    sys.exit("Input and output have different extensions")

  try:
    input_image = Image.open(input_path)
  except FileNotFoundError:
    sys.exit("Input file does not exist")
  try:
    shirt = Image.open("shirt.png")
  except FileNotFoundError:
    sys.exit("Shirt image (shirt.png) does not exist")
  except Exception as e:
    sys.exit(f"Error opening shirt image: {e}")

  try:
    # Resize and crop the input image to match the size of the shirt
    size = shirt.size
    input_image = ImageOps.fit(input_image, size)

    # Paste the shirt onto the resized input image at position (0, 0)
    input_image.paste(shirt, (0, 0), shirt)  # Pass shirt as mask for transparency

    input_image.save(output_path)
    print("Image saved successfully")
  except Exception as e:
    sys.exit(f"Error processing image: {e}")

if __name__ == "__main__":
  main()
