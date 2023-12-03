import random
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
        """Set units to imperial or metric based on country if possible"""
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None
    
def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°F")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")


def suggest_outfit(weather_data):
    description = weather_data['weather'][0]['description'].lower()
    temperature = weather_data['main']['temp']

    outfit_suggestions = []

    if "rain" in description:
        outfit_suggestions = ["Bring an umbrella and wear a waterproof jacket and boots."]
    elif "snow" in description:
        outfit_suggestions = ["Wear a warm coat and boots."]
    elif "cloud" in description:
        outfit_suggestions = ["A light jacket may be needed."]
    else:
        outfit_suggestions = ["Make sure to use some sunscreen!"]

    if temperature <32:
        outfit_suggestions = ["Wear thicker layers like thermal underwear beneath jeans or snow pants, paired with a down-filled coat and heavy-duty snow boots", 
                            "Wear a wool or cashmere sweater under a quilted or fur-lined parka, paired with insulated leggings or pants and snow boots", 
                            "Wear fleece-lined everything: leggings, tops, and a down-filled jacket, along with snow pants and insulated, waterproof boots"]
    elif temperature < 50:
        outfit_suggestions = ["Wear a sweater layered over a long-sleeved shirt or blouse, paired with jeans or trousers and ankle boots", "Try a puffer vest over a button-up shirt, paired with corduroy pants or leggings and sneakers", 
                            "Wear a turtleneck under a wool coat, paired with jeans or a skirt and knee-high boots", "Wear some fleece-lined leggings or thermal pants layered under jeans or a long skirt, paired with a chunky knit sweater and winter boots", 
                            "Wear a parka or down jacket over a sweater, paired with insulated pants or jeans and snow boots", "Wear a thermal top under a heavy coat, paired with fleece-lined pants or leggings and insulated waterproof boots"]
    elif temperature > 80:
        outfit_suggestions = ["Wear some linen pants or culottes paired with a sleeveless top or breezy blouse", "Wear breathable cotton or linen shorts with a loose-fitting tank top or crop top and sandals"]
    else:
        outfit_suggestions = ["Wear a light sweater or cardigan paired with jeans or trousers", "Wear a long-sleeved shirt with a lightweight jacket and jeans", 
                            "Wear a T-shirt layered with a denim or utility jacket and leggings", "Wear a T-shirt or blouse with jeans or shorts", 
                            "Wear shorts or a skirt with a breezy blouse or T-shirt", " Wear linen pants paired with a tank top or a lightweight blouse"]
        
    suggestion = random.choice(outfit_suggestions)

    return suggestion

def suggest_activities(weather_data):
    description = weather_data['weather'][0]['description'].lower()
    temperature = weather_data['main']['temp']

    activities = []

    if "rain" in description:
        activities = ["Visit a museum", "Watch a movie", "Have a movie marathon", "Read a book", "Play a board game", "Solve a puzzle", "Listen to some music", "Have a home spa day", "Organize or clean your home", "Connect with friends online", "Relax and meditate"]
    elif "snow" in description:
        activities = ["Go skiing", "Build a snowman", "Have a snowball fight", "Find a hill to sled down", "Have some hot cocoa and warm treats", "Bake somesomething sweet", "Go on a winter hike", "Watch a movie or show", "Have a snowy photoshoot", "cozy up and read something"]
    elif "cloud" in description:
        activities = ["Take a walk in the park", "Go for a hike", "Visit a botanical garden", "Do some photography", "Go on a jog", "Take some time to meditate", "Watch a movie", "Do some home projects", "Visit a museum", "Visit an art gallery"]
    else:
        activities = ["Have a picnic", "Play some sports", "Go for a bike ride", "Go on a hike", "Have a barbecue", "Visit a Farmer's market", "Do some photography", "Vist botanical gardens or parks", "Do some bird watching"]

    if temperature < 50:
        activities += ["Bake cookies", "Have a cozy movie night", "Do indoor exercises"]
    elif temperature > 80:
        activities += ["Go swimming", "Have a picnic in the shade", "Play water sports"]

    suggestion = random.choice(activities)

    return suggestion


