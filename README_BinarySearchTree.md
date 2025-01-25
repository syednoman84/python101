# Goal
- Implement two classes with specified instructions.
- Class 1: ```public class BinarySearchTree```
- Class 2: ```public class Node```

# Instructions - BinarySearchTree Class
1. Add below line as the first line of your class file for package:
``` java package datastructures.without.generics.binarysearchtree;```
2. Name your class as ```public class BinarySearchTree```
3. Create a class level variables for root as ```Node root``` becuase test cases rely on i5.
4. Create any constructors if required
4. Implement isEmpty() method with signature ```public boolean isEmpty()```
4. Implement addIteratively() method with signature ```public boolean addIteratively(int value)```
5. Implement addRecursively() method with signature ```public boolean addRecursively(int value)```
5. Implement searchIteratively() method with signature ```public boolean searchIteratively(int value)```
5. Implement searchRecursively() method with signature ```public boolean searchRecursively(int value)```
5. Implement deleteIteratively() method with signature ```public boolean deleteIteratively(Node currentNode, int value)```
5. Implement deleteRecursively() method with signature ```public Node deleteRecursively(Node currentNode, int value)```
5. Depth-First Search - Implement preTraverse() method with signature ```public String preTraverse(Node root)``` where the returned value format should be 2, 1, 8, 5, 3, 9
5. Depth-First Search - Implement inTraverse() method with signature ```public String inTraverse(Node root)``` where the returned value format should be 2, 1, 8, 5, 3, 9
5. Depth-First Search - Implement postTraverse() method with signature ```public String postTraverse(Node root)``` where the returned value format should be 2, 1, 8, 5, 3, 9
5. Breadth-First Search - Implement levelOrderTraverse() method with signature ```public String postTraverse(Node root)``` where the returned value format should be 2, 1, 8, 5, 3, 9
9. Add any imports as necessary for your class.

# Instructions - Node Class
1. Add below line as the first line of your class file for package:
   ``` java package datastructures.without.generics.binarysearchtree;```
2. Name your class as ```public class Node```
3. Create a private class variable as int data
4. Create two private class variables as ```Node leftChild``` and ```Node rightChild```
5. Create a constructor with this signature: ```public Node(int data)```
6. Create getters and setters for all of your class variables