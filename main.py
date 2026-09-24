"""
AI & Data Science Project: Simple Rule-Based Sentiment Analyzer
Demonstrates foundational NLP concepsts learened through self-directed study.
"""

def analyze_sentiment(text: str) -> dict:    
  # Keywords representing postive and negative sentiment
  positive_words = {"great", "wonderful", "growth", "innovative", "good", "promising", "successful", "breakthrough"}
  negative_words = {"decline", "risky", "loss", "failure", "crisis", "danger", "refuse", "delay"}

  # Tokenization & normalization  (converting text to lowercase words)
  words = text.lower().replace(".","").replace(",","").split()

  pos_count = sum(1 for word in words if word in postive_words)
  neg_count = sum(1 for word in words if word in negative_words)

  total_matches = pos_count + neg_count

  if total_matches ==0:
      sentiment = "NEUTRAL"
      confidence = 0.0
elif pos_count > neg_count:
     sentiment = "POSITIVE"
      confidence = round(pos_count / len(words), 2)
else:
       sentiment = "NEUTRAL" 
       confidence = 0.5

 return {
      "text": text,
       "sentiment": sentiment,
       "positive_words_count": pos_count,
       "negative_word_count": neg_count,
       "confidence_score": confidence

   
#Example usage to demonstrate functionality
if __name__ == "__main__": 
    headline = [
        "NVIDIA announces an innovative breakthrough in AI model training.",
        "Market experiences a concerning drop due to global supply delays."
        "The committee met today to review quarterly financial reports." 
   ]  

   print("---AI Sentiment Analysis Demo ---")
   for headline in headlines:
        result = analyze_sentiment(headline)  
        print(f"\nTEXT: \"{result['text']}\"")
        print(f"Result: {result['sentiment']} | Confindence: {result['confidenc_score']}")
