# Core Engineering Technical Screen

The repository contains a single Python file, named `main.py` that implements the **sort** function used by 
the robotic arm to determine package handling.

---

## Algorithm

Classification is determined by package volume and mass.

### Classification types
These are the different types of classification that are returned by the ```sort``` function.

| Classification | Definition |
| --- | --- |
| STANDARD | Package can be handled automatically/normally by robotic arm |
| SPECIAL | Package requires manaual and/or special handling |
| REJECTED | Package is rejected and cannot be handled |

### How classificaion types are determined

A package is considered **STANDARD** unless it's dimensions and mass limits matches or exceed the following parameters:

- One of the package dimension (width, height, or length) is greather or equal to 150 | classification is **SPECIAL**
- Total volume of package dimension (width * height * lenght) greater or equal to 1,000,000 | classification is **SPECIAL**
- Mass of package is greater or equal to 20 | classification is **SPECIAL**
- A package that exceeds BOTH volume and mass | classification is **REJECTED**

---

## Setup

### Prerequisites

- Python 3.11+ 

### Instructions

#### Clone this repo to your environment

```
git clone https://github.com/LiorAbitbol/core-engineering-technical-screen.git
```

#### Navigate to the `core-engineering-technical-screen` directory

```
cd core-engineering-technical-screen
```

#### Run the script with Python

```
python main.py
```

#### Expected Output

The ```main.py``` script will produce the following test output:

```
Input: (150, 1, 1, 1) -> Output: SPECIAL (Expected: SPECIAL)
Input: (1, 150, 1, 1) -> Output: SPECIAL (Expected: SPECIAL)
Input: (1, 1, 150, 1) -> Output: SPECIAL (Expected: SPECIAL)
Input: (100, 100, 100, 1) -> Output: SPECIAL (Expected: SPECIAL)
Input: (90, 90, 90, 10) -> Output: STANDARD (Expected: STANDARD)
Input: (100, 100, 100, 20) -> Output: REJECTED (Expected: REJECTED)
Input: (0, 1, 1, 1) -> Output: ValueError (Expected: ValueError)
Input: (1, 0, 1, 1) -> Output: ValueError (Expected: ValueError)
Input: (1, 1, 0, 1) -> Output: ValueError (Expected: ValueError)
Input: (1, 1, 1, 0) -> Output: ValueError (Expected: ValueError)
Input: (-1, 1, 1, 1) -> Output: ValueError (Expected: ValueError)
Input: (1, -1, 1, 1) -> Output: ValueError (Expected: ValueError)
Input: (1, 1, -1, 1) -> Output: ValueError (Expected: ValueError)
Input: (1, 1, 1, -1) -> Output: ValueError (Expected: ValueError)
```

