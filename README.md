# Cerebras-Fellowship

**AI-Powered SWE Technical Interview Prep**

**Project Overview**:
This platform simulates software engineering technical interview scenarios, providing users with realistic questions and personalized feedback. By leveraging Cerebras’s resources and integrating advanced tools, the platform enables college students, new graduates, and professionals to enhance their interview preparedness.

**Goal**:
- To create a dynamic, user-focused virtual interview preparation platform that:
- Simulates realistic SWE technical interview scenarios drawn from topics such as LeetCode problems and real-world challenges.
Evaluates and provides tailored feedback to users on their responses, helping them refine their problem-solving approaches.

**Success Criteria**:

**_Short-Term Metrics:_**
- Users complete the journey from question generation to feedback.
- Regular platform usage tracked over 15/30/60-day intervals, indicating user engagement.
  
**_Long-Term Metrics:_**
- Users report high satisfaction with question accuracy and feedback comprehensiveness.
- Demonstrated improvement in users’ confidence and preparedness for technical interviews based on surveys and test results.

**Use Case**:
The platform is tailored for:
- College students and new graduates preparing for technical interviews.

**Enhanced Platform Features**:
Dynamic Question Generation
- Users select a topic and difficulty level (e.g., Arrays, Graphs, Dynamic Programming).
- Questions are generated using the Cerebras API, integrating prompts tailored to simulate real interview conditions.
Feedback on User Responses
- The system evaluates user answers against expected solutions.
- Provides detailed insights into areas of improvement.
Structured Outputs
- Questions and solutions are parsed for clarity using a "### Solution" delimiter, ensuring that solutions are only displayed post-evaluation.
Iterative Practice
- Users can opt to answer another question after receiving feedback, encouraging consistent practice.

**Implementation Details**:
API Integration:
- Cerebras AI API: Generates questions and structured solutions based on the user-selected topic and difficulty.
Code Features:
- generate_question Function:
   - Fetches interview questions with clear problem statements and step-by-step solutions.
- parse_question Function:
   - Separates problems and solutions using the "### Solution" delimiter to ensure solutions are hidden initially.
interview_simulation Function:
   - Simulates a complete interview process, including question generation, response capture, evaluation, and feedback.

**Future Roadmap**:
- Advanced Evaluation
   - Enhance response evaluation using LLMs to provide nuanced feedback (e.g., recognizing partially correct answers).
- Gamification and Analytics
   - Introduce scoring, progress tracking, and gamified elements to improve user engagement.
- Website 
   - Create a front-end website to deploy this simulator. 


