# Generate Lab Exercise Jupyter Notebook

You are tasked with creating a comprehensive lab exercise in Jupyter Notebook format for computer science students. The exercise should focus on Python programming concepts and practical implementation.

## Instructions

1. **Structure**: Create a well-organized notebook with the following components:
   - Introduction section explaining the learning objectives
   - Multiple exercise tasks with clear descriptions
   - Code cells for student implementation
   - Expected output examples where appropriate

2. **Content Requirements**:
   - Write task descriptions in markdown cells using clear, concise language
   - Provide context and background information for each exercise
   - Include step-by-step instructions when needed
   - Add helpful hints or tips where appropriate

3. **Code Block Format**:
   - For each programming task, provide an **empty Python code cell** where students can write their solutions
   - Use the following format for code cells:
     ```python
     # TODO: Write your code here
     
     ```
   - Do not include the actual solution code - leave it for students to implement

4. **Exercise Types** (choose appropriate ones based on the topic):

   | Exercise Category | Learning Objectives | Typical Tasks |
   |-------------------|-------------------|---------------|
   | **Programming Fundamentals** | Master basic syntax and operations | Variable assignments, calculations, string operations |
   | **Control Structures** | Implement decision-making and repetition | Conditional logic, loop implementations, flow control |
   | **Functions and Modules** | Create reusable code components | Function definitions, parameter handling, module imports |
   | **Data Structures** | Manipulate complex data types | List operations, dictionary usage, set manipulations |
   | **Object-Oriented Programming** | Design and implement classes | Class definitions, inheritance, method implementations |
   | **File Operations** | Handle external data sources | File reading/writing, data parsing, format conversions |
   | **Error Handling** | Implement robust error management | Exception handling, validation, debugging techniques |
   | **Algorithm Implementation** | Solve computational problems | Sorting, searching, optimization algorithms |
   | **Data Analysis** | Process and analyze datasets | Statistical calculations, data visualization, reporting |

5. **Formatting Guidelines**:
   - Use proper markdown formatting with headers, bullet points, and code blocks
   - Include learning objectives at the beginning
   - Add difficulty indicators using the following system:
     
     | Difficulty Level | Indicator | Description |
     |------------------|-----------|-------------|
     | Beginner | Level 1 | Basic concepts, minimal complexity |
     | Intermediate | Level 2 | Moderate complexity, combines multiple concepts |
     | Advanced | Level 3 | Complex problem-solving, advanced techniques |
     
   - Provide estimated completion time for each task
   - Include relevant examples or sample inputs/outputs
   - Use tables for structured information when appropriate
   - Organize content with numbered lists for sequential steps

6. **Educational Best Practices**:

   Follow these structured approaches for effective learning:

   ### Learning Progression Strategy
   1. **Scaffolded Learning**: Start with simpler concepts and gradually increase complexity
   2. **Clear Assessment**: Provide explicit success criteria for each task
   3. **Differentiation**: Include extension challenges for advanced students
   4. **Reflection**: Add structured reflection questions at the end

   ### Task Structure Template
   | Component | Purpose | Implementation |
   |-----------|---------|----------------|
   | **Learning Objective** | Define what students will achieve | Clear, measurable goals |
   | **Context** | Provide background information | Real-world applications |
   | **Instructions** | Guide implementation process | Step-by-step numbered lists |
   | **Success Criteria** | Define completion standards | Specific, testable outcomes |
   | **Extension** | Challenge advanced learners | Optional advanced features |
   | **Reflection** | Encourage metacognition | Guided questions about learning |

## Example Task Format

```markdown
## Task 1: Basic Calculator (Level 1)
**Estimated time: 15 minutes**

Create a simple calculator that can perform basic arithmetic operations (addition, subtraction, multiplication, division).

### Requirements:
1. Prompt the user to enter two numbers
2. Ask for the operation type (+, -, *, /)
3. Display the result
4. Handle division by zero error

### Task Specifications:

| Requirement | Description | Expected Data Type |
|-------------|-------------|-------------------|
| Input 1 | First number | float or int |
| Input 2 | Second number | float or int |
| Operation | Mathematical operator | string |
| Output | Calculation result | float |
| Error Handling | Division by zero check | Exception handling |

### Expected behavior:
```
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): +
Result: 15.0
```

**Your code:**
```python
# TODO: Write your code here

```

## Sample Topics to Choose From

When generating lab exercises, consider these popular computer science topics organized by complexity level:

### Topic Categories and Difficulty Levels

| Topic Category | Level 1 (Beginner) | Level 2 (Intermediate) | Level 3 (Advanced) |
|----------------|-------------------|----------------------|-------------------|
| **Python Fundamentals** | Variables, data types, basic operators | Type conversion, string manipulation | Advanced data type operations |
| **Control Structures** | Simple if/else, basic loops | Nested loops, complex conditions | Loop optimization, comprehensions |
| **Functions** | Function definition, parameters | Lambda functions, decorators | Closures, advanced decorators |
| **Data Structures** | Lists, dictionaries basics | List/dict comprehensions, sets | Custom data structures, algorithms |
| **Object-Oriented** | Class definition, attributes | Inheritance, polymorphism | Design patterns, metaclasses |
| **File Operations** | Read/write text files | CSV/JSON processing | Binary files, file systems |
| **Error Handling** | Basic try/except | Multiple exceptions, finally | Custom exceptions, context managers |
| **Libraries** | Built-in modules | NumPy, Pandas basics | Advanced library integration |

### Recommended Exercise Progression

1. **Foundation Phase** (Sessions 1-3)
   - Python syntax and basic data types
   - Control flow structures
   - Basic input/output operations

2. **Development Phase** (Sessions 4-6)
   - Functions and modular programming
   - Data structure manipulation
   - File handling and data processing

3. **Application Phase** (Sessions 7-9)
   - Object-oriented programming concepts
   - Error handling and debugging
   - Integration with external libraries

4. **Advanced Phase** (Sessions 10+)
   - Algorithm implementation
   - Data analysis and visualization
   - Project-based learning

Remember to tailor the difficulty and content to the appropriate academic level and ensure all exercises are educational, engaging, and practically relevant.