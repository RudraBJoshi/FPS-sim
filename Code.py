# FPS GIPS Interactive Simulation

def identify_challenges(scenario):
    print(f"\nStep 1: Identify Challenges\nScenario: {scenario}")
    challenges = []
    print("\nEnter 16 challenges based on the scenario.")
    for i in range(16):
        challenge = input(f"Challenge {i+1}: ")
        challenges.append(challenge)
    
    return challenges

def select_underlying_problem(challenges):
    print("\nStep 2: Select an Underlying Problem")
    print("Challenges identified:")
    for idx, challenge in enumerate(challenges, 1):
        print(f"{idx}. {challenge}")
    
    problem_choice = int(input("\nSelect the number of the challenge that represents the underlying problem: "))
    underlying_problem = challenges[problem_choice - 1]

    # Ask the user to rephrase their problem in the specific format
    print("\nNow, please rephrase your underlying problem using the format:")
    print("because [fact from future scene] how might we [blank] so that [blank] in the [time topic place]")
    
    formatted_problem = input("Rephrase your underlying problem here: ")

    return formatted_problem

def produce_solution_ideas(problem):
    print(f"\nStep 3: Produce Solution Ideas\nProblem: {problem}")
    solutions = []
    print("Enter 16 solutions to the underlying problem.")
    for i in range(16):
        solution = input(f"Solution {i+1}: ")
        solutions.append(solution)
    
    return solutions

def generate_criteria():
    print("\nStep 4: Generate Criteria")
    criteria = []
    print("Enter 3 criteria to evaluate your solutions (e.g., cost, feasibility, time to implement).")
    for i in range(3):
        criterion = input(f"Criterion {i+1}: ")
        criteria.append(criterion)
    
    return criteria

def evaluate_solutions(solutions, criteria):
    print("\nStep 5: Evaluate Solutions")
    scores = {}
    for solution in solutions:
        print(f"\nEvaluating: {solution}")
        total_score = 0
        for criterion in criteria:
            score = int(input(f"Rate the solution based on '{criterion}' (1-10): "))
            total_score += score
        scores[solution] = total_score
    
    # Rank solutions based on scores
    ranked_solutions = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print("\nSolution Rankings:")
    for idx, (solution, score) in enumerate(ranked_solutions, 1):
        print(f"{idx}. {solution} - Total Score: {score}")
    
    return ranked_solutions[0][0]  # Return the top-ranked solution

def develop_action_plan(top_solution):
    print(f"\nStep 6: Develop an Action Plan\nTop Solution: {top_solution}")
    print("Describe the action plan to implement this solution.")
    action_plan = input("Enter your action plan: ")
    
    return action_plan

def fps_gips_simulation():
    print("Welcome to the FPS GIPS Interactive Simulation!")
    scenario = input("\nEnter the scenario or problem to solve: ")

    # Step 1: Identify Challenges
    challenges = identify_challenges(scenario)

    # Step 2: Select an Underlying Problem
    underlying_problem = select_underlying_problem(challenges)
    print(f"\nSelected Underlying Problem: {underlying_problem}")

    # Step 3: Produce Solution Ideas
    solutions = produce_solution_ideas(underlying_problem)

    # Step 4: Generate Criteria
    criteria = generate_criteria()

    # Step 5: Evaluate Solutions
    top_solution = evaluate_solutions(solutions, criteria)
    print(f"\nTop-Ranked Solution: {top_solution}")

    # Step 6: Develop an Action Plan
    action_plan = develop_action_plan(top_solution)
    print("\nYour Action Plan has been developed!")

    print(f"\nSummary:\nScenario: {scenario}\nUnderlying Problem: {underlying_problem}")
    print(f"Top Solution: {top_solution}\nAction Plan: {action_plan}")

# Start the simulation
fps_gips_simulation()
