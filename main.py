import time
import random

class Question:
    def __init__(self, prompt, options, answer, explanation, difficulty):
        self.prompt = prompt
        self.options = options
        self.answer = answer
        self.explanation = explanation
        self.difficulty = difficulty

    def ask(self, timed=False, time_limit=10):
        print(self.prompt)
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option}")
            
        if timed:
            start_time = time.time()
            response = input(f"Enter your answer (1, 2, 3, 4). You have {time_limit} seconds: ")
            end_time = time.time()
            
            if end_time - start_time > time_limit:
                print("Time's up!")
                return False
        else:
            response = input("Enter your answer (1, 2, 3, 4): ")
            
        correct = self.check_response(response)
        
        if correct:
            print(self.explanation)
        return correct

    def check_response(self, response):
        try:
            if int(response) == self.answer:
                print("Correct!\n")
                return True
            else:
                print("Wrong! Better luck next time.\n")
                return False
        except ValueError:
            print("Invalid input. Please enter a number from 1-4.\n")
            return False

class Leaderboard:
    def __init__(self, filename="scores.txt"):
        self.filename = filename
        self.entries = self.load_entries()

    def load_entries(self):
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
                entries = [self.parse_entry(line.strip()) for line in lines]
                return sorted(entries, key=lambda x: x['score'], reverse=True)
        except FileNotFoundError:
            return []

    def parse_entry(self, line):
        parts = line.split('-')
        score_parts = parts[0].strip().split('/')
        return {
            'score': int(score_parts[0].strip()),
            'total': int(score_parts[1].strip()),
            'difficulty': parts[1].strip().split(':')[1].strip()
        }

    def add_entry(self, score, total, difficulty):
        with open(self.filename, "a") as f:
            f.write(f"{score}/{total} - Difficulty: {difficulty}\n")
        self.entries = self.load_entries()

    def display(self, top_n=5):
        print("\nLeaderboard (Top 5 scores):")
        for idx, entry in enumerate(self.entries[:top_n], 1):
            print(f"{idx}. {entry['score']}/{entry['total']} on {entry['difficulty']} level")

def quiz_game():
    questions = [
        Question("Which language is known as the mother of all languages?",
                 ["C", "Python", "Java", "Assembly"], 4, "Assembly language is a low-level language and is considered the mother of all languages.", "Easy"),
        Question("Which of the following is not a relational database?",
                 ["MySQL", "MongoDB", "PostgreSQL", "Oracle"], 2, "MongoDB is a NoSQL database, not a relational one.", "Medium"),
        Question("In which language is Python written?",
                 ["Python", "C", "Java", "Perl"], 2, "Python is primarily written in C.", "Easy")
    ]

    difficulty = input("Choose difficulty (Easy, Medium): ").capitalize()
    timed_mode = input("Do you want timed mode? (yes/no): ").lower() == "yes"

    filtered_questions = [q for q in questions if q.difficulty == difficulty]
    random.shuffle(filtered_questions)

    score = 0

    print("\nSoftware Engineering Quiz Game\n")
    for question in filtered_questions:
        if question.ask(timed=timed_mode):
            score += 1

    print(f"You got {score}/{len(filtered_questions)} questions right!")
    
    leaderboard = Leaderboard()
    leaderboard.add_entry(score, len(filtered_questions), difficulty)
    leaderboard.display()

if __name__ == "__main__":
    quiz_game()
