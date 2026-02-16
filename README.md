# Student-Course Data Portal

A Python-based web application that generates dynamic HTML reports for **student** and **course** data using Jinja2 templates.  
It supports validation, aggregation, and visualization of marks with histograms.

## Features
- Render **student details** (courses, marks, total).
- Render **course details** (average, maximum marks).
- Generate **histogram plots** of marks using Matplotlib.
- Error handling with fallback HTML template.

## Tech Stack
- Python 3
- Jinja2 (templating)
- Matplotlib (visualization)
- CSV (data storage)

## Usage
1. Place your data in `data.csv` with columns:  
   `Student id, Course id, Marks`
2. Run the script:
   ```bash
   python main.py -s <student_id>
   python main.py -c <course_id>
