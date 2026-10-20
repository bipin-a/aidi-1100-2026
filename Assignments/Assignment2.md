# Assignment 2

### **Expectations**

1. **What You Submit**:
   - A **Python file** containing your complete FastAPI application for the **one coding question** below.
   - A **link to your own public GitHub repo** containing that file.
   - A **recording** (4 minutes or less) that shows your **screen** and includes your **voice and face** (use your webcam). Explain your choices and demonstrate your endpoint.
   - Submit the recording separately, not in the repo.
   - No written explanations are needed. Code comments are fine.

2. **How This Assignment Works**:
   - Build the application yourself. There is no supplied code to fix.
   - Run it locally and send requests to your endpoint using FastAPI's interactive documentation at `/docs` (for example, `http://127.0.0.1:8000/docs` when your app runs on port `8000`) or another API client.
   - Use the same application for all three test cases. Change the request inputs, not the code between tests.

3. **Recording Expectations**:
   - Explain **why you chose GET or POST** for this operation.
   - Explain **what adding two strings would produce** and **how your code ensures numerical addition**. Point to the relevant code and explain what it does.
   - **Show me:** show your code, run your application, and send the three requests listed below. Make the inputs and responses visible.

4. **How the Recording Is Marked**:
   - I'm marking how well **you understand** your code, not how polished you sound.
   - Pauses, "umm", and "wait, let me check that" are completely fine.
   - Don't read from a script. Talk to me like you're explaining it to a classmate. I may ask any student a few short follow-up questions in person. **Explanation marks may be adjusted after that conversation.**

5. **Open Book**:
   - Use your notes, the class examples, and the Python and FastAPI documentation.

**Academic Integrity**: This question is short, so many correct solutions will look alike, and that's fine. Your recording is how I confirm the work is yours. If there is evidence of unauthorized collaboration or copying (for example, a recording that can't explain the submitted code, or identical unusual mistakes across submissions), I will follow up with the students involved and may refer it under the college's academic integrity policy.

### **Question 1: Add Two Numbers [Video]**

Create a FastAPI application with one endpoint, `/add`, that receives two required query parameters, `a` and `b`, and returns their sum.

**Requirements**:

- Choose **GET or POST** yourself. Be ready to explain why your choice fits the operation.
- Calculate the answer from the two values supplied in each request.
- Return a JSON response with one key, `sum`. Its value must be a **number**.
- The endpoint only calculates and returns the answer. It does not save or update any data.
- For this question, you only need to handle valid integer inputs, including zero and negative integers.

**Demonstrate all three test cases**:

| `a` | `b` | Expected JSON response |
|-----|-----|------------------------|
| 2 | 3 | `{"sum": 5}` |
| 12 | 8 | `{"sum": 20}` |
| -4 | 4 | `{"sum": 0}` |

### **Marking**

| Component | Marks |
|-----------|-------|
| **Working endpoint:** the application runs, accepts both required parameters, and returns the correct numerical sum in the required JSON format for all three test cases. Partial credit is available for code that partly works. | 4 |
| **HTTP method explanation:** explains the chosen method and why it fits this operation. Marks are based on the reasoning, not just naming GET or POST. | 2 |
| **Data-type explanation:** explains what adding strings would do and how the submitted code ensures numerical addition. | 2 |
| **Demonstration:** sends all three requests to the running endpoint and shows their inputs and responses. | 2 |
| **Total** | **10** |
