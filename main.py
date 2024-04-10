from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from documentation import api_documentation

app = FastAPI(title="Snacc Score",
              description=api_documentation,
              version="1.0.0")


# Models
class User(BaseModel):
  height: float  # in centimeters
  weight: float  # in kilograms
  gender: str
  age: int


class Nutrition(BaseModel):
  calories: float
  protein_g: float
  carbohydrates_g: float
  fats_g: float
  fibers_g: float
  added_sugars_g: float
  saturated_fat_g: float


class MealLog(BaseModel):
  food_item: str
  ingredients: List[str]
  portion_size: str
  nutrition: Nutrition


class ExerciseLog(BaseModel):
  exercise_minutes: int
  active_calories: float


class SnaccScore(BaseModel):
  date: str  # Example date format: "2023-01-01"
  score: float


# Endpoint to calculate protein goals percentage
@app.post("/calculate_protein_goal_percentage/")
def calculate_protein_goal_percentage(user: User,
                                      daily_protein_intake: float) -> float:
  """
    Calculate the percentage of protein goal achieved.

    - **user**: User object containing physical attributes.
    - **daily_protein_intake**: Total protein intake for the day in grams.
    - **return**: Percentage of protein goal achieved.
    """
  protein_goal = user.weight * 0.8  # Example: 0.8g per kg body weight
  percentage = (daily_protein_intake / protein_goal) * 100
  return percentage


# Endpoint to calculate calorie balance
@app.post("/calculate_calorie_balance/")
def calculate_calorie_balance(user: User, nutrition: Nutrition,
                              target_calories: float) -> float:
  """
    Calculate points based on achieving net zero or calorie deficit.

    - **user**: User object containing physical attributes.
    - **nutrition**: Daily nutritional intake.
    - **target_calories**: Target daily calorie intake.
    - **return**: Points for calorie balance.
    """
  calorie_balance = nutrition.calories - target_calories
  return 2.0 if calorie_balance <= 0 else 0.0  # 2 points for net zero or deficit


# Endpoint to calculate nutrition diversity score
@app.post("/calculate_nutrition_diversity_score/")
def calculate_nutrition_diversity_score(meal_logs: List[MealLog]) -> float:
  """
    Calculate nutrition diversity score based on the variety of nutrients consumed.

    - **meal_logs**: List of meal logs for a day.
    - **return**: Nutrition diversity score.
    """
  unique_ingredients = {
    ingredient
    for meal in meal_logs for ingredient in meal.ingredients
  }
  diversity_score = min(len(unique_ingredients) / 10,
                        2.0)  # Assume 2 points max
  return diversity_score


# Endpoint to calculate exercise minutes goals
@app.post("/calculate_exercise_goals/")
def calculate_exercise_goals(exercise_log: ExerciseLog,
                             target_minutes: int) -> float:
  """
    Calculate points based on achieving exercise minutes goals.

    - **exercise_log**: Log of daily exercise.
    - **target_minutes**: Target exercise minutes per day.
    - **return**: Points for exercise goals.
    """
  return 1.5 if exercise_log.exercise_minutes >= target_minutes else 0.0  # 1.5 points max


# Endpoint to calculate active calorie goals
@app.post("/calculate_active_calorie_goals/")
def calculate_active_calorie_goals(exercise_log: ExerciseLog,
                                   target_active_calories: float) -> float:
  """
    Calculate points based on meeting active calorie goals.

    - **exercise_log**: Log of daily exercise.
    - **target_active_calories**: Target active calories to burn per day.
    - **return**: Points for active calorie goals.
    """
  return 1.5 if exercise_log.active_calories >= target_active_calories else 0.0  # 1.5 points max


@app.post("/calculate_daily_snacc_score/")
def calculate_daily_snacc_score(protein_percentage: float,
                                calorie_balance: float,
                                nutrition_diversity: float,
                                exercise_goals: float,
                                active_calorie_goals: float) -> float:
  """
    Calculate total daily Snacc Score.
    """
  return protein_percentage + calorie_balance + nutrition_diversity + exercise_goals + active_calorie_goals


# Business Logic for Weekly Calculations


def calculate_weekly_snacc_score(daily_scores: List[SnaccScore]) -> float:
  """
    Calculate the weekly Snacc Score as a rolling average of the last 7 days.

    - **daily_scores**: List of daily Snacc Scores over the last 7 days.
    - **return**: Weekly Snacc Score as a rolling average.
    """
  total_score = sum(score.score for score in daily_scores)
  return total_score / len(daily_scores)


# Endpoint for Weekly Snacc Score Calculation
@app.post("/calculate_weekly_snacc_score/")
def weekly_snacc_score_endpoint(daily_scores: List[SnaccScore]) -> float:
  """
    Endpoint to calculate the weekly Snacc Score.

    - **daily_scores**: List of daily Snacc Scores over the last 7 days.
    - **return**: Weekly Snacc Score as a rolling average.
    """
  return calculate_weekly_snacc_score(daily_scores)


# Additional logic for distributing Snacc Coins and other gamification features can be added similarly