def suggest_meals(weather_data):
    description = weather_data['weather'][0]['description'].lower()
    temperature = weather_data['main']['temp']

    breakfasts = []
    lunches = []
    dinners = []

    if "rain" in description:
        breakfasts = ["Oatmeal", "Pancakes", "French toast", "Eggs Benedict", "Waffles", "Breakfast burrito", "Bagel with cream cheese", "Smoothie bowl", "Avocado toast", "Fruit salad"]
        lunches = ["Soup and sandwich", "Grilled cheese", "Ramen", "Caesar salad", "Caprese sandwich", "Quiche", "BLT sandwich", "Chicken wrap", "Greek salad", "Vegetarian sushi"]
        dinners = ["Chicken noodle soup", "Spaghetti", "Vegetable curry", "Baked ziti", "Stir-fry", "Beef stew", "Chicken Alfredo", "Shrimp scampi", "Chickpea curry", "Mushroom risotto"]
        drinks = ["Hot tea", "Cocoa", "Chai latte", "Mulled wine", "Hot chocolate", "Warm apple cider", "Irish coffee", "Ginger tea", "Mocha", "Spiced chai latte"]
    elif "snow" in description:
        breakfasts = ["Porridge", "Waffles", "Eggs Benedict", "Pancakes", "French toast", "Breakfast burrito", "Bagel with cream cheese", "Smoothie bowl", "Avocado toast", "Fruit salad"]
        lunches = ["Tomato soup", "Baked potatoes", "Beef stew", "Chili", "Chicken pot pie", "Potato soup", "Chicken and rice casserole", "Clam chowder", "Meatball stew", "Shepherd's pie"]
        dinners = ["Fondue", "Roast chicken", "Beef chili", "Beef stroganoff", "Chicken marsala", "Coq au vin", "Lasagna", "Chicken Parmesan", "Vegetable curry", "Mushroom risotto"]
        drinks = ["Mulled wine", "Hot chocolate", "Warm apple cider", "Irish coffee", "Peppermint hot chocolate", "Hot toddy", "Eggnog", "Spiced chai latte", "Irish cream coffee", "Caramel apple cider"]
    elif "cloud" in description:
        breakfasts = ["Yogurt with granola", "Fruit smoothie", "Avocado toast", "Omelette", "Bacon and eggs", "Bagel with lox and cream cheese", "Frittata", "Crepes", "Peaches and cream oatmeal", "Breakfast parfait"]
        lunches = ["Caesar salad", "Caprese sandwich", "Quiche", "Greek salad", "Tomato and mozzarella salad", "Chicken Caesar wrap", "Grilled vegetable panini", "Spinach and feta salad", "Shrimp and avocado salad", "Mediterranean wrap"]
        dinners = ["Pasta with pesto", "Stir-fry", "Vegetarian curry", "Baked salmon", "Caprese pasta", "Vegetable stir-fry", "Ratatouille", "Margherita pizza", "Chickpea and spinach curry", "Mushroom risotto"]
        drinks = ["Iced tea", "Smoothie", "Cold brew coffee", "Lemonade", "Iced coffee", "Fruit-infused water", "Green tea lemonade", "Mango smoothie", "Peach iced tea", "Strawberry banana smoothie"]
    else:
        breakfasts = ["Fruit salad", "Smoothie bowl", "Eggs and bacon", "Pancakes", "French toast", "Breakfast burrito", "Bagel with cream cheese", "Yogurt with granola", "Frittata", "Avocado toast"]
        lunches = ["Grilled chicken salad", "Wrap", "Sushi", "Caesar salad", "Caprese sandwich", "Quinoa salad", "Greek salad", "Cobb salad", "Shrimp sushi rolls", "Chicken Caesar wrap"]
        dinners = ["BBQ ribs", "Grilled fish", "Vegetable stir-fry", "Chicken Alfredo", "Salmon with lemon dill sauce", "Teriyaki chicken", "Pesto pasta with chicken", "Mango chicken curry", "Caprese pizza", "Garlic butter shrimp pasta"]
        drinks = ["Iced water", "Lemonade", "Iced coffee", "Iced tea", "Fruit-infused water", "Mango smoothie", "Strawberry banana smoothie", "Peach iced tea", "Pineapple coconut smoothie", "Green tea lemonade"]


    breakfast = random.choice(breakfasts)
    lunch = random.choice(lunches)
    dinner = random.choice(dinners)
    drink = random.choice(drinks)

    return breakfast, lunch, dinner, drink




    
if __name__ == "__main__":
    api_key = "c9a340caa354b220f863dc4586383dc6"
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

    outfits = suggest_outfit(weather_data)
    print("\nOutfit Suggestions:")
    for suggestion in outfits:
        print(suggestion)

    activities = suggest_activities(weather_data)
    print("\nActivity Suggestions:")
    for suggestion in activities:
        print(suggestion)

    breakfast, lunch, dinner = suggest_meals(weather_data)
    print("\nMeal Suggestions:")
    print(f"Breakfast: {breakfast}")
    print(f"Lunch: {lunch}")
    print(f"Dinner: {dinner}")
    print(f"Drink: {drink}")