# Restaurant ChatBot - Grosso Salís

## Overview
This project is a chatbot assistant for the "Grosso Salís" restaurant, designed to help customers place food orders for delivery or pickup. The chatbot uses OpenAI's GPT-3.5-turbo model to handle natural language interactions and generates a JSON summary of the order at the end of the conversation.

## Features
- **Interactive Chat Interface**: Built with Panel for a user-friendly experience
- **Order Management**: Handles pizza orders with customizable sizes and extra ingredients
- **Delivery/Pickup Options**: Asks customers for their preferred order method and collects delivery addresses when needed
- **JSON Order Summary**: Generates a structured JSON file summarizing the order details
- **Custom Styling**: Dark-themed UI with responsive design elements

## Menu Options
### Pizzas
- Margarita (€10)
- Pepperoni (€12)
- Hawaiana (€11)
- Vegetal (€10)

**Sizes**:
- Small (-€2)
- Medium (base price)
- Large (+€2)

### Extra Ingredients
- Cheese (€1.5)
- Mushrooms (€1)
- Ham (€2)
- Olives (€1)

### Drinks
- Soda (€2)
- Water (€1.5)
- Beer (€3)

## How It Works
1. The chatbot greets the customer and asks what they'd like to order
2. It guides the customer through the ordering process, asking about:
   - Pizza type and size
   - Extra ingredients
   - Drink selections
   - Delivery or pickup preference
   - Delivery address (if applicable)
3. At the end of the conversation, clicking "Finalizar pedido" (Finish Order) generates a JSON file with the order details

## Technical Details
- **Backend**: OpenAI GPT-3.5-turbo model
- **Frontend**: Panel library for Python
- **Dependencies**:
  - openai
  - panel
  - jupyter_bokeh
  - json

## Setup
```bash
pip install jupyter_bokeh openai panel
