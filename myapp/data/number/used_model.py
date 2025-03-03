import matplotlib #type: ignore
matplotlib.use('Agg')  # ใช้ non-GUI backend

import tensorflow as tf #type: ignore
import pandas as pd #type: ignore
import numpy as np #type: ignore
import matplotlib.pyplot as plt #type: ignore

def predict(user_input):
    # ตรวจสอบขนาดของ user_input
    if user_input.shape != (28, 28):
        print("Input image must be of size 28x28")
        return
    
    # แปลงข้อมูลจาก (28, 28) เป็น (1, 28, 28, 1) เพื่อให้เหมาะกับโมเดล
    user_input = np.expand_dims(user_input, axis=-1)  # เพิ่มมิติที่ 3 (channels) เพื่อให้มีขนาดเป็น (28, 28, 1)
    user_input = np.expand_dims(user_input, axis=0)   # เพิ่มมิติที่ 0 (batch size) เพื่อให้มีขนาดเป็น (1, 28, 28, 1)
    
    # โหลดโมเดล
    loaded_model = tf.keras.models.load_model('myapp/data/number/model.h5')
    
    # ทำนายผล
    predictions = loaded_model.predict(user_input)
    
    # แสดงผลลัพธ์การทำนาย
    print(predictions)
    predicted_class = np.argmax(predictions)  # หา class ที่โมเดลทำนาย
    print(f"Predicted Class: {predicted_class}")
    


 

