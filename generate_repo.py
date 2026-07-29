from pathlib import Path

root = Path(r"c:\Users\Kiran Kumar\OneDrive\Desktop\astrain\python-placement-training-2026")
root.mkdir(parents=True, exist_ok=True)


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_day(day_no, title, topic):
    day_dir = root / f"Day-{day_no:02d}_{title.replace(' ', '_')}"
    day_dir.mkdir(parents=True, exist_ok=True)

    write(day_dir / "README.md", f"""# {title}

## Date
06/07/2026

## Topics Covered
- {topic}
- Python syntax and fundamentals
- Interview preparation essentials

## Theory
This day introduces the fundamental concepts of {topic.lower()} in Python. The content is designed for beginners and intermediate learners preparing for placement interviews.

## Definitions
- Variable: A named storage location used to hold data.
- Function: A reusable block of code dedicated to a specific task.
- Loop: A control structure used to repeat a block of code.

## Syntax
```python
value = 10
print(value)
```

## Flow Diagram
```text
Start -> Learn concept -> Practice examples -> Solve exercises -> Review interview questions -> Summary
```

## Advantages
- Improves problem-solving skills.
- Builds confidence for coding interviews.
- Strengthens practical coding ability.

## Disadvantages
- Needs regular practice.
- Some concepts may feel abstract initially.

## Real-Time Applications
- Automation scripts
- Data validation
- Student record handling

## Examples
- Basic examples for {topic.lower()}
- Simple real-world scenarios

## Python Programs
Use the Python Programs folder for beginner-friendly examples.

## Interview Questions
Review the interview_questions.md file for common questions.

## LeetCode Problems
Use the LeetCode folder for daily practice references.

## Summary
This day focuses on understanding the core concept of {topic.lower()} and applying it in small coding exercises.

## Learning Outcome
- Understand the theory behind the topic.
- Write simple Python programs independently.
- Explain the concept clearly in interviews.

## References
- Python Official Documentation
- W3Schools Python Tutorial
- Placement interview preparation notes
""")

    write(day_dir / "Notes.md", f"""# Notes for {title}

- Practice the concept with small examples.
- Write comments in every program.
- Review syntax carefully.
- Connect the topic to a real-world use case.
""")

    write(day_dir / "leetcode.md", f"""# LeetCode Practice for {title}

## LeetCode Profile
https://leetcode.com/u/mohamedashfakali/

## My Public Submission Link
My Public Submission Link: __________________

## Suggested Practice
- Two Sum
- Reverse String
- Array Manipulation
""")

    write(day_dir / "interview_questions.md", f"""# Interview Questions for {title}

1. What is the main purpose of {topic.lower()} in Python?
2. How does it differ from related concepts?
3. Can you explain a real-world example?
4. What are common mistakes while using it?
5. How would you optimize a solution using this concept?
""")

    write(day_dir / "practice_questions.md", f"""# Practice Questions for {title}

- Write a program to demonstrate the topic.
- Solve 3 beginner-level problems.
- Explain the logic in simple words.
- Compare two approaches and choose the better one.
""")

    subfolders = [
        "Python Programs",
        "Exercises",
        "Summary",
        "Learning Outcome",
        "Real-Time Examples",
        "Interview Tips",
        "Important Points",
        "Common Mistakes",
        "Folder Documentation",
        "LeetCode",
    ]
    for folder in subfolders:
        folder_path = day_dir / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        write(folder_path / "README.md", f"# {folder}\n\nThis folder contains supporting material for {title}.\n")

    write(day_dir / "Python Programs" / f"{title.lower().replace(' ', '_')}_program.py", f'''"""{title} example program."""

# This program demonstrates a simple Python example for {title}.
# Comments are included to make the logic easy to follow.

print("Hello from {title}!")

# Add your own logic below.
value = 10
print(f"The value is: {{value}}")
''')

    write(day_dir / "Exercises" / f"exercise_{day_no:02d}.py", f'''"""Practice exercise for {title}."""

# Write your own solution here.
# Example: create a small program based on the topic.

print("Exercise for {title}")
''')

    write(day_dir / "Summary" / f"summary_day_{day_no:02d}.md", f"""# Summary for Day {day_no:02d}

- Covered the basics of {topic.lower()}.
- Wrote a simple Python example.
- Reviewed interview and practice ideas.
""")

    write(day_dir / "Learning Outcome" / f"learning_outcome_day_{day_no:02d}.md", f"""# Learning Outcome

By the end of this day, the learner should be able to:
- Understand the topic clearly.
- Apply the concept in a small program.
- Explain the concept during an interview.
""")

    write(day_dir / "Real-Time Examples" / f"examples_day_{day_no:02d}.md", f"""# Real-Time Examples

- Automation of repetitive tasks.
- Data processing and validation.
- Student record handling.
""")

    write(day_dir / "Interview Tips" / f"tips_day_{day_no:02d}.md", f"""# Interview Tips

- Practice explaining the concept in simple words.
- Be ready to discuss time and space complexity.
- Write code clearly with comments.
""")

    write(day_dir / "Important Points" / f"points_day_{day_no:02d}.md", f"""# Important Points

- Focus on accuracy before speed.
- Understand the logic before memorizing syntax.
- Review mistakes after every practice session.
""")

    write(day_dir / "Common Mistakes" / f"mistakes_day_{day_no:02d}.md", f"""# Common Mistakes

- Missing indentation in Python programs.
- Confusing variable names.
- Not handling edge cases.
""")

    write(day_dir / "Folder Documentation" / f"folder_doc_day_{day_no:02d}.md", f"""# Folder Documentation

This folder contains the learning resources for Day {day_no:02d}.
Use the README file first, then practice with the Python programs and exercises.
""")

    leetcode_dir = day_dir / "LeetCode"
    write(leetcode_dir / "README.md", f"""# LeetCode Practice Index for {title}

- [Problem 01: Two Sum](problem_01_two_sum.md)
""")

    write(leetcode_dir / "problem_01_two_sum.md", f"""# Problem 01: Two Sum

## Python Solution
See [problem_01_two_sum.py](problem_01_two_sum.py)

## Explanation
This is a beginner-friendly problem for practice.

## Algorithm
1. Use a dictionary.
2. Check the complement for each element.
3. Return the indices.

## Brute Force
Use nested loops to compare every pair.

## Optimized Approach
Use a hash map for faster lookup.

## Time Complexity
O(n)

## Space Complexity
O(n)

## Sample Input
[2, 7, 11, 15], 9

## Sample Output
[0, 1]

## Interview Tips
Explain why the hash map approach is faster.

## Official LeetCode Problem Link
https://leetcode.com/problems/two-sum/
""")

    write(leetcode_dir / "problem_01_two_sum.py", '''"""Solution for Two Sum."""

# This is a beginner-friendly solution example.
# Comments explain the logic clearly.


def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
''')


