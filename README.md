# Cerebras-Systems-Fellowship

**AI-Powered SWE Technical Interview Prep**

**Project Overview**
This platform simulates technical interview scenarios for software engineering roles, generating realistic questions and providing tailored feedback to improve user readiness. Leveraging Cerebras AI resources and advanced language model integrations like LlamaIndex, the platform is designed for college students, new graduates, and professionals seeking a dynamic and personalized interview preparation experience.


**Goal**:
- To create a dynamic, user-focused virtual interview preparation platform that:
    - Simulates realistic SWE technical interview scenarios drawn from topics such as LeetCode problems and real-world challenges.
    - Provides detailed, LLM-powered feedback to help users refine their solutions and understand correct approaches.


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
  
LLM-Enhanced Feedback and Evaluation
- Uses LlamaIndex and Cerebras language models to evaluate user responses.
- Provides tailored feedback, indicating which parts of the solution are correct, partially correct, or incorrect, along with explanations for improvement.
  
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
- interview_simulation Function:
   - Simulates a complete interview process, including question generation, response capture, evaluation, and feedback.

**Future Roadmap**:
- Behavioral Interview Module
   - Use LlamaIndex for sentiment analysis and structured feedback on behavioral responses.
- Website Deployment
   - Develop a front-end interface to make the simulator widely accessible to users.
 


