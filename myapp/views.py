from django.shortcuts import render #type: ignore
from .data.emotion import use_model

def home(request):
  return render(request, 'home.html')

def emotion_details(request):
  return render(request, 'emotion_details.html')

def show_emotion_predict(user_input):
  result = use_model.predict(user_input)
  return result

def show_emotion_graph(user_input):
  result = use_model.graph(user_input)
  return result

def emotion_model(request):
  return render(request, 'emotion_model.html')

def show_result(request):
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

  return render(request, 'show_result.html', {"details": details})