write(root / "README.md", """# Python Placement Training 2026

![Python Placement Training Banner](https://img.shields.io/badge/Python-Placement%20Training-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Ongoing-orange?style=for-the-badge)
![College](https://img.shields.io/badge/College-Dhaanish%20Chennai%20College%20of%20Engineering-green?style=for-the-badge)
![Department](https://img.shields.io/badge/Department-B.Tech%20AI%26DS-purple?style=for-the-badge)

## Professional Summary
This repository is a complete placement training portfolio for Mohamed ASHFAK Ali A, a B.Tech AI&DS student from Dhaanish Chennai College of Engineering. It contains structured Python learning notes, daily practice materials, interview preparation resources, mini projects, and a final project showcase.

## Student Information
- Student Name: Mohamed ASHFAK Ali A
- College: Dhaanish Chennai College of Engineering
- Department: B.Tech AI&DS
- Training Start Date: 06/07/2026
- Training Status: Ongoing
- GitHub Profile: https://github.com/mohamedashfakali?tab=repositories
- LinkedIn: https://www.linkedin.com/in/mohamed-ashfak-ali-6b1033327

## Table of Contents
- [Training Timeline](#training-timeline)
- [Daily Progress](#daily-progress-table)
- [Skills Learned](#skills-learned)
- [Technology Stack](#technology-stack)
- [Folder Structure](#folder-structure)
- [LeetCode Section](#leetcode-section)
- [Database Section](#database-section)
- [Mini Projects](#mini-projects)
- [Final Project](#final-project)
- [Future Goals](#future-goals)
- [Repository Statistics](#repository-statistics)
- [Acknowledgements](#acknowledgements)

## Training Timeline
- Start Date: 06/07/2026
- Current Focus: Python core concepts, SQL, OOP, and interview preparation
- Target Outcome: Placement-ready Python and database portfolio

## Daily Progress Table
| Day | Topic | Status |
|-----|-------|--------|
| 01 | Python Introduction | Completed |
| 02 | Variables and Data Types | Completed |
| 03 | Conditional Statements | Completed |
| 04 | Loops | Completed |
| 05 | Lists and Tuples | Completed |
| 06 | Sets and Dictionaries | Completed |
| 07 | Functions | Completed |
| 08 | Lambda and Modules | Completed |
| 09 | File Handling | Completed |
| 10 | Exception Handling | Completed |
| 11 | OOP Classes | Completed |
| 12 | OOP Advanced | Completed |
| 13 | Standard Libraries | Completed |
| 14 | SQLite | Completed |
| 15 | CRUD | Completed |
| 16 | Current Progress | Ongoing |

## Skills Learned
- Python fundamentals
- Control structures
- Data structures
- Functions and modules
- File handling
- Exception handling
- Object-oriented programming
- SQLite and CRUD basics
- Interview preparation and coding practice

## Technology Stack
- Python 3.x
- SQLite
- Markdown
- Git and GitHub
- VS Code

## Folder Structure
```text
python-placement-training-2026/
├── README.md
├── Day-01_Python_Introduction/
├── Day-02_Variables_DataTypes/
├── ...
├── MCQ-Tests/
├── Mini-Projects/
├── Final-Project/
├── Assets/
├── Images/
├── Resources/
├── Documentation/
└── .gitignore
```

## LeetCode Section
- Daily practice notes and sample solutions are available inside each day folder.
- LeetCode profile: https://leetcode.com/u/mohamedashfakali/

## Database Section
The repository includes database practice material such as:
- Student Management System
- Employee Management System
- Library Management System
- Hospital Management System
- SQLite CRUD
- SQL Queries

### Training Database Resources
Database Task Link
https://1drv.ms/f/c/B6DA027EC1331087/IgCUmbGv7GHFToGrtriPR0QoAdYI7OW4YGXlH4b7rbTZYng?e=GJg6i5

## Mini Projects
- Calculator App
- Quiz App
- To-Do List App

## Final Project
- Project Name: AI DIGITAL TWIN
- Description: Personalized Learning For Each Student

## Future Goals
- Build more Python automation projects
- Strengthen DSA and interview preparation
- Create a strong GitHub portfolio for placements

## Repository Statistics
- Total Days: 16
- Practice Files: Included
- Mini Projects: 3
- Final Project: 1

## Acknowledgements
Thanks to all mentors, instructors, and learning resources that supported this training journey.

## Footer
Prepared by Mohamed ASHFAK Ali A for placement training and portfolio growth.
""")

