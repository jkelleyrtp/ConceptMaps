import json

with open("discreteconceptmapfinal.json", "r") as data:
    digraph_data = json.load(data)
    output_data = {}
    edges = {}

    # set the edges
    for edge in digraph_data["edges"]:
        # edges.setdefault( str(edge["source"]) , []).append(str(edge["target"]))
        edges.setdefault( str(edge["target"]) , []).append(str(edge["source"]))

    # Set the nodes
    for node in digraph_data["nodes"]:
        _id = node["title"].replace(" ", "_")

        output_data[str(node["id"])] = {
            "summary": "",
            "dependencies": [],
            "id": _id,
            "title": node["title"]
        }

    # Connect the edges
    for key, value in output_data.items():
        print(value)
        node_id = value["id"]

        if edges.__contains__(key):
            for edge in edges[key]:
                value["dependencies"].append({"source":output_data[edge]["id"]})
    
    real_output = []
    for key, value in output_data.items():
        real_output.append(value)

    with open("output_kmap.json", "w") as output:
        print(real_output, file=output)