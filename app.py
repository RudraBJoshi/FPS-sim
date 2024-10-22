from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def identify_challenges(scenario):
    challenges = request.form.getlist("challenges")  # Get challenges from the form
    return challenges

def select_underlying_problem(challenges, problem_choice):
    underlying_problem = challenges[int(problem_choice) - 1]  # Select based on user's choice
    formatted_problem = request.form.get("formatted_problem")  # Get formatted problem from the form
    return formatted_problem

def produce_solution_ideas(problem):
    solutions = request.form.getlist("solutions")  # Get solutions from the form
    return solutions

def generate_criteria():
    criteria = request.form.getlist("criteria")  # Get criteria from the form
    return criteria

def evaluate_solutions(solutions, criteria):
    scores = {}
    for solution in solutions:
        total_score = 0
        for criterion in criteria:
            score = int(request.form.get(f'score_{solution}_{criterion}'))  # Get score for each solution
            total_score += score
        scores[solution] = total_score
    ranked_solutions = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked_solutions[0][0]  # Return the top-ranked solution

def develop_action_plan(top_solution):
    action_plan = request.form.get("action_plan")  # Get action plan from the form
    return action_plan

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_simulation', methods=['POST'])
def run_simulation():
    scenario = request.form.get("scenario")
    challenges = identify_challenges(scenario)
    
    problem_choice = request.form.get("problem_choice")  # Get user's choice of underlying problem
    underlying_problem = select_underlying_problem(challenges, problem_choice)
    
    solutions = produce_solution_ideas(underlying_problem)
    criteria = generate_criteria()
    
    top_solution = evaluate_solutions(solutions, criteria)
    action_plan = develop_action_plan(top_solution)

    summary = {
        "scenario": scenario,
        "underlying_problem": underlying_problem,
        "top_solution": top_solution,
        "action_plan": action_plan
    }
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)
