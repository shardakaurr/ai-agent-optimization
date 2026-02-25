prompt_history = []
from flask import Flask, render_template, request
from agents import planning_agent, authoring_agent, validation_agent, refinement_agent

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    steps = []

    if request.method == "POST":
        user_prompt = request.form.get("prompt")

        prompt_history.append(user_prompt)

        plan = planning_agent(user_prompt)
        steps.append("Planning Agent Completed")

        draft = authoring_agent(plan)
        steps.append("Authoring Agent Completed")

        validation = validation_agent(draft)
        steps.append("Validation Agent Completed")

        result = refinement_agent(validation)
        steps.append("Refinement Agent Completed")

    return render_template("index.html", result=result, steps=steps, history=prompt_history)

if __name__ == "__main__":
    app.run(debug=True)