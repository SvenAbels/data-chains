from rdflib.graph import Graph
from rdflib.namespace import Namespace
from rdflib.plugins.sparql import prepareQuery

NSDICT = { "schema": Namespace("http://schema.org")}

KB_LOCATION = "https://raw.githubusercontent.com/sclopit/data-chains/master/eu-data-supply-chains.html"
KB_FORMAT = 'rdfa'

# loading the graph from the HTML+RDFa knowledge base stored on GitHub.

g = Graph()
g.parse(KB_LOCATION, format=KB_FORMAT)


# A list of prepared queries to extract various types of information from the graph.

all_query = prepareQuery('SELECT DISTINCT ?s ?p ?o WHERE {?s ?p ?o .}')

buyers_query = prepareQuery('SELECT DISTINCT ?buyer WHERE { ?sale schema:agent ?buyer .}', initNs = NSDICT)

# running one of the queries and displaying the results

for row in g.query(all_query):
    print(row)
