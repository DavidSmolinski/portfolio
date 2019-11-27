## **[sort_search.cpp by David Smolinski](https://github.com/DavidSmolinski/portfolio/blob/master/C%2B%2B/sort_and_search/sort_search.cpp)**

What this adds to my portfolio:
- c++ class and object
- getter and setter
- vector

The program makes a class that can do this:
- Store an original and sorted vectors of ints.
- Sort with insertion sort.
- binary search

The search and sort algorithms:
- I did not invent these.
- I made them as readable as I could. I fixed the insertion sort so that elements "i" and "j" will always be in alphabetical order.
- I chose to sort with vectors (not arrays) because their variable size allows for insertion features to be added. The binary search feature can be modified to allow the user to insert elements and keep the vector sorted.
- Insertion sort is the fastest sort in some situations where the list is mostly sorted. It can be very slow (O(n^2) average).

Links:
- [my portfolio](https://github.com/DavidSmolinski/portfolio)
- [Resume](https://docs.google.com/document/d/1NmaSZmUnfOo0ZlQYJZyDy648Fhi-4z7evU47rpatxZ4) 
- [Linkedin](https://www.linkedin.com/in/davidsmolinski/) 


## **The program's output:**

searching and sorting vectors

vector 1
original vector: 2 10 7 1 22 8 2 33 3 
sorted vector: 1 2 2 3 7 8 10 22 33 
In the sorted vector, element 7 is at index 4.

vector 2 (the default)
original vector: 4 8 15 16 23 42 
sorted vector: 4 8 15 16 23 42 
In the sorted vector, element 42 is at index 5.

searches done: 2
