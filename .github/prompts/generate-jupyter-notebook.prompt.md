---
description: Generate comprehensive lab exercise Jupyter Notebooks for computer science students
mode: agent
tools: [workspace, file_search]
---

# Generate Lab Exercise Jupyter Notebook

Create a comprehensive lab exercise in Jupyter Notebook format for computer science students, focusing on Python programming concepts and practical implementation.

## Objective

Generate structured Jupyter Notebooks for Python programming lab exercises with clear instructions, organized sections, and empty code cells for student implementation.

---

## Core Requirements

### Design Principles

1. **Clarity First**: Exercise descriptions must be concise and actionable
2. **Original Text Preservation**: Use source material verbatim when provided
3. **Logical Organization**: Include complete table of contents for navigation
4. **Progressive Complexity**: Arrange exercises from simple to complex

### Required Components

The notebook MUST include these components in order:

1. **Title Section**
   - Lab title with topic
   - Total number of exercises
   - Estimated completion time
   - NO course/subject codes

2. **Table of Contents**
   - Placed immediately after title
   - Numbered list format (1., 2., 3., ...)
   - NO categorization or grouping
   - Descriptive exercise names only

3. **Learning Objectives**
   - Presented in table format
   - Clear, measurable outcomes
   - Aligned with exercise content

4. **Exercise Groups**
   - Organized by topic/concept
   - 3-5 exercises per group
   - Section headers for each group

5. **Code Cells**
   - One empty Python cell per exercise
   - Comment header with exercise name
   - `# TODO: Write your code here` placeholder

---

## Format Standards

### Exercise Title Format

```markdown
### Exercise Title (Level X)
```

- NO "Exercise N:" prefix
- Descriptive title only
- Difficulty level in parentheses
- Keep description to one concise line

**Example:**
```markdown
### Name Repetition (Level 1)
Write a programme that asks the user to enter their name and a number. If the number is less than 10, display their name that many times; otherwise, display "Too high" three times.
```

### Code Cell Format

```python
# Exercise Title
# TODO: Write your code here
```

- Comment header matches exercise title
- Standard TODO placeholder
- NO solution code

### Table of Contents Format

```markdown
# Table of Contents

1. [Name Repetition](#name-repetition-level-1)
2. [Selective Total](#selective-total-level-1)
3. [Direction Counter](#direction-counter-level-1)
...
```

- Numbered list (1., 2., 3., ...)
- NO categorization/grouping
- Markdown links to exercises
- Descriptive names only

---

## Exercise Categories

Organize exercises by these categories:

| Category | Focus Area | Typical Tasks |
|----------|------------|---------------|
| **Control Structures** | Loops & conditionals | for loops, while loops, if-else statements |
| **Functions** | Reusable components | Function definitions, parameters, return values |
| **Data Structures** | Collections & storage | Lists, dictionaries, tuples, arrays |
| **Random Operations** | Randomization | Random selections, number generation, probability |
| **File Operations** | I/O processing | Read/write files, data parsing, format conversion |
| **Object-Oriented** | Classes & objects | Class definition, inheritance, polymorphism |
| **Algorithms** | Problem solving | Sorting, searching, optimization |
| **Error Handling** | Exceptions | Try-except blocks, validation, debugging |

---

## Difficulty Levels

Assign one difficulty level to each exercise:

| Level | Target Audience | Characteristics | Time Range |
|-------|----------------|----------------|------------|
| **Level 1** | Beginner | Single concept, minimal complexity, clear instructions | 10-20 min |
| **Level 2** | Intermediate | Multiple concepts, moderate complexity, requires planning | 20-30 min |
| **Level 3** | Advanced | Complex problem-solving, integration, advanced techniques | 30+ min |

**Assignment Guidelines:**
- Start each topic group with Level 1 exercises
- Progress to Level 2 and 3 within the group
- Most exercises should be Level 1-2
- Reserve Level 3 for challenging integration tasks

---

## Implementation Guidelines

### Content Best Practices

1. **Clarity & Conciseness**
   - Exercise descriptions: one concise line capturing the core requirement
   - Use source material verbatim when provided
   - Avoid ambiguous terms or complex explanations

2. **Progressive Structure**
   - Start each topic with Level 1 exercises
   - Gradually increase complexity within groups
   - Build on previously introduced concepts

