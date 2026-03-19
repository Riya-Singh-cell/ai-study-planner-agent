from planner import generate_plan

def main():
    print("📚 AI Study Planner Agent\n")

    goal = input("Enter your goal: ")
    days = int(input("Enter number of days: "))

    plan = generate_plan(goal, days)

    print("\n📅 Your Study Plan:\n")
    print(plan)

if __name__ == "__main__":
    main()