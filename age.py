from deepface import DeepFace

result = DeepFace.verify(img1_path="../../../photos/joce.jpg",
                         img2_path="../../../photos/joce_phone.jpg")

info = DeepFace.analyze(img_path="../../../photos/joce.jpg",
                        actions=['age', 'gender', 'race', 'emotion']
                        )

print(f"Same Person: {result['verified']}")

print(f"Gender: {info[0]['dominant_gender']} \n"
      f"Race: {info[0]['dominant_race']} \n"
      f"Age: {info[0]['age']} \n"
      f"Emotion: {info[0]['dominant_emotion']} \n"
      )
