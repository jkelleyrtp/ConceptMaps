kmap
====

Knowledge map visualization library (work in progress)


## Demos
The knowledge map library is the core component for Metacademy's interactive knowledge map, e.g. [metacademy graph demo](http://metacademy.org/graphs/concepts/deep_belief_networks#focus=deep_belief_networks&mode=explore)
<p align="center">
<a href="http://metacademy.org/graphs/concepts/deep_belief_networks#focus=deep_belief_networks&mode=explore" alt="demo kmap">
<img src="http://obphio.us/media/images/meta-graph-dbn.png" alt="Metacademy Logo" height="350px"/>
</a>
</p>


See the html and associated javascript files in [/demo](/demo)

[Demo: Khan Academy Content](http://obphio.us/kmap/demo/khan.html#implicit-differentiation)

[Demo: Metacademy Content](http://obphio.us/kmap/demo/dev.html)





## Installation

1. Clone this repository

        git clone https://github.com/cjrd/kmap.git

1. Run a local server, e.g.

        python -m SimpleHTTPServer

1. Run the tests by navigating to `http://localhost:8000/tests.html`

1. See a simple demo at `http://localhost:8000/demo/dev.html`


## Data Format


The minimal expected data format is as follows (only ids are required):

        [node1, node2, ...]

        nodeX =
        {
                id: "node_id" // this is the only required attribute for nodes
                title: "display title for node"
                summary: "summary of node"
                dependencies: [dep1, dep2, ...]
        }

        depX =
        {
                source: "source_id", // this is the only require attribute for deps
                reason: "reason for dep"
        }


## Graph View settings
You can change the following settings by passing an object into the GraphView constructor with the appropriate settings field specified, e.g. from the `demo/demojs/khan.js` demo: `graphView = new KMap.GraphView(settings);`

        settings.useWisps {boolean}: show wisp edges instead of long edges (default: true)
        settings.minWispLenPx {number > 0}: the minimum length to make an edge a wisp edge (default: 285)
        settings.includeShortestDep {boolean}: always show the shortest inlink for each node, regardless of its length (default: false)
        settings.includeShortestOutlink {boolean}: always show the shortest outlink for each node, regardless of its length (default: false)
        settings.showEdgeSummary {boolean}: show the edge summary field on hover (default: true)
        settings.showNodeSummar {boolean}: show the node summary field on hover (default: true)
        settings.graphDirection {"BT", "TB", "LR", "RL"}: direction of graph edges, e.g. TB = "top-to-bottom" (default: "TB")
        settings.showTransEdgesWisps {boolean}: show transitive edges as wisps (default: true)


## Graph Model settings
You can change the following settings by passing an object into the GraphModel constructor with the appropriate settings field specified, e.g. from the `demo/demojs/khan.js` demo: `var graphModel = new KMap.GraphModel({allowCycles: true});`

        settings.addCycles {boolean}: allows cycles in the graph if set to true (default: false)

## Notes
The knowledge map visualization library is a work in progress -- it was extracted from the [metacademy application codebase](https://github.com/metacademy/metacademy-application). I am currently working on making this code easy to use by itself while still maintaining compatability with metacademy. Please contact me (coloradoNospam at berkeley dot edu, remove the no spam part) if you want to use this code for your own project but are having trouble figuring out the code.