for day_no, title, topic in [
    (1, "Python Introduction", "Python basics, syntax, and environment setup"),
    (2, "Variables DataTypes", "Variables, constants, and Python data types"),
    (3, "Conditional Statements", "If, elif, and else logic"),
    (4, "Loops", "For loops, while loops, and iteration"),
    (5, "List Tuple", "Lists, tuples, and common operations"),
    (6, "Sets Dictionaries", "Sets, dictionaries, and key-value storage"),
    (7, "Functions", "Functions, parameters, and return values"),
    (8, "Lambda Modules", "Lambda expressions and importing modules"),
    (9, "File Handling", "Reading and writing files in Python"),
    (10, "Exception Handling", "Try, except, and error handling"),
    (11, "OOP Classes", "Classes, objects, and constructors"),
    (12, "OOP Advanced", "Inheritance, polymorphism, and encapsulation"),
    (13, "Standard Libraries", "Math, random, datetime, and utilities"),
    (14, "SQLite", "Working with SQLite databases"),
    (15, "CRUD", "Create, read, update, and delete operations"),
    (16, "Current Progress", "Current learning progress and revisions"),
]:
    make_day(day_no, title, topic)

mcq_dir = root / "MCQ-Tests"
mcq_dir.mkdir(parents=True, exist_ok=True)
write(mcq_dir / "README.md", "# MCQ Tests\n\nThis folder contains beginner and intermediate question tests for interview preparation.\n")
for idx in range(1, 4):
    write(mcq_dir / f"Test-{idx:02d}.md", f"""# MCQ Test {idx:02d}

Date:

Score:

Remarks:

Topics Covered:

Performance Analysis:
""")

