class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s

        # Create list of empty strings
        sr = [""] * numRows

        row = 0
        direction = 1   # 1 means going down, -1 means going up

        for ch in s:

            # Add character in current row
            sr[row] += ch

            # Change direction at boundaries
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            # Move row pointer
            row += direction

        # Join all rows
        return "".join(sr)
                

            