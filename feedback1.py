student_name = input("Which student would you like to give feedback for? (Type 'q' to quit) ")

overall_performance_score = int(input("Overall performance (1-4): "))
general_understanding_score = int(input("General understanding (1-4): "))
contribution_score = int(input("Contribution (1-4): "))
lab_completion_score = int(input("Lab completion (1-4): "))
punctuality_score = int(input("Punctuality (1-4): "))
engagement_score = int(input("Engagement (1-4): "))
further_study_rec = int(input("Further study level (1-4): "))

general_comments = {
    "overall_performance":{
        1: "has built an awareness of the topics within this module",
        2: "is in their early stages of development",
        3: "has performed well overall",
        4: "has performed exceptionally well overall",
    },
    "general_understanding":{
    1: "beginning to grasp the key concepts of this module",
    2: "demonstrating an understanding of the key concepts",
    3: "showing a good understanding of the key concepts",
    4: "demonstrating a strong understanding of the key concepts",
    },
    "contribution":{
        1: "occassionally sharing their ideas during classes, especially when prompted",
        2: "is making some contributions to classes",
        3: "contributing positively to classes",
        4: "actively contributing to class discussions and activities",
    },
    "lab_completion":{
        1: "hasn't completed any of the labs but has been guided through them",
        2: "has completed some of the labs with support from myself or their peers",
        3: "has completed all of the labs, largely independently",
        4: "has completed all of the labs efficiently and independently",
    },
}

punctuality_comments = {
    "punctuality":{
        1: "is developing their time management skills",
        2: "is continuously improving their time management skills",
        3: "has been punctual throughout the module",
        4: "has been consistently punctual throughout the module",
    },
    "engagement":{
        1: "has engaged with the classes through Webex",
        2: "has engaged well through Webex",
        3: "has engaged well through Webex, as well as in-class discussions",
        4: "has engaged exceptionally well through Webex, as well as in-class discussions",
},
}

further_study_recommendations = {
    1: "Continue to investigate design and fundamental logic for a better grasp on the language. Watching code-alongs on YouTube or live coding projects may be useful",
    2: "Continue to investigate design and logic in python, building on your knowledge of classes, recurssion and error handling.",
    3: "Start to incorporate testing logic or TDD into your code and build a deeper understanding of class architecture.",
    4: "Look into creating virtual environments for your code to align with best practices. Delve a bit deeper into SQL and you could also look into N-tier, microservice architecture for APIs and applications.",
}

feedback_template = (f"General Comments\n{student_name} {general_comments['overall_performance'][overall_performance_score]}. They are {general_comments['general_understanding'][general_understanding_score]} and {general_comments['contribution'][contribution_score]}. \n{student_name} {general_comments['lab_completion'][lab_completion_score]}.\n\n{student_name} {punctuality_comments['punctuality'][punctuality_score]} and {punctuality_comments['engagement'][engagement_score]}.\n\nRecommendations on further learning: {further_study_recommendations[further_study_rec]}.") 


with open(f"{student_name}_feedback.txt", "w") as feedback_file:
    feedback_file.write(feedback_template)
    print(f"Feedback for {student_name} has been saved to {student_name}_feedback.txt")

