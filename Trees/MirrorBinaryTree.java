void mirror(Node *nodePtr)
{
  if(nodePtr == NULL) return;

  //swap left and right element of nodePtr
  Node *temp = nodePtr->left;
  nodePtr->left = nodePtr->right;
  nodePtr->right = temp;

  //Call mirror function to swap element of left and right node
  mirror(nodePtr->left);
  mirror(nodePtr->right);
}
