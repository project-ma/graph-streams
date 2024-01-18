MATCH (u:User)-[r:RATED]->(m:Movie)
WHERE m.title = "Star Wars: Episode IV - A New Hope (1977)"
RETURN u,r,m
LIMIT 10;

MATCH (u:User)-[r:RATED]->(m:Movie {title:"Star Wars: Episode IV - A New Hope (1977)"})
WHERE r.rating > 4
RETURN u,r,m
LIMIT 100;

MATCH (u:User {id:561})-[r:RATED]-(m:Movie)
WHERE r.rating > 4
RETURN u, r, m
LIMIT 25;

