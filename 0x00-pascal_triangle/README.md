# Pascal's Triangle Generator<br>

This repository contains a Python script for generating Pascal's Triangle. Pascal's Triangle is a triangular array of the binomial coefficients, which is used in various mathematical and programming applications.

## Description<br>

The provided Python script generates Pascal's Triangle up to a specified number of rows. Each row of the triangle represents the coefficients of the binomial expansion and is computed based on the values of the previous row.

## How It Works<br>

1. **Initialization**: Start with an empty list to hold the rows of Pascal's Triangle.
2. **Row Generation**: Iterate through each row index and create a row of ones. For rows beyond the first, compute interior values based on the previous row's values.
3. **Appending Rows**: Append each generated row to the list.
