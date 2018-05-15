TNode * make BSTfromArray(int a[], int min, int max) {
    if(min>max) return NULL;

    int midIdx = (min + max )/2;
    cout << endl << " a[" << midIdx <<"]: "<<a[midIdx];

    TNode *nodePtr = createNode(a[midIdx]);
    nodePtr->left = makeBSTfromArray(a, min, midIdx-1);
    nodePtr->right = makeBSTfromArray(a, midIdx+1, max);

    return nodePtr;
}
