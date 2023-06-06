void sort(Stack<Integer> s) {
    Stack<Integer> r = new Stack<Integer>();
    while (!s.isEmpty()) {
        int tmp = s.pop();
        while (!r.isEmpty() && r.peek() > tmp) {
            s.push(r.pop());
        }
        r.push(tmp);
    }

    while (!r.isEmpty()) {
        s.push(r.pop());
    }
}