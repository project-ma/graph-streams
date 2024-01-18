# FROM memgraph/memgraph-mage:1.3
# FROM memgraph/memgraph-platform
# FROM memgraph/memgraph-mage:1.13-memgraph-2.13
FROM memgraph/memgraph-mage:latest

# Copy the local query modules and transformations
# COPY transformations/ /transformations
COPY transformations/ /usr/lib/memgraph/query_modules
# COPY query_modules/ /usr/lib/memgraph/query_modules