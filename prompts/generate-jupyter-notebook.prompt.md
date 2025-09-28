# Generate Lab Exercise Jupyter Notebook

You are tasked with creating a comprehensive lab exercise in Jupyter Notebook format for computer science students. The exercise should focus on Python programming concepts and practical implementation.

## Core Requirements

### Design Principles
- **Keep it Simple**: Exercise descriptions must be concise, one line that captures the core requirement
- **Use Original Text**: If source materials exist, prioritize using the original text description to maintain accuracy
- **Clear Structure**: Must include a complete table of contents for easy navigation

### Required Components (in order)
1. **Title** - Lab title with topic, total exercises, and estimated time
2. **Table of Contents** - Place after title, use numbered list format (1. 2. 3...), NO categories/grouping
3. **Learning Objectives** - Clear and concise objectives table
4. **Exercise Groups** - Organize by topic, 3-5 exercises per group
5. **Code Cells** - Each exercise followed by empty Python code cell

### Exercise Format Standard
```markdown
### Exercise X: Title (Level X)
One concise line describing what the student needs to do.
```

### Code Cell Format
```python
# Exercise X: Title
# TODO: Write your code here
```

### Table of Contents Format
Use numbered list without categorization:
```markdown
# Table of Contents

1. [Exercise 1: Title](#exercise-1-title-level-x)
2. [Exercise 2: Title](#exercise-2-title-level-x)
3. [Exercise 3: Title](#exercise-3-title-level-x)
...
```

## Exercise Categories

| Category | Focus | Typical Tasks |
|----------|-------|---------------|
| **Control Structures** | Loops and conditionals | For loops, while loops, if-else statements |
| **Functions** | Reusable code | Function definitions, parameters, return values |
| **Data Structures** | Lists, dicts, tuples | List operations, dictionary manipulation, tuple handling |
| **Random Operations** | Random number generation | Random selections, probability, games |
| **File Operations** | Data input/output | File reading/writing, data processing |
| **Object-Oriented** | Classes and objects | Class definition, inheritance, methods |
| **Algorithms** | Problem solving | Sorting, searching, optimization |

## Difficulty Levels

| Level | Description | Characteristics |
|-------|-------------|----------------|
| **Level 1** | Beginner | Single concept, minimal complexity |
| **Level 2** | Intermediate | Multiple concepts, moderate complexity |
| **Level 3** | Advanced | Complex problem-solving, advanced techniques |

## Best Practices

### Content Guidelines
- **Simplicity First**: Keep exercise descriptions to one line when possible
- **Original Text**: Use source material verbatim when available
- **Progressive Difficulty**: Start with Level 1, gradually increase complexity
- **Clear Instructions**: Avoid complex explanations, focus on what to do
- **No Exercise Numbers**: Remove "Exercise X:" prefixes from titles

### Notebook Structure
1. **Title** - Clear, descriptive lab title (no subject codes)
2. **Table of Contents** - Numbered list, no categories, descriptive names only
3. **Learning Objectives** - Simple table format
4. **Exercises** - Grouped by topic, clean descriptive titles
5. **Code Cells** - Empty cells with descriptive comments

## Example Format

```markdown
# Lab Exercises - 2: Python Repetition

**Topic:** Python Programming - Control Structures, Functions, and Data Structures
**Total Exercises:** 30
**Estimated Time:** 7-8 hours

---

# Table of Contents

1. [Name Repetition](#name-repetition-level-1)
2. [Selective Total](#selective-total-level-1)
3. [Direction Counter](#direction-counter-level-1)

---

## For Loops Exercises

### Name Repetition (Level 1)
Write a programme that asks the user to enter their name and a number. If the number is less than 10, then display their name that number of times; otherwise, display the message "Too high" three times.
```

```python
# Name Repetition
# TODO: Write your code here
```

## Key Requirements Summary

### Must Have Elements:
1. **Clear Title** - Lab title with topic, total exercises, and estimated time (no subject/course codes)
2. **Table of Contents** - Numbered list (1. 2. 3...) after title, no categorization
3. **Simple Exercise Format** - One line description per exercise, NO "Exercise X:" prefixes
4. **Empty Code Cells** - Each exercise followed by `# TODO: Write your code here`
5. **Level Indicators** - Level 1, 2, or 3 for each exercise
6. **Topic Grouping** - Group related exercises under section headers
7. **Clean Titles** - Exercise titles should be descriptive names only, not numbered

### Common Topics by Difficulty:

**Level 1 (Beginner)**
- Basic loops and conditionals
- Simple input/output
- Variable operations
- Basic list operations

**Level 2 (Intermediate)**
- Functions with parameters
- Data structure manipulation
- Error handling
- Random operations

**Level 3 (Advanced)**
- Complex algorithms
- 2D data structures
- Advanced problem solving
- Integration of multiple concepts

### Output Requirements:
- Generate complete notebook ready for student use
- Include 15-30 exercises depending on topic scope
- Ensure progressive difficulty within each topic group
- Keep descriptions concise and actionable
