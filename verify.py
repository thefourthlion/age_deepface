from deepface import DeepFace

result = DeepFace.verify(img1_path="./photos/everett/me.jpg",
                         img2_path="./photos/everett/me_phone.jpg")

print(f"Same Person: {result['verified']}")

# print all results
# print(result)
