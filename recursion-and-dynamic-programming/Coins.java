int makeChange(int n, int[] denoms) {
    int[][] map = new int[n + 1][denoms.length];
    return makeChangeHelper(n, denoms, 0, map);
}

int makeChangeHelper(int total, int[] demons, int index, int[][] map) {
    if (map[total][index] > 0) {
        return map[total][index];
    }

    int coin = denoms[index];

    if (index == denoms.length - 1) {
        int remaining = total % coin;
        return remaining == 0 ? 1 : 0;
    }

    int numberOfWays = 0;
    for (int amount = 0; amount <= total; amount += coin) {
        numberOfWays += makeChangeHelper(total - amount, denoms, index + 1, map);
    }

    map[total][index] = numberOfWays;
    return numberOfWays;
}