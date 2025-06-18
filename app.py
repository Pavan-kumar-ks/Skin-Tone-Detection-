import stone  # pip install skin-tone-classifier
import cv2  # pip install opencv-python
from tkinter import Tk, filedialog, Button, Label, Frame, Toplevel
from PIL import Image, ImageTk
from json import dumps

image_references = []

TONE_LABELS = {
    "CL": "Cool Light",
    "CI": "Cool Intermediate",
    "CG": "Cool Fair",
    "CW": "Cool Warm",
    "DW": "Dark Warm",
    "MW": "Medium Warm",
    "CE": "Cool Sand",
    "CD": "Deep Brown" 
    # Add additional mappings as necessary
}

def process_image():
    filepath = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    )
    if not filepath:
        print("No file selected.")
        return

    result = stone.process(filepath, image_type="color", return_report_image=True)

    report_images = result.pop("report_images") 

    if report_images:
        display_results(filepath, result["faces"], report_images)
    else:
        print("No faces detected in the image.")

    result_json = dumps(result, indent=4)
    print("Result in JSON format:")
    print(result_json)


def display_results(filepath, faces, report_images):
    result_window = Toplevel()
    result_window.title("Skin Tone Analysis")
    result_window.geometry("1000x650")


    heading_label = Label(
        result_window,
        text="SKIN TONE DETECTION WITH MNACHINE LEARNING",
        font=("Arial", 20, "bold"),
        fg="dark blue",
        bg="#ffffff"
    )
    heading_label.pack(pady=10)

    img = Image.open(filepath)
    img.thumbnail((400, 400))
    photo = ImageTk.PhotoImage(img)

    image_references.append(photo)

    images_frame = Frame(result_window, bg="#ffffff")
    images_frame.pack(side="top", fill="x", pady=20)  

    img_label = Label(images_frame, image=photo)
    img_label.pack(side="left", padx=10)  
    results_frame = Frame(result_window, bg="#ffffff", padx=10, pady=10)
    results_frame.pack(side="right", fill="both", expand=True)

    for face in faces:
        tone_label = face.get("tone_label", "Unknown")
        tone_description = TONE_LABELS.get(tone_label, "Unknown Tone")
        accuracy = face.get("accuracy", 0.0)
        face_id = face.get("face_id", "N/A")

        Label(
            results_frame,
            text=f"Face ID: {face_id}\nTone Label: {tone_label} ({tone_description}) \nAccuracy: {accuracy:.2f}%",
            font=("Arial",16),
            fg="blue",
            bg="#ffffff",
            anchor="w",
            justify="left",
        ).pack(pady=10, anchor="w")

    face_id = 1  
    if face_id in report_images:
        report_img = report_images[face_id]
        report_photo = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(report_img, cv2.COLOR_BGR2RGB)))

        image_references.append(report_photo)

        report_label = Label(images_frame, image=report_photo)
        report_label.pack(side="left", padx=10)  



# Create the main GUI
root = Tk()
root.title("Skin Tone Classifier")
root.geometry("1000x450")
root.configure(bg="#f0f0f0")

frame = Frame(root, bg="#ffffff", padx=20, pady=20, relief="groove", borderwidth=2)
frame.pack(expand=True, fill="both", pady=40, padx=40)

# Add a heading at the top
Label(
    frame,
    text="SKIN TONE DETECTION WITH MNACHINE LEARNING",
    font=("Helvetica", 18, "bold"),
    fg="dark blue",
    bg="#ffffff"
).pack(pady=10)

# Add the label and button for selecting an image
Label(
    frame,
    text="Select an image to process:",
    font=("Helvetica", 12),
    bg="#ffffff"
).pack(pady=10)

Button(
    frame,
    text="Choose Image",
    command=process_image,
    bg="#4CAF50",
    fg="white",
    font=("Helvetica", 10, "bold"),
    padx=10,
    pady=5,
).pack(pady=10)

root.mainloop()
