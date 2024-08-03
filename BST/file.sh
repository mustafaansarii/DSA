#!/bin/bash

# List of problems with category, filename, and URL
problems=(
  # Easy
  "Easy 01_Ceil_in_BST.py https://leetcode.com/problems/ceil-in-a-binary-search-tree"
  "Easy 02_Floor_in_BST.py https://leetcode.com/problems/floor-in-a-binary-search-tree"
  "Easy 03_Insert_in_BST.py https://leetcode.com/problems/insert-into-a-binary-search-tree"
  "Easy 04_Introduction_to_BST.py https://leetcode.com/problems/introduction-to-binary-search-tree"
  "Easy 05_Search_in_BST.py https://leetcode.com/problems/search-in-a-binary-search-tree"
  "Easy 06_Search_and_Insertion.py https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/"

  # Medium
  "Medium 01_Delete_in_BST.py https://leetcode.com/problems/delete-node-in-a-binary-search-tree"
  "Medium 02_Find_Kth_in_BST.py https://leetcode.com/problems/kth-smallest-element-in-a-bst"
  "Medium 03_Check_BST_or_BT.py https://practice.geeksforgeeks.org/problems/check-for-bst/1"
  "Medium 04_LCA_in_BST.py https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1"
  "Medium 05_Construct_BST_from_Preorder.py https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/"
  "Medium 06_Inorder_Successor_in_BST.py https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1"
  "Medium 07_Two_Sum_in_BST.py https://leetcode.com/problems/two-sum-iv-input-is-a-bst"
  "Medium 08_Find_Min_Max_in_BST.py https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1"
  "Medium 09_Binary_Tree_to_BST.py https://practice.geeksforgeeks.org/problems/binary-tree-to-bst/1"
  "Medium 10_Count_BST_Nodes_in_Range.py https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1"
  "Medium 11_Brothers_from_Different_Root.py https://practice.geeksforgeeks.org/problems/brothers-from-different-root/1"
  "Medium 12_Find_Median_in_BST.py https://www.geeksforgeeks.org/find-median-bst-time-o1-space/"
  "Medium 13_Check_Whether_BST_Contains_Dead_End.py https://practice.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1"
  "Medium 14_Preorder_to_Postorder.py https://practice.geeksforgeeks.org/problems/preorder-to-postorder/0"
  "Medium 15_Populate_Inorder_Successor.py https://practice.geeksforgeeks.org/problems/populate-inorder-successor-for-all-nodes/1"

  # Hard
  "Hard 01_Merge_2_BSTs.py https://leetcode.com/problems/merge-two-binary-search-trees"
  "Hard 02_Recover_BST.py https://leetcode.com/problems/recover-binary-search-tree"
  "Hard 03_Largest_BST_in_Binary_Tree.py https://www.geeksforgeeks.org/largest-bst/"
  "Hard 04_Convert_Normal_BST_to_Balanced_BST.py https://www.geeksforgeeks.org/convert-normal-bst-balanced-bst/"
  "Hard 05_Flatten_BST_to_Sorted_List.py https://www.geeksforgeeks.org/flatten-bst-to-sorted-list-increasing-order/"
  "Hard 06_Merge_Two_Balanced_BSTs.py https://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/"
)

# Create directories
mkdir -p Easy Medium Hard

# Create .py files
for problem in "${problems[@]}"; do
  IFS=' ' read -r category filename url <<< "$problem"
  filepath="$category/$filename"

  # Check if the file already exists
  if [[ ! -f "$filepath" ]]; then
    echo "# Problem URL: $url" > "$filepath"
    echo "# TODO: Implement the solution" >> "$filepath"
    echo >> "$filepath"
    echo "def solution():" >> "$filepath"
    echo "    # TODO: Implement the solution for $filename" >> "$filepath"
    echo "    pass" >> "$filepath"
    
    echo "Created $filepath"
  else
    echo "$filepath already exists, skipping."
  fi
done