3. **Consistent Formatting**
   - Remove "Exercise N:" prefixes from titles
   - Use descriptive names that indicate the task
   - Maintain consistent markdown structure throughout

4. **Student-Focused Design**
   - Provide clear success criteria
   - Include expected behaviors or outputs
   - Use actionable language (e.g., "Write a programme that...")

### Notebook Organization

Follow this structure exactly:

```
1. Title Section
   ├── Lab title (descriptive, no codes)
   ├── Topic description
   ├── Total exercises count
   └── Estimated completion time

2. Table of Contents
   └── Numbered list with markdown links

3. Learning Objectives
   └── Table format with objectives

4. Exercise Groups
   ├── Section header (##)
   ├── Exercises (###)
   │   ├── Title with difficulty level
   │   ├── One-line description
   │   └── Optional: requirements or examples
   └── Code cell (Python)
       ├── Comment header
       └── TODO placeholder

5. Reflection/Next Steps (optional)
```

---

## Complete Example

Below is a correctly formatted notebook example:

````markdown
# Lab Exercises - Python Repetition

**Topic:** Control Structures, Functions, and Data Structures  
**Total Exercises:** 30  
**Estimated Time:** 7-8 hours

---

# Table of Contents

1. [Name Repetition](#name-repetition-level-1)
2. [Selective Total](#selective-total-level-1)
3. [Direction Counter](#direction-counter-level-1)
4. [Continuous Addition](#continuous-addition-level-1)
...

---

## Learning Objectives

| Objective | Skills Developed |
|-----------|------------------|
| Control Structures | Implement for loops, while loops, and conditionals |
| User Interaction | Handle input/output and validation |
| Data Management | Work with variables and data structures |

---

## For Loops Exercises

### Name Repetition (Level 1)
Write a programme that asks the user to enter their name and a number. If the number is less than 10, display their name that many times; otherwise, display "Too high" three times.
````

````python
# Name Repetition
# TODO: Write your code here
````

````markdown
### Selective Total (Level 1)
Set a variable called `total` to 0. Ask the user to enter five numbers and after each input, ask if they want it included. Display the final total.
````

````python
# Selective Total
# TODO: Write your code here
````

---

## Execution Checklist

When generating a notebook, ensure these requirements are met:

### ✓ Structure Requirements

- [ ] Title section with topic, exercise count, and time estimate
- [ ] Table of contents with numbered list (no categorization)
- [ ] Learning objectives in table format
- [ ] Exercises grouped by topic (3-5 per group)
- [ ] One empty code cell per exercise

### ✓ Format Requirements

- [ ] NO "Exercise N:" prefixes in titles
- [ ] Descriptive exercise names only
- [ ] Difficulty level (Level 1/2/3) for each exercise
- [ ] One-line concise descriptions
- [ ] Code cells with comment header and TODO placeholder

### ✓ Content Requirements

- [ ] Progressive difficulty within each group
- [ ] Clear, actionable instructions
- [ ] Original source text preserved when provided
- [ ] 15-30 exercises total (adjust based on scope)
- [ ] Appropriate time estimates

---

## Common Topic Patterns

### Level 1 (Beginner - 10-20 min)
- Basic loops (for, while)
- Simple conditionals
- Variable operations
- Basic input/output
- Simple list operations

### Level 2 (Intermediate - 20-30 min)
- Functions with parameters
- Dictionary manipulation
- Error handling basics
- Random number generation
- File operations
- Nested structures

### Level 3 (Advanced - 30+ min)
- Complex algorithms
- 2D data structures
- Multiple concept integration
- Advanced problem solving
- Optimization tasks

---

## Quality Standards

**DO:**
- Use clear, unambiguous language
- Provide specific requirements
- Include expected behaviors
- Keep descriptions concise
- Use original source text

**DON'T:**
- Include solution code
- Use ambiguous terms
- Add unnecessary complexity
- Number exercise titles
- Include subject/course codes in title

---

## Final Output

Generate a complete Jupyter Notebook (.ipynb format) that:
1. Is ready for immediate student use
2. Contains 15-30 exercises based on topic scope
3. Follows all format and structure requirements
4. Includes empty code cells for student implementation
5. Maintains progressive difficulty throughout
