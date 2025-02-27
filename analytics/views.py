# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from textblob import TextBlob
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# @api_view(['POST'])  # Ensure it's POST
# def analyze_feedback(request):
#     feedback_text = request.data.get("feedback", "")

#     analyzer = SentimentIntensityAnalyzer()
#     sentiment_score = analyzer.polarity_scores(feedback_text)

#     if sentiment_score["compound"] >= 0.05:
#         sentiment = "Positive"
#     elif sentiment_score["compound"] <= -0.05:
#         sentiment = "Negative"
#     else:
#         sentiment = "Neutral"

#     return Response({"feedback": feedback_text, "sentiment": sentiment})



from rest_framework.decorators import api_view
from rest_framework.response import Response
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from .models import Feedback

@api_view(['POST'])
def analyze_feedback(request):
    feedback_text = request.data.get("feedback", "")

    # Sentiment Analysis
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(feedback_text)

    if sentiment_score["compound"] >= 0.05:
        sentiment = "Positive"
    elif sentiment_score["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Attrition Risk (Placeholder logic, we can improve this)
    attrition_risk = "High" if sentiment == "Negative" else "Low"

    # Save to Database
    feedback = Feedback.objects.create(
        text=feedback_text, sentiment=sentiment, attrition_risk=attrition_risk
    )

    return Response({
        "feedback": feedback.text,
        "sentiment": feedback.sentiment,
        "attrition_risk": feedback.attrition_risk
    })
