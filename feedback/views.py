from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Feedback
from .serializers import FeedbackSerializer
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

@api_view(['POST'])
def submit_feedback(request):
    """
    API to submit anonymous feedback.
    """
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        feedback = serializer.save()

        # Analyze sentiment using VADER
        sentiment_score = sia.polarity_scores(feedback.text)
        if sentiment_score['compound'] >= 0.05:
            feedback.sentiment = "positive"
        elif sentiment_score['compound'] <= -0.05:
            feedback.sentiment = "negative"
        else:
            feedback.sentiment = "neutral"

        feedback.save()
        return Response({"message": "Feedback submitted successfully!"})
    
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def list_feedback(request):
    """
    API to list all anonymous feedback.
    """
    feedback = Feedback.objects.all().order_by('-created_at')
    serializer = FeedbackSerializer(feedback, many=True)
    return Response(serializer.data)