mini_dir = root / "Mini-Projects"
mini_dir.mkdir(parents=True, exist_ok=True)
write(mini_dir / "README.md", "# Mini Projects\n\nThis folder contains small practical projects for portfolio development.\n")
for project in ["Calculator_App", "Quiz_App", "To_Do_List"]:
    pdir = mini_dir / project
    pdir.mkdir(parents=True, exist_ok=True)
    write(pdir / "README.md", f"# {project.replace('_', ' ')}\n\nA mini project demonstrating Python programming concepts.\n")
    write(pdir / f"{project.lower()}.py", f'''"""{project.replace('_', ' ')} demo program."""

print("Mini project ready")
''')

final_dir = root / "Final-Project"
final_dir.mkdir(parents=True, exist_ok=True)
write(final_dir / "README.md", """# Final Project

## Project Name
AI DIGITAL TWIN

## Project Description
Persionalized Learning For Each Student

## Objectives
- Support personalized learning.
- Provide simple and interactive dashboards.
- Demonstrate project planning and documentation skills.
""")
for name in ["Architecture", "Workflow", "Objectives", "Features", "Technology Stack", "Installation", "Folder Structure", "Screenshots", "Future Scope", "License", "Contributors", "Timeline", "Progress"]:
    write(final_dir / f"{name}.md", f"# {name}\n\nThis section is being prepared for the final project documentation.\n")

for folder in ["Assets", "Images", "Resources", "Documentation"]:
    d = root / folder
    d.mkdir(parents=True, exist_ok=True)
    write(d / "README.md", f"# {folder}\n\nThis folder contains supporting assets and documentation for the repository.\n")

# Database section
for folder in ["Student Management System", "Employee Management System", "Library Management System", "Hospital Management System", "SQLite CRUD", "SQL Queries", "Database Schema", "Python Programs", "Documentation"]:
    p = root / "Documentation" / folder
    p.mkdir(parents=True, exist_ok=True)
    write(p / "README.md", f"# {folder}\n\nDatabase practice material for placement preparation.\n")

write(root / "Documentation" / "Training_Database_Resources.md", """# Training Database Resources

Database Task Link
https://1drv.ms/f/c/B6DA027EC1331087/IgCUmbGv7GHFToGrtriPR0QoAdYI7OW4YGXlH4b7rbTZYng?e=GJg6i5

This link is used only as a reference for training tasks and is not copied directly.
""")

write(root / ".gitignore", "__pycache__/\n*.pyc\n.env\n")
write(root / "LICENSE", "MIT License\n\nCopyright (c) 2026 Mohamed ASHFAK Ali A\n")

print("Repository created successfully at", root)
print("Folders created:")
for child in sorted([p.name for p in root.iterdir()]):
    print("-", child)
