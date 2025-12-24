# # Codeforces Problem Analyzer

A Python tool that analyzes a Codeforces user's solved problems and provides
topic-wise statistics, difficulty distribution, weak areas, and visualizations.

## Features
- Fetches solved problems using Codeforces API
- Removes duplicate problems
- Computes difficulty buckets
- Analyzes topic-wise performance
- Identifies weak and strong topics
- Visualizes results using matplotlib

## Project Structure
fetch_cf.py - Fetches and cleans Codeforces data

analyze.py - Computes statistics and weakness analysis

visualize.py - Generates graphs

solved.json - Cleaned problem data

## How to Run
python fetch_cf.py
python analyze.py
python visualize.py

