class Solution {
public:

    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int numRows = matrix.size();
        int numCols = matrix[0].size();
        
        // Find row first
        int left = 0;
        int right = numRows - 1;
        int rowMid;

        while (left <= right) {
            rowMid = (left + right) / 2;

            if (matrix[rowMid][0] > target) {
                right = rowMid - 1;
            } else if (matrix[rowMid][0] < target) {
                left = rowMid + 1;
            } else {
                return true;  // Exact match found
            }
        }

        // At this point, rowMid is the row to search, check for valid row
        rowMid = right;  // rowMid now represents the highest row with the first element <= target
        if (rowMid < 0 || matrix[rowMid][0] > target || matrix[rowMid][numCols - 1] < target) {
            return false;  // Target cannot be in matrix
        }

        // Check cols
        left = 0;
        right = numCols - 1;
        int colMid;

        while (left <= right) {
            colMid = (left + right) / 2;

            if (matrix[rowMid][colMid] > target) {
                right = colMid - 1;
            } else if (matrix[rowMid][colMid] < target) {
                left = colMid + 1;
            } else {
                return true;  // Exact match found
            }
        }


        return false;

    }
};
