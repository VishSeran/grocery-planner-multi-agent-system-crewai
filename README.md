# Structured Meal & Grocery Planner with CrewAI

A multi-agent AI system that turns a simple meal craving into a complete, budget-conscious shopping plan — recipe research, an organized shopping list, cost analysis, leftover management, and a consolidated report, all generated automatically by a coordinated team of AI agents.

## Overview

Planning meals and grocery shopping usually means hours of manual work: browsing recipes, calculating quantities, checking prices, organizing lists by store section, and making sure everything fits your budget and dietary needs. This project automates that entire workflow using [CrewAI](https://www.crewai.com/) to orchestrate a team of specialized AI agents, each responsible for one part of the process.

By the end of this project, you'll have a reusable framework that can generate comprehensive, organized shopping plans for any meal in minutes.

## What This Project Builds

- **Structured data models** using Pydantic to keep grocery lists and meal plans consistent and validated.
- **Specialized AI agents** for recipe research, shopping organization, budget optimization, leftover management, and report compilation.
- **A coordinated, sequential workflow** that transforms a meal request into a complete shopping strategy.
- **A reusable YAML configuration** for declaratively defining agents, tasks, and crew behavior.
- **A class-based `CrewBase` setup** that combines Python code with external YAML files, enabling clean separation of configuration from logic.

## The Agent Team

| Agent | Role |
|---|---|
| **Meal Planner & Recipe Researcher** | Searches for recipes matching dietary needs, budget, and skill level, and produces a structured meal plan |
| **Shopping Organizer** | Converts the meal plan into a shopping list grouped by store section, with quantities scaled to servings |
| **Budget Advisor** | Analyzes total cost against the budget and researches current prices and money-saving alternatives |
| **Leftover Manager** | Suggests creative uses for leftover ingredients to reduce food waste (defined via YAML + `CrewBase`) |
| **Report Compiler** | Consolidates every agent's output into one cohesive, user-friendly shopping guide |

## Data Models

Built with Pydantic for validated, predictable structure:

- **`GroceryItem`** — a single grocery item (name, quantity, estimated price, store category)
- **`MealPlan`** — a recipe with difficulty, servings, and researched ingredients
- **`ShoppingCategory`** — a store section with its items and an estimated subtotal
- **`GroceryShoppingPlan`** — the full plan: budget, meal plans, shopping sections, and money-saving tips

## How It Works

1. Provide a meal request — dish name, servings, budget, dietary restrictions, and cooking skill level.
2. The **Meal Planner** researches a matching recipe and ingredient list.
3. The **Shopping Organizer** groups those ingredients by store section and scales quantities.
4. The **Budget Advisor** checks the total against your budget and adds cost-saving suggestions.
5. The **Leftover Manager** proposes bonus recipes to use up any excess ingredients.
6. The **Report Compiler** merges everything into a single, comprehensive shopping guide.

Agents run sequentially, each with access to the outputs of the agents before it via CrewAI's task `context`.

## Tech Stack

- [`pydantic`](https://docs.pydantic.dev/latest/) — data validation and structured models
- [`crewai`](https://www.crewai.com/) / [`crewai-tools`](https://github.com/crewAIInc/crewAI-tools) — multi-agent orchestration and tools
- [`langchain`](https://python.langchain.com/) / [`langchain-openai`](https://python.langchain.com/) — LLM orchestration
- An LLM of your choice (configurable via `crewai.LLM`)
- [`SerperDevTool`](https://serper.dev/) — web search for real-time recipe and pricing information

## Getting Started

### Prerequisites

- Python 3.10+
- An LLM provider of your choice, configured with your own API key
- A [Serper](https://serper.dev/) API key for web search

### Installation

```bash
pip install langchain crewai langchain-community langchain-openai crewai-tools
```

### Configuration

Set your LLM credentials as required by your provider, and add your Serper API key:

```python
import os
os.environ["SERPER_API_KEY"] = "your-serper-api-key"
```

Then initialize an LLM of your choice, for example:

```python
from crewai import LLM
llm = LLM(model="your-model-name")
```

### Project Structure

```
.
├── config/
│   ├── agents.yaml      # YAML-based agent definitions (e.g. Leftover Manager)
│   └── tasks.yaml       # YAML-based task definitions
├── leftover.py          # CrewBase class wiring the YAML-configured agent/task
├── meal_grocery_planner.ipynb
└── README.md
```

### Running the Crew

```python
from crewai import Crew, Process

complete_grocery_crew = Crew(
    agents=[meal_planner, shopping_organizer, budget_advisor, yaml_leftover_manager, summary_agent],
    tasks=[meal_planning_task, shopping_task, budget_task, yaml_leftover_task, summary_task],
    process=Process.sequential,
    verbose=True
)

result = complete_grocery_crew.kickoff(
    inputs={
        "meal_name": "Chicken Stir Fry",
        "servings": 4,
        "budget": "$25",
        "dietary_restrictions": ["no nuts", "low sodium"],
        "cooking_skill": "beginner"
    }
)

print(result)
```

## Extending the Project

- **Add a Nutrition Analyst agent** to estimate calories and macronutrients and suggest healthier alternatives.
- **Support weekly meal planning** by extending the Pydantic models with a `MealType` enum and weekly plan structures instead of single meals.
- Swap in different LLMs, add new agents, or adjust the YAML configuration without touching the core crew logic.

## Why YAML + `CrewBase`?

CrewAI supports defining agents and tasks declaratively in YAML instead of hardcoding them in Python. This keeps configuration separate from logic, makes it easier for non-developers to tweak agent behavior, and scales better for production use. The `@CrewBase` class decorator auto-discovers methods marked with `@agent`, `@task`, and `@crew`, and loads their configuration from the `config/` directory automatically.

> Note: `@CrewBase` and its decorators rely on Python's file-inspection tools and don't work reliably inside notebook cells — define `CrewBase` classes in a standalone `.py` file (as done here with `leftover.py`).

## License

Add your preferred license here.
