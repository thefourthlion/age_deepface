from deepface import DeepFace

info = DeepFace.analyze(img_path="./photos/everett/me.jpg",
                        actions=['age', 'gender', 'race', 'emotion']
                        )

print(f"Gender: {info[0]['dominant_gender']} \n"
      f"Race: {info[0]['dominant_race']} \n"
      f"Age: {info[0]['age']} \n"
      f"Emotion: {info[0]['dominant_emotion']} \n"
      )

# print all information
# print(info)
