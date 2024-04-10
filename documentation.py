api_documentation = """
# FastAPI Application for Nutrition Tracking and Gamification

## Motivation

The primary goal of this FastAPI application is to encourage users to build and maintain healthy eating habits through consistent nutrition tracking. By gamifying the experience, the app aims to make the process of tracking nutrition engaging and rewarding. Users are motivated not only by personal health benefits but also by the prospect of social validation and competition. The system assigns scores and ranks, fostering a community environment where users can compare their progress and compete in a friendly manner. This approach helps users stay committed to their nutrition and fitness goals, making healthy eating a consistent part of their lifestyle.

## Snacc Score System

The Snacc Score is a comprehensive metric used to quantify a user's adherence to nutritional goals, exercise routines, and overall healthy lifestyle practices. The system breaks down into several components, each reflecting different aspects of health and wellness:

- **Protein Goals Percentage:** Reflects how well users meet their daily protein intake targets based on their physical metrics.
- **Calorie Balance:** Evaluates users' success in achieving a net zero or calorie deficit, aiding in weight management.
- **Nutrition Diversity Score:** Measures the variety of nutrients in the user’s diet, promoting balanced eating habits.
- **Exercise Minutes Goals:** Tracks whether users are meeting their daily exercise duration targets.
- **Active Calorie Goals:** Assesses if users are reaching their daily active calorie burn objectives.

Each of these components contributes to the daily Snacc Score, which is then averaged over a week to calculate the weekly Snacc Score, providing a longer-term view of the user's habits.

## Using the Endpoints

Developers integrating with this API can utilize the following endpoints to implement the gamification system:

- **POST /calculate_protein_goal_percentage/**: Accepts user details and daily protein intake to calculate the percentage of protein goal achieved.
- **POST /calculate_calorie_balance/**: Takes user information, daily nutritional data, and target calories to determine the calorie balance score.
- **POST /calculate_nutrition_diversity_score/**: Receives a list of meal logs to compute the nutrition diversity score based on the variety of consumed foods.
- **POST /calculate_exercise_goals/**: Requires exercise log details and target exercise minutes to calculate the exercise goals score.
- **POST /calculate_active_calorie_goals/**: Accepts exercise data to evaluate the achievement of active calorie burn goals.
- **POST /calculate_daily_snacc_score/**: Combines the scores from all categories to yield the daily Snacc Score.
- **POST /calculate_weekly_snacc_score/**: Uses a list of daily Snacc Scores to compute the average weekly Snacc Score.

Developers should ensure that the user’s activity data is collected and sent to these endpoints accurately to calculate the respective scores. The daily and weekly Snacc Scores can then be used within the application to display user progress, rank users in leaderboards, and distribute rewards, thereby enhancing user engagement and promoting healthy competition.

This FastAPI setup facilitates easy integration and expansion, allowing developers to further build on this system with additional features such as notifications, personalized health tips, and community challenges, enhancing the overall user experience and engagement.

"""