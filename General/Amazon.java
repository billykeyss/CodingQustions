array[x][y] = n;

void replaceValues(int x, int y, int[][] arr, int swappedNumber) {
    if(arr[x][y] == swappedNumber) {
        return;
    }

    Queue q = new Queue();
    q.push(new Vertex(x,y));

    while(!q.isEmpty()) {
        Vertex point = q.pop();

        int x = point.getX();
        int y = point.getY();

        int valueAtVertex = arr[x][y];

        if(arr[x+1][y] == valueAtVertex) { //right
            q.push(new Vertex(x+1, y));
        }

        if(arr[x][y+1] == valueAtVertex) { //down
            q.push(new Vertex(x, y+1));
        }

        if(arr[x-1][y] == valueAtVertex) { //left
            q.push(new Vertex(x-1, y));
        }

        if(arr[x][y-1] == valueAtVertex) { //up
            q.push(new Vertex(x, y-1));
        }

        arr[x][y] = swappedNumber;
    }
}

class Vertex {
    int x;
    int y;

    public Vertex(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
