# Linked List Workshop

Implement the solutions for the following exercises.

## 1. Add Two Numbers
You are given two non-empty linked lists representing two 
non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two 
numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

**Example 1**:

<img height="300" src="./assets/example_sum_linkedlist.png" width="400"/>

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2**:
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3**:
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
``` 

## 2. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes. You may not
modify the values in the list's nodes. Only nodes itself may be
changed.

**Example 1**:

```
Input: [1,2,3,4]
Output: [2,1,4,3]
```

**Example 2**:

```
Input: []
Output: []
```

**Example 3**:

```
Input: [1]
Output: [1]
```

**Example 4**:

```
Input: [1,2,3]
Output: [2,1,3]
```

## 3. Insertion Sort List

Sort a linked list using insertion sort.

The steps of the insertion sort algorithm are:

1. Insertion sort iterates, consuming one input element each 
repetition, and growing a sorted output list.
2. At each iteration, insertion sort removes one element from
the input data, finds the location it belongs within the sorted
list and inserts it there.
3. It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm.
The partially sorted list (black) initially contains only the first
element in the list. One element (red) is removed from the input data
and inserted in-place into the sorted list with each iteration.

![](./assets/Insertion-sort-example-300px.gif)

**Example 1**:

```
Input: [4,2,1,3]
Output: [1,2,3,4]
```

**Example 2**:

```
Input: [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

## 4. Design Browser History

You have a browser of one tab where you start on the `homepage` 
and you can visit another `url`, get back in the history a number
of `steps` or move forward in the history a number of `steps`.

Implement the `BrowserHistory` class:

- `BrowserHistory(string homepage)` Initializes the object with the 
  homepage of the browser.
- `void visit(string url)` Visits `url` from the current page. It 
  clears up all the forward history.
- `string back(int steps)` Move `steps` back in history. If you can 
  only return `x` steps in the history and `steps > x`, you will return 
  only `x` steps. Return the current `url` after moving back in history 
  at most `steps`.
- `string forward(int steps)` Move `steps` forward in history. If you 
  can only forward `x` steps in the history and `steps > x`, you will 
  forward only `x` steps. Return the current `url` after forwarding in 
  history at most `steps`.

**Example**:

```
Input:
["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "visit", "forward", "back", "back"]
[["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]]

Output:
[null, null, null, null, "facebook.com", "google.com", "facebook.com", null, "linkedin.com", "google.com", "leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "google.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "facebook.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "youtube.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "facebook.com"
browserHistory.back(1);                   // You are in "google.com", move back to "leetcode.com" return "google.com"
browserHistory.forward(1);                // You are in "leetcode.com", move forward to "google.com" return "leetcode.com"
browserHistory.visit("linkedin.com");      // You are in "linkedin.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "google.com" then to "leetcode.com" return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com" return "leetcode.com"
``` 