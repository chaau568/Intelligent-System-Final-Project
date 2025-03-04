import json
import base64
import numpy as np #type: ignore
from PIL import Image #type: ignore
from io import BytesIO
from django.http import JsonResponse #type: ignore
from django.views.decorators.csrf import csrf_exempt #type: ignore
from django.shortcuts import render #type: ignore
from .data.emotion import use_model as model_emo
from .data.number import used_model as model_num

def home(request):
  return render(request, 'home.html')

def emotion_details(request):
  return render(request, 'emotion_details.html')

def show_emotion_predict(user_input):
  result = model_emo.predict(user_input)
  return result

def show_emotion_graph(user_input):
  result = model_emo.graph(user_input)
  return result

def show_number_predict(user_input):
  result = model_num.predict(user_input)
  return result

def show_number_graph(user_input):
  result = model_num(user_input)
  return result

def emotion_model(request):
  return render(request, 'emotion_model.html')

def show_result_emo(request):
  details = {
    'text': None,
    'predict': None,
    'confidence': None,
    'graph': None
  }
  if request.method == "POST":
    user_input = request.POST.get('user_input', '')
    details['text'] = user_input

    result = show_emotion_predict(user_input)
    if isinstance(result, dict):
      details['predict'] = result.get('predict', None)
      details['confidence'] = result.get('confidence', None)
    details['graph'] = show_emotion_graph(user_input)

  return render(request, 'show_result_emo.html', {"details": details})

def number_details(request):
  return render(request, 'number_details.html')

def number_model(request):
  return render(request, 'number_model.html')

@csrf_exempt
def show_result_num(request):
  details = {
    'predict': None,          
    'confidence': None,  
    'all_predictions': None,
    'graph': None  
  }
  if request.method == "POST":
    try:
      data = json.loads(request.body)
      image_data = data.get("image", "")

      if not image_data:
        return JsonResponse({"error": "No image data"}, status=400)

      # แปลง Base64 -> NumPy Array
      image_data = image_data.split(",")[1]  # ตัด "data:image/png;base64,"
      img = Image.open(BytesIO(base64.b64decode(image_data)))

      img = img.convert("L").resize((28, 28))  # แปลงเป็นขาวดำ + ปรับขนาด 28 x 28
      img_array = np.array(img) / 255.0  # Normalize เป็น 0-1

      result = show_number_predict(img_array)
      if isinstance(result, dict):
        details['predict'] = result.get('predict', None)
        details['confidence'] = result.get('confidence', None)
        details['all_predictions'] = result.get('all_predictions', None)
        # details['graph'] = show_number_graph(details['all_predictions'])
        print("Yes")
        # return render(request, 'show_result_num.html', {"details": details})
      return JsonResponse({"message": "Image processed successfully!"})
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=500)

  return JsonResponse({"error": "Invalid request"}, status=400)