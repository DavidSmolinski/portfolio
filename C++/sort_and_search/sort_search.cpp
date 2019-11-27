/* By David Smolinski (except for search and sort algorithms) */
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

// This sorts an int vector with insertion sort, and has a method for doing a
// binary search.
class BiSearchableVec
{
private:
    vector<int> originalVec;

    void printV(vector<int> v) // print vector
    {
        for (auto e : v)
        {
            cout << e << " ";
        }
        cout << "\n";
    }

    vector<int> insertionSort(vector<int> vec)
    {
        int i, j, temp, n;
        n = originalVec.size();
        for (j = 1; j < n; j++)
        {
            temp = vec[j];
            i = j - 1;

            while (i >= 0 && vec[i] > temp)
            {
                vec[i + 1] = vec[i];
                i = i - 1;
            }
            vec[i + 1] = temp;
        }
        return vec;
    }

public:
    vector<int> sortedVec;
    static int searches;
    int vecSize;

    void commonConstructorCode()
    {
        vecSize = this->originalVec.size();
    }
    BiSearchableVec(vector<int> originalVec)
    {
        setOriginalVec(originalVec);
        sortedVec = insertionSort(originalVec);
        commonConstructorCode();
    }
    BiSearchableVec()
    {
        setOriginalVec();
        sortedVec = originalVec;
        commonConstructorCode();
    }

    void setOriginalVec(vector<int> originalVec = {4, 8, 15, 16, 23, 42})
    {
        this->originalVec = originalVec;
    }
    vector<int> getOriginalVec()
    {
        return originalVec;
    }

    // vecChoice = "o" for originalVec, "s" for sortedVec
    void printVec(char vecChoice)
    {
        vector<int> v;
        switch (vecChoice)
        {
        case 'o':
            cout << "original vector: ";
            printV(originalVec);
            break;
        case 's':
            cout << "sorted vector: ";
            printV(sortedVec);
            break;

        default:
            cout << "sorted vector (default): ";
            printV(sortedVec);
            break;
        }
    }
    int binarySearch(int e)
    {
        searches++;
        int leftI = 0; // left index
        int rightI = sortedVec.size() - 1;
        int midI;
        int midV; // middle value

        while (leftI <= rightI)
        {
            midI = leftI + floor((rightI - leftI) / 2);
            midV = sortedVec[midI];

            if (midV == e)
            {

                return midI;
            }
            else if (e < midV)
            {
                rightI = midI - 1;
            }
            else
            {
                leftI = midI + 1;
            }
        }
        return -1;
    }
};
int BiSearchableVec::searches = 0;

// void classTest(BiSearchableVec& bsv, int element)
void classTest(BiSearchableVec bsv, int element)
{
    bsv.printVec('o'); // print original vector
    bsv.printVec('s'); // sorted vector
    int index = bsv.binarySearch(element);

    if (index == -1)
    {
        printf("Element %i was not found.\n", element);
    }
    else
    {
        printf("In the sorted vector, element %i is at index %i.\n"
        , element, index);
    }
}

int main(int argc, char **argv)
{
    cout << "searching and sorting vectors\n\n";
    cout << "vector 1" << endl;
    vector<int> vec = {2, 10, 7, 1, 22, 8, 2, 33, 3};
    BiSearchableVec bsv1(vec);
    classTest(bsv1, 7);

    cout << "\nvector 2 (the default)" << endl;
    BiSearchableVec bsv2;
    classTest(bsv2, 42);

    cout << "\nsearches done: " << BiSearchableVec::searches;

    return 0;
}
