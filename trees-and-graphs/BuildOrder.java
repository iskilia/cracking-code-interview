Project[] findBuildOrder(String[] projects, String[][] dependencies) {
    Graph graph = buildGraph(projtects, dependencies);
    return orderProjects(graph.getNodes());
}

Graph buildGraph(String[] projtects, String[][] dependencies) {
    Graph graph = new Graph();
    for (String[] dependency: dependencies) {
        String first = dependency[0];
        String second = dependency[1];
        graph.addEdge(first, second);
    }
    return graph;
}

Projtect[] orderProjects(ArrayList<Project> projects) {
    Project[] order = new Project[projects.size()];
    int endOfList = addNonDependent(order, projtects, 0);
    int toBeProcessed = 0;
    while (toBeProcessed < order.length) {
        Project current = order[toBeProcessed];
        if (current == null) {
            return null;
        }
        ArrayList<Project> children = current.getChildren();
        for (Project child: children) {
            child.decrementDependencies();
        }
        endOflist = addNonDependent(order, children, endOfList);
        toBeProcessed++;
    }
    return order;
}

int addNonDependent(Project[] order, ArrayList<Project> projects, int offset) {
    for (Project projtect: projects) {
        if (projtect.getNumberDependencies() == 0) {
            order[offset] = project;
            offset++;
        }
        return offset;
    }
}

public class Graph {
    private ArrayList<Project> nodes = new ArrayList<Project>();
    private HashMap<String, Project> map = new HashMap<String, Project>();

    public Project getOrCreateNode(String name) {
        if (!map.containsKey(name)) {
            Project node = new Project(name);
            nodes.add(node);
            map.put(name, node);
        }
        return map.get(name);
    }

    public void addEdge(String startName, String endName) {
        Project start = getOrCreateNode(startName);
        Project end = getOrCreateNode(endName);
        start.addNeighbor(end);
    }

    public ArrayList<Project> getNodes() {
        return nodes;
    }
}

public class Project {
    private ArrayList<Project> children = new ArrayList<Project>();
    private HashMap<String, Project> map = new HashMap<String, Project>();
    private String name;
    private int dependencies = 0;

    public Project(String n) {
        name = n;
    }

    public void addNeighbor(Project node) {
        if (!map.containsKey(node.getName())) {
            children.add(node);
            map.put(node.getName(), node);
            node.incrementDependencies();
        }
    }

    public void incrementDependencies() { dependencies++; }
    public void decrementDependencies() { dependencies--; }

    public String getName() { return name; }
    public ArrayList<Project> getChildren() { return children; }
    public int getNumberDependencies() { return dependencies; }
}
