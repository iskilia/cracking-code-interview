void addParen(ArrayList<String> list, int leftRem, int rightRem, char[] str, int index) {
    if (leftRem < 0 || rightRem < leftRem) return;

    if (leftRem == 0 && rightRem == 0) {
        list.add(String.copyValueOf(str));
    } else {
        str[index] = '(';
        addParen(list, leftRem - 1, rightRem, str, index + 1);
        str[index] = ')';
        addParen(list, leftRem, rightRem - 1, str, index + 1);
    }
}

Set<String> generateParens(int count) {
    char[] str = new char[count * 2];
    ArrayList<String> list = new ArrayList<String>();
    addParen(list, count, count, str, 0);
    return list;
}