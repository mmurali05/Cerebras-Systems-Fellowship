import requests
from dotenv import load_dotenv
import os

# Load the .env file to access environment variables
load_dotenv()

# Cerebras API Configuration
CEREBRAS_API_URL = "https://api.cerebras.ai/v1/chat/completions"
API_KEY = os.getenv("API_KEY")  # Retrieve the API key from .env

# Validate the API key
if not API_KEY:
    raise ValueError("API Key not found. Ensure it is set in the .env file.")

API_HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Function to generate a technical interview question
def generate_question(topic, difficulty):
    """
    Generate a software engineering technical interview question
    using the Cerebras API.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a {difficulty} software engineering technical interview question on {topic}.\nInclude:\n1. A clear problem statement.\n2. A hint for solving the problem.\n3. A detailed solution prefixed by '### Solution:'."}
    ]
    payload = {
        "model": "llama3.1-8b",
        "messages": messages,
        "max_completion_tokens": 1000
    }

    try:
        response = requests.post(CEREBRAS_API_URL, headers=API_HEADERS, json=payload)

        if response.status_code == 200:
            output = response.json().get("choices", [])[0].get("message", {}).get("content", "")
            return parse_question(output)
        else:
            print("Error in Cerebras API:", response.status_code)
            print("Error Response Content:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Network error occurred:", e)
        return None

def parse_question(output):
    """
    Parse the output to extract the problem and solution.
    """
    if not output:
        return {"problem": "No question generated.", "solution": "No solution provided."}

    # Split content into problem and solution using the "### Solution:" delimiter
    parts = output.split("### Solution:")
    problem = parts[0].strip() if len(parts) > 0 else "No problem statement."
    solution = parts[1].strip() if len(parts) > 1 else "No solution provided."
    return {"problem": problem, "solution": solution}

def evaluate_answer_with_llm(user_answer, expected_solution):
    """
    Use cerebras LLM to evaluate user's response + provide feedback on how close it is to expected solution
    """

    messages = [
        {"role": "system", "content": "You are a helpful assistant that evaluates coding answers."},
        {"role": "user", "content": f"Evaluate the following user's solution compared to the expected solution. Provide specific feedback on which parts are correct, partially correct, or incorrect.\n\nUser's Solution:\n{user_answer}\n\nExpected Solution:\n{expected_solution}\n\nProvide detailed feedback on the similarities and differences."}
    ]
    payload = {
        "model": "llama3.1-8b",
        "messages": messages,
        "max_completion_tokens": 500
    }

    try:
        response = requests.post(CEREBRAS_API_URL, headers = API_HEADERS, json=payload)
        if response.status_code == 200:
            output = response.json().get("choices", [])[0].get("message", {}).get("content", "")
            return output
        else:
            print("Error in Cerebras API:", response.status_code)
            print("Error Response Content:", response.text)
            return "Error in evaluation. Please try again."
    except requests.exceptions.RequestException as e:
        print("Network error occurred during evaluation:", e)
        return "Network error occurred. Please try again."                         

# Function to simulate an interview session
def interview_simulation():
    """
    Simulate a software engineering technical interview session.
    """
    print("Welcome to the SWE Technical Interview Simulator!")
    print("You will be asked questions, and your responses will be evaluated. No pressure! \n")

    # Step 1: Choose a topic and difficulty level
    topic = input("Choose a topic (e.g., Arrays, Dynamic Programming, Graphs): ").strip()
    difficulty = input("Choose difficulty (Easy, Medium, Hard): ").strip()

    # Step 2: Generate a question using the API
    print("\nGenerating your question...")
    question_data = generate_question(topic, difficulty)

    if not question_data or not question_data["problem"].strip():
        print("Failed to generate a question. Please try again.")
        return

    # Step 3: Display the question
    print("\nHere is your question:")
    print(question_data["problem"])

    # Step 4: Capture the user's response
    user_answer = input("\nEnter your solution or press Enter to skip: ").strip()

     # Step 5: Evaluate the user's response only if they did not skip
    expected_solution = question_data["solution"].strip()
    if user_answer.lower() == "skip":
        print("\nYou chose to skip the question. No evaluation performed.")
    else:
        print("\nEvaluating your response...")
        # Use LLM Evaluation for feedback on user answer
        detailed_feedback = evaluate_answer_with_llm(user_answer, expected_solution)
        print("\nDetailed Feedback:")
        print(detailed_feedback)
    
    # Display the correct solution regardless of skip
    print("\nHere's the correct solution:")
    print(expected_solution)

    # Step 6: Prompt to repeat or exit
    repeat = input("\nWould you like to try another question? (yes/no): ").strip().lower()
    if repeat == "yes":
        interview_simulation()
    else:
        print("Thank you for using the SWE Technical Interview Simulator. Go ace that interview!")

# Main execution block
if __name__ == "__main__":
    interview_simulation()
