"""
AI Engineering Fundamentals: Basic Single-Neuron Prediction Model
Demonstrates how AI models multiply input features by weight to make a prediction.
"""

def predict_house_price(size_sqft: float) -> float: 
     # Simulated AI model Parameters (Weight and Bias)
      weight = 150.0 # Estimated price increase per square foot
       bias = 25000.0 # Base starting price

        # The fundamental AI equation: Output = (Input * Weight) + Bias
         predicted_price = (size_sqft * weight) + bias
          return predicted_price
  if __name__ = "__main__":
      house_sizes = [800, 1200, 2000]
      print("--- Basic AI Linear Regression Demo ---")
       for size in house_sizes: 
           price = predict_house_price(size)
           print(f"House Size: {size} sq ft | Predicted Price: ${price:,.2f}")